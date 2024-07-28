## Table of Contents

- [Project Overview](#project-overview)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Frontend Web App](#frontend-web-app)
- [Backend Web App](#backend-web-app)
- [Docker Images](#docker-images)
- [Deployed App Links](#deployed-app-links)
- [Contributing](#contributing)
- [License](#license)

# Building Machine Learning APIs with FastAPI
### Sepsis Cases Prediction Among ICU Patients Using Machine Learning

Sepsis is a life-threatening condition triggered by an immune overreaction to infection, leading to organ failure or even death. The objective of this project is to predict whether a patient in the Intensive Care Unit (ICU) will develop sepsis or not using machine learning models. Timely diagnosis and treatment of sepsis are crucial due to its immediate death risk, often resulting in patients' death within one hour. The project aims to predict the survival of patients within minutes using minimal and easily accessible medical features.

## Project Overview

In this project, we will build a machine learning classification model that can accurately predict whether a patient in the ICU will develop sepsis or not based on the provided features. The project will follow the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.In addition to building the machine learning model, this project will also involve creating restful machine learning APIs using fastAPI. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python. By creating APIs, the model can be deployed and accessed by other applications or systems for real-time predictions. The fastAPI framework provides efficient and scalable options for serving machine learning models over HTTP.Lastly, we shall containerize the application with Docker. 


## Data
The dataset used for this study is from Kaggle database and contains the training and validation datasets. The training and testing datasets  contains 599 and 169 ICU patients respectively. The features in the training and testing datasets includes:

- **ID:** Unique identifier for patients' ID.
- **PRG:** Plasma glucose.
- **PL:** Blood Work Result-1 (mu U/ml).
- **PR:** Blood Pressure (mm Hg).
- **SK:** Blood Work Result-2 (mu U/ml).
- **TS:** Blood Work Result-3 (mu U/ml).
- **M11:** Body mass index (Weight in kg/(height in m)^2).
- **BD2:** Blood Work Result-4 (mu U/ml).
- **AGE:** Patients age (Age in years).
- **Insurance:** If the patient holds a valid insurance card.
- **Sepsis:** Positive: If the patient in ICU develops sepsis and Negative: Otherwise.


## Installation

To run this project locally, follow these steps:

Clone the repository: git clone https://github.com/Davis-Azangu-DataAnalyst/Machine-Learning-API
Navigate to the project directory: cd Machine-Learning-API
Install the necessary dependencies for the backend API: pip install -r requirements.txt
Install the required dependencies for the Streamlit frontend: pip install streamlit
Run the FastAPI backend: uvicorn main:app --reload
Launch the Streamlit frontend: streamlit run main.py

By following these steps, you can set up both the backend API and the frontend Streamlit application for this project on your local machine.

## Usage


1. Make sure you have installed the required dependencies (see [Installation](#installation)).
2. Prepare your input data in the same format as the provided dataset.
3. Run the Streamlit app: `streamlit run main.py`
4. The web app will start running locally, and you can access it in your web browser at `http://localhost:8501/`.

## Model Training

Two best performing models (Logistic_Regression and SVC models) were selected from 'LP5V1.ipynb' at this repository: [https://github.com/Davis-Azangu-DataAnalyst/Machine-Learning-API](https://github.com/Davis-Azangu-DataAnalyst/Machine-Learning-API). The EDA and data training, validation and modeling are  described in detail in the `LP5V1.ipynb` Jupyter Notebook. It covers data preprocessing, feature engineering, model selection, and model training using various machine learning algorithms.

## Frontend Web App

The Streamlit web app is implemented through this command `streamlit run main.py`. It utilizes the trained sepsis prediction model to make predictions based on user input. The app provides a user interface where users can enter patient's information and receive sepsis predictions instantly.

The streamlit web app should look like this:
![Alt text](Utils\Capture.PNG)


## Backend FastAPI

The FastAPI backend API is implemented trough this command `uvicorn api:app --reload`. It serves the machine learning model and provides endpoints for making predictions based on input data. The API allows users to interact with the model programmatically.

The FastAPI backend API should look like this:
![Alt text](Utils\Capture_1.PNG)

## Docker Images

### Backend FastAPI Image
- Image Name: `api`
- Description: Docker image for the FastAPI backend API.
- Command to Run: `docker-compose up`
- [Link to access](http://localhost/docs)

### Frontend Streamlit Image
- Image Name: `client`
- Description: Docker image for the Streamlit frontend web app.
- Command to Run: `docker-compose up`
- [Link to access](http://localhost:3030/)

## Deployed App Links

The images are deployed at Docker Hub and can be accessed at:
Frontend: Streamlit app [Deployment Link](https://hub.docker.com/repository/docker/datawhizz04/lp5-machine-learning-api-client).

Backend: FastAPI app[Deployment Link](https://https://hub.docker.com/repository/docker/datawhizz04/lp5-machine-learning-api-api)

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).