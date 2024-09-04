# Asteroid Hazard Prediction

Developed a machine learning model to predict the likelihood of an asteroid being hazardous based on features such as estimated diameter, velocity, and miss distance. The model is designed to assist in identifying potentially dangerous asteroids by analyzing key features. This project includes a web application built with Streamlit that allows users to input asteroid data and receive real-time hazard predictions.

## Dataset
The dataset contains information about various asteroids, including estimated diameter, relative velocity, miss distance, absolute magnitude, and whether the asteroid is hazardous.

- **Source:** [https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects](https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects)
- **Attributes:**
  - `est_diameter_min`: Minimum estimated diameter (km)
  - `est_diameter_max`: Maximum estimated diameter (km)
  - `relative_velocity`: Relative velocity (km/s)
  - `miss_distance`: Miss distance (km)
  - `absolute_magnitude`: Absolute magnitude
  - `hazardous`: Target variable (1 = Hazardous, 0 = Not Hazardous)

## Web Application
A web application was developed using Streamlit to allow users to interact with the model. Users can input asteroid parameters and receive predictions on whether the asteroid is hazardous.

### Features:
- Input fields for asteroid data
- Real-time predictions
- Probability display of the asteroid being hazardous or not


## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/asteroid-hazard-prediction.git
   cd asteroid-hazard-prediction

```bash
pip install -r requirements.txt
    streamlit run app.py