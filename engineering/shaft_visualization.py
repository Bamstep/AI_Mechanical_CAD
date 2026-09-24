import math
import matplotlib.pyplot as plt


def visualize_shaft(
    torque,
    required_fos,
    recommended_diameter,
    allowable_stress=150
):

    # =================================
    # CALCULATE VALUES
    # =================================

    diameters = list(range(10, 61))

    fos_values = []
    stress_values = []

    for diameter in diameters:

        torque_nmm = torque * 1000

        shear_stress = (
            16 * torque_nmm
        ) / (
            math.pi * diameter**3
        )

        factor_of_safety = (
            allowable_stress / shear_stress
        )

        fos_values.append(factor_of_safety)
        stress_values.append(shear_stress)

    # =================================
    # RECOMMENDED DESIGN VALUES
    # =================================

    torque_nmm = torque * 1000

    recommended_stress = (
        16 * torque_nmm
    ) / (
        math.pi * recommended_diameter**3
    )

    recommended_fos = (
        allowable_stress /
        recommended_stress
    )

    # =================================
    # DESIGN INFORMATION
    # =================================

    print("\n================================")
    print("     DESIGN VISUALIZATION")
    print("================================")

    print(f"Torque: {torque} N.m")
    print(f"Required FOS: {required_fos}")

    print(
        f"Recommended Diameter: "
        f"{recommended_diameter} mm"
    )

    print(
        f"Shear Stress: "
        f"{recommended_stress:.2f} MPa"
    )

    print(
        f"Actual FOS: "
        f"{recommended_fos:.2f}"
    )

    print("================================")

    # =================================
    # GRAPH 1: FACTOR OF SAFETY
    # =================================

    plt.figure(figsize=(10, 6))

    plt.plot(
        diameters,
        fos_values,
        label="Factor of Safety"
    )

    plt.scatter(
        recommended_diameter,
        recommended_fos,
        s=100,
        zorder=5,
        label=(
            f"Recommended: "
            f"{recommended_diameter} mm"
        )
    )

    plt.axhline(
        required_fos,
        linestyle="--",
        label=(
            f"Required FOS = "
            f"{required_fos}"
        )
    )

    plt.annotate(
        f"{recommended_diameter} mm\n"
        f"FOS = {recommended_fos:.2f}",
        (
            recommended_diameter,
            recommended_fos
        ),
        xytext=(
            recommended_diameter + 3,
            recommended_fos + 1
        ),
        arrowprops=dict(
            arrowstyle="->"
        )
    )

    plt.xlabel("Shaft Diameter (mm)")
    plt.ylabel("Factor of Safety")

    plt.title(
        "Shaft Diameter vs Factor of Safety"
    )

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()

    # =================================
    # GRAPH 2: SHEAR STRESS
    # =================================

    plt.figure(figsize=(10, 6))

    plt.plot(
        diameters,
        stress_values,
        label="Shear Stress"
    )

    plt.scatter(
        recommended_diameter,
        recommended_stress,
        s=100,
        zorder=5,
        label=(
            f"Recommended: "
            f"{recommended_diameter} mm"
        )
    )

    plt.axhline(
        allowable_stress,
        linestyle="--",
        label=(
            f"Allowable Stress = "
            f"{allowable_stress} MPa"
        )
    )

    plt.annotate(
        f"{recommended_diameter} mm\n"
        f"Stress = {recommended_stress:.2f} MPa",
        (
            recommended_diameter,
            recommended_stress
        ),
        xytext=(
            recommended_diameter + 3,
            recommended_stress + 20
        ),
        arrowprops=dict(
            arrowstyle="->"
        )
    )

    plt.xlabel("Shaft Diameter (mm)")
    plt.ylabel("Shear Stress (MPa)")

    plt.title(
        "Shaft Diameter vs Shear Stress"
    )

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()