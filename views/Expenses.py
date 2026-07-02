import streamlit as st


from database.expense_operations import (
    add_expense,
    get_expenses,
    delete_expense,
    search_expenses
)


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
        st.rerun()

        st.success("Expense Added Successfully!")

    st.divider()

    st.subheader("Saved Expenses")

    search = st.text_input("🔍 Search Expenses")

    if search:
        expenses = search_expenses(search)
    else:
        expenses = get_expenses()

    if expenses:

        for expense in expenses:

            col1, col2, col3, col4, col5, col6 = st.columns(
                [1, 2, 2, 3, 2, 1]
            )

            with col1:
                st.write(expense[0])

            with col2:
                st.write(f"₹{expense[1]}")

            with col3:
                st.write(expense[2])

            with col4:
                st.write(expense[3])

            with col5:
                st.write(expense[4])

            with col6:

                if st.button("🗑️", key=f"del_{expense[0]}"):

                    delete_expense(expense[0])

                    st.rerun()

    else:

        st.info("No expenses found.")