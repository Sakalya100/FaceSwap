import os
import cv2
import streamlit as st
import numpy as np

from face_detection import select_face, select_all_faces
from face_swap import face_swap

# Function to read image and convert to RGB
def read_image(image_file):
    image = np.array(bytearray(image_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Streamlit app
st.title('FaceSwapApp')

st.sidebar.title("Upload Images")
src_file = st.sidebar.file_uploader("Upload Source Image", type=["jpg", "jpeg", "png"])
dst_file = st.sidebar.file_uploader("Upload Target Image", type=["jpg", "jpeg", "png"])

warp_2d = st.sidebar.checkbox('2D Warp', value=False)
correct_color = st.sidebar.checkbox('Correct Color', value=False)

submit = st.sidebar.button('Generate')
if submit:
    if src_file and dst_file:
        # Read and display the uploaded images
        src_image = read_image(src_file)
        dst_image = read_image(dst_file)
        
        # Set up the layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(src_image, caption='Source Image', use_column_width=True)
            st.image(dst_image, caption='Target Image', use_column_width=True)

        # Process the images
        src_points, src_shape, src_face = select_face(src_image)
        dst_faceBoxes = select_all_faces(dst_image)

        if dst_faceBoxes is None:
            st.error('No face detected in target image!')
        else:
            output = dst_image.copy()
            for k, dst_face in dst_faceBoxes.items():
                output = face_swap(src_face, dst_face["face"], src_points,
                                dst_face["points"], dst_face["shape"],
                                output, warp_2d=warp_2d, correct_color=correct_color)
            
            # Display the result
            with col2:
                st.image(output, caption='Swapped Image', use_column_width=True)
            
                # Option to download the result
                result_path = 'output/result.png'
                cv2.imwrite(result_path, cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
                with open(result_path, "rb") as file:
                    st.download_button(
                        label="Download Swapped Image",
                        data=file,
                        file_name="result.png",
                        mime="image/png"
                    )
                os.remove(result_path)
    else:
        st.error('Please upload both source and target images!')
