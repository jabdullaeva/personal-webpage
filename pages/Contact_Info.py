# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

st.set_page_config(page_title="Contact Info", layout="wide")
st.markdown("# Contact Info")

# Function to send email
def send_email(to_email, subject, message):
    # Email configuration
    from_email = "jabdullaeva@fordham.edu"
    from_password = "Jesika2004"
    
    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        # Establish a secure session with gmail's outgoing SMTP server using your gmail account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        
        # Send email
        server.send_message(msg)
        server.quit()
        
        return "Email sent successfully!"
    except Exception as e:
        return str(e)
    
# Add the CSS for the button in the top right corner
st.markdown("""
    <style>
    .say-hello-button {
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #007FFF;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-family: 'Roboto', sans-serif;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Add the "Say Hello" button
if st.button('Say Hello', key='say-hello-button', help='Click to say hello!'):
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        question = st.text_area("Your Question")
        submit_button = st.form_submit_button(label='Send')

        if submit_button:
            subject = f"Question from {name}"
            message = f"Name: {name}\nEmail: {email}\n\nQuestion:\n{question}"
            response = send_email("jabdullaeva@fordham.edu", subject, message)
            st.success(response)
