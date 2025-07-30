#!/bin/bash

# Script to start sphinx-autobuild for local development
# Run this after installing dependencies with: pip install -r requirements.txt

echo "Starting Sphinx autobuild server..."
echo "Make sure you have installed dependencies first:"
echo "  pip install -r requirements.txt"
echo ""
echo "Starting server on http://localhost:8000"
echo "The server will automatically reload when files change."
echo ""

cd "$(dirname "$0")/docs"

# Check if sphinx-autobuild is available
if ! command -v sphinx-autobuild &> /dev/null; then
    echo "sphinx-autobuild is not installed. Please install it with:"
    echo "  pip install sphinx-autobuild"
    exit 1
fi

# Start sphinx-autobuild
sphinx-autobuild source build/html --host 0.0.0.0 --port 8000 --open-browser