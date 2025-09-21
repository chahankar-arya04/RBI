import mysql.connector
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# -----------------------------
# Step 1: Connect to MySQL
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cyber@rya10",  # your MySQL password
    database="rbi_dashboard"
)

# -----------------------------
# Step 2: Fetch tables into pandas
# -----------------------------
monetary_df = pd.read_sql("SELECT * FROM monetary_indicators", conn)
frauds_df = pd.read_sql("SELECT * FROM cyber_frauds", conn)

print(monetary_df.head())
print(frauds_df.head())

# -----------------------------
# Step 3: Create charts with Plotly
# -----------------------------
fig_repo = px.line(
    monetary_df,
    x='date',
    y='repo_rate',
    title='Repo Rate Over Time'
)

fig_fraud = px.bar(
    frauds_df,
    x='bank_name',
    y='amount_lost',
    title='Fraud Amount by Bank'
)

# -----------------------------
# Step 4: Dash app layout
# -----------------------------
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("RBI Dashboard"),
    dcc.Graph(figure=fig_repo),
    dcc.Graph(figure=fig_fraud)
])

# -----------------------------
# Step 5: Run the Dash server
# -----------------------------
# -----------------------------
# Step 5: Run the Dash server
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
