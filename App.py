import streamlit as st
from rag_core import rag_chat

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="College Admission Counselor",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ================= PROFESSIONAL LIGHT-DARK UI =================
st.markdown("""
<style>

/* RESET */
html, body {
    background: #F1F5F9 !important;
}

/* MAIN CONTAINER */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #F8FAFC 0%, #E2E8F0 100%) !important;
    color: #0F172A;
}

/* CENTER CONTENT */
.main {
    max-width: 720px;
    margin: auto;
    padding-top: 2rem;
}

/* HEADER */
h1 {
    font-weight: 700;
    text-align: center;
    color: #0F172A;
}
.stCaption {
    text-align: center;
    color: #475569;
}

/* CHAT BUBBLES */
.stChatMessage {
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 10px;
}

/* USER */
.stChatMessage[data-testid="stChatMessage-user"] {
    background: #2563EB !important;
    color: white;
}

/* ASSISTANT */
.stChatMessage[data-testid="stChatMessage-assistant"] {
    background: #F1F5F9 !important;
    border: 1px solid #E2E8F0;
    color: #0F172A;
}

/* INPUT */
textarea {
    background: white !important;
    border-radius: 12px !important;
    border: 1px solid #CBD5E1 !important;
    color: #0F172A !important;
    padding: 12px !important;
}

/* BUTTONS */
.stButton > button {
    background: #2563EB !important;
    color: white;
    border-radius: 10px;
    font-weight: 600;
}

/* REMOVE FOOTER */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.title("🎓 Admission Counselor")
st.caption("Professional AI guidance for college admissions")

# ================= SESSION STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome message
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello 👋 I’m your AI Admission Counselor. Feel free to ask about programs, fees, eligibility, or campus facilities."
    })

# ================= CHAT HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ================= INPUT =================
user_input = st.chat_input("Ask your admission question...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = rag_chat(user_input)
            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# ================= FOOTER =================
st.markdown(
    "<center style='color:#64748B; margin-top:20px;'>"
    "© 2026 • Built by <b>Waqas Gurmani</b>"
    "</center>",
    unsafe_allow_html=True
)
