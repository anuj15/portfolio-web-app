import pandas as pd
import streamlit as st

MY_BIO = """
Hi, I’m Anuj Gupta!\n
I graduated with a degree in Computer Engineering in 2014.\n
I'm currently work as a Software Quality Engineer at S&P Global.
"""

APP_INTRO = """
<div style="text-align: center">
<br>Below you can find some of the apps that I have build in Python. Feel free to contact me!<br><hr>
</div>"""

st.set_page_config(page_title='My Portfolio', layout='wide')
col1, col2 = st.columns(spec=2)

with col1:
    st.image(image='images/image.png')

with col2:
    st.title(body='Anuj Gupta')
    st.info(MY_BIO)

st.write(APP_INTRO, unsafe_allow_html=True)

col3, empty_col, col4 = st.columns(spec=[1.5, 0.5, 1.5])
df = pd.read_csv(filepath_or_buffer='data.csv', sep=';')


def show_app_data():
    st.subheader(body=row.title)
    st.write(row.description)
    st.image(image=f'images/{row.image}')
    st.write(f'[Source Code]({row.url})')
    st.write('<hr>', unsafe_allow_html=True)


with col3:
    for item, row in df[:10].iterrows():
        show_app_data()

st.write('<hr>', unsafe_allow_html=True)

with col4:
    for item, row in df[10:].iterrows():
        show_app_data()
