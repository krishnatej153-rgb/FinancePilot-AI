import streamlit as st

from components.cards import metric_card
from components.charts import show_chart

from database.dashboard_operations import (
    get_total_expenses,
    get_recent_transactions
)


def show_dashboard():

    st.title("🏠 Dashboard")

    st.write("Welcome back, Krishna!")

    # Get data from database FIRST
    total_expenses = get_total_expenses()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("💰 Balance", f"₹{-total_expenses:.2f}")

    with col2:
        metric_card("💸 Expenses", f"₹{total_expenses:.2f}")

    with col3:
        metric_card("💵 Income", "₹0")

    with col4:
        metric_card("🎯 Savings", "Coming Soon")

    st.divider()

    show_chart()

    st.divider()

    st.subheader("🕒 Recent Transactions")

    transactions = get_recent_transactions()

    if transactions:
        st.table(transactions)
    else:
        st.info("No transactions yet.")