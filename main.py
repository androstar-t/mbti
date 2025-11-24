import streamlit as st

# 세션 상태 초기화 (이전 코드에서 사용하던 클릭 카운터를 유지합니다)
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

st.title("수평 배치된 위젯 예제 ➡️")

# --- 1. 컬럼(열) 정의 ---
# 3:1 비율로 두 개의 컬럼을 만듭니다. (입력창이 버튼보다 3배 넓게)
col1, col2 = st.columns([3, 1])

# --- 2. 입력창 배치 (왼쪽 컬럼) ---
with col1:
    # 레이블을 "입력"으로 변경
    user_name = st.text_input("입력", "") 

# --- 3. 버튼 배치 (오른쪽 컬럼) ---
with col2:
    # 버튼 레이블을 공백으로 설정하고 'key'를 지정합니다.
    # 이렇게 하면 버튼이 텍스트 없이 아이콘만 있는 것처럼 보여 높이가 입력창과 비슷하게 정렬됩니다.
    # 버튼이 입력창 바로 아래가 아닌 수평 위치에 오도록 st.text_input 바로 아래에 배치해야 합니다.
    # 또한, 버튼이 위젯 중앙에 오지 않도록 'Enter'와 같은 텍스트로 높이를 시각적으로 맞추는 기법을 사용합니다.
    # *참고: st.button은 기본적으로 버튼 클릭 시 앱을 다시 실행(rerun)합니다.*
    st.write(" ") # 공백을 넣어 버튼 위치를 입력창과 비슷하게 맞추는 시각적인 트릭
    is_clicked = st.button("실행", key="execute_button", use_container_width=True)


# --- 4. 버튼 클릭 및 입력에 따른 메시지 출력 (기존 로직 유지) ---
if is_clicked:
    if user_name:
        st.session_state.click_count += 1
        
        # 3번에 한 번씩 풍선 효과 실행 (빈도 조절 로직)
        if st.session_state.click_count % 3 == 0:
            st.balloons() 
            
        greeting_message = f"**안녕하세요, {user_name}님!** 🌟 헬로 월드 (Hello World)! "
        st.success(greeting_message)
        st.write(f"현재 클릭 횟수: {st.session_state.click_count}")

    elif not user_name:
        st.warning("이름을 입력한 후에 버튼을 눌러주세요.")
        
else:
    st.info("이름을 입력하고 버튼을 누르면 메시지가 나타납니다.")
