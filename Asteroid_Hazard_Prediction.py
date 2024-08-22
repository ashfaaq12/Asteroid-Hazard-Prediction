import streamlit as st
import pandas as pd
import pickle

with open(r"C:\Users\hp\Documents\GitHub\Asteroid-Hazard-Prediction\models\Asteroid_Hazard_Prediction.pkl", 'rb') as file:
    data = pickle.load(file)

model = data['model']
scaler = data['scaler']


def main():
    st.title("Asteroid Hazard Prediction Web App")
    st.write("""
    This app predicts whether an asteroid is hazardous based on various features like diameter, velocity, and miss distance.
    """)


    est_diameter_min = st.number_input("Estimated Diameter Min (km)", min_value=0.0, step=0.01, format="%.2f")
    est_diameter_max = st.number_input("Estimated Diameter Max (km)", min_value=0.0, step=0.01, format="%.2f")
    relative_velocity = st.number_input("Relative Velocity (km/s)", min_value=0.0, step=0.01, format="%.2f")
    miss_distance = st.number_input("Miss Distance (km)", min_value=0.0, step=0.01, format="%.2f")
    absolute_magnitude = st.number_input("Absolute Magnitude", min_value=0.0, step=0.01, format="%.2f")

    input_data = pd.DataFrame({
        'est_diameter_min': [est_diameter_min],
        'est_diameter_max': [est_diameter_max],
        'relative_velocity': [relative_velocity],
        'miss_distance': [miss_distance],
        'absolute_magnitude': [absolute_magnitude]
    })

    input_data_scaled = scaler.transform(input_data)

    if st.button("Predict"):
        prediction = model.predict(input_data_scaled)
        prediction_proba = model.predict_proba(input_data_scaled)

        st.success(f"The asteroid is {'Hazardous' if prediction[0] == 1 else 'Not Hazardous'}.")
        st.write(
            f"Prediction Probability: {prediction_proba[0][1] * 100:.2f}% Hazardous, {prediction_proba[0][0] * 100:.2f}% Not Hazardous.")


if __name__ == "__main__":
    main()