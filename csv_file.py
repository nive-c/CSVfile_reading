import streamlit as st
import pandas as pd
import plotly.express as px

#psge setup
st.set_page_config(page_title="Data viewer with csv",layout="wide")

st.title("CSV data viewer with charts")
st.write("Upload a CSV file to view  visualize the data with charts")

upload_file=st.file_uploader("upload a csv file", type="csv")

if upload_file:
    df= pd.read_csv(upload_file)
    st.success("Data uploaded successfully!")

    st.subheader("Data Preview")
    st.dataframe(df.head())

    all_columns= df.columns.tolist()
    x_axis= st.selectbox("Select X-axis", all_columns)

    numeric_cols= df.select_dtypes(include='number').columns.tolist()
    y_axis= st.selectbox("Select Y-axis", numeric_cols)

    st.subheader("Chart Settings")
    chart_type= st.radio("Select chart type", ("Bar chart", "Pie Chart"))

    if chart_type == "Bar chart":
        st.subheader("Bar Chart")
        fig= px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Pie Chart":
        st.subheader("Pie Chart")
        fig= px.pie(df, names=x_axis, values=y_axis, title=f"{y_axis} distribution by {x_axis}")
        st.plotly_chart(fig, use_container_width=True)


else:
    st.info("Upload a CSV file to begin")