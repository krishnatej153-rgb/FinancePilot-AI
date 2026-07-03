import streamlit as st
import plotly.express as px

from database.dashboard_operations import get_category_expenses


def show_chart():

    data = get_category_expenses()

    if not data:
        st.info("No expense data available.")
        return

    categories = []
    amounts = []

    for category, amount in data:
        categories.append(category)
        amounts.append(amount)

    fig = px.pie(
    names=categories,
    values=amounts,
    title="Expense Distribution",
    hole=0.45
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(fig, use_container_width=True)