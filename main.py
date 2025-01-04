import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# 데이터 로드
df = pd.read_csv('total_fertility.csv')

st.title("대한민국 합계 출산율 분석")
st.text("\n\n")
st.write("한국의 출산율은 경제협력개발기구(OECD) 회원국 중 압도적으로 꼴찌다. 지난 2013년부터 11년째 최하위를 기록 중이며, OECD 평균(1.58명)의 절반에도 미치지 못한다.")
st.text("\n\n")
st.text("\n\n")
# 사이드바에 시각화 옵션 추가
visualization_option = st.sidebar.selectbox(
    "시각화 선택",
    ["선 그래프", "막대 그래프", "산점도", "데이터 테이블"]
)

# 연도 범위 선택
year_range = st.sidebar.slider(
    "연도 범위 선택",
    min_value=int(df['연도'].min()),
    max_value=int(df['연도'].max()),
    value=(1970, 2023)
)

# 데이터 필터링
filtered_df = df[(df['연도'] >= year_range[0]) & (df['연도'] <= year_range[1])]

if visualization_option == "선 그래프":
    st.subheader("연도별 합계출산율 추이")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(filtered_df['연도'], filtered_df['합계출산율(명)'], marker='o')
    ax.set_xlabel('연도')
    ax.set_ylabel('합계출산율(명)')
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif visualization_option == "막대 그래프":
    st.subheader("연도별 출생아 수")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(filtered_df['연도'], filtered_df['출생아수(명)'])
    ax.set_xlabel('연도')
    ax.set_ylabel('출생아 수(명)')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif visualization_option == "산점도":
    st.subheader("출생아 수와 합계출산율의 관계")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(filtered_df['출생아수(명)'], filtered_df['합계출산율(명)'])
    ax.set_xlabel('출생아 수(명)')
    ax.set_ylabel('합계출산율(명)')
    st.pyplot(fig)

else:
    st.subheader("원본 데이터")
    st.dataframe(filtered_df)

# 주요 통계 표시
st.subheader("주요 통계")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "현재 합계출산율",
        f"{filtered_df['합계출산율(명)'].iloc[-1]:.3f}명"
    )

with col2:
    st.metric(
        "최고 합계출산율",
        f"{filtered_df['합계출산율(명)'].max():.3f}명"
    )

with col3:
    st.metric(
        "최저 합계출산율",
        f"{filtered_df['합계출산율(명)'].min():.3f}명"
    )

# 데이터 다운로드 버튼
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="CSV 파일 다운로드",
    data=csv,
    file_name="출산율_데이터.csv",
    mime="text/csv"
)
