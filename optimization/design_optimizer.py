import math

print("================================")
print("    AI SHAFT DESIGN OPTIMIZER")
print("================================")

# Get user inputs
torque = float(input("Enter applied torque (N.m): "))
required_fos = float(input("Enter required FOS: "))
allowable_stress = float(input("Enter allowable shear stress (MPa): "))

# Search for the smallest suitable diameter
for diameter in range(10, 101):

    torque_nmm = torque * 1000

    shear_stress = (
        16 * torque_nmm
    ) / (math.pi * diameter**3)

    factor_of_safety = allowable_stress / shear_stress

    if factor_of_safety >= required_fos:

        print("\n================================")
        print("       DESIGN RESULT")
        print("================================")
        print(f"Torque: {torque} N.m")
        print(f"Required FOS: {required_fos}")
        print(f"Allowable stress: {allowable_stress} MPa")
        print(f"Recommended diameter: {diameter} mm")
        print(f"Shear stress: {shear_stress:.2f} MPa")
        print(f"Actual FOS: {factor_of_safety:.2f}")
        print("Status: PASS")
        print("================================")

        break