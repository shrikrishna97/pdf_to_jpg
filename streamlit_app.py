import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io
import os

def pdf_to_images(pdf_path):
    images = []
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap()
        images.append(Image.frombytes("RGB", [image.width, image.height], image.samples))

    pdf_document.close()
    return images

def save_uploaded_file(uploaded_file):
    # Create the "uploads" directory if it doesn't exist
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    # Save the uploaded file with its original name
    pdf_filename = os.path.join("uploads", uploaded_file.name)
    with open(pdf_filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return pdf_filename

def save_jpg_file(img, pdf_filename):
    # Save the JPG file with the fixed name "give.jpg"
    jpg_filename = os.path.join("uploads", "give.jpg")

    # Save the JPG file
    img.save(jpg_filename, format='JPEG')
    return jpg_filename

def main():
    st.title("PDF to Image Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.subheader("PDF Preview")

        # Display uploaded PDF file
        st.write(f"You selected: {uploaded_file.name}")

        # Save the uploaded file with its original name
        pdf_filename = save_uploaded_file(uploaded_file)

        # Convert PDF to images (using PyMuPDF)
        try:
            images = pdf_to_images(pdf_filename)
        except Exception as e:
            st.error(f"Error: {e}")
            return

        st.subheader("Converted Images")

        # Display converted images
        for i, img in enumerate(images):
            # Convert the PIL Image to bytes
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='JPEG')
            img_bytes = img_bytes.getvalue()

            # Display the image
            st.image(img_bytes, caption=f"Page {i+1}", use_column_width=True)

            # Save the corresponding JPG file as "give.jpg"
            jpg_filename = save_jpg_file(img, pdf_filename)

            # Add a button to trigger the download
            download_button_str = f"Download Image {i+1}"
            if st.button(download_button_str):
                st.download_button(
                    label="Click here to download",
                    data=img_bytes,
                    file_name=f"{os.path.basename(jpg_filename)}",
                    key=f"download_button_{i}"
                )

if __name__ == "__main__":
    main()


