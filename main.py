import streamlit as st
import home
import data_viz
import ml
import data_entry
import about

# Create a dictionary to store the page names and corresponding functions
pages = {
    "Home": home.main,
    "Data Visualization": data_viz.data_viz_page,
    "Machine Learning": ml.ml_page,
    "Data Entry": data_entry.data_entry_page,
    "About": about.about_page
}

def main():
    st.sidebar.title("Navigation")
    # Create a sidebar menu to navigate between pages
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Call the selected page's function
    pages[]

if __name__ == "__main__":
    main()
