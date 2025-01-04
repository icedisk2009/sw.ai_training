import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc

# 한글 폰트 설정 (맑은 고딕 사용)
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows 환경
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# CSV 파일 읽기
file_path = "noiningu.csv"  # 파일 경로 설정
df = pd.read_csv(file_path)

# 데이터 확인 및 전처리
df.columns = df.columns.str.strip()  # 컬럼명 공백 제거

# Streamlit 앱 구성
st.title('🚀 한국 사회: 실버 ATTACK에 대비하라! 🚀')
st.write(
    """
    한국은 빠르게 다가오는 고령화 시대의 한가운데에 있습니다.
    출산율은 낮아지고 연로한 인구는 증가하는 이 복잡한 여정 속에서,
    우리는 어떤 미래를 만들어 나가야 할까요?
    """
)

# 여백 추가를 위해 빈 줄 삽입
st.text("\n")

st.subheader("📊 행정구역별 고령화 데이터")
st.dataframe(df)

# 여백 추가
st.text("\n")

st.subheader("🔍 주요 통계")
total_population = df["전체인구 (명)"].sum()
elderly_population = df["65세이상인구 (명)"].sum()
elderly_ratio = (elderly_population / total_population) * 100

st.write(f"**전국 총 인구:** {total_population:,}명")
st.write(f"**전국 고령 인구:** {elderly_population:,}명")
st.write(f"**전국 고령 인구 비율:** {elderly_ratio:.2f}%")

# 여백 추가
st.text("\n")

# 고령화 비율 상위 지역 필터링
st.subheader("🏆 고령화 비율 상위 지역")
top_elderly_regions = df.nlargest(5, "고령인구비율 (%)")[["행정구역별", "고령인구비율 (%)"]]
st.table(top_elderly_regions)

# 여백 추가
st.text("\n")

# 사용자 입력: 특정 지역 검색
st.subheader("🔎 특정 지역 정보 검색")
selected_region = st.selectbox("지역을 선택하세요:", df["행정구역별"])
region_data = df[df["행정구역별"] == selected_region]

if not region_data.empty:
    st.write(f"**{selected_region}의 고령화 데이터:**")
    st.write(region_data)

# 여백 추가
st.text("\n")

# 막대그래프 시각화 (Seaborn으로 색상 개선)
st.subheader("📊 행정구역별 고령화 비율 비교")
fig, ax = plt.subplots(figsize=(12, 7))
sns.barplot(
    x="행정구역별",
    y="고령인구비율 (%)",
    data=df,
    palette="coolwarm",
    ax=ax
)
ax.set_title("행정구역별 고령인구비율 (%)", fontsize=16)
ax.set_xlabel("행정구역", fontsize=12)
ax.set_ylabel("고령인구비율 (%)", fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig)
