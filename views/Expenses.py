import streamlit as st

def show_expenses():

    st.title("💸 Expense Tracker")

    if "expenses" not in st.session_state:
        st.session_state.expenses = []

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

        expense = {
            "Amount": amount,
            "Category": category,
            "Description": description,
            "Date": str(date)
        }

        st.session_state.expenses.append(expense)

        st.success("Expense Added Successfully!")

    st.divider()

    st.subheader("Saved Expenses")

    if st.session_state.expenses:

        st.dataframe(st.session_state.expenses)

    else:

        st.info("No expenses added yet.")