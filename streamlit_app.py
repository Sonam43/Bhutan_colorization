"""
Bhutan Image Colorizer - Streamlit Interface
Simple interface for AI-powered image colorization.
"""

import io
from pathlib import Path
from typing import Tuple

import cv2
import numpy as np
import streamlit as st
import tensorflow as tf

# Configuration
HEIGHT = 224
WIDTH = 224
MODEL_PATH = Path("bhutan_colorizer_latest.keras")


@st.cache_resource(show_spinner=True)
def load_model(model_path: Path) -> tf.keras.Model:
    """Load and cache the colorization model."""
    if not model_path.exists():
        st.error(
            f"❌ Model file '{model_path}' not found!\n\n"
            f"Please ensure the model file is in the same directory as this app."
        )
        st.stop()
    
    try:
        model = tf.keras.models.load_model(model_path)
        model.make_predict_function()
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.stop()


def preprocess_image(image_bytes: bytes) -> Tuple[np.ndarray, np.ndarray]:
    """Preprocess uploaded image for model input."""
    np_bytes = np.frombuffer(image_bytes, np.uint8)
    image_bgr = cv2.imdecode(np_bytes, cv2.IMREAD_COLOR)
    
    if image_bgr is None:
        raise ValueError("Unable to decode the uploaded image.")
    
    # Convert to RGB and resize
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    image_rgb = cv2.resize(image_rgb, (WIDTH, HEIGHT), interpolation=cv2.INTER_LANCZOS4)
    
    # Convert to grayscale for model input
    gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    lab_gray = cv2.cvtColor(gray_rgb, cv2.COLOR_RGB2Lab).astype(np.float32)
    l_channel = lab_gray[:, :, 0:1] / 255.0
    
    return l_channel[np.newaxis, ...], gray_rgb


def predict_color(model: tf.keras.Model, l_batch: np.ndarray) -> np.ndarray:
    """Get colorization prediction from model."""
    pred_ab = model.predict(l_batch, verbose=0)
    l_channel = l_batch[0, :, :, 0:1] * 255.0
    ab_channels = pred_ab[0] * 128.0 + 128.0
    
    # Reconstruct LAB image
    lab_image = np.concatenate([l_channel, ab_channels], axis=-1)
    lab_uint8 = np.clip(lab_image, 0, 255).astype(np.uint8)
    rgb_pred = cv2.cvtColor(lab_uint8, cv2.COLOR_Lab2RGB)
    return rgb_pred


def main():
    """Main Streamlit app."""
    # Page configuration
    st.set_page_config(
        page_title="Bhutan Image Colorizer",
        page_icon="🎨",
        layout="centered"
    )
    
    # Header
    st.title("🎨 Bhutan Image Colorizer")
    st.markdown("Transform grayscale images into vibrant colorized versions using AI")
    st.markdown("---")
    
    # Load model
    with st.spinner("🔄 Loading colorization model..."):
        model = load_model(MODEL_PATH)
    
    st.success("✅ Model loaded successfully!")
    
    # Image upload
    uploaded_file = st.file_uploader(
        "📤 Upload an image to colorize",
        type=["jpg", "jpeg", "png", "webp", "bmp"],
        help="Upload a grayscale or color image. The model will convert it to grayscale and add colors."
    )
    
    if uploaded_file is not None:
        # Display original image
        st.subheader("📷 Original Image")
        st.image(uploaded_file, caption="Uploaded image", use_container_width=True)
        
        # Colorize button
        if st.button("🎨 Colorize Image", type="primary", use_container_width=True):
            try:
                with st.spinner("🔄 Processing image..."):
                    # Preprocess image
                    file_bytes = uploaded_file.read()
                    l_batch, gray_rgb = preprocess_image(file_bytes)
                    
                    # Get prediction
                    rgb_colorized = predict_color(model, l_batch)
                
                # Display results
                st.subheader("✨ Colorized Result")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**📸 Input (Grayscale)**")
                    st.image(gray_rgb, clamp=True, use_container_width=True)
                
                with col2:
                    st.markdown("**🎨 Colorized Result**")
                    st.image(rgb_colorized, clamp=True, use_container_width=True)
                
                # Download button
                st.markdown("---")
                success, buffer = cv2.imencode(
                    ".png",
                    cv2.cvtColor(rgb_colorized, cv2.COLOR_RGB2BGR)
                )
                
                if success:
                    st.download_button(
                        label="📥 Download Colorized Image",
                        data=io.BytesIO(buffer.tobytes()),
                        file_name=f"{Path(uploaded_file.name).stem}_colorized.png",
                        mime="image/png",
                        use_container_width=True,
                        type="primary"
                    )
                
                st.success("✅ Colorization complete!")
                
            except Exception as e:
                st.error(f"❌ Error processing image: {str(e)}")
                st.exception(e)
    
    else:
        # Show instructions
        st.info("👆 Upload an image above to get started!")
        
        with st.expander("ℹ️ How to use"):
            st.markdown("""
            ### Simple Steps:
            
            1. **Upload an image** using the file uploader above
               - Supported formats: JPG, JPEG, PNG, WEBP, BMP
               - Works with both grayscale and color images
            
            2. **Click "Colorize Image"** to process your photo
            
            3. **View the result** and download if you like it!
            
            ### Tips:
            - Works best with heritage photos and traditional images
            - The model processes images at 224×224 pixels
            - Results are saved as PNG format for best quality
            """)


if __name__ == "__main__":
    main()
