import streamlit as st

# Streamlit 앱의 제목 설정
st.title("간단한 인사 메시지 생성기 👋")

# --- 1. 사용자 이름 입력 받기 ---
# st.text_input을 사용하여 사용자가 이름을 입력할 수 있는 텍스트 상자를 만듭니다.
user_name = st.text_input("당신의 이름을 입력해주세요:", "")

# --- 2. 입력에 따른 메시지 출력 ---
# user_name 변수에 값이 있을 경우 (즉, 사용자가 이름을 입력했을 경우)
if user_name:
    # f-string을 사용하여 입력받은 이름과 "헬로 월드"를 조합한 메시지를 생성합니다.
    greeting_message = f"**안녕하세요, {user_name}님!** 🌟 헬로 월드 (Hello World)! "
    
    # st.success를 사용하여 메시지를 눈에 띄게 출력합니다.
    st.success(greeting_message)
    
    # 추가적인 텍스트를 출력할 수도 있습니다.
    st.write("Streamlit 웹 앱에 오신 것을 환영합니다.")
else:
    # 이름이 입력되지 않았을 경우 안내 메시지를 출력합니다.
    st.info("메시지를 보려면 위에 이름을 입력하세요.")
