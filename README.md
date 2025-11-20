# UPDATED-portfolio-management-application-
Superstore EDA Dashboard

This project is an interactive analytics application built with Streamlit, Pandas, and Plotly.
It uses the classic Sample Superstore dataset and turns it into a clean, intuitive dashboard that lets you explore sales and profit trends without writing a single line of code.

The goal of the dashboard is simple:
make exploratory data analysis fast, visual, and actually enjoyable.

⭐ Features

Interactive filtering by Region, State, City, and Date Range

Category-wise and Region-wise Sales visualizations

Monthly/Yearly time-series analysis

Treemap hierarchy (Region → Category → Sub-Category)

Scatterplot of Sales vs Profit

Styled summary tables for quick insights

One-click CSV export for filtered datasets

Clean dark UI inspired by modern finance dashboards (JPMorgan/Goldman-style look)

🛠 Tech Stack

Python 3.12

Streamlit – front-end UI and layout

Pandas – data cleaning and processing

Plotly – interactive charts

Plotly Figure Factory – styled tables

🚀 How to Run the App

Install the required packages:

pip install streamlit pandas plotly


Launch the dashboard:

python -m streamlit run superstore_app.py


Once it starts, your browser will automatically open:

http://localhost:8501

📁 Dataset

You can:

Upload your own dataset through the UI (CSV, TXT, XLSX, XLS), or

Place a file named Superstore.csv in the project folder.

Expected fields include:

Order Date

Sales, Profit, Quantity

Region, State, City

Category, Sub-Category

Segment
