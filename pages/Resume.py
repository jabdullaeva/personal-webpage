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

    st.title("Jasmina Abdullaeva")
    st.markdown("""
    **Email:** jabdullaeva@fordham.edu  
    **Phone:** 929-278-0293  
    **Website:** [abdullaevajasmina.streamlit.app](https://abdullaevajasmina.streamlit.app)
    """)

    st.header("Education")
    st.markdown("""
    **Fordham University, New York, NY**  
    Anticipated Graduation: May 2027  
    **Major:** Computer Science  
    **Minor:** Business Administration  
    **GPA:** 3.9
    """)
    st.markdown("""
    **Awards:**  
    - City Council Citation for Robotics  
    - Computer Science & Engineering Technology Seal  
    - Community Service Award  
    - FTC World Championship Division Finalists  
    - NYC FIRST Tech Challenge Champions  
    - Loyola Scholar  
    - Scholar-Athlete Award  
    """)

    st.header("Technical Skills")
    st.markdown("""
    **Languages:**  
    - C/C++  
    - Java  
    - JavaScript  
    - Python  
    - SQL  
    - basic HTML, CSS, TypeScript  

    **Software and OS:**  
    - XCode  
    - Android Studio  
    - Digital Circuit Design  
    - Arduino  
    - OnShape  
    - Streamlit  
    - Svelte  
    - GitHub  
    - Visual Studio  
    """)

    st.header("Relevant Projects")
    st.markdown("""
    **Eco-Tourism, DEVFEST (February 2024)**  
    Developed a Svelte web app to help travelers discover lesser-known sustainable destinations worldwide, with features like mapping, booking eco-tours, and real-time incident reporting to protect environments.  
    Focused on creating an intuitive, user-friendly interface with a clean, modern design, allowing seamless search, browsing of destinations, and access to sustainable travel tips.  

    **CheckMD, HACKNJIT (October 2023)**  
    Built a surgical error prevention web app using Streamlit in Python and enhanced site design using HTML and CSS.  
    Integrated the application with MS Excel for efficient data management.  
    Contributed to a significant reduction in preventable errors in the operating room by implementing critical safety measures.  

    **FIRST POWERPLAY Autonomous and Tele-Op Period for the Robot (September 2022 - June 2023)**  
    Incorporated OpenCV pipeline, which effortlessly detects the RGB values of the three different colored zones.  
    Programmed the robot in Java language on Android Studio; the robot efficiently scored 1+5 during the autonomous period.  
    Implemented roadrunner/odometry for faster and smoother movement while maintaining control of velocity and acceleration.  

    **Light Robot (February 2023 - March 2023)**  
    Engineered the robot that navigates towards the light, and its speed depends on the brightness.  
    Utilized phototransistors to detect light presence, piezo speakers, and touch-sensitive whiskers when a bot is running.  
    Designed a CAD blueprint for the robot using OnShape and coded the robot using C++ language on Arduino.  
    """)

    st.header("Relevant Experience")
    st.markdown("""
    **Quality Assurance Developer, Public Affairs Department, Fordham University, New York (August 2023 - Present)**  
    Test and ensure the quality of the university’s website through Terminal 4 using JavaScript, SQL, HTML, and CSS.  
    Collaborate with the Assistant Director and marketing team to improve Fordham’s website and social media.  

    **Software Engineer Intern, JPMorgan Chase & Co., New York (June 2024 - August 2024)**  
    Completed tasks focused on interfacing with a stock price data feed, fixing scripts, and manipulating financial data using Python, Git, React, and TypeScript.  

    **Mentor & Team Captain, First Tech Challenge Robotics Team, Metrobotics FTC 14212, New York (September 2019 - June 2023)**  
    Ranked Division finalists at FTC World Championships (ranked #1 in NYC and #32 in the world out of 6,000 teams).  
    Arranged meetings with Google, NASA, and NNL to learn more about the robotics field.  
    Worked with FDNY Robotics, One Earth Conservation, and AFYA Foundation and held fundraisers.  
    Organized STEM community events (workshops for high school and middle school students, STEM days, FTC scrimmages).  

    **Programming Specialist Intern, Think Design Program, New York (July 2022 - August 2022)**  
    Provided technical assistance and support to create the Escape Room using my programming skills in Java and Python.  
    Presented 3 robotics courses in the Escape Room, using Arduino building and coding.  
    """)

    st.header("Leadership Experience")
    st.markdown("""
    **Founder & President, Project Pixel Organization (Intro to Robotics and Coding), New York City, NY (January 2024 - Present)**  
    Direct weekly 2-hour coding workshops in Java for Project Pixel members to gain programming experience.  
    Introduced a curriculum focused on game development and robotics, which received positive feedback from 60+ participants.  

    **Undergraduate Representative, Cybersecurity Club, Fordham University, NY (December 2023 - Present)**  
    Execute engaging cybersecurity workshops with guest speakers from IBM, Google, and KPMG with over 100 participants.  
    Spearheaded club outreach and recruitment initiatives through social media, resulting in a 20% increase in membership.  

    **Senator of the Programming Committee, Commuting Student Association, Fordham University, NY (October 2023 - Present)**  
    Championed commuter student needs by securing $5,000 in scholarship funding.  
    Curated 3 innovative events: “Urban Night” (200+ attendees), “Game Night: Level Up Your Skills” (promoted teamwork and problem-solving), and “Networking Event” (15 internship offers).  
    """)

    st.header("Languages and Skills")
    st.markdown("""
    **Languages:**  
    - Fluent in Russian, Tajik  
    - Intermediate in French, Uzbek  

    **Skills:**  
    - Testing  
    - Communication  
    - Debugging  
    - Problem-Solving  
    - Time Management  
    - Detail Oriented  
    - Organized  
    - Teamwork  
    """)

if __name__ == "__main__":
    run()
