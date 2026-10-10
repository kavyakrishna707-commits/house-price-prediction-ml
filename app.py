
from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

app = Flask(__name__)

# 1. Load historical house price data
data = pd.read_csv("house_data.csv")

# 2. Select input features and target
features = [
    "area_sqft",
    "bedrooms",
    "bathrooms",
    "age_years"
]

X = data[features]
y = data["price"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 4. Create and train the machine learning model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate the model
test_predictions = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    test_predictions
)

print("House Price Prediction Model Trained Successfully!")
print(f"Mean Absolute Error: ₹{mae:,.2f}")


# 6. Home page
@app.route("/")
def home():
    return render_template("index.html")


# 7. Handle house price prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values submitted from the HTML form
        area = float(request.form["area_sqft"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        age = float(request.form["age_years"])

        # Validate the input values
        if (
            area <= 0
            or bedrooms <= 0
            or bathrooms <= 0
            or age < 0
        ):
            return render_template(
                "index.html",
                error="Please enter valid house details."
            )

        # Create input data in the same feature order
        house_data = pd.DataFrame(
            [[area, bedrooms, bathrooms, age]],
            columns=features
        )

        # Predict the house price
        predicted_price = model.predict(house_data)[0]

        # Check the prediction
        if predicted_price <= 0:
            return render_template(
                "index.html",
                error=(
                    "Unable to estimate a valid price. "
                    "Please try different house details."
                )
            )

        # Display the result on the webpage
        return render_template(
            "index.html",
            prediction=f"₹{predicted_price:,.0f}",
            mae=f"₹{mae:,.0f}"
        )

    except (ValueError, TypeError, KeyError):
        return render_template(
            "index.html",
            error="Please enter valid numeric values."
        )


# 8. Run the application on localhost port 5001
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=True
    )
