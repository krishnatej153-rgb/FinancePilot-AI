import streamlit as st

from components.cards import metric_card
from components.charts import show_chart


def show_dashboard():

    st.title("🏠 Dashboard")

    st.write("Welcome back, Krishna!")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("💰 Balance", "₹0")

    with col2:
        metric_card("💸 Expenses", "₹0")

    with col3:
        metric_card("💵 Income", "₹0")

    with col4:
        metric_card("🎯 Savings", "₹0")

    st.divider()

    show_chart()

    st.divider()

    st.subheader("🕒 Recent Transactions")

    st.info("No transactions yet.")