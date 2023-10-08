import streamlit as st

def data_entry_page():
    st.title("Data Entry Page")
    st.write("Enter data here:")
    # Create input fields for data entry
    x_value = st.number_input("Enter x value:")
    y_value = st.number_input("Enter y value:")

    # Save entered data to a file or database
    if st.button("Save Data"):
        # Code to save data goes here
        st.success("Data saved successfully!")

if __name__ == "__main__":
    data_entry_page()
