#!/bin/bash

# Selective Merge Script: feature/ja-rough -> main
# Only merge .claude/ and CLAUDE.md, exclude personal files

set -e

echo "==================================="
echo "  Selective Merge to Main"
echo "==================================="
echo ""

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" != "feature/ja-rough" ]; then
    echo "❌ Error: Must be on feature/ja-rough branch"
    echo "   Current branch: $CURRENT_BRANCH"
    exit 1
fi

echo "✓ Current branch: $CURRENT_BRANCH"
echo ""

# Confirm with user
echo "This will merge the following to main:"
echo "  - .claude/ directory"
echo "  - CLAUDE.md"
echo ""
echo "Excluded (will NOT merge):"
echo "  - DEPLOYMENT.md"
echo "  - PLAN.md"
echo "  - docs_ja/ (work in progress)"
echo ""

read -p "Continue? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

# Switch to main
echo ""
echo "Switching to main branch..."
git checkout main

# Pull latest
echo "Pulling latest main..."
git pull origin main

# Merge selectively
echo ""
echo "Merging .claude/ and CLAUDE.md from feature/ja-rough..."
git checkout feature/ja-rough -- .claude/
git checkout feature/ja-rough -- CLAUDE.md

# Show status
echo ""
echo "==================================="
echo "  Changes staged for commit:"
echo "==================================="
git status --short

echo ""
echo "==================================="
echo "  Next steps:"
echo "==================================="
echo ""
echo "1. Review changes:"
echo "   git diff --cached"
echo ""
echo "2. Commit (use English message):"
echo "   git commit -m \"docs: <your message>\""
echo ""
echo "   Example:"
echo "   git commit -m \"chore: update Claude Code configuration"
echo ""
echo "   - Add custom slash commands"
echo "   - Add terminology dictionary"
echo "   - Update workflow documentation\""
echo ""
echo "3. Push to main:"
echo "   git push origin main"
echo ""
echo "4. Return to feature/ja-rough:"
echo "   git checkout feature/ja-rough"
echo ""
