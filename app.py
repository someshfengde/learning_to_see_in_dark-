from numpy.lib.shape_base import expand_dims
import streamlit as st
from functionality import *

st.title('learning to see in dark implementation')
readme_text = st.markdown(get_file_content_as_string("README.md"))

# expander =  st.beta_expander(label='sample images',expanded=True)

col1, col2 = st.beta_columns(2)
c1 = col1.markdown(
    "<h2 style='text-align: center; color: gray;'>Dark image input</h1>", unsafe_allow_html=True)
c2 = col2.markdown(
    "<h2 style='text-align: center; color: gray;'>Enhanced image</h1>", unsafe_allow_html=True)
i1 = col1.image('https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/input1.png',
                use_column_width=True)
i2 = col2.image('https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/output1.png',
                use_column_width=True)
col3, col4 = st.beta_columns(2)
i3 = col3.image('https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/input2.png',
                use_column_width=True)
i4 = col4.image('https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/output2.png',
                use_column_width=True)

st.sidebar.title("What to do")
app_mode = st.sidebar.selectbox("Choose the app mode",
                                ["Show instructions", "Run the app", "Source code"])
if app_mode == "Show instructions":
    st.sidebar.success('To continue select "Run the app".')
elif app_mode == "Source code":
    readme_text.empty()
    i1.empty()
    i2.empty()
    i3.empty()
    i4.empty()
    c1.empty()
    c2.empty()
    col1.empty()
    col2.empty()
    st.title('Code:')
    st.code(get_file_content_as_string("app.py"))
    st.title('Functionality')
    st.code(get_file_content_as_string("functionality.py"))
elif app_mode == "Run the app":
    readme_text.empty()
    col1.empty()
    col2.empty()
    i1.empty()
    i2.empty()
    i3.empty()
    i4.empty()
    c1.empty()
    c2.empty()
    run_the_app()
