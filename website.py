import streamlit as st
from main import to_gpt

# Set the title of the application
st.title('받는 이')
# Create a text input for the recipient's name
to = st.text_input("이름", placeholder='ex) 김선우 교수님')

# Set the title for the sender's information
st.title('보내는 이')
# Create text inputs for the sender's name, student number, and class
myname = st.text_input("이름", placeholder='ex) 홍길동')
stud_num = st.text_input("학번", placeholder='ex) 202411200')
class_ = st.text_input('수강과목', placeholder='ex) 일반화학1')

# Initialize the purpose variable
purpose = None
# Create a select box for the purpose of the request
if st.selectbox('요청사항', ['요청사항을 선택하세요','병결 처리']) == '병결 처리':
    # If the selected purpose is '병결 처리', create a text input for the reason
    purpose = st.text_input('사유', placeholder='ex) 병결로 인한 출석 인정')

# Create a radio button for language selection
Language = st.radio('언어 선택', ['Korean', 'English'])

# Initialize session state for buttons if not already done
if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = False
if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = False

# Create the first button and handle its click event
if st.button("스타일1", disabled=st.session_state.button1_clicked):
    st.session_state.button1_clicked = True
    st.write("로딩중..")
    st.write(to_gpt(to, myname, stud_num, class_, purpose, is_short=True, Language=Language))

# Create the second button and handle its click event
if st.button("스타일2", disabled=st.session_state.button2_clicked):
    st.session_state.button2_clicked = True
    st.write("로딩중..")
    st.write(to_gpt(to, myname, stud_num, class_, purpose, is_short=False, Language=Language))
