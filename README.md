NutriVIsion - Food Classification and Nutrient Information API


Welcome to NutriVIsion, an advanced food classification and nutrient information API powered by cutting-edge technology. This repository houses the backend server built using Python Flask, integrated with the powerful BiT-M Fine-Tuned Image Classification Model. NutriVIsion seamlessly analyzes images of various foods and provides comprehensive macronutrient information based on the identified food class.
Table of Contents

    Introduction
    Features
    Getting Started
        Prerequisites
        Installation
        Usage
    API Endpoints
        Classify Food
    Advanced Configuration
        Model Fine-Tuning
        Customization
    Contributing
    License

Introduction

NutriVIsion is designed to simplify the process of obtaining macronutrient information for a wide array of foods. Whether you're a health-conscious individual or a developer seeking to enhance your application with nutritional insights, NutriVIsion has got you covered. The integration of the BiT-M model enables high-precision food classification, ensuring accurate identification of food items from images.
Features

    State-of-the-Art Model: NutriVIsion employs a fine-tuned BiT-M image classification model, providing accurate food recognition.
    Effortless Integration: The Python Flask server ensures easy integration into your applications.
    Multipart Image Support: Submit food images via multipart form data to receive prompt classifications.
    Comprehensive Nutrient Data: Obtain detailed macronutrient information based on the recognized food class.
    Customizable: Tailor NutriVIsion's configuration to your specific requirements for enhanced performance.

Getting Started

Follow these steps to set up NutriVIsion on your local machine or server.
Prerequisites

    Python 3.6+
    Pip package manager
    Virtual environment (recommended)

Installation

    Clone this repository: git clone https://github.com/your-username/nutrivision.git
    Navigate to the project directory: cd nutrivision
    Create a virtual environment: python -m venv venv
    Activate the virtual environment:
        On Windows: venv\Scripts\activate
        On macOS and Linux: source venv/bin/activate
    Install the required dependencies: pip install -r requirements.txt

Usage

    Start the Flask server: python app.py
    Make POST requests to http://localhost:5000/classify with the food image using multipart form data.
    Receive the food class and macronutrient information in the response.

API Endpoints
Classify Food

    Endpoint: /classify
    Method: POST
    Request Body: Multipart form data with an image field containing the food image.
    Response:

    json

    {
      "food_class": "apple_pie",
      "macronutrients": {
        "calories": 250,
        "protein": 2.5,
        "carbohydrates": 40.2,
        "fat": 9.8
      }
    }

Advanced Configuration
Model Fine-Tuning

NutriVIsion's classification accuracy can be further improved by fine-tuning the BiT-M model on a custom food dataset. Refer to the model_fine_tuning_guide.md for detailed instructions.
Customization

Tailor NutriVIsion to your specific needs by adjusting parameters in the config.py file. You can modify the confidence threshold for predictions, enable GPU support, and more.
Contributing

We welcome contributions from the open-source community. If you're interested in enhancing NutriVIsion, please read our contribution guidelines.
License

NutriVIsion is released under the MIT License.

Elevate your application's capabilities with NutriVIsion's powerful food classification and nutrient information API. Turn images into nutritional insights effortlessly. For any queries, contact us at contact@nutrivisionapi.com or visit our website www.nutrivisionapi.com.
