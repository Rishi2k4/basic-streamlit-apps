import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance

# App Title
st.title("🖼️ Image Filter App")
st.markdown("Upload an image and apply cool filters in real-time!")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Filter options
filters = ["Original", "Grayscale", "Sepia", "Invert", "Blur", "Increase Brightness"]
selected_filter = st.selectbox("Select a filter to apply", filters)

# Brightness slider
brightness = st.slider("Adjust Brightness", 0.5, 3.0, 1.0, step=0.1)

# Filter functions
def apply_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_sepia(image):
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_img = cv2.transform(image, sepia_filter)
    return np.clip(sepia_img, 0, 255).astype(np.uint8)

def apply_invert(image):
    return cv2.bitwise_not(image)

def apply_blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)

def adjust_brightness(pil_img, factor):
    enhancer = ImageEnhance.Brightness(pil_img)
    return enhancer.enhance(factor)

# Main Logic
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    img_array = np.array(image.convert("RGB"))
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    if selected_filter == "Grayscale":
        filtered = apply_grayscale(img_bgr)
        st.image(filtered, caption="Grayscale Image", channels="GRAY", use_column_width=True)

    elif selected_filter == "Sepia":
        filtered = apply_sepia(img_bgr)
        filtered_rgb = cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB)
        st.image(filtered_rgb, caption="Sepia Image", use_column_width=True)

    elif selected_filter == "Invert":
        filtered = apply_invert(img_bgr)
        filtered_rgb = cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB)
        st.image(filtered_rgb, caption="Inverted Image", use_column_width=True)

    elif selected_filter == "Blur":
        filtered = apply_blur(img_bgr)
        filtered_rgb = cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB)
        st.image(filtered_rgb, caption="Blurred Image", use_column_width=True)

    elif selected_filter == "Increase Brightness":
        bright_img = adjust_brightness(image, brightness)
        st.image(bright_img, caption=f"Brightness: {brightness}x", use_column_width=True)

    else:
        st.info("Showing original image.")
