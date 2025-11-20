# UPDATED-portfolio-management-application-
A Streamlit-powered interactive analytics application, This project is an interactive Exploratory Data Analysis (EDA) dashboard built using Python, Streamlit, and Plotly.
Superstore EDA Dashboard

This project is an interactive analytics dashboard built with Streamlit and Plotly. It uses the Sample Superstore dataset to explore sales, profit, product categories, and regional trends through a set of dynamic visualizations and filters.

The goal of the dashboard is to make exploratory data analysis quick, visual, and intuitive without needing to write code.

Features : 

Interactive filters for Region, State, City, and Date Range

Category-wise and Region-wise Sales breakdowns

Time-series analysis (Sales by Month/Year)

Treemap hierarchy (Region → Category → Sub-Category)

Sales vs. Profit scatterplot

Summary tables with styling

CSV export for any filtered dataset

Clean UI with a dark theme inspired by modern finance dashboards

Tech Stack

- Python 3.12

- Streamlit for UI

- Pandas for data processing

- Plotly for charts

- Figure Factory for styled tables

Running the App

Install dependencies:

pip install streamlit pandas plotly


Start the Streamlit server:

python -m streamlit run superstore_app.py


Your browser will open the dashboard automatically at:

http://localhost:8501

Dataset

You can upload your own file through the UI (CSV, TXT, XLSX, XLS),
or place a local file named Superstore.csv in the project folder.

Expected fields include:

Order Date, Sales , Profit , Quantity , Region / State / City , Category / Sub-Category ,Segment


The dashboard was designed to be minimal, clean, and easy to use.

Layout and styling were tweaked to give it a more enterprise-grade look (similar to internal dashboards used at large financial firms).

No external APIs or cloud services are required.
