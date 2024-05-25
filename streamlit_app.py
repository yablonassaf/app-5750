import streamlit as st
import pandas as pd

# Set the title of the app-main
st.title("DATS 5750 Project 1")

# Create a sidebar menu
st.sidebar.header("Menu")
option = st.sidebar.selectbox("Select an option:", ["Home", "About", "Data"])

# Display content based on the selected option
if option == "Home":
    st.header("Welcome to DATS 5750 Project 1")
    st.write("This is a basic Streamlit app-main for data visualization and analysis.")

elif option == "About":
    st.header("About the Project")
    st.write("This project aims to explore app-main deployments on GCP.")

elif option == "Data":
    st.header("Data Exploration")

    # Load sample data
    data = {
        'Name': ['John', 'Alice', 'Bob', 'Emily'],
        'Age': [25, 30, 28, 22],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    df = pd.DataFrame(data)

    # Display the data in a table
    st.table(df)

# Footer
st.write("Created by Assaf Yablon")