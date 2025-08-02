import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# ========== Model Setup ==========
def create_dummy_model():
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    X = np.random.rand(100, 6)
    y = np.random.choice(['Low Risk', 'Medium Risk', 'High Risk'], size=100)
    model.fit(X, y)
    return model

model = create_dummy_model()

# ========== Session History ==========
if "history" not in st.session_state:
    st.session_state.history = []

# ========== Risk Prediction Function ==========
def predict_health_risk(data):
    input_array = np.array([[
        data["sleep_hours"],
        data["exercise_hours"],
        data["stress_level"],
        data["social_activity"],
        data["work_hours"],
        data["screen_time"]
    ]])
    return model.predict(input_array)[0]

# ========== Streamlit App Layout ==========
st.set_page_config(page_title="Mental Health Risk Predictor", page_icon="🧠", layout="wide")
st.title("🧠 Mental Health Risk Predictor")
st.write("Enter your health data to predict your mental health risk.")

col1, col2 = st.columns(2)

# ========== Left: Input ==========
with col1:
    st.subheader("Enter Your Details")
    sleep_hours = st.slider("Weekly Sleep Hours", 0.0, 12.0, 7.0, 0.5)
    exercise_hours = st.slider("Weekly Exercise Hours", 1, 10, 5)
    stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
    social_activity = st.slider("Social Activity (1-10)", 1, 10, 5)
    work_hours = st.slider("Daily Work Hours", 0.0, 16.0, 8.0, 0.5)
    screen_time = st.slider("Daily Screen Time (Hours)", 0.0, 12.0, 4.0, 0.5)

    if st.button("Predict Risk"):
        user_data = {
            "sleep_hours": sleep_hours,
            "exercise_hours": exercise_hours,
            "stress_level": stress_level,
            "social_activity": social_activity,
            "work_hours": work_hours,
            "screen_time": screen_time
        }

        prediction = predict_health_risk(user_data)

        # Save to history
        st.session_state.history.append({
            **user_data,
            "prediction": prediction,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

        st.success(f"Your predicted mental health risk is: **{prediction}**")

# ========== Right: History ==========
with col2:
    st.subheader("Prediction History")
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        df = df[[
            "timestamp", "sleep_hours", "exercise_hours", "stress_level",
            "social_activity", "work_hours", "screen_time", "prediction"
        ]]
        st.dataframe(df)
    else:
        st.write("No prediction history available yet.")
