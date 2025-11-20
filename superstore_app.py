import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_title="Portfolio Analytics", layout="wide")

st.markdown("""
<style>
/* GLOBAL FONT */
html, body, [class*="css"] {
    font-family: 'Merriweather', serif !important;
}

/* Background Colors */
body {
    background-color: #0E1117;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0D0F14;
    border-right: 1px solid #2A2D35;
}

h1, h2, h3, h4 {
    color: #C5A572 !important;        /* Gold title color */
}

label, .stMarkdown, .stText, .css-16idsys {
    color: #E8E8E8 !important;
}

/* Buttons */
.stDownloadButton button, .stButton button {
    background-color: #C5A572 !important;
    color: black !important;
    border-radius: 6px;
    border: none;
}

/* Card-like expanders */
.streamlit-expanderHeader {
    background-color: #1A1D24 !important;
    color: #C5A572 !important;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

st.title("📊 Portfolio Analytics — Executive Dashboard")


# DATA LOAD

fl = st.file_uploader("Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")
else:
    os.chdir(r"C:\\Users\\erich\\OneDrive\\Desktop\\python project")
    df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")

col1, col2 = st.columns((2))
df["Order Date"] = pd.to_datetime(df["Order Date"])

startDate = df["Order Date"].min()
endDate = df["Order Date"].max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))
with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()


# SIDEBAR FILTERS

st.sidebar.header("Filters")

region = st.sidebar.multiselect("Region", df["Region"].unique())
df2 = df[df["Region"].isin(region)] if region else df.copy()

state = st.sidebar.multiselect("State", df2["State"].unique())
df3 = df2[df2["State"].isin(state)] if state else df2.copy()

city = st.sidebar.multiselect("City", df3["City"].unique())

if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df["Region"].isin(region)]
elif not region and not city:
    filtered_df = df[df["State"].isin(state)]
elif state and city:
    filtered_df = df3[df3["State"].isin(state) & df3["City"].isin(city)]
elif region and city:
    filtered_df = df3[df3["Region"].isin(region) & df3["City"].isin(city)]
elif region and state:
    filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state)]
elif city:
    filtered_df = df3[df3["City"].isin(city)]
else:
    filtered_df = df3.copy()


# CATEGORY SALES

category_df = filtered_df.groupby(by=["Category"], as_index=False)["Sales"].sum()

with col1:
    st.subheader("Category Sales")
    fig = px.bar(
        category_df,
        x="Category",
        y="Sales",
        text=['${:,.0f}'.format(x) for x in category_df["Sales"]],
        template="plotly_dark",
        color_discrete_sequence=["#C5A572"]
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Region Sales")
    fig = px.pie(
        filtered_df,
        values="Sales",
        names="Region",
        hole=0.5,
        color_discrete_sequence=px.colors.sequential.YlOrBr
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)


# TIME SERIES

filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")

st.subheader("Time Series — Monthly Sales Trend")
linechart = (
    filtered_df
    .groupby(filtered_df["month_year"].dt.strftime("%Y-%b"))["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    linechart,
    x="month_year",
    y="Sales",
    markers=True,
    template="plotly_dark",
    color_discrete_sequence=["#C5A572"]
)
st.plotly_chart(fig2, use_container_width=True)


# TREEMAP

st.subheader("Sales Hierarchy — Region → Category → Sub-Category")
fig3 = px.treemap(
    filtered_df,
    path=["Region", "Category", "Sub-Category"],
    values="Sales",
    hover_data=["Sales"],
    color="Sales",
    color_continuous_scale="YlOrBr"
)
st.plotly_chart(fig3, use_container_width=True)


# PIE CHARTS

chart1, chart2 = st.columns((2))

with chart1:
    st.subheader("Segment Sales")
    fig = px.pie(
        filtered_df,
        values="Sales",
        names="Segment",
        template="plotly_dark",
        color_discrete_sequence=px.colors.sequential.YlOrBr
    )
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    st.subheader("Category Sales Mix")
    fig = px.pie(
        filtered_df,
        values="Sales",
        names="Category",
        template="plotly_dark",
        color_discrete_sequence=px.colors.sequential.YlOrBr
    )
    st.plotly_chart(fig, use_container_width=True)


# SUMMARY TABLE
import plotly.figure_factory as ff

st.subheader("Sub-Category Summary Table")

with st.expander("View Summary Table"):
    df_sample = df[0:5][["Region", "State", "City", "Category", "Sales", "Profit", "Quantity"]]
    fig = ff.create_table(df_sample)
    fig.update_layout(title=None)
    st.plotly_chart(fig, use_container_width=True)

    filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    sub_category_Year = pd.pivot_table(
        data=filtered_df, values="Sales", index=["Sub-Category"], columns="month"
    )
    st.write(sub_category_Year.style.background_gradient(cmap="Blues"))


# SCATTER: SALES vs PROFIT
st.subheader("Sales vs Profit — Bubble Chart")
data1 = px.scatter(
    filtered_df,
    x="Sales",
    y="Profit",
    size="Quantity",
    color="Quantity",
    template="plotly_dark",
    color_continuous_scale="YlOrBr"
)

data1.update_layout(
    title=dict(
        text="Relationship between Sales & Profit",
        font=dict(size=22, color="#C5A572")
    ),
    xaxis=dict(title=dict(text="Sales", font=dict(size=18))),
    yaxis=dict(title=dict(text="Profit", font=dict(size=18)))
)

st.plotly_chart(data1, use_container_width=True)


# DOWNLOAD ORIGINAL DATA
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download Full Dataset", csv, "SuperstoreData.csv", "text/csv")
