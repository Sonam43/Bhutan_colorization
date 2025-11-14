@echo off
REM Setup script for Git LFS with large model files
echo ========================================
echo Git LFS Setup for Bhutan Colorizer
echo ========================================
echo.

REM Check if Git LFS is installed
git lfs version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git LFS is not installed!
    echo.
    echo Please install Git LFS first:
    echo 1. Download from: https://git-lfs.github.com/
    echo 2. Or use: winget install GitHub.GitLFS
    echo 3. Or use: choco install git-lfs
    echo.
    pause
    exit /b 1
)

echo [OK] Git LFS is installed
echo.

REM Initialize Git LFS
echo [1/4] Installing Git LFS hooks...
git lfs install
echo.

REM Track large files
echo [2/4] Tracking large model files...
git lfs track "*.keras"
git lfs track "*.h5"
git lfs track "*.pkl"
echo.

REM Initialize git if not already done
if not exist .git (
    echo [3/4] Initializing Git repository...
    git init
    echo.
) else (
    echo [3/4] Git repository already initialized
    echo.
)

REM Show status
echo [4/4] Git LFS status:
git lfs ls-files
echo.
echo ========================================
echo Setup complete!
echo.
echo Next steps:
echo 1. Create a repository on GitHub
echo 2. Run these commands:
echo    git add .
echo    git commit -m "Initial commit"
echo    git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
echo    git branch -M main
echo    git push -u origin main
echo.
pause

