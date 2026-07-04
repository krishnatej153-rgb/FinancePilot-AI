import streamlit as st

from services.gemini_service import ask_gemini
from database.dashboard_operations import get_financial_summary


def show_ai():

    st.title("🤖 FinancePilot AI Coach")
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    financial_summary = get_financial_summary()

    for role, message in st.session_state.chat_history:

        with st.chat_message(role):
            st.markdown(message)

    question = st.chat_input(
        "Ask about your finances..."
    )

    if question:

        st.session_state.chat_history.append(
            ("user", question)
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Analyzing your finances..."):

                response = ask_gemini(
                    financial_summary,
                    question
                )

                st.markdown(response)

        st.session_state.chat_history.append(
            ("assistant", response)
        )