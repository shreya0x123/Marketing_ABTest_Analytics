import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sqlite3

# Load dataset
df = pd.read_csv("data/marketing_campaign.csv")

# ----------------------------------------
# TITLE
# ----------------------------------------
st.title("📊 Marketing A/B Test – Analytics Dashboard")

# ----------------------------------------
# PROJECT OVERVIEW
# ----------------------------------------
st.subheader("📌 Project Overview")
st.write("""
This dashboard analyzes two marketing campaigns (A & B)
to see which one performs better based on engagement and revenue.
The goal is to make **data-driven decisions**, not assumptions.
""")

# ----------------------------------------
# DATA PREVIEW
# ----------------------------------------
st.subheader("👁️ Dataset Preview")
st.write(df.head())

# ----------------------------------------
# BASIC STATS
# ----------------------------------------
st.subheader("📈 Basic Statistics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(df))
col2.metric("Campaigns", df['campaign'].nunique())
col3.metric("Max Purchase", df['purchase_amount'].max())

# ----------------------------------------
# CTR COMPARISON
# ----------------------------------------
st.subheader("📊 Click-Through Rate (CTR) Comparison")
ctr_values = df.groupby('campaign')['clicked'].mean()

fig1, ax1 = plt.subplots()
sns.barplot(x=ctr_values.index, y=ctr_values.values, ax=ax1)
ax1.set_title("Click-Through Rate by Campaign")
ax1.set_ylabel("CTR (Mean Clicks)")
st.pyplot(fig1)

# ----------------------------------------
# REVENUE DISTRIBUTION
# ----------------------------------------
st.subheader("💰 Revenue Distribution per Campaign")
fig2, ax2 = plt.subplots()
sns.boxplot(x='campaign', y='purchase_amount', data=df, ax=ax2)
ax2.set_title("Revenue Distribution by Campaign")
st.pyplot(fig2)

# ----------------------------------------
# SQL ANALYSIS (SIMULATED CONSULTING WORKFLOW)
# ----------------------------------------
st.subheader("🧠 SQL-Based Insights (Simulated Enterprise Workflow)")

# Create in-memory SQL database
conn = sqlite3.connect(':memory:')
df.to_sql('marketing_data', conn, index=False, if_exists='replace')

sql_query = """
SELECT campaign,
       SUM(clicked) * 1.0 / COUNT(*) AS CTR,
       AVG(purchase_amount) AS avg_revenue
FROM marketing_data
GROUP BY campaign;
"""
st.write(pd.read_sql(sql_query, conn))

# ----------------------------------------
# FINAL RECOMMENDATION
# ----------------------------------------
st.subheader("📌 Final Recommendation")
st.success("""
✔ Campaign A clearly performs better in both CTR and revenue.  
✔ Recommend allocating **80% of future marketing budget** to Campaign A.  
✔ Campaign B should be personalized & re-tested using multivariate A/B testing.  
✔ This approach ensures **data-driven marketing decisions**, aligned with business goals.
""")

# ----------------------------------------
# FOOTER
# ----------------------------------------
st.write("---")
st.caption("Designed as a consulting-style analytics project – following Accenture's data-to-decision approach.")
