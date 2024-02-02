import streamlit as st
import openai
# from dotenv import load_dotenv

# load_dotenv()

def main():
    # 기본 설정
    st.set_page_config(
        page_title="음성비서 프로그램",
        layout="wide"
    )
    
    st.header("음성비서 프로그램")
    st.markdown("---")
    
    # 기본 설명
    with st.expander("음성비서 프로그램에 관하여", expanded=True):
        st.write(
    """
    - 음성 비서 프로그램 UI
    - STT는 Whisper AI를 활용
    - 답변은 OpenAI의 GPT모델을 활용
    - TTS는 구글의 TTS를 활용
    """
        )
        st.markdown("")
    
    # sesstion state 초기화
    if "chat" not in st.session_state:
        st.session_state["chat"] = []
    
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]
    
    if "check_audio" not in st.session_state:
        st.session_state["check_audio"]
    
    #사이드바
    with st.sidebar:
        openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key", value="", type="password")
        st.markdown("---")
        
        model = st.radio(label="GPT 모델", options=["gpt-4", "gpt-3.5-turbo"])
        
        st.markdown("---")
        
        if st.button(label="초기화"):
            #리셋 코드
            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]
    
    # columns는 영역임
    col1, col2 = st.columns(2)
    with col1:
        # 왼쪽 영역 작성
        st.subheader("질문하기")
    
    with col2:
        # 왼쪽 영역 작성
        st.subheader("질문/답변")
    
    
    
    
if __name__ == "__main__":
    main()