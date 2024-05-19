import time
import json
import os


OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
from openai import OpenAI
model_list = ['gpt-4-1106-preview', 'gpt-4-0125-preview', 'gpt-3.5-turbo']
selected_model = model_list[0]

client = OpenAI(
    api_key=OPENAI_KEY,
)

def create(message):
# OpenAI API를 사용하여 문장 생성
    response = client.chat.completions.create(
            model=selected_model,
            messages=[
                {"role": "system", "content": "you are a helpful assistant."},
                {"role": "user", "content": message}
                ],
            temperature=0.8,
            stream=False,
        )

    return response

def create_short(message):
# OpenAI API를 사용하여 문장 생성
    response = client.chat.completions.create(
            model=selected_model,
            messages=[
                {"role": "system", "content": "you are a helpful assistant."},
                {"role": "user", "content": message}
                ],
            temperature=0.8,
            stream=False,
        )

    return response

#사용자의 input을 받음, # input 및 prompt는 예시임.
def to_gpt(to, myname, student_num, class_, purpose, is_short ,Language="Korean"):
    prompt = f"To: {to}\nmy name: {myname}\nstudent number: {student_num}\nclass: {class_}\npurpose: {purpose}\nlanguage:{Language}" 
    prompt += (f"you are writing an email for Professor. you should write short and clear\npuporse: {purpose}" if is_short else "")
    response = create(prompt)
    result = response.choices[0].message.content
    print(result)
    return result

is_Korean = True
is_short = True
to = "박석호" if is_Korean else "Mark Silverlock" #input("To: ") 
myname = "김선우" #input("my name: ")
student_num = "202311045"#input("student number: ")
class_  = "자동제어시스템" if is_Korean else "Academic English"#input("class: ")
purpose = "병결로 인한 출석 인정"#input("Purpose: ")
Language = "Korean" if is_Korean else "English"#input("Language: ")
prompt = f"To: {to}\nmy name: {myname}\nstudent number: {student_num}\nclass: {class_}\npurpose: {purpose}\nlanguage:{Language}" 
prompt += f"you are writing an email for Professor. you should write short and clear\npuporse: {purpose}"
response = create_short(prompt) if is_short else create(prompt)


#print(response.choices[0].message.content)