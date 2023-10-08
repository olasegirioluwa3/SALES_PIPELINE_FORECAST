# Import necessary libraries and data
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def data_viz_page():
    st.title("Data Visualization Page")
    # Load and display data
    data = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx")
    
    data_path = "data/Sales_PipeLine_Forecast_Model_2023.xlsx"
    sheet_name = "SuperPixel"
    data = pd.read_excel(data_path, sheet_name=sheet_name)
    # excel_file_path = "your_excel_file.xlsx"  # Replace with your actual file path

    # Create an ExcelFile object
    xls = pd.ExcelFile(data_path)

    # SuperPixel
    # Wasted Spend Calculator
    # Audience Builder
    # Affiliate Program

    # Get the sheet names
    sheet_names = xls.sheet_names

    # Print or display the sheet names
    st.write("Sheet names in the Excel file:")
    for sheet_name in sheet_names:
        st.write(sheet_name)

    st.write("Here is some sample data:")
    st.write(data)

    # Create a simple plot
    st.subheader("Simple Plot")
    plt.plot(data["x"], data["y"])
    st.pyplot()

if __name__ == "__main__":
    data_viz_page()
