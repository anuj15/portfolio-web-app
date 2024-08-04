import streamlit as st

from send_mail import send_mail

st.title(body='Contact Me')


def email():
    msg = f'subject:Mail from StreamLit Portfolio App\n{st.session_state.message}'
    send_mail(to_=st.session_state.to_email, msg_=msg)


with st.form(key='send mail'):
    st.text_input(label='Your Email Address', key='to_email', placeholder='Enter your email here...')
    st.text_area(label='Your message', key='message', placeholder='Enter your message here...')
    button = st.form_submit_button(label='Submit', on_click=email)
    if button:
        st.info(body='Your email was sent successfully.')
