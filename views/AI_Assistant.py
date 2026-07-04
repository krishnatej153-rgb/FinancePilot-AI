import streamlit as st

from services.gemini_service import ask_gemini
from database.dashboard_operations import get_financial_summary


def show_ai():

    st.title("🤖 AI Financial Coach")

    st.write(
        "Ask questions about your finances and receive AI-powered advice."
    )

    question = st.text_area(
        "Ask your question",
        placeholder="Example: How can I reduce my monthly expenses?"
    )

    if st.button("🚀 Generate Advice"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            financial_summary = get_financial_summary()

            with st.spinner("Analyzing your financial data..."):

                response = ask_gemini(
                    financial_summary,
                    question
                )

            st.success("AI Recommendation")

            st.write(response)

            with st.expander("📊 Financial Summary Sent to AI"):

                st.code(financial_summary)