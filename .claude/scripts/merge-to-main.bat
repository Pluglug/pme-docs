@echo off
REM Selective Merge Script: feature/ja-rough -> main
REM Only merge .claude/ and CLAUDE.md, exclude personal files

echo ===================================
echo   Selective Merge to Main
echo ===================================
echo.

REM Check current branch
for /f "tokens=*" %%i in ('git branch --show-current') do set CURRENT_BRANCH=%%i

if not "%CURRENT_BRANCH%"=="feature/ja-rough" (
    echo X Error: Must be on feature/ja-rough branch
    echo    Current branch: %CURRENT_BRANCH%
    exit /b 1
)

echo [OK] Current branch: %CURRENT_BRANCH%
echo.

REM Show what will be merged
echo This will merge the following to main:
echo   - .claude/ directory
echo   - CLAUDE.md
echo.
echo Excluded (will NOT merge):
echo   - DEPLOYMENT.md
echo   - PLAN.md
echo   - docs_ja/ (work in progress)
echo.

set /p CONFIRM="Continue? (y/n): "
if /i not "%CONFIRM%"=="y" (
    echo Cancelled.
    exit /b 0
)

REM Switch to main
echo.
echo Switching to main branch...
git checkout main

REM Pull latest
echo Pulling latest main...
git pull origin main

REM Merge selectively
echo.
echo Merging .claude/ and CLAUDE.md from feature/ja-rough...
git checkout feature/ja-rough -- .claude/
git checkout feature/ja-rough -- CLAUDE.md

REM Show status
echo.
echo ===================================
echo   Changes staged for commit:
echo ===================================
git status --short

echo.
echo ===================================
echo   Next steps:
echo ===================================
echo.
echo 1. Review changes:
echo    git diff --cached
echo.
echo 2. Commit (use English message):
echo    git commit -m "docs: ^<your message^>"
echo.
echo    Example:
echo    git commit -m "chore: update Claude Code configuration
echo.
echo    - Add custom slash commands
echo    - Add terminology dictionary
echo    - Update workflow documentation"
echo.
echo 3. Push to main:
echo    git push origin main
echo.
echo 4. Return to feature/ja-rough:
echo    git checkout feature/ja-rough
echo.

pause
