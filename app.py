import streamlit as st
import random

st.set_page_config(page_title="感情ラベリング", page_icon="🧠", layout="centered")

# --- CSS ---
st.markdown("""
<style>
.custom-title {
    font-size: 1.8rem;
    font-weight: 700;
}
.blue-box {
    padding: 18px;
    border-radius: 10px;
    background-color: #e8f4ff;
    border: 1px solid #bcdfff;
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 20px;
}
.blue-title {
    font-weight: bold;
    margin-bottom: 8px;
    font-size: 1.15rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-title">🧠 感情ラベリング</div>', unsafe_allow_html=True)
st.write("今の気持ちをすべて選んでね")

emotions = [
    "寂しい", "悲しい", "不安", "怒り",
    "虚しい", "苦しい", "疲れた", "モヤモヤ",
]

# --- セッション状態 ---
if "selected" not in st.session_state:
    st.session_state.selected = []

# --- UI ---
selected = st.multiselect(
    "いまの感情を選択",
    emotions,
    default=st.session_state.selected,
    placeholder="タップして選んでね",
)

# 選択を state に反映
st.session_state.selected = selected

messages = [
    "大波のあとは凪になって落ち着くよ",
    "大切にされていい人だからね。自分を粗末にしないで",
    "抱えすぎないで、肩の力を抜いてみよ",
    "「あなたはあなたの時間」があり「私は私の時間」がある（「森と心」）",
    "価値に気づくことで些細なことに振り回されなくなる（「「人の期待」に縛られなくなるレッスン」）",
    "人に優しくすることは、結局自分を守ることにもなる",
    "一回深呼吸して、間をあけてみよう",
    "今は優しく自分を扱ってあげてね",
]

if selected:
    message = random.choice(messages)
    st.markdown(
        f"""
        <div class="blue-box">
            <div class="blue-title">🍀そっと寄り添うひとこと🍀</div>
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )

# --- リセット ---
if st.button("リセット"):
    st.session_state.selected = []   # ← widget key は触らない
    st.rerun()
