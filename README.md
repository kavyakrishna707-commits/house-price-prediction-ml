# House Price Prediction

A machine learning web application that predicts house prices based on area, number of bedrooms, number of bathrooms, and house age using historical data.

## Technologies Used
- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSS

## Machine Learning Algorithm
Linear Regression

## Features
- Predict house prices using house details
- Train the model using CSV data
- Modern dark-themed user interface
- Display predicted prices on the webpage

## Project Structure
```text
house-price-prediction/
├── app.py
├── house_data.csv
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## How to Run
1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   ```
   Windows PowerShell:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
4. Install the required libraries:
   ```bash
   pip install flask pandas scikit-learn
   ```
5. Run the application:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5001/` in your browser.

## Dataset
The `house_data.csv` file contains house area, bedrooms, bathrooms, age, and price. The model learns from these historical examples to estimate prices for new inputs.
