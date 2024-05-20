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

    st.markdown("""<h1 style = "font-family: 'Roboto', cursive; text-align: center; font-size: 36px;"><b>Designer, Frontend Developer & Mentor</b></h1>""", unsafe_allow_html=True)
  
    st.markdown("""<p style="font-family:'Roboto', cursive; text-align: center; font-size: 16px; font-weight: normal;">I design and code 
        beautifully simple things, and I love what I do.</p>""", unsafe_allow_html=True)

    blue_container = """
    <div style="background-color: #007FFF; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="font-family: 'Roboto', sans-serif; text-align: center; font-size: 25px; color: white;">Hi, I’m Jasmina. Nice to meet you.👋</h2>
        <p style="font-family: 'Roboto', sans-serif; text-align: center; font-size: 16px; color: white;">
        Since beginning my journey, I thrive on tackling complex problems 
        and creating bright solutions. I first discovered my love for programming during my involvement 
        in competitive robotics. As one of the leaders of an award-winning FIRST Tech Challenge team #14212, 
        I honed my skills by designing and coding robots to autonomously navigate obstacle courses. 
        I'm quietly confident, naturally curious, and perpetually working on improving my chops.
        </p>
    </div>
    """
    st.write(" ")
    
    # Define the HTML and CSS for the table with detailed descriptions
    roles_table = """
    <style>
        .rounded-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Arial', sans-serif;
            border-radius: 15px;
            overflow: hidden;
        }
        .rounded-table th, .rounded-table td {
            border: 1px solid #ddd;
            padding: 16px;
            text-align: center;
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
        <thead>
            <tr>
                <th>Frontend Developer</th>
                <th>Mentor</th>
                <th>Designer</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>
                    <p style="color: #007FFF;"><b>Frontend Developer</b></p>
                    <p>I like to code things from scratch, and enjoy bringing ideas to life in the browser.</p>
                    <p><b>Languages I speak:</b> Java, Python, C++, HTML, CSS</p>
                    <p><b>Dev Tools:</b> Github, Netlify, Tailwind CSS, VS Code</p>
                </td>
                <td>
                    <p style="color: #007FFF;"><b>Mentor</b></p>
                    <p>I genuinely care about people, and enjoy helping them work on their craft.</p>
                    <p><b>Experiences I draw from:</b> UX/UI, Quality Assurance, Product design</p>
                    <p><b>Mentor Stats:</b> 9+ years experience, 30+ short courses, 65+ bootcamps, 250+ students, 2,500+ mentor sessions, 60+ group critiques, 18,000+ bits of feedback</p>
                </td>
                <td>
                    <p style="color: #007FFF;"><b>Designer</b></p>
                    <p>I value simple content structure, clean design patterns, and thoughtful interactions.</p>
                    <p><b>Things I enjoy designing:</b> UX, UI, Web, Apps, Logos</p>
                    <p><b>Design Tools:</b> Affinity Designer, Figma, Pen & Paper, Sketch</p>
                </td>
            </tr>
        </tbody>
    </table>
    """

    # Combine the blue container and the roles table
    combined_content = blue_container + roles_table

    # Display the combined content
    st.markdown(combined_content, unsafe_allow_html=True)

if __name__ == "__main__":
    run()
