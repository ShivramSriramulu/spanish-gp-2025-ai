import streamlit as st
import json
from PIL import Image

# Set up the page
st.set_page_config(page_title="Spanish GP 2025 - AI Prediction", layout="wide")
st.title("🏁 Spanish Grand Prix 2025 - AI Race Simulation Dashboard")

# Load Agentic AI Results
with open("spanish_gp_2025_results.json", "r") as file:
    prediction_data = json.load(file)

# Extract sections
performance = prediction_data["analyses"]["Performance Analysis"]
weather = prediction_data["analyses"]["Weather Strategy"]
circuit = prediction_data["analyses"]["Circuit Analysis"]
team = prediction_data["analyses"]["Team Dynamics"]
technical = prediction_data["analyses"]["Technical Assessment"]
final_prediction = prediction_data["final_prediction"]
winner = prediction_data["predicted_winner"]

# Overview Section
st.markdown("## 📋 Overview")
st.write("This dashboard shows a realistic simulation of the 2025 Spanish Grand Prix using Agentic AI powered by LangGraph, OpenAI GPT-4o, and FastF1. Below are visualizations and agent outputs.")

# Agentic AI Analysis
st.markdown("## 🧠 Agentic AI Analysis")

with st.expander("🔍 Performance Analysis"):
    st.text(performance)

with st.expander("🌤️ Weather Strategy"):
    st.text(weather)

with st.expander("🏎️ Circuit Analysis"):
    st.text(circuit)

with st.expander("🤝 Team Dynamics"):
    st.text(team)

with st.expander("🔧 Technical Assessment"):
    st.text(technical)

# Final Prediction
st.markdown("## 🏆 Final Prediction")
st.success(f"🥇 Predicted Winner: {winner}")
st.code(final_prediction, language='markdown')

# Visuals
st.markdown("## 📊 Race Simulation Charts")

col1, col2 = st.columns(2)
with col1:
    st.image(Image.open("raceposition.png"), caption="📉 Race Position Progression", use_column_width=True)
with col2:
    st.image(Image.open("top5.png"), caption="⏱️ Lap Time Analysis (Top 5 Drivers)", use_column_width=True)

st.image(Image.open("top10bar.png"), caption="🏆 Final Results - Top 10 Finishers", use_column_width=True)

# Footer
st.markdown("---")
st.info("✅ Built with FastF1, LangGraph, and OpenAI for the 2025 F1 Season Prediction Series.")
