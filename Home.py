import streamlit as st

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.title("YOLO V5 Object Detection App")
st.caption("This web application demonstrate Object Detection")

#Content
st.markdown("""
### This App detects objects from Images
- Automatically detects 10 objects from image
- [Click here for App](/YOLO_for_image/)  

Below give are the object the our model will detect
1. Afghan_hound
2. Maltese_dog
3. Shih-Tzu
4. Blenheim_spaniel
5. Japanese_spaniel
6. papillon 
7. Rhodesian_ridgeback
8. chihuahua
9. toy_terrier
10. Pekinese
           
            """)