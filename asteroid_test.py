import streamlit as st
import pandas as pd
import pickle

# Load the trained model and scaler
with open(r"C:\Users\hp\Downloads\Asteroid_Hazard_Prediction.pkl", 'rb') as file:
    data = pickle.load(file)

model = data['model']
scaler = data['scaler']


# Custom CSS for background image and font style
def add_custom_style():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://www.enkey.it/wp-content/uploads/2020/09/Near-Earth-Objects-1.jpg");
            background-size: cover;
        }}
        /* Custom font for the text */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        html, body, [class*="css"]  {{
            font-family: 'Roboto', sans-serif;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Define the Streamlit app
def main():
    add_custom_style()  # Call the function to add background image and custom font

    st.title("Asteroid Hazard Prediction Web App")
    st.write("""
    This application predicts the likelihood of an asteroid being hazardous based on several key features. 
    Please enter the details below to get the prediction.
    """)

    st.header("Input Features")

    col1, col2 = st.columns(2)

    with col1:
        est_diameter_min = st.number_input(
            "Estimated Diameter Min (km)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            help="Enter the minimum estimated diameter of the asteroid in kilometers."
        )
        est_diameter_max = st.number_input(
            "Estimated Diameter Max (km)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            help="Enter the maximum estimated diameter of the asteroid in kilometers."
        )
        relative_velocity = st.number_input(
            "Relative Velocity (km/s)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            help="Enter the relative velocity of the asteroid in kilometers per second."
        )

    with col2:
        miss_distance = st.number_input(
            "Miss Distance (km)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            help="Enter the miss distance of the asteroid in kilometers."
        )
        absolute_magnitude = st.number_input(
            "Absolute Magnitude",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            help="Enter the absolute magnitude of the asteroid."
        )

    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'est_diameter_min': [est_diameter_min],
        'est_diameter_max': [est_diameter_max],
        'relative_velocity': [relative_velocity],
        'miss_distance': [miss_distance],
        'absolute_magnitude': [absolute_magnitude]
    })

    # Scale the input data using the loaded scaler
    input_data_scaled = scaler.transform(input_data)

    # Prediction
    if st.button("Predict"):
        prediction = model.predict(input_data_scaled)
        prediction_proba = model.predict_proba(input_data_scaled)

        st.success(f"The asteroid is {'Hazardous' if prediction[0] == 1 else 'Not Hazardous'}.")
        st.write(
            f"Prediction Probability: {prediction_proba[0][1] * 100:.2f}% Hazardous, {prediction_proba[0][0] * 100:.2f}% Not Hazardous."
        )


if __name__ == "__main__":
    main()
