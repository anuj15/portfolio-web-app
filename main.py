import streamlit as st

st.set_page_config(page_title='My Portfolio', layout='wide')
col1, col2 = st.columns(spec=2)

with col1:
    st.image(image='images/photo.png', width=600)

with col2:
    st.title(body='Anuj Gupta')
    content = """
    Hi, I’m Anuj Gupta!\n
    I graduated with a degree in Computer Engineering in 2014.\n
    I'm currently work as a Software Quality Engineer at S&P Global.
    """
    st.info(content)
