# Import necessary libraries and data
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def audience_builder_page():
    st.title("Audience Builder")
    # Load and display data
    data = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx")
    
    data_path = "data/Sales_PipeLine_Forecast_Model_2023.xlsx"
    sheet_name = "Audience Builder"
    data = pd.read_excel(data_path, sheet_name=sheet_name)
    
    st.write("Here is Audience Builder data:")
    st.write(data)

    # Create a simple plot
    st.subheader("Simple Plot")
    plt.plot(data["x"], data["y"])
    st.pyplot()

if __name__ == "__main__":
    audience_builder_page()
