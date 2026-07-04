import streamlit as st

from database.income_operations import (
    add_income,
    get_income,
    delete_income
)


def show_income():

    st.title("💵 Income Manager")

    with st.form("income_form"):

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=1.0
        )

        source = st.selectbox(
            "Income Source",
            [
                "Salary",
                "Freelancing",
                "Investment",
                "Business",
                "Other"
            ]
        )

        description = st.text_input("Description")

        date = st.date_input("Date")

        submitted = st.form_submit_button("💾 Save Income")

    if submitted:

        add_income(
            amount,
            source,
            description,
            str(date)
        )

        st.success("Income Added Successfully!")

        st.rerun()

    st.divider()

    st.subheader("Income Records")

    income = get_income()

    if income:

        for record in income:

            col1, col2, col3, col4, col5, col6 = st.columns([1,2,2,3,2,1])

            with col1:
                st.write(record[0])

            with col2:
                st.write(f"₹{record[1]:.2f}")

            with col3:
                st.write(record[2])

            with col4:
                st.write(record[3])

            with col5:
                st.write(record[4])

            with col6:

                if st.button("🗑️", key=f"income_{record[0]}"):

                    delete_income(record[0])

                    st.rerun()

    else:

        st.info("No income records yet.")