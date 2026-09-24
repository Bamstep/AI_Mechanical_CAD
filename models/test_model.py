from pathlib import Path
import pandas as pd
import math
import random

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "shaft_dataset.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Features and target
X = df[["diameter_mm", "torque_nm"]]
y = df["status"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Test 100 new shaft designs
correct = 0
total = 100

for i in range(total):

    diameter = random.randint(10, 60)
    torque = random.randint(100, 1000)

    # ML prediction
    new_shaft = pd.DataFrame({
        "diameter_mm": [diameter],
        "torque_nm": [torque]
    })

    ml_prediction = model.predict(new_shaft)[0]

    # Engineering calculation
    torque_nmm = torque * 1000

    shear_stress = (
        16 * torque_nmm
    ) / (math.pi * diameter**3)

    factor_of_safety = 150 / shear_stress

    if factor_of_safety >= 2:
        engineering_result = "PASS"
    else:
        engineering_result = "FAIL"

    # Compare
    if ml_prediction == engineering_result:
        correct += 1

accuracy = (correct / total) * 100

print("================================")
print("      ML MODEL VALIDATION")
print("================================")
print(f"Test cases: {total}")
print(f"Correct predictions: {correct}")
print(f"Accuracy: {accuracy:.2f}%")
print("================================")