import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ------------------ 🎨 Page Setup ------------------
st.set_page_config(
    page_title="Digital Addiction Predictor",
    page_icon="📱",
    layout="centered"
)

# Custom CSS for classy styling
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #2C3E50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 0.5em 1em;
        }
        .stButton>button:hover {
            background-color: #1A252F;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ 🎯 Title Section ------------------
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>📱 Digital Addiction Level Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d;'>Understand your screen time habits and get personalized insights.</p>", unsafe_allow_html=True)
st.markdown("---")

# ------------------ 🧠 User Inputs ------------------
st.subheader("📋 Enter your usage details")

col1, col2 = st.columns(2)
with col1:
    daily_usage = st.slider("Daily Device Usage (hrs)", 0.0, 24.0, 6.0, step=0.1)
    phone_checks = st.number_input("Phone Checks per Day", 0, 300, 45, step=1)
    time_social = st.slider("Time on Social Media (hrs)", 0.0, 12.0, 2.5, step=0.1)

with col2:
    sleep_hours = st.slider("Sleep Hours (hrs)", 0.0, 15.0, 7.0, step=0.1)
    apps_used = st.number_input("Apps Used Daily", 0, 50, 6, step=1)
    time_gaming = st.slider("Time on Gaming (hrs)", 0.0, 12.0, 1.0, step=0.1)

predict_btn = st.button("🚀 Analyze My Addiction Level")

# ------------------ 🔮 Prediction ------------------
if predict_btn:
    input_features = np.array([[daily_usage, sleep_hours, phone_checks, apps_used, time_social, time_gaming]])
    prediction = model.predict(input_features)[0]

    # Map output
    addiction_map = {
        0: ("🟢 Low Addiction", "#27ae60", "You’re doing great! Your digital habits are well-balanced."),
        1: ("🟠 Moderate Addiction", "#f39c12", "You’re on the edge. Try reducing unnecessary screen time."),
        2: ("🔴 High Addiction", "#c0392b", "Consider reducing your device use. Take digital detoxes regularly.")
    }

    label, color, message = addiction_map[prediction]

    st.markdown(f"<h2 style='color:{color}; text-align:center;'>{label}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; font-size:18px;'>{message}</p>", unsafe_allow_html=True)

# ------------------ 👣 Footer ------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 14px; color: gray;'>✨ Made for awareness, not diagnosis • Crafted by Nafay Aftab</p>",
    unsafe_allow_html=True
)
