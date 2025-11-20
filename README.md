# MOST UPDATED (needed to make changes to UI!)-portfolio-management-application-
README 

This EDA Dashboard is a lightweight, interactive analytics application built with Streamlit, Plotly, and Pandas. It’s designed to make exploring the Sample Superstore dataset simple and intuitive. I wanted to create something that could give users the ability to filter data by region, state, city, and date range while instantly updating all visualizations on the screen. The dashboard includes category level and region level sales information, a time series view of the monthly performance, a hierarchical treemap for drilling down into product segments, and a scatterplot that shows the relationship between sales and profit. All tables are styled for readability, and any filtered dataset can be downloaded with one click. The layout follows a clean, modern dark-theme aesthetic inspired by professional finance dashboards. The app runs entirely locally, requires no external APIs, and accepts both uploaded files and a bundled Superstore.csv dataset. By combining quick interaction with clear visuals, this project offers a fast and user-friendly way to perform exploratory data analysis without writing a single line of code.


How to Run This Project
✅ 1. Install Python (Required)

✅ 2. Download the Project

If the repo is public:
git clone https://github.com/codefor4fun888/codefor4fun888.git
cd codefor4fun888

Or you can  — Download ZIP

Go to GitHub repo

Click Code → Download ZIP

Extract the folder

Open the extracted folder in VS Code or Terminal

✅ 3. Open a Terminal inside the project folder

On Windows:

Right-click inside the folder

Click Open in Terminal or Open PowerShell window here

You should see something like:

PS C:\Users\YourName\Desktop\codefor4fun888>

✅ 4. Install Required Python Libraries

This project needs:

Streamlit

Plotly

Pandas

Run this command:
pip install streamlit pandas plotly


OR (if you include requirements.txt in repo):

pip install -r requirements.txt

✅ 5. Add the Dataset

The dashboard needs data.

You have two options:

Option A — Upload a file through the app

When you run it, you'll see an upload button for CSV/XLSX.

Option B — Use the default file

Place your dataset in the project folder and name it:

Superstore.csv

✅ 6. Run the Application

Now start the app by typing:

streamlit run superstore_app.py


If Streamlit installed correctly, the browser will open automatically.

If not, manually visit:

👉 http://localhost:8501

✅ 7. Use the Dashboard

You will now see:

Filters (Region, State, City, Dates)

Sales charts

Profit analysis

Treemaps

Time-series visualizations

CSV download buttons

Everything is interactive.

⚠️ If “streamlit not recognized” Happens

Run this:

python -m streamlit run superstore_app.py



Dashboard opens at:
http://localhost:8501


http://localhost:8501
