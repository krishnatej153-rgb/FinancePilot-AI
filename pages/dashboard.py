import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="🏠")

st.title("🏠 Dashboard")

st.write("Welcome back, Krishna!")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Balance", "₹0")

with col2:
    st.metric("💸 Expenses", "₹0")

with col3:
    st.metric("💵 Income", "₹0")

with col4:
    st.metric("🎯 Savings", "₹0")

st.markdown("---")

st.subheader("📊 Monthly Overview")

st.info("Charts will appear here after adding transactions.")

st.markdown("---")

st.subheader("🕒 Recent Transactions")

st.write("No transactions yet.")