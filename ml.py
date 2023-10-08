# Import necessary libraries and ML model
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def ml_page():
    st.title("Machine Learning Page")
    # Load and display data
    data = pd.read_excel("data/Sales_PipeLine_Forecast_Model_2023.xlsx")
    st.write("Here is some sample data:")
    st.write(data)

    # Train a simple ML model
    st.subheader("Simple Linear Regression")
    X = data["x"].values.reshape(-1, 1)
    y = data["y"].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Display model's performance
    st.write("Model R-squared:", model.score(X_test, y_test))

if __name__ == "__main__":
    ml_page()
