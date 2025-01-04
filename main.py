import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("대한민국 합계 출산율 분석")
st.write("한국의 출산율은 경제협력개발기구(OECD) 회원국 중 압도적으로 꼴찌다. 지난 2013년부터 11년째 최하위를 기록 중이며, OECD 평균(1.58명)의 절반에도 미치지 못한다.")


years = list(range(2015, 2025))
regions = ["서울", "경기", "인천", "부산", "대구"]
data = {
    "년도": np.repeat(years, len(regions)),
    "지역": regions * len(years),
    "PM10 평균 농도 (µg/m³)": np.random.randint(20, 100, size=len(years) * len(regions)),
}

df = pd.DataFrame(data)

# 데이터 표시
st.subheader("데이터 미리보기")
st.write(df.head())

# 지역별 PM10 평균 농도 변화 시각화
st.subheader("지역별 PM10 평균 농도 변화")
selected_region = st.selectbox("지역 선택", regions)
filtered_data = df[df["지역"] == selected_region]

fig, ax = plt.subplots()
ax.plot(filtered_data["년도"], filtered_data["PM10 평균 농도 (µg/m³)"], marker="o")
ax.set_title(f"{selected_region}의 PM10 평균 농도 변화")
ax.set_xlabel("년도")
ax.set_ylabel("PM10 평균 농도 (µg/m³)")
st.pyplot(fig)

# 전국 평균 PM10 농도 변화 시각화
st.subheader("전국 평균 PM10 농도 변화")
national_avg = df.groupby("년도")["PM10 평균 농도 (µg/m³)"].mean()

fig2, ax2 = plt.subplots()
ax2.plot(national_avg.index, national_avg.values, marker="o", color="orange")
ax2.set_title("전국 PM10 평균 농도 변화")
ax2.set_xlabel("년도")
ax2.set_ylabel("PM10 평균 농도 (µg/m³)")
st.pyplot(fig2)

# 데이터 다운로드 기능 추가
st.subheader("데이터 다운로드")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="CSV 파일 다운로드",
    data=csv,
    file_name="미세먼지_데이터.csv",
    mime="text/csv",
)
