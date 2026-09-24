import math

print("================================")
print("     SHAFT ANALYZER v1.0")
print("================================")

# Get information from the user
diameter = float(input("Enter shaft diameter (mm): "))
torque = float(input("Enter applied torque (N.m): "))

# Convert torque from N.m to N.mm
torque_nmm = torque * 1000

# Calculate shear stress
shear_stress = (16 * torque_nmm) / (math.pi * diameter**3)

# Display result
print("\n========== RESULT ==========")
print(f"Diameter: {diameter} mm")
print(f"Torque: {torque} N.m")
print(f"Shear stress: {shear_stress:.2f} MPa")
print("============================")

# Next step: add Factor of Safety
allowable_stress = float(input("Enter allowable shear stress (MPa): "))
factor_of_safety = allowable_stress / shear_stress
print(f"Factor of safety: {factor_of_safety:.2f}")

if factor_of_safety >= 2:
    print("Status: PASS")
else:
    print("Status: FAIL")