import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Data Visualization App", layout="wide")
st.title("Data Visualization App")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())

    st.sidebar.header("Visualization Settings")
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])
    x_axis = st.sidebar.selectbox("Select X-axis", df.columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", df.columns)

    if chart_type == "Line Chart":
        fig, ax = plt.subplots()
        ax.plot(df[x_axis], df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig)

    elif chart_type == "Bar Chart":
        fig, ax = plt.subplots()
        ax.bar(df[x_axis], df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig)

    elif chart_type == "Scatter Plot":
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
        st.plotly_chart(fig)