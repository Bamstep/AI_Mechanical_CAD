from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "shaft_dataset.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Features
X = df[["diameter_mm", "torque_nm"]]

# Target
y = df["status"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# Create the ML model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")

# Test the model
accuracy = model.score(X_test, y_test)

print(f"Model accuracy: {accuracy * 100:.2f}%")

# Test the model with a new shaft
new_shaft = pd.DataFrame({
    "diameter_mm": [37],
    "torque_nm": [650]
})

prediction = model.predict(new_shaft)

print("\nNEW SHAFT")
print("Diameter: 37 mm")
print("Torque: 650 N.m")
print("ML Prediction:", prediction[0])

# Calculate the actual engineering result
import math

diameter = 37
torque = 650
allowable_stress = 150

torque_nmm = torque * 1000

shear_stress = (16 * torque_nmm) / (math.pi * diameter**3)

factor_of_safety = allowable_stress / shear_stress

if factor_of_safety >= 2:
    engineering_result = "PASS"
else:
    engineering_result = "FAIL"

print("\nENGINEERING CALCULATION")
print(f"Shear stress: {shear_stress:.2f} MPa")
print(f"Factor of safety: {factor_of_safety:.2f}")
print("Engineering Result:", engineering_result)