#!/usr/bin/env bash
set -euo pipefail

VENV_DIR="venv"
REQUIREMENTS=("pyyaml" "jinja2" "openai")
PY_SCRIPT_BOOK="generate_prompts.py"
PY_SCRIPT_HANDBOOK="generate_handbook.py"

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
    err "Usage: ./run_handbook.sh <yaml_file> <output_dir> [--handbook] [--verbose]"
    exit 1
fi

YAML_FILE="$1"
OUT_DIR="$2"
MODE="book"
VERBOSE=""

for arg in "${@:3}"; do
    case "$arg" in
        --handbook) MODE="handbook" ;;
        --verbose) VERBOSE="--verbose" ;;
        *)
            err "Unknown argument: $arg"
            exit 1
            ;;
    esac
done

if [[ ! -f "$YAML_FILE" ]]; then
    err "YAML '$YAML_FILE' not found"
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

log "Ensuring dependencies..."
for pkg in "${REQUIREMENTS[@]}"; do
    if ! python3 -c "import ${pkg%%=*}" 2>/dev/null; then
        log "Installing $pkg"
        pip install "$pkg"
    else
        log "$pkg already installed"
    fi
done

if [[ "$MODE" == "handbook" ]]; then
    log "Running in HANDBOOK mode"
    CMD=(python3 "$PY_SCRIPT_HANDBOOK" "$YAML_FILE" "$OUT_DIR")
else
    log "Running in BOOK mode"
    CMD=(python3 "$PY_SCRIPT_BOOK" "$YAML_FILE" "$OUT_DIR")
fi

[[ -n "$VERBOSE" ]] && CMD+=("$VERBOSE")

log "Executing: ${CMD[*]}"
"${CMD[@]}"

log "Generation complete."
