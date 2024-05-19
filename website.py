import streamlit as st
from main import to_gpt

st.title('받는 이')
to = st.text_input("이름", placeholder='ex) 김선우')

#st.checkbox('교수')
#st.checkbox('조교')

st.title('보내는 이')
myname = st.text_input("이름", placeholder='ex) 홍길동')
stud_num = st.text_input("학번", placeholder='ex) 202411200')
class_ = st.text_input('수강과목', placeholder='ex) 일반화학1')
purpose = None
if st.selectbox('요청사항', ['요청사항을 선택하세요','병결 처리']) == '병결 처리':
    purpose = st.text_input('사유', placeholder='ex) 병결로 인한 출석 인정')
Language = st.radio('언어 선택', ['Korean', 'English'])

if st.button("스타일1"):
    st.write(to_gpt(to, myname, stud_num, class_, purpose, is_short=True, Language=Language))
if st.button("스타일2"):
    st.write(to_gpt(to, myname, stud_num, class_, purpose, is_short=False, Language=Language))