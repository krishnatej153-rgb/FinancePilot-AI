import streamlit as st
import plotly.express as px

from database.dashboard_operations import (
    get_total_expenses,
    get_category_expenses,
    get_highest_category
)


def show_analytics():

    st.title("📊 Analytics")

    total = get_total_expenses()

    category_data = get_category_expenses()

    highest = get_highest_category()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💸 Total Expenses", f"₹{total:.2f}")

    with col2:
        st.metric("📂 Categories", len(category_data))

    with col3:
        if highest:
            st.metric("🏆 Highest Category", highest[0])
        else:
            st.metric("🏆 Highest Category", "-")

    st.divider()

    if category_data:

        categories = []
        amounts = []

        for category, amount in category_data:
            categories.append(category)
            amounts.append(amount)

        pie = px.pie(
            names=categories,
            values=amounts,
            hole=0.45,
            title="Expense Distribution"
        )

        st.plotly_chart(pie, use_container_width=True)

        bar = px.bar(
            x=categories,
            y=amounts,
            title="Category Spending"
        )

        st.plotly_chart(bar, use_container_width=True)

    else:
        st.info("No expense data available.")