import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import io
import os

def pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    return images

def save_uploaded_file(uploaded_file):
    # Create the "uploads" directory if it doesn't exist
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    
    # Save the uploaded file to a temporary location
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join("uploads", uploaded_file.name)

def main():
    st.title("PDF to Image Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.subheader("PDF Preview")

        # Display uploaded PDF file
        st.write(f"You selected: {uploaded_file.name}")

        # Save the uploaded file to a temporary location
        pdf_path = save_uploaded_file(uploaded_file)

        # Convert PDF to images
        images = pdf_to_images(pdf_path)

        st.subheader("Converted Images")

        # Display converted images
        for i, img in enumerate(images):
            # Convert the PIL Image to bytes
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='PNG')
            img_bytes = img_bytes.getvalue()

            # Display the image
            st.image(img_bytes, caption=f"Page {i+1}", use_column_width=True)

            # Add a download button for each image
            download_button_str = f"Download Image {i+1}"
            st.download_button(
                label=download_button_str,
                data=img_bytes,
                file_name=f"page_{i+1}.png",
                key=f"download_button_{i}"
            )

if __name__ == "__main__":
    main()
