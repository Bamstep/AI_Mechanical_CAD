import math
import csv

data = []

# Different shaft diameters
for diameter in range(10, 61):

    # Different torque values
    for torque in range(100, 1001, 100):

        torque_nmm = torque * 1000

        # Calculate shear stress
        shear_stress = (16 * torque_nmm) / (math.pi * diameter**3)

        # Assume allowable shear stress = 150 MPa
        allowable_stress = 150

        # Calculate factor of safety
        factor_of_safety = allowable_stress / shear_stress

        # Determine status
        if factor_of_safety >= 2:
            status = "PASS"
        else:
            status = "FAIL"

        data.append([
            diameter,
            torque,
            shear_stress,
            factor_of_safety,
            status
        ])

# Save dataset
with open("data/shaft_dataset.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "diameter_mm",
        "torque_nm",
        "shear_stress_mpa",
        "factor_of_safety",
        "status"
    ])

    writer.writerows(data)

print("Dataset created successfully!")
print("Number of samples:", len(data))