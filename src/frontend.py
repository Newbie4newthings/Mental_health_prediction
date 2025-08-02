import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Mental Health Risk Predictor", 
    page_icon="🧠", 
    layout="wide"
)

# main title and description
st.title("🧠 Mental Health Risk Predictor")
st.write("Enter your health data to predict your mental health risk.")


# Create 2 columns for better layout organization
col1, col2 = st.columns(2)

# left column for user inputs
with col1:
    st.subheader("Enter Your Details")
    # sliders input - each slider has specific range and default value
    sleep_hours = st.slider (
        "Weekly Sleep Hours",
        0.0, 12.0, 7.0, 0.5, 
        help="How many hours do sleep on average?"
    )
    exercise_hours = st.slider(
        "Weekly Exercise Hours",
        1, 10, 5,
        help="How many hours do you exercise in a week?"
    )
    stress_level = st.slider(
        "Stress Level (1-10)",
        1, 10, 5,
        help="On a scale of 1 to 10, how would you rate your stress level?"
    )
    social_activity = st.slider(
        "Social Activity (1-10)",
        1, 10, 5,
        help="On a scale of 1 to 10, how socially active are you?"
    )
    work_hours = st.slider(
        "Daily Work Hours",
        0.0, 16.0, 8.0, 0.5,
        help="How many hours do you work in a day?"
    )
    screen_time = st.slider(
        "Daily Screen Time (Hours)",
        0.0, 12.0, 4.0, 0.5,
        help="How many hours do you spend on screens daily?(laptop, phone, etc.)"
    )

# Prediction button 
if st.button("Predict Risk"):
    data = {
        "sleep_hours": sleep_hours,
        "exercise_hours": exercise_hours,
        "stress_level": stress_level,
        "social_activity": social_activity,
        "work_hours": work_hours,
        "screen_time": screen_time
    } 
    # Send data to the API
    try:
        # Make a POST request to the prediction endpoint
        response = requests.post("http://localhost:8000/predict", json=data)
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"Your predicted mental health risk is: **{prediction}**")
        else:
            st.error("Error in prediction. Please try again.")
    except requests.exceptions.ConnectionError: 
        st.error("Could not connect to the prediction service. Is the backend server running?")

# right column for displaying prediction history
with col2:
    st.subheader("Prediction History")
    try:
        # Fetch prediction history from the API
        response = requests.get("http://localhost:8000/history")
        if response.status_code == 200:
            records = response.json()
            if records:
                # Convert records to DataFrame for better display
                df = pd.DataFrame(records)
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%d %H:%M")
                # History table with selected columns displayed
                st.dataframe(
                    df[["timestamp", "sleep_hours", 
                        "exercise_hours", 
                        "stress_level", "social_activity", 
                        "work_hours", "screen_time", "prediction"]]
            )
            else:
                st.write("No prediction history available yet.")
    except requests.exceptions.ConnectionError:
        st.error("Could not fetch prediction history. Is the backend server running?")