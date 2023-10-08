import streamlit as st
from streamlit import components

# Import the individual page files
import home
import super_pixel_page
import wasted_spend_calculator_page
import audience_builder_page
import affiliate_program_page
import data_entry
import data_viz
import ml

# Create a SessionState class for managing page state
class SessionState:
    def __init__(self):
        self.page = "Home"  # Default page is Home

# Create a shared session state
session_state = SessionState()

# Define the page names and their corresponding functions
pages = {
    "Home": home.main,
    "Super Pixel Page": super_pixel_page.super_pixel_page,
    "Wasted Spend Calculator": wasted_spend_calculator_page.wasted_spend_calculator_page,
    "Audience Builder": audience_builder_page.audience_builder_page,
    "Affiliate Program": affiliate_program_page.affiliate_program_page,
    "Data Entry": data_entry.data_entry_page,
    "Data VIZ": data_viz.data_viz_page,
    "Machine Learning": ml,
}

# Create the horizontal navbar
st.sidebar.title("Sales Forecast Model")
selected_page = st.sidebar.radio("Go to", list(pages.keys()))
session_state.page = selected_page

# Display the selected page
pages[session_state.page]()
