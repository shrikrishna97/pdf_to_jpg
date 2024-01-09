import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import io

def pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    return images

def main():
    st.title("PDF to Image Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.subheader("PDF Preview")

        # Display uploaded PDF file
        st.write(f"You selected: {uploaded_file.name}")

        # Convert PDF to images
        images = pdf_to_images(uploaded_file)

        st.subheader("Converted Images")

        # Display converted images
        for i, img in enumerate(images):
            # Convert the PIL Image to bytes
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='PNG')
            img_bytes = img_bytes.getvalue()

            # Display the image
            st.image(img_bytes, caption=f"Page {i+1}", use_column_width=True)

if __name__ == "__main__":
    main()
