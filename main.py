import streamlit as st

# 세션 상태 초기화 (클릭 카운터는 그대로 유지)
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

st.title("가로 배치된 인사 메시지 생성기 ➡️")
st.info("이름을 입력하고 버튼을 누르면 메시지가 나타납니다.")

# --- 1. 입력창과 버튼을 위한 컬럼 생성 ---
# 컬럼을 두 개 생성합니다. [4, 1]은 입력창(첫 번째 컬럼)이 버튼(두 번째 컬럼)보다 4배 넓게 공간을 사용하도록 지정합니다.
col1, col2 = st.columns([4, 1]) 

# --- 2. 첫 번째 컬럼(col1)에 입력창 배치 ---
with col1:
    # 사용자 이름 입력 받기
    user_name = st.text_input("당신의 이름을 입력해주세요:", "", label_visibility="collapsed", placeholder="여기에 이름을 입력하세요") 
    # label_visibility="collapsed"를 사용하여 기본 라벨("당신의 이름을 입력해주세요:")이 입력창 위에 나타나지 않도록 숨깁니다.

# --- 3. 두 번째 컬럼(col2)에 버튼 배치 ---
with col2:
    # 버튼을 배치합니다. 버튼은 입력창과 같은 높이에 있도록 st.button 앞에 약간의 공간을 줄 수도 있지만, 
    # 여기서는 간단하게 바로 버튼을 배치합니다. (Streamlit이 적절히 정렬합니다.)
    # 버튼이 입력창과 높이를 맞추도록 st.empty() 등을 사용하여 위쪽에 공간을 확보하는 트릭을 쓰기도 하지만, 
    # st.columns 내에서는 Streamlit이 어느 정도 맞춰줍니다.
    st.write("") # 버튼이 텍스트 입력창과 세로로 정렬되도록 공백(또는 CSS 트릭)을 추가하는 대신, 
                 # st.columns에서 바로 위젯을 넣으면 Streamlit이 알아서 중앙에 가깝게 배치합니다.
    is_clicked = st.button("생성", use_container_width=True) # use_container_width=True로 컬럼 폭에 맞게 버튼을 확장합니다.


# --- 4. 버튼 클릭 및 입력에 따른 메시지 출력 ---
if is_clicked and user_name:
    # 클릭 카운터 증가 및 풍선 효과 로직
    st.session_state.click_count += 1
    if st.session_state.click_count % 3 == 0:
        st.balloons() 
        
    greeting_message = f"**안녕하세요, {user_name}님!** 🌟 헬로 월드 (Hello World)! "
    st.success(greeting_message)
    st.write(f"Streamlit 웹 앱에 오신 것을 환영합니다. (클릭 횟수: {st.session_state.click_count})")

elif is_clicked and not user_name:
    st.warning("이름을 입력한 후에 버튼을 눌러주세요.")
