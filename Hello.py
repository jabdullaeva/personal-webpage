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
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    st.markdown("""<h1 style="font-family: 'Roboto', cursive; text-align: center; font-size: 36px;"><b>Designer, Frontend Developer & Mentor</b></h1>""", unsafe_allow_html=True)
    st.markdown("""<p style="font-family:'Roboto', cursive; text-align: center; font-size: 16px; font-weight: normal;">I design and code 
        beautifully simple things, and I love what I do.</p>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image('jasminaphoto1.jpg', width=200, use_column_width=True)

    blue_container = """
    <div style="background-color: #007FFF; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="font-family: 'Roboto', sans-serif; text-align: center; font-size: 25px; color: white;">Hi, I’m Jasmina. Nice to meet you.👋</h2>
        <p style="font-family: 'Roboto', sans-serif; text-align: center; font-size: 16px; color: white;">
        Since beginning of my journey, I have always thrived to tackle complex problems and create bright solutions. I first discovered my love for programming during my involvement 
        in competitive robotics. As one of the leaders of an award-winning FIRST Tech Challenge team #14212, 
        I honed my skills by designing and coding robots to autonomously navigate obstacle courses. 
        I'm quietly confident, naturally curious, and working on improving my chops.
        </p>
    </div>
    """
    st.markdown(blue_container, unsafe_allow_html=True)
    
    roles_table = """
    <style>
        .rounded-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            font-family: 'Roboto', sans-serif;
            border: 1px solid #007FFF;
            border-radius: 15px;
            overflow: hidden;
        }
        .rounded-table th, .rounded-table td {
            border: 1px solid #007FFF;
            padding: 16px;
            text-align: center;
            vertical-align: top;
        }
        .rounded-table thead tr {
            background-color: #f2f2f2;
        }
        .rounded-table tbody tr:nth-child(odd) {
            background-color: #f9f9f9;
        }
        .rounded-table tbody tr:nth-child(even) {
            background-color: #ffffff;
        }
        @media only screen and (max-width: 600px) {
            .rounded-table th, .rounded-table td {
                display: block;
                width: 100%;
                text-align: left;
            }
        }
    </style>
    <table class="rounded-table">
        <tbody>
            <tr>
                <td>
                    <p style="color: #007FFF;"><b>Quality Assurance Developer</b><p>
                    <p style="color: #000000;">
                    I ensure optimal user experiences through rigorous testing and quality standards.<br><br>
                    <b>Areas of Expertise:</b><br>
                    Web Application Testing<br>
                    Test Automation (JavaScript, SQL)<br>
                    Cross-Browser/Device Compatibility<br>
                    Accessibility & Usability Testing<br>
                    Defect Tracking & Reporting<br>
                    <p>
                </td>
                <td>                    
                    <p style="color: #007FFF;"><b>Frontend Developer</b><p>
                    <p style="color: #000000;">
                    I like to code things from scratch, and enjoy bringing ideas to life in the browser.<br><br>
                    <b>Languages I speak:</b><br>
                    Java, Python, C++, HTML, CSS<br><br>
                    <b>Dev Tools:</b><br>
                    Github<br>
                    Netlify<br>
                    Tailwind CSS<br>
                    VS Code
                    <p>
                </td>
                <td>
                    <p style="color: #007FFF;"><b>Mentor</b></p>
                    <p style="color: #000000;">
                    I genuinely care about people, and enjoy helping them work on their craft.<br><br>
                    <b>Experiences I draw from:</b><br>
                    UX/UI, Quality Assurance, Product design<br><br>
                    <b>Mentor Stats:</b><br>
                    3+ years experience<br>
                    100+ students<br>
                    10+ mentor sessions<br>
                    <p>
                </td>
            </tr>
        </tbody>
    </table>
    """

    st.markdown(roles_table, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    .say-hello-button {
        position: fixed;
        top: 50px;
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
    <a href="mailto:jabdullaeva@fordham.edu" class="say-hello-button">Say Hello</a>
    """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    run()
