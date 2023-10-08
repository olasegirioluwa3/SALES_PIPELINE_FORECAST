# Import necessary libraries and data
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def wasted_spend_calculator_page():
    st.title("Wasted Spend Calculator")
    # Load and display data
    data = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx")
    
    data_path = "data/Sales_PipeLine_Forecast_Model_2023.xlsx"
    sheet_name = "Wasted Spend Calculator"
    data = pd.read_excel(data_path, sheet_name=sheet_name)
    # excel_file_path = "your_excel_file.xlsx"  # Replace with your actual file path

    # Audience Builder
    # Affiliate Program

    st.write("Here is Wasted Spend Calculator data:")
    st.write(data)

    # Create a simple plot
    st.subheader("Simple Plot")
    plt.plot(data["x"], data["y"])
    st.pyplot()

if __name__ == "__main__":
    wasted_spend_calculator_page()
