import streamlit as st

# Streamlit 앱의 제목 설정
st.title("버튼으로 실행하는 인사 메시지 생성기 👆")

# --- 1. 사용자 이름 입력 받기 ---
# st.text_input을 사용하여 사용자가 이름을 입력할 수 있는 텍스트 상자를 만듭니다.
user_name = st.text_input("당신의 이름을 입력해주세요:", "")

# --- 2. 입력 버튼 추가 ---
# st.button을 사용하여 버튼을 만들고, 버튼이 클릭되었는지 여부를 is_clicked 변수에 저장합니다.
is_clicked = st.button("인사 메시지 생성")

# --- 3. 버튼 클릭 및 입력에 따른 메시지 출력 ---
# 버튼이 클릭되었고(is_clicked == True), user_name 변수에 값이 있을 경우에만 실행
if is_clicked and user_name:
    
    # f-string을 사용하여 입력받은 이름과 "헬로 월드"를 조합한 메시지를 생성합니다.
    greeting_message = f"**안녕하세요, {user_name}님!** 🌟 헬로 월드 (Hello World)! "
    
    # st.balloons()를 추가하여 버튼 클릭 시 축하 효과를 줍니다.
    st.balloons() 
    
    # st.success를 사용하여 메시지를 눈에 띄게 출력합니다.
    st.success(greeting_message)
    
    # 추가적인 텍스트를 출력합니다.
    st.write("Streamlit 웹 앱에 오신 것을 환영합니다.")

# 버튼이 클릭되지 않았거나, 이름이 입력되지 않았을 경우
elif is_clicked and not user_name:
    # 버튼은 눌렀지만 이름이 비어있을 경우 경고 메시지를 출력합니다.
    st.warning("이름을 입력한 후에 버튼을 눌러주세요.")
    
else:
    # 기본 안내 메시지
    st.info("이름을 입력하고 버튼을 누르면 메시지가 나타납니다.")
