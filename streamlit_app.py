import streamlit as st
from pdf2image import convert_from_path
from PIL import Image

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
        st.image(uploaded_file)

        # Convert PDF to images
        images = pdf_to_images(uploaded_file)

        st.subheader("Converted Images")

        # Display converted images
        for i, img in enumerate(images):
            st.image(img, caption=f"Page {i+1}", use_column_width=True)

if __name__ == "__main__":
    main()
