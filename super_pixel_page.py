# Import necessary libraries and data
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def super_pixel_page():
    st.title("SuperPixel")
    # Load and display data
    data = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx")
    
    data_path = "data/Sales_PipeLine_Forecast_Model_2023.xlsx"
    sheet_name = "SuperPixel"
    data = pd.read_excel(data_path, sheet_name=sheet_name)
    # SuperPixel

    st.write("Here is SuperPixel data:")
    st.write(data)

    # Create a simple plot
    st.subheader("Simple Plot")
    plt.plot(data["x"], data["y"])
    st.pyplot()

if __name__ == "__main__":
    super_pixel_page()
