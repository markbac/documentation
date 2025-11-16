#!/usr/bin/env bash

# export OPENAI_API_KEY=


# my name is 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

set -euo pipefail

# -----------------------------
# Configuration
# -----------------------------

VENV_DIR="venv"
REQUIREMENTS=("openai" "pyyaml" "jinja2")
PYTHON_SCRIPT="generate_prompts.py"

# -----------------------------
# Helper functions
# -----------------------------

timestamp() {
    date +"%Y-%m-%d %H:%M:%S"
}

log() {
    echo "$(timestamp) [INFO] $*"
}

err() {
    echo "$(timestamp) [ERROR] $*" >&2
}

# -----------------------------
# Argument checking
# -----------------------------

if [[ $# -lt 2 ]]; then
    err "Usage: ./run.sh <topics.yaml> <output_dir> [--verbose]"
    exit 1
fi

YAML_FILE="$1"
OUTPUT_DIR="$2"
VERBOSE_FLAG="${3:-}"

if [[ ! -f "$YAML_FILE" ]]; then
    err "YAML file '$YAML_FILE' not found."
    exit 1
fi

# -----------------------------
# Check OPENAI_API_KEY
# -----------------------------

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
    err "OPENAI_API_KEY is not set."
    echo ""
    echo "Set it like this:"
    echo "    export OPENAI_API_KEY=\"your_key_here\""
    exit 1
fi

# -----------------------------
# Create venv if missing
# -----------------------------

if [[ ! -d "$VENV_DIR" ]]; then
    log "Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# -----------------------------
# Activate venv
# -----------------------------

log "Activating virtual environment..."
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"

# -----------------------------
# Install required packages
# -----------------------------

log "Checking/installing dependencies..."

for pkg in "${REQUIREMENTS[@]}"; do
    if ! python3 -c "import ${pkg%%=*}" >/dev/null 2>&1; then
        log "Installing: $pkg"
        pip install "$pkg"
    else
        log "$pkg already installed."
    fi
done

# -----------------------------
# Run the Python script
# -----------------------------

CMD=(python3 "$PYTHON_SCRIPT" "$YAML_FILE" "$OUTPUT_DIR")

if [[ "$VERBOSE_FLAG" == "--verbose" || "$VERBOSE_FLAG" == "-v" ]]; then
    CMD+=("--verbose")
fi

log "Running: ${CMD[*]}"
echo ""

"${CMD[@]}"

log "Completed successfully."
