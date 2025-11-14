# 🚀 Deployment Guide - GitHub with Large Model Files

This guide will help you push your project to GitHub even with large model files using Git LFS (Large File Storage).

## 📋 Prerequisites

1. **Git installed** on your computer
2. **GitHub account**
3. **Git LFS installed** (see installation below)

## 🔧 Step 1: Install Git LFS

### Windows:
```bash
# Download and install from: https://git-lfs.github.com/
# Or use Chocolatey:
choco install git-lfs

# Or use winget:
winget install GitHub.GitLFS
```

### After installation, verify:
```bash
git lfs version
```

## 📝 Step 2: Initialize Git LFS

Open PowerShell or Command Prompt in your project directory and run:

```bash
# Navigate to your project
cd C:\Users\Sheru\Desktop\deep_learning_project

# Initialize Git (if not already done)
git init

# Install Git LFS hooks
git lfs install

# Track large files (model files)
git lfs track "*.keras"
git lfs track "*.h5"
git lfs track "*.pkl"

# This creates/updates .gitattributes file
```

## 📦 Step 3: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** icon → **"New repository"**
3. Name it (e.g., `bhutan-colorizer`)
4. Choose **Public** or **Private**
5. **DO NOT** initialize with README, .gitignore, or license
6. Click **"Create repository"**

## 🔄 Step 4: Push to GitHub

```bash
# Add all files (Git LFS will handle large files automatically)
git add .

# Commit your files
git commit -m "Initial commit: Bhutan Image Colorizer with model"

# Add your GitHub repository as remote
# Replace YOUR_USERNAME and REPO_NAME with your actual values
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note:** First push with LFS files may take longer. Be patient!

## ✅ Step 5: Verify LFS Files

After pushing, verify on GitHub:
1. Go to your repository
2. Click on `bhutan_colorizer_latest.keras`
3. You should see: **"Stored with Git LFS"** badge

## 🎯 Alternative: If Git LFS Doesn't Work

If you encounter issues or want a simpler approach:

### Option A: Host Model on Google Drive / Dropbox
1. Upload model to Google Drive/Dropbox
2. Get shareable link
3. Download in Streamlit app using `requests` or `gdown`

### Option B: Use Hugging Face Model Hub
1. Create account on [Hugging Face](https://huggingface.co)
2. Upload model there
3. Load in Streamlit using `huggingface_hub`

### Option C: Use Streamlit Secrets for Model URL
Store model URL in Streamlit Cloud secrets and download on first run.

## 🔍 Troubleshooting

### Issue: "Git LFS not installed"
**Solution:** Install Git LFS (see Step 1)

### Issue: "File too large" error
**Solution:** Make sure you ran `git lfs track "*.keras"` before adding files

### Issue: Push fails
**Solution:** 
```bash
# Check LFS status
git lfs ls-files

# Re-track if needed
git lfs track "*.keras"
git add .gitattributes
git commit -m "Add LFS tracking"
git push
```

### Issue: Model not tracked by LFS
**Solution:**
```bash
# Remove from cache and re-add
git rm --cached bhutan_colorizer_latest.keras
git add bhutan_colorizer_latest.keras
git commit -m "Re-add model with LFS"
git push
```

## 📊 Git LFS Limits

- **GitHub Free:** 1 GB storage, 1 GB bandwidth/month
- **GitHub Pro:** 50 GB storage, 50 GB bandwidth/month
- **GitHub Team/Enterprise:** Higher limits

If your model exceeds limits, use alternative hosting (Option A, B, or C above).

## 🎉 Next Steps After Pushing

1. **Deploy to Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Deploy!

2. **Update README.md** with your repository link

3. **Share your app** with others!

## 💡 Quick Commands Reference

```bash
# Check LFS status
git lfs ls-files

# Check file size
git lfs env

# Migrate existing files to LFS (if needed)
git lfs migrate import --include="*.keras" --everything
```

