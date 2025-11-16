#!/usr/bin/env bash
set -euo pipefail

VENV_DIR="venv"
REQUIREMENTS=("pyyaml" "jinja2" "openai")
PY_SCRIPT="generate_prompts.py"

timestamp() {
    date +"%Y-%m-%d %H:%M:%S"
}

log() {
    echo "$(timestamp) [INFO] $*"
}

err() {
    echo "$(timestamp) [ERROR] $*" >&2
}

if [[ $# -lt 2 ]]; then
    err "Usage: ./run_book.sh <book.yaml> <output_dir> [--verbose]"
    exit 1
fi

BOOK_YAML="$1"
OUT_DIR="$2"
VERBOSE="${3:-}"

if [[ ! -f "$BOOK_YAML" ]]; then
    err "YAML '$BOOK_YAML' not found"
    exit 1
fi

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
    err "OPENAI_API_KEY is not set"
    exit 1
fi

if [[ ! -d "$VENV_DIR" ]]; then
    log "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

log "Activating environment..."
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"

log "Ensuring deps..."
for pkg in "${REQUIREMENTS[@]}"; do
    if ! python3 -c "import ${pkg%%=*}" 2>/dev/null; then
        log "Installing $pkg"
        pip install "$pkg"
    else
        log "$pkg already installed"
    fi
done

CMD=(python3 "$PY_SCRIPT" "$BOOK_YAML" "$OUT_DIR")
[[ "$VERBOSE" == "--verbose" ]] && CMD+=("--verbose")

log "Running: ${CMD[*]}"
"${CMD[@]}"

log "Book generation complete."
