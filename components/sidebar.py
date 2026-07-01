import streamlit as st


def show_sidebar():
    st.sidebar.title("💰 FinancePilot AI")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Expenses",
            "Income",
            "Analytics",
            "AI Assistant",
            "Settings"
        ]
    )

    return page