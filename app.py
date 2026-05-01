import streamlit as st
import random

st.set_page_config(page_title="感情ラベリング", page_icon="🧠", layout="centered")

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
    "寂しい",
    "悲しい",
    "不安",
    "怒り",
    "虚しい",
    "苦しい",
    "疲れた",
    "モヤモヤ",
]

# セッション状態に選択を保持
if "selected_emotions" not in st.session_state:
    st.session_state.selected_emotions = []

selected = st.multiselect(
    "いまの感情を選択",
    emotions,
    default=st.session_state.selected_emotions,
    placeholder="タップして選んでね",
    key="emotion_multiselect",
)

# 毎回セッションに反映
st.session_state.selected_emotions = selected

messages = [
    "大波のあとは凪になって落ち着くよ",
    "大切にされていい人だからね。自分を粗末にしないで",
    "抱えすぎないで、肩の力を抜いてみよ",
    "「あなたはあなたの時間」があり「私は私の時間」がある。それぞれがそれぞれの時空を持っている（「森と心」",
    "価値に気づくことで目の前の些細な、自分の価値とは無関係のことには振り回されなくなります（「「人の期待」に縛られないレッスン」）",
    "他人を嫌うこと、他人をいじめることは、いつの間にか自分を深く傷つけることになるのだ。だから、人に優しく関わるチャンスを無視したり、ないがしろにしたりすると、結局自分が損をする（「本当にわかる心理学」）",
    "一回深呼吸して、間をあけてみよう",
    "今日は優しく自分を扱ってあげてね",
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

# リセットボタン：選択を空にする
if st.button("リセット"):
    st.session_state.selected_emotions = []
    st.session_state.emotion_multiselect = []
    st.rerun()
