# Import necessary libraries and data
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def affiliate_program_page():
    st.title("Affiliate Program")
    # Load and display data
    data = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx")
    
    data_path = "data/Sales_PipeLine_Forecast_Model_2023.xlsx"
    sheet_name = "Affiliate Program"
    data = pd.read_excel(data_path, sheet_name=sheet_name)

    st.write("Here is Affiliate Program data:")
    st.write(data)

    # Create a simple plot
    st.subheader("Simple Plot")
    plt.plot(data["x"], data["y"])
    st.pyplot()

if __name__ == "__main__":
    affiliate_program_page()

