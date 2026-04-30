import streamlit as st

st.set_page_config(page_title="感情ラベリング", page_icon="🧠", layout="centered")

st.title("🧠 感情ラベリング")
st.write("今の気持ちをすべて選んでください。")

emotions = [
    "寂しい",
    "悲しい",
    "不安",
    "怒り",
    "虚しい",
    "苦しい",
]

selected = st.multiselect(
    "感情を選択",
    emotions,
    placeholder="タップして選んでください"
)

if selected:
    st.subheader("📝 選択された感情")
    for e in selected:
        st.write(f"- **{e}**")

if st.button("リセット"):
    st.experimental_rerun()
