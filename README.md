# 🎨 Bhutan Image Colorizer

A Streamlit web application for AI-powered image colorization using a deep learning model trained on Bhutan heritage images.

## 🚀 Features

- **AI-Powered Colorization**: Transform grayscale images into vibrant colorized versions
- **Advanced Post-Processing**: Enhanced colorization with adjustable saturation and contrast
- **Real-time Preview**: Compare raw predictions with enhanced results
- **Easy Download**: Save your colorized images in high quality
- **User-Friendly Interface**: Intuitive controls and settings

## 📋 Requirements

- Python 3.8+
- TensorFlow 2.20.0
- Streamlit 1.40.0+
- OpenCV
- NumPy

## 🛠️ Installation

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure the model file `bhutan_colorizer_latest.keras` is in the same directory as `streamlit_app.py`

## 🏃 Running Locally

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

## ☁️ Deploying to Streamlit Cloud

1. **Push to GitHub**:
   - Create a GitHub repository
   - Push all files including:
     - `streamlit_app.py`
     - `requirements.txt`
     - `bhutan_colorizer_latest.keras` (model file)
     - `README.md` (optional)

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `streamlit_app.py`
   - Click "Deploy"

3. **Important Notes**:
   - The model file (`bhutan_colorizer_latest.keras`) must be in your repository
   - If the model is large (>100MB), consider using Git LFS or hosting it elsewhere
   - First deployment may take a few minutes

## 🎛️ Usage

1. Upload an image (JPG, PNG, WEBP, or BMP)
2. Adjust enhancement settings in the sidebar:
   - **Saturation Boost**: Control color vibrancy (0.5-2.5)
   - **Contrast Boost**: Control image contrast (0.5-2.0)
   - **Smoothing Filter**: Enable/disable color smoothing
3. Click "Colorize Image"
4. Compare results and download your favorite version

## 📝 Model Information

- **Input Size**: 224×224 pixels
- **Color Space**: LAB (Luminance + Chrominance)
- **Architecture**: U-Net based encoder-decoder
- **Training**: Trained on Bhutan heritage images

## 🔧 Customization

You can customize the app by modifying:
- `saturation_boost` default value (line ~120)
- `contrast_boost` default value (line ~130)
- Model path (line ~15)
- Image dimensions (lines ~13-14)

## 📄 License

This project is for educational and research purposes.

## 🙏 Acknowledgments

- Model trained on Bhutan heritage image dataset
- Uses TensorFlow/Keras for deep learning
- Streamlit for web interface

