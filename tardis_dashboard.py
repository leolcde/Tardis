import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# import joblib

# Load dataset and model
df = pd.read_csv("cleaned_dataset.csv")
# model = joblib.load("trained_model.pkl")  # Optional: only if model is trained and ready

st.set_page_config(page_title="TARDIS – SNCF Dashboard", layout="wide")
st.title("🚄 TARDIS – Train Delay Analysis Dashboard")

# --- Metrics Section ---
st.header("📊 Key Statistics Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Delay at Departure", f"{df['Average delay of all trains at departure'].mean():.2f} min")
col2.metric("Avg Delay at Arrival", f"{df['Average delay of all trains at arrival'].mean():.2f} min")
col3.metric("Cancellation Rate", f"{(df['Number of cancelled trains'].sum() / df['Number of scheduled trains'].sum()) * 100:.2f}%")

# --- Delay Distribution ---
st.subheader("📈 Delay Distribution (Departure & Arrival)")
delay_type = st.selectbox("Select delay type", [
    "Average delay of all trains at departure",
    "Average delay of all trains at arrival"
])
fig, ax = plt.subplots()
sns.histplot(df[delay_type], bins=50, kde=True, ax=ax)
st.pyplot(fig)

# --- Station-Level Analysis ---
st.subheader("🏙️ Station-Level Analysis")
station_col = st.selectbox("Select Station Type", ["Departure station", "Arrival station"])
selected_station = st.selectbox("Choose a station", df[station_col].dropna().unique())

filtered_df = df[df[station_col] == selected_station]
st.write(f"🔹 Average delay at departure: {filtered_df['Average delay of all trains at departure'].mean():.2f} min")
st.write(f"🔹 Average delay at arrival: {filtered_df['Average delay of all trains at arrival'].mean():.2f} min")
st.write(f"🔹 Cancellation rate: {(filtered_df['Number of cancelled trains'].sum() / filtered_df['Number of scheduled trains'].sum()) * 100:.2f}%")

# Optional bar chart
fig_bar = px.bar(
    filtered_df,
    x="Date",
    y=["Average delay of all trains at departure", "Average delay of all trains at arrival"],
    title="Daily Delay Trends",
    labels={"value": "Minutes", "Date": "Date"},
    barmode="group"
)
st.plotly_chart(fig_bar, use_container_width=True)

# --- Correlation Heatmap ---
st.subheader("🔍 Correlation Between Delay Causes")
corr_columns = [
    "Pct delay due to external causes",
    "Pct delay due to infrastructure",
    "Pct delay due to traffic management",
    "Pct delay due to rolling stock",
    "Pct delay due to station management and equipment reuse",
    "Pct delay due to passenger handling (crowding, disabled persons, connections)"
]
corr = df[corr_columns].corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# --- Prediction Section (Optional) ---
st.subheader("🔮 Delay Prediction (Optional)")
with st.form("prediction_form"):
    dep_station = st.selectbox("Departure Station", df["Departure station"].dropna().unique())
    arr_station = st.selectbox("Arrival Station", df["Arrival station"].dropna().unique())
    avg_journey_time = st.slider("Avg Journey Time (min)", 0, 500, step=10)
    scheduled = st.slider("Scheduled Trains", 1, 100)
    traffic_pct = st.slider("Pct Delay Due to Traffic Management", 0.0, 100.0, step=1.0)

    predict_btn = st.form_submit_button("Predict Delay")

    if predict_btn:
        X_input = pd.DataFrame([[
            dep_station,
            arr_station,
            avg_journey_time,
            scheduled,
            traffic_pct
        ]], columns=[
            "Departure station",
            "Arrival station",
            "Average journey time",
            "Number of scheduled trains",
            "Pct delay due to traffic management"
        ])

        # Encode if necessary
        # prediction = model.predict(X_input)[0]
        # st.success(f"Predicted average delay: {prediction:.2f} minutes")

# --- Data Explorer ---
st.subheader("🧾 Raw Data Explorer")
with st.expander("View Raw Dataset"):
    st.dataframe(df.head(100))
