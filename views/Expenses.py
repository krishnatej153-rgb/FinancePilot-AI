import streamlit as st

from database.expense_operations import add_expense, get_expenses


def show_expenses():

    st.title("💸 Expense Tracker")

    with st.form("expense_form"):

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=1.0
        )

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Travel",
                "Shopping",
                "Bills",
                "Entertainment",
                "Health",
                "Other"
            ]
        )

        description = st.text_input("Description")

        date = st.date_input("Date")

        submitted = st.form_submit_button("💾 Save Expense")

    if submitted:

        add_expense(
            amount,
            category,
            description,
            str(date)
        )

        st.success("Expense Added Successfully!")

    st.divider()

    st.subheader("Saved Expenses")

    expenses = get_expenses()

    if expenses:

        st.dataframe(
            expenses,
            column_config={
                0: "ID",
                1: "Amount",
                2: "Category",
                3: "Description",
                4: "Date"
            },
            hide_index=True
        )

    else:

        st.info("No expenses found.")