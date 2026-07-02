import streamlit as st

from database.db import create_tables

from components.sidebar import show_sidebar

from views.Dashboard import show_dashboard
from views.Expenses import show_expenses
from views.Income import show_income
from views.Analytics import show_analytics
from views.AI_Assistant import show_ai
from views.Settings import show_settings

# Streamlit page configuration FIRST
st.set_page_config(
    page_title="FinancePilot AI",
    page_icon="💰",
    layout="wide"
)

# Then create the database and tables
create_tables()

# Sidebar
page = show_sidebar()

# Navigation
if page == "Dashboard":
    show_dashboard()

elif page == "Expenses":
    show_expenses()

elif page == "Income":
    show_income()

elif page == "Analytics":
    show_analytics()

elif page == "AI Assistant":
    show_ai()

elif page == "Settings":
    show_settings()