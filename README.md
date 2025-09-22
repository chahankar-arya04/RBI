# RBI Dashboard Project

## Description  
A project that visualizes RBI monetary indicators (Repo Rate, CRR, SLR, Inflation, Liquidity) and cyber fraud data (by bank, fraud type, region).  
Dashboard created using **Python (Dash + Pandas)** for backend, **MySQL** for data storage, and **Power BI** for visualization.

## Features  
- Interactive Python dashboard with live MySQL data  
- Power BI dashboard with charts, slicers and filters  
- Exported CSVs of data  
- Dual-page dashboard:  
  - Monetary Indicators  
  - Cyber Frauds

## Tech Stack  
- Python  
- MySQL  
- Dash / Plotly  
- Power BI  
- CSV for data export

## How to Run Locally

```bash
# Clone this repo
git clone https://github.com/chahankar-arya04/RBI.git
cd RBI

# Python dashboard
# Make sure MySQL server is running and database rbi_dashboard exists
# And the tables monetary_indicators & cyber_frauds are populated

python rbi_dashboard.py
