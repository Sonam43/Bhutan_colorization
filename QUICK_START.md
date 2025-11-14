# 🚀 Quick Start - Push to GitHub

## Method 1: Using Git LFS (Recommended)

### Step 1: Install Git LFS
```bash
# Windows - Download from: https://git-lfs.github.com/
# Or use:
winget install GitHub.GitLFS
```

### Step 2: Run Setup Script
```bash
# Double-click or run:
setup_git_lfs.bat
```

### Step 3: Manual Setup (if script doesn't work)
```bash
# Navigate to project folder
cd C:\Users\Sheru\Desktop\deep_learning_project

# Install Git LFS hooks
git lfs install

# Track model files
git lfs track "*.keras"
git lfs track "*.h5"

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Bhutan Image Colorizer"
```

### Step 4: Create GitHub Repository & Push
1. Go to [github.com](https://github.com) → New repository
2. Name it (e.g., `bhutan-colorizer`)
3. **Don't** initialize with README
4. Copy the repository URL

```bash
# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## Method 2: Alternative - Host Model Elsewhere

If Git LFS is too complicated, you can host the model separately:

### Option A: Google Drive
1. Upload `bhutan_colorizer_latest.keras` to Google Drive
2. Get shareable link
3. Update `streamlit_app.py` to download model on first run:

```python
import gdown

MODEL_URL = "YOUR_GOOGLE_DRIVE_LINK"
MODEL_PATH = Path("bhutan_colorizer_latest.keras")

if not MODEL_PATH.exists():
    st.info("Downloading model...")
    gdown.download(MODEL_URL, str(MODEL_PATH), quiet=False)
```

Add to `requirements.txt`:
```
gdown>=4.6.0
```

### Option B: Hugging Face
1. Create account at [huggingface.co](https://huggingface.co)
2. Create a model repository
3. Upload your model
4. Load in Streamlit:

```python
from huggingface_hub import hf_hub_download

MODEL_PATH = hf_hub_download(
    repo_id="YOUR_USERNAME/bhutan-colorizer",
    filename="bhutan_colorizer_latest.keras"
)
```

---

## Method 3: Streamlit Cloud Secrets

1. Push code to GitHub (without model)
2. Upload model to a cloud storage (Google Drive, Dropbox, etc.)
3. Get direct download link
4. In Streamlit Cloud → Settings → Secrets, add:
```toml
[MODEL]
DOWNLOAD_URL = "your_model_download_link"
```

5. Update `streamlit_app.py`:
```python
import requests

MODEL_URL = st.secrets["MODEL"]["DOWNLOAD_URL"]
MODEL_PATH = Path("bhutan_colorizer_latest.keras")

if not MODEL_PATH.exists():
    with st.spinner("Downloading model..."):
        response = requests.get(MODEL_URL)
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)
```

---

## 📊 Which Method to Choose?

- **Git LFS**: Best if model < 1GB and you want everything in one repo
- **Google Drive/Dropbox**: Simple, free, works for any size
- **Hugging Face**: Professional, good for sharing models
- **Streamlit Secrets**: Good for private deployment

---

## ✅ After Pushing to GitHub

1. **Deploy to Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Main file: `streamlit_app.py`
   - Click "Deploy"

2. **Wait for deployment** (first time may take 5-10 minutes)

3. **Share your app!** 🎉

---

## 🆘 Need Help?

See `DEPLOYMENT_GUIDE.md` for detailed troubleshooting.

