import sys
from pathlib import Path
import math
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# =================================
# PROJECT PATH
# =================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from engineering.shaft_visualization import visualize_shaft

DATA_FILE = PROJECT_ROOT / "data" / "shaft_dataset.csv"

# =================================
# AI SHAFT ASSISTANT
# =================================

print("================================")
print("      AI SHAFT ASSISTANT")
print("================================")

# =================================
# LOAD DATASET
# =================================

df = pd.read_csv(DATA_FILE)

X = df[["diameter_mm", "torque_nm"]]
y = df["status"]

# =================================
# TRAIN ML MODEL
# =================================

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

print("ML model trained successfully!")

# =================================
# USER INPUT
# =================================

diameter = float(
    input("\nEnter proposed shaft diameter (mm): ")
)

torque = float(
    input("Enter applied torque (N.m): ")
)

# =================================
# ML PREDICTION
# =================================

new_shaft = pd.DataFrame({
    "diameter_mm": [diameter],
    "torque_nm": [torque]
})

prediction = model.predict(new_shaft)[0]

print("\n================================")
print("        ML PREDICTION")
print("================================")
print(f"Diameter: {diameter} mm")
print(f"Torque: {torque} N.m")
print(f"ML Prediction: {prediction}")
print("================================")

# =================================
# ENGINEERING VERIFICATION
# =================================

allowable_stress = 150

torque_nmm = torque * 1000

shear_stress = (
    16 * torque_nmm
) / (math.pi * diameter**3)

factor_of_safety = (
    allowable_stress / shear_stress
)

if factor_of_safety >= 2:
    engineering_result = "PASS"
else:
    engineering_result = "FAIL"

print("\n================================")
print("    ENGINEERING VERIFICATION")
print("================================")
print(f"Shear stress: {shear_stress:.2f} MPa")
print(f"Factor of safety: {factor_of_safety:.2f}")
print(f"Engineering Result: {engineering_result}")
print("================================")

# =================================
# COMPARE RESULTS
# =================================

if prediction == engineering_result:
    print("ML and Engineering: MATCH")
else:
    print("ML and Engineering: DIFFER")

# =================================
# OPTIMIZATION
# =================================

required_fos = float(
    input("\nEnter required FOS for optimization: ")
)

recommended_diameter = None
recommended_fos = None

for test_diameter in range(10, 101):

    test_torque_nmm = torque * 1000

    test_shear_stress = (
        16 * test_torque_nmm
    ) / (math.pi * test_diameter**3)

    test_fos = (
        allowable_stress / test_shear_stress
    )

    if test_fos >= required_fos:

        recommended_diameter = test_diameter
        recommended_fos = test_fos

        break

# =================================
# CHECK DESIGN
# =================================

if recommended_diameter is None:

    print(
        "\nNo suitable diameter found "
        "between 10 mm and 100 mm."
    )

    exit()

# =================================
# OPTIMIZED DESIGN
# =================================

print("\n================================")
print("       OPTIMIZED DESIGN")
print("================================")
print(f"Torque: {torque} N.m")
print(f"Required FOS: {required_fos}")
print(
    f"Recommended diameter: "
    f"{recommended_diameter} mm"
)
print(
    f"Actual FOS: "
    f"{recommended_fos:.2f}"
)
print("Status: PASS")
print("================================")

# =================================
# VERIFY OPTIMIZED DESIGN
# =================================

optimized_torque_nmm = torque * 1000

optimized_shear_stress = (
    16 * optimized_torque_nmm
) / (
    math.pi * recommended_diameter**3
)

optimized_fos = (
    allowable_stress /
    optimized_shear_stress
)

if optimized_fos >= required_fos:
    optimized_engineering_result = "PASS"
else:
    optimized_engineering_result = "FAIL"

# =================================
# ML CHECK OF OPTIMIZED DESIGN
# =================================

optimized_shaft = pd.DataFrame({
    "diameter_mm": [recommended_diameter],
    "torque_nm": [torque]
})

optimized_prediction = (
    model.predict(optimized_shaft)[0]
)

# =================================
# AI DESIGN CONFIRMATION
# =================================

print("\n================================")
print("     AI DESIGN CONFIRMATION")
print("================================")

print(
    f"Optimized diameter: "
    f"{recommended_diameter} mm"
)

print(
    f"Shear stress: "
    f"{optimized_shear_stress:.2f} MPa"
)

print(
    f"Engineering FOS: "
    f"{optimized_fos:.2f}"
)

print(
    f"ML prediction: "
    f"{optimized_prediction}"
)

print(
    f"Engineering result: "
    f"{optimized_engineering_result}"
)

if (
    optimized_prediction == "PASS"
    and optimized_engineering_result == "PASS"
):

    print("FINAL DESIGN: PASS")

else:

    print("FINAL DESIGN: REVIEW REQUIRED")

print("================================")

# =================================
# DESIGN VISUALIZATION
# =================================

visualize_shaft(
    torque=torque,
    required_fos=required_fos,
    recommended_diameter=recommended_diameter,
    allowable_stress=allowable_stress
)