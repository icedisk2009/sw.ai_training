
import streamlit as st
import pandas as pd

# 데이터 불러오기
data = {
    "행정구역별": [
        "전국", "서울특별시", "부산광역시", "대구광역시", "인천광역시", "광주광역시",
        "대전광역시", "울산광역시", "세종특별자치시", "경기도", "강원특별자치도",
        "충청북도", "충청남도", "전북특별자치도", "전라남도", "경상북도",
        "경상남도", "제주특별자치도"
    ],
    "고령인구비율 (%)": [
        18.6, 18.3, 22.4, 19.4, 16.4, 16.3, 16.6, 15.7, 10.5, 15.4,
        23.4, 19.9, 20.1, 23.4, 25.4, 23.8, 20.0, 17.5
    ],
    "65세이상인구 (명)": [
        9608981, 1714624, 733701, 462548, 495272, 237330,
        244415, 173398, 40741, 2122758,
        357924, 326972, 446264, 413812, 450865,
        615461, 654605, 118291
    ],
    "전체인구 (명)": [
        51774521, 9384512, 3279604, 2379188, 3025950,
        1457090, 1470336, 1107432, 386261,
        13815367, 1528014, 1641481,
        2216332, 1768491, 1776668,
        2589880, 3271148, 676767
    ]
}

df = pd.DataFrame(data)

# Streamlit 앱 구성
st.title('🚀 한국 사회: 실버 ATTACK에 대비하라! 🚀')
st.write(
    """
    한국은 빠르게 다가오는 고령화 시대의 한가운데에 있습니다.
    출산율은 낮아지고 연로한 인구는 증가하는 이 복잡한 여정 속에서,
    우리는 어떤 미래를 만들어 나가야 할까요?
    """
)

st.subheader("📊 행정구역별 고령화 데이터")
st.dataframe(df)

st.subheader("🔍 주요 통계")
total_population = df["전체인구 (명)"].sum()
elderly_population = df["65세이상인구 (명)"].sum()
elderly_ratio = (elderly_population / total_population) * 100

st.write(f"**전국 총 인구:** {total_population:,}명")
st.write(f"**전국 고령 인구:** {elderly_population:,}명")
st.write(f"**전국 고령 인구 비율:** {elderly_ratio:.2f}%")

# 고령화 비율 상위 지역 필터링
st.subheader("🏆 고령화 비율 상위 지역")
top_elderly_regions = df.nlargest(5, "고령인구비율 (%)")[["행정구역별", "고령인구비율 (%)"]]
st.table(top_elderly_regions)

# 사용자 입력: 특정 지역 검색
st.subheader("🔎 특정 지역 정보 검색")
selected_region = st.selectbox("지역을 선택하세요:", df["행정구역별"])
region_data = df[df["행정구역별"] == selected_region]

if not region_data.empty:
    st.write(f"**{selected_region}의 고령화 데이터:**")
    st.write(region_data)
