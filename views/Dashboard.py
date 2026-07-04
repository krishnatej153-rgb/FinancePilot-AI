import streamlit as st

from components.cards import metric_card
from components.charts import show_chart

from database.dashboard_operations import (
    get_dashboard_summary,
    get_recent_transactions
)

from services.health_score import calculate_health_score


def show_dashboard():

    st.title("🏠 Dashboard")

    st.write("Welcome back, Krishna!")

    summary = get_dashboard_summary()

    health = calculate_health_score(
        summary["income"],
        summary["expenses"]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("💰 Balance", f"₹{summary['balance']:.2f}")

    with col2:
        metric_card("💸 Expenses", f"₹{summary['expenses']:.2f}")

    with col3:
        metric_card("💵 Income", f"₹{summary['income']:.2f}")

    with col4:
        metric_card("🎯 Savings", f"₹{summary['savings']:.2f}")

    st.divider()

    st.subheader("🏥 Financial Health")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Health Score", f"{health['score']}/100")

    with col2:
        st.metric("Status", health["status"])

    st.progress(health["score"] / 100)

    st.info(
        f"💡 {health['recommendation']}\n\n"
        f"💰 Savings Rate: {health['savings_rate']}%"
    )

    st.divider()

    show_chart()

    st.divider()

    st.subheader("🕒 Recent Transactions")

    transactions = get_recent_transactions()

    if transactions:
        st.table(transactions)
    else:
        st.info("No transactions yet.")