import streamlit as st

# 세션 상태 초기화 (클릭 카운터를 유지합니다)
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

st.title("수평 배치된 위젯 예제 ➡️")

# --- 1. 컬럼(열) 정의 ---
col1, col2 = st.columns([3, 1])

# --- 2. 입력창 배치 (왼쪽 컬럼) ---
with col1:
    user_name = st.text_input("입력", "") 

# --- 3. 버튼 배치 (오른쪽 컬럼) ---
with col2:
    st.write(" ") # 시각적 높이 맞춤 트릭
    is_clicked = st.button("실행", key="execute_button", use_container_width=True)


# --- 4. 버튼 클릭 및 입력에 따른 메시지 출력 ---
if is_clicked:
    if user_name:
        st.session_state.click_count += 1
        
        # 3번에 한 번씩 풍선 대신 눈 효과 실행
        if st.session_state.click_count % 3 == 0:
            # 💡 변경된 부분: st.balloons() 대신 st.snow() 사용
            st.snow() 
            
        greeting_message = f"**안녕하세요, {user_name}님!** ❄️ 헬로 월드 (Hello World)! "
        st.success(greeting_message)
        st.write(f"현재 클릭 횟수: {st.session_state.click_count}")

    elif not user_name:
        st.warning("이름을 입력한 후에 버튼을 눌러주세요.")
        
else:
    st.info("이름을 입력하고 버튼을 누르면 메시지가 나타납니다.")
