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

def run():
    st.set_page_config(page_title="Resume", page_icon="📄")

    # Define main color
    main_color = "#007FFF"

    # Add CSS for custom styling
    st.markdown(f"""
        <style>
            .header {{
                background-color: {main_color};
                color: white;
                padding: 10px;
                border-radius: 10px;
                text-align: center;
            }}
            .subheader {{
                color: {main_color};
                margin-top: 20px;
                text-align: center;
                font-size: 24px;
            }}
            .section {{
                margin-top: 20px;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .section h3 {{
                color: {main_color};
            }}
            .section p {{
                margin: 0;
                padding: 5px 0;
            }}
            .contact {{
                text-align: center;
                margin-top: 20px;
            }}
            .contact p {{
                margin: 5px 0;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Header with shape
    st.markdown(f"""
        <div class="header">
            <h1>Jasmina Abdullaeva</h1>
            <p>jabdullaeva@fordham.edu | 929-278-0293 | <a href="https://abdullaevajasmina.streamlit.app" style="color: white;">Website</a></p>
            <div style="background-color: {main_color}; height: 10px; border-radius: 0px 0px 10px 10px;"></div>
        </div>
    """, unsafe_allow_html=True)

    # Education
    st.markdown("""
        <div class="section">
            <h2 class="subheader">Education</h2>
            <h3>Fordham University, New York, NY</h3>
            <p><strong>Anticipated Graduation:</strong> May 2027</p>
            <p><strong>Major:</strong> Computer Science</p>
            <p><strong>Minor:</strong> Business Administration</p>
            <p><strong>GPA:</strong> 3.9</p>
            <p><strong>Awards:</strong></p>
            <ul>
                <li>City Council Citation for Robotics</li>
                <li>Computer Science & Engineering Technology Seal</li>
                <li>Community Service Award</li>
                <li>FTC World Championship Division Finalists</li>
                <li>NYC FIRST Tech Challenge Champions</li>
                <li>Loyola Scholar</li>
                <li>Scholar-Athlete Award</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Technical Skills
    st.markdown("""
        <div class="section">
            <h2 class="subheader">Technical Skills</h2>
            <p><strong>Languages:</strong> C/C++, Java, JavaScript, Python, SQL, basic HTML, CSS, TypeScript</p>
            <p><strong>Software and OS:</strong> XCode, Android Studio, Digital Circuit Design, Arduino, OnShape, Streamlit, Svelte, GitHub, Visual Studio</p>
        </div>
    """, unsafe_allow_html=True)

    # Relevant Projects
    st.markdown("""
        <div class="section">
            <h2 class="subheader">Relevant Projects</h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>Eco-Tourism, DEVFEST (February 2024)</h3>
            <p>Developed a Svelte web app to help travelers discover lesser-known sustainable destinations worldwide, with features like mapping, booking eco-tours, and real-time incident reporting to protect environments.</p>
            <p>Focused on creating an intuitive, user-friendly interface with a clean, modern design, allowing seamless search, browsing of destinations, and access to sustainable travel tips.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>CheckMD, HACKNJIT (October 2023)</h3>
            <p>Built a surgical error prevention web app using Streamlit in Python and enhanced site design using HTML and CSS.</p>
            <p>Integrated the application with MS Excel for efficient data management.</p>
            <p>Contributed to a significant reduction in preventable errors in the operating room by implementing critical safety measures.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>FIRST POWERPLAY Autonomous and Tele-Op Period for the Robot (September 2022 - June 2023)</h3>
            <p>Incorporated OpenCV pipeline, which effortlessly detects the RGB values of the three different colored zones.</p>
            <p>Programmed the robot in Java language on Android Studio; the robot efficiently scored 1+5 during the autonomous period.</p>
            <p>Implemented roadrunner/odometry for faster and smoother movement while maintaining control of velocity and acceleration.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>Light Robot (February 2023 - March 2023)</h3>
            <p>Engineered the robot that navigates towards the light, and its speed depends on the brightness.</p>
            <p>Utilized phototransistors to detect light presence, piezo speakers, and touch-sensitive whiskers when a bot is running.</p>
            <p>Designed a CAD blueprint for the robot using OnShape and coded the robot using C++ language on Arduino.</p>
        </div>
    """, unsafe_allow_html=True)

    # Relevant Experience
    st.markdown("""
        <div class="section">
            <h2 class="subheader">Relevant Experience</h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>Quality Assurance Developer, Public Affairs Department, Fordham University, New York (August 2023 - Present)</h3>
            <p>Test and ensure the quality of the university’s website through Terminal 4 using JavaScript, SQL, HTML, and CSS.</p>
            <p>Collaborate with the Assistant Director and marketing team to improve Fordham’s website and social media.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>Software Engineer Intern, JPMorgan Chase & Co., New York (June 2024 - August 2024)</h3>
            <p>Completed tasks focused on interfacing with a stock price data feed, fixing scripts, and manipulating financial data using Python, Git, React, and TypeScript.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>Mentor & Team Captain, First Tech Challenge Robotics Team, Metrobotics FTC 14212, New York (September 2019 - June 2023)</h3>
            <p>Ranked Division finalists at FTC World Championships (ranked #1 in NYC and #32 in the world out of 6,000 teams).</p>
            <p>Arranged meetings with Google, NASA, and NNL to learn more about the robotics field.</p>
            <p>Worked with FDNY Robotics, One Earth Conservation, and AFYA Foundation and held fundraisers.</p>
            <p>Organized STEM community events (workshops for high school and middle school students, STEM days, FTC scrimmages).</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>Programming Specialist Intern, Think Design Program, New York (July 2022 - August 2022)</h3>
            <p>Provided technical assistance and support to create the Escape Room using my programming skills in Java and Python.</p>
            <p>Presented 3 robotics courses in the Escape Room, using Arduino building and coding.</p>
        </div>
    """, unsafe_allow_html=True)

    # Leadership Experience
    st.markdown("""
        <div class="section">
            <h2 class="subheader">Leadership Experience</h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>Founder & President, Project Pixel Organization (Intro to Robotics and Coding), New York City, NY (January 2024 - Present)</h3>
            <p>Direct weekly 2-hour coding workshops in Java for Project Pixel members to gain programming experience.</p>
            <p>Introduced a curriculum focused on game development and robotics, which received positive feedback from 60+ participants.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <h3>Undergraduate Representative, Cybersecurity Club, Fordham University, NY (December 2023 - Present)</h3>
            <p>Execute engaging cybersecurity workshops with guest speakers from IBM, Google, and KPMG with over 100 participants.</p>
            <p>Spearheaded club outreach and recruitment initiatives through social media, resulting in a 20% increase in membership.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="section">
            <h3>Senator of the Programming Committee, Commuting Student Association, Fordham University, NY (October 2023 - Present)</h3>
            <p>Championed commuter student needs by securing $5,000 in scholarship funding.</p>
            <p>Curated 3 innovative events: “Urban Night” (200+ attendees), “Game Night: Level Up Your Skills” (promoted teamwork and problem-solving), and “Networking Event” (15 internship offers).</p>
        </div>
    """, unsafe_allow_html=True)

    # Languages and Skills
    st.markdown("""
        <div class="section">
            <h2 class="subheader">Languages and Skills</h2>
            <p><strong>Languages:</strong> Fluent in Russian, Tajik; Intermediate in French, Uzbek</p>
            <p><strong>Skills:</strong> Testing, Communication, Debugging, Problem-Solving, Time Management, Detail Oriented, Organized, Teamwork</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run()

