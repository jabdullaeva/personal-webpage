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

    st.sidebar.success("Select a demo above.")

    st.markdown("""<h1 style = "font-family:new roman;"><b>Hello there! 👋</b></h1>""", unsafe_allow_html=True)

    st.markdown(
    """
    <em style = "font-size:15px">My name is Jasmina Abdullaeva. Currently, I am pursuing B.S. in Computer Science at Fordham University. 
       I am passionate about technology and innovation. As an aspiring programmer, 
       I thribe on tackling complex problems and creating bright solutions.
       I first discovered my love for programming during my involvement in competitive robotics.
       As one of the leaders of an award-winning FIRST Tech Challenge team #14212, 
       I honed my skills in Java, Python, C++, HTML and CSS by designing and coding robots to
       autonomously navigate obstacle courses. This experience sparkled in me a relentless curiosity 
       to push boundaries and expand my caoabilities.

       Find more of my work in the Project Section!</em>
    """,
    unsafe_allow_html=True
)


if __name__ == "__main__":
    run()
