import streamlit as st
import ollama

# 세션 상태로 대화 기록 관리
if "msgs" not in st.session_state:
    st.session_state["msgs"] = []

st.set_page_config(layout="wide")
st.title("자비스")

# 기존 대화 출력
for msg in st.session_state["msgs"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 사용자 입력 받기
user_input = st.chat_input("궁금한 게 있으면 물어보세요!")

if user_input:
    # 사용자 메시지 추가
    st.session_state["msgs"].append({"role": "user", "content": user_input})

    # Ollama 챗봇 호출
    try:
        response = ollama.chat(
            model="gemma2:9b",
            messages=st.session_state["msgs"]
        )
        assistant_content = response["message"]["content"]
    except Exception as e:
        assistant_content = f"오류가 발생했습니다: {e}"

    # 챗봇 답변 추가
    st.session_state["msgs"].append({"role": "assistant", "content": assistant_content})

    # 답변 출력
    with st.chat_message("assistant"):
        st.write(assistant_content)