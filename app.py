import time
import pandas as pd
import streamlit as str_app
import plotly.express as px
from datetime import datetime

# Enterprise Dashboard Page Configuration
str_app.set_page_config(
    page_title="CryptoPulse Real-Time Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Main Title and Subtitle
str_app.title("📊 CryptoPulse Real-Time Streaming Analytics")
str_app.subheader("Live Enterprise Market Ingestion Pipeline Monitoring Terminal")
str_app.markdown("---")

# Active Real-Time Stream Execution Loop
while True:
    try:
        # Read the real-time CSV database managed by the ETL pipeline
        df = pd.read_csv("crypto_live_data.csv")
        
        # Ensure timestamp is parsed correctly for visualization
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        
        # Pull the latest entry row for real-time Metric KPIs
        latest_record = df.iloc[-1]
        
        # Top-level KPI Metrics Layout (Two parallel metric columns)
        metric_col1, metric_col2 = str_app.columns(2)
        
        with metric_col1:
            str_app.metric(
                label="🚀 Bitcoin Market Rate (USD)", 
                value=f"${latest_record['btc_usd']:,}"
            )
            
        with metric_col2:
            str_app.metric(
                label="💎 Ethereum Market Rate (USD)", 
                value=f"${latest_record['eth_usd']:,}"
            )
            
        str_app.markdown(f"**Last Ingestion Synchronization Time Stamp:** `{latest_record['timestamp']}`")
        str_app.markdown("---")
        
        # Operational Real-Time Charts Layout
        chart_col1, chart_col2 = str_app.columns(2)
        
        with chart_col1:
            str_app.markdown("### Bitcoin Asset Performance (60s Intervals)")
            btc_chart = px.line(
                df, x="timestamp", y="btc_usd", 
                labels={"timestamp": "Execution Time", "btc_usd": "Price (USD)"},
                template="plotly_dark"
            )
            str_app.plotly_chart(btc_chart, use_container_width=True)
            
        with chart_col2:
            str_app.markdown("### Ethereum Asset Performance (60s Intervals)")
            eth_chart = px.line(
                df, x="timestamp", y="eth_usd", 
                labels={"timestamp": "Execution Time", "eth_usd": "Price (USD)"},
                template="plotly_dark"
            )
            str_app.plotly_chart(eth_chart, use_container_width=True)
            
        str_app.markdown("---")
        
        # Raw Streaming Data Ledger Inspection Section
        str_app.markdown("### Production Data Log View (Recent Records)")
        str_app.dataframe(df.tail(10), use_container_width=True)
        
    except FileNotFoundError:
        str_app.warning("Waiting for the upstream ETL pipeline to generate the target CSV repository...")
    except Exception as error:
        str_app.error(f"Operational Analytics Terminal Error: {error}")
        
    # Polling frequency interval: Dashboard refreshes every 5 seconds
    time.sleep(5)
    str_app.rerun()