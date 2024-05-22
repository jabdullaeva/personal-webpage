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

# Main content
def run():
    st.set_page_config(
        page_title="Projects",
        page_icon="🚀",
    )

    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    st.markdown("""<h1 style="font-family: 'Roboto', sans-serif; text-align: center; font-size: 36px;"><b>My Projects</b></h1>""", unsafe_allow_html=True)
    st.markdown("""<p style="font-family: 'Roboto', sans-serif; text-align: center; font-size: 16px; font-weight: normal;">Here are some of the projects I've worked on recently. I take pride in creating solutions that make a difference.</p>""", unsafe_allow_html=True)

    projects = [
        {
            "title": "Eco-Tourism, DEVFEST",
            "date": "February 2024",
            "description": """
                Developed a Svelte web app to help travelers discover lesser-known sustainable destinations worldwide, with features like mapping, booking eco-tours, and real-time incident reporting to protect environments.
                Focused on creating an intuitive, user-friendly interface with a clean, modern design, allowing seamless search, browsing of destinations, and access to sustainable travel tips.
            """
        },
        {
            "title": "CheckMD, HACKNJIT",
            "date": "October 2023",
            "description": """
                Built a surgical error prevention web app using Streamlit in Python and enhanced site design using HTML and CSS.
                Integrated the application with MS Excel for efficient data management.
                Contributed to a significant reduction in preventable errors in the operating room by implementing critical safety measures.
            """
        },
        {
            "title": "FIRST POWERPLAY Autonomous and Tele-Op Period for the Robot",
            "date": "September 2022 - June 2023",
            "description": """
                Incorporated OpenCV pipeline, which effortlessly detects the RGB values of the three different colored zones.
                Programmed the robot in Java language on Android Studio; the robot efficiently scored 1+5 during the autonomous period.
                Implemented roadrunner/odometry for faster and smoother movement while maintaining control of velocity and acceleration.
            """
        },
        {
            "title": "Light Robot",
            "date": "February 2023 - March 2023",
            "description": """
                Engineered the robot that navigates towards the light, and its speed depends on the brightness.
                Utilized phototransistors to detect light presence, piezo speakers, and touch-sensitive whiskers when a bot is running.
                Designed a CAD blueprint for the robot using OnShape and coded the robot using C++ language on Arduino.
            """
        }
    ]

    # Display projects
    for project in projects:
        st.markdown(f"""
        <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <h2 style="font-family: 'Roboto', sans-serif; color: #007FFF;">{project['title']}</h2>
            <p style="font-family: 'Roboto', sans-serif; font-size: 14px; color: #555;"><i>{project['date']}</i></p>
            <p style="font-family: 'Roboto', sans-serif; font-size: 16px; color: #333;">{project['description']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Add the CSS for the button in the top right corner
    st.markdown("""
        <style>
        .back-home-button {
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
            font-color: #FFFFFF
            font-size: 16px;
            z-index: 1000;
        }
        </style>
        <a href="Hello.py" class="back-home-button">Home</a>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run()
