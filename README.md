## Table of Contents

- [Project Overview](#project-overview)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Web App](#web-app)
- [Getting Started with FastAPI](#getting-started-with-fast-api)
- [Getting Started with Docker](#getting-started-with-docker)
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

To run this project locally, you need to follow these steps:

1. Clone this repository: `https://github.com/Davis-Azangu-DataAnalyst/Machine-Learning-API`
2. Navigate to the project directory: `cd Machine-Learning-API`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage


1. Make sure you have installed the required dependencies (see [Installation](#installation)).
2. Prepare your input data in the same format as the provided dataset.
3. Run the Streamlit app: `streamlit run 01_Home.py`
4. The web app will start running locally, and you can access it in your web browser at `http://localhost:8503`.

## Model Training

Two best performing models (KNN and Logistic Regression models) were selected from my previous project: [https://github.com/Davis-Azangu-DataAnalyst/Classification-Project-LP2](https://github.com/Davis-Azangu-DataAnalyst/Classification-Project-LP2). The EDA and data training, validation and modeling are  described in detail in the `Churn_LP2 1_V2.ipynb` Jupyter Notebook. It covers data preprocessing, feature engineering, model selection, and model training using various machine learning algorithms.

## Web App

The Streamlit web app is implemented in the `01_Home.py` file. It utilizes the trained churn prediction model to make predictions based on user input. The app provides a user interface where users can enter customer information and receive churn predictions instantly.

## Getting Started with FastAPI
FastAPI is causing a sensation in the realm of web development with its remarkable speed and developer-centric ecosystem. To commence this adventure, you'll need to configure your development environment to accommodate FastAPI. This segment will steer you through the initial configuration process and acquaint you with the fundamental principles that render FastAPI an exceptional option for deploying machine learning models.

## Getting Started  with Docker

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).