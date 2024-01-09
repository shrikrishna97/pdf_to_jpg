# pdf_to_image_converter.py
import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import io
import os
import tempfile

def pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    return images

def save_uploaded_file(uploaded_file):
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
    return temp_pdf.name

def main():
    st.title("PDF to Image Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.subheader("PDF Preview")

        # Display uploaded PDF file
        st.write(f"You selected: {uploaded_file.name}")

        # Save the uploaded file with a specific name (take.pdf)
        pdf_path = save_uploaded_file(uploaded_file)

        # Convert PDF to images
        images = pdf_to_images(pdf_path)

        st.subheader("Converted Images")

        # Display converted images
        for i, img in enumerate(images):
            # Convert the PIL Image to bytes
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='JPEG')
            img_bytes = img_bytes.getvalue()

            # Display the image
            st.image(img_bytes, caption=f"Page {i+1}", use_column_width=True)

            # Save the JPEG file with a specific name (give.jpg)
            jpeg_path = f"give_{i+1}.jpg"
            img.save(jpeg_path)

            # Add a download button for each image
            download_button_str = f"Download Image {i+1}"
            st.download_button(
                label=download_button_str,
                data=img_bytes,
                file_name=jpeg_path,
                key=f"download_button_{i}"
            )

if __name__ == "__main__":
    main()
