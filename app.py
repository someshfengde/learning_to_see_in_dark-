import streamlit as st 
from functionality import *

st.title('learning to see in dark implementation')

img = st.file_uploader(label= 'upload image to convert it to daytime here',type = ['jpg','png','jpeg'])

st.image(img,caption = 'your image')
if img : 
    predicted_image = predict(img)
    st.immage(predicted_image,caption = 'converted image')
else : 
    st.write('upload the image first')
    

