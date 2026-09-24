import sys
from pathlib import Path
import math
import tkinter as tk
from tkinter import messagebox

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# =================================
# PROJECT PATH
# =================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# =================================
# IMPORT VISUALIZATION
# =================================

from engineering.shaft_visualization import visualize_shaft


# =================================
# IMPORT CAD GENERATOR
# =================================

from cad.shaft_dxf_generator import create_shaft_dxf


# =================================
# DATASET
# =================================

DATA_FILE = PROJECT_ROOT / "data" / "shaft_dataset.csv"


# =================================
# LOAD DATASET
# =================================

df = pd.read_csv(DATA_FILE)

X = df[["diameter_mm", "torque_nm"]]
y = df["status"]


# =================================
# TRAIN ML MODEL
# =================================

model = DecisionTreeClassifier(
    random_state=42
)

model.fit(X, y)


# =================================
# MAIN WINDOW
# =================================

window = tk.Tk()

window.title(
    "AI Mechanical CAD Assistant"
)

window.geometry(
    "800x800"
)

window.minsize(
    700,
    700
)


# =================================
# MAIN CONTAINER
# =================================

main_frame = tk.Frame(
    window
)

main_frame.pack(
    fill="both",
    expand=True
)


# =================================
# TITLE
# =================================

title = tk.Label(
    main_frame,
    text="AI MECHANICAL CAD ASSISTANT",
    font=("Arial", 22, "bold")
)

title.pack(
    pady=(20, 5)
)


# =================================
# SUBTITLE
# =================================

subtitle = tk.Label(
    main_frame,
    text="AI-Powered Shaft Design & Analysis",
    font=("Arial", 12)
)

subtitle.pack(
    pady=(0, 15)
)


# =================================
# INPUT FRAME
# =================================

input_frame = tk.Frame(
    main_frame
)

input_frame.pack(
    pady=5
)


# =================================
# DIAMETER
# =================================

tk.Label(
    input_frame,
    text="Shaft Diameter (mm):",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=7,
    sticky="e"
)

diameter_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Arial", 12)
)

diameter_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=7
)


# =================================
# TORQUE
# =================================

tk.Label(
    input_frame,
    text="Applied Torque (N.m):",
    font=("Arial", 12)
).grid(
    row=1,
    column=0,
    padx=10,
    pady=7,
    sticky="e"
)

torque_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Arial", 12)
)

torque_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=7
)


# =================================
# REQUIRED FOS
# =================================

tk.Label(
    input_frame,
    text="Required FOS:",
    font=("Arial", 12)
).grid(
    row=2,
    column=0,
    padx=10,
    pady=7,
    sticky="e"
)

fos_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Arial", 12)
)

fos_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=7
)


# =================================
# SHAFT LENGTH
# =================================

tk.Label(
    input_frame,
    text="Shaft Length (mm):",
    font=("Arial", 12)
).grid(
    row=3,
    column=0,
    padx=10,
    pady=7,
    sticky="e"
)

length_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Arial", 12)
)

length_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=7
)


# =================================
# RESULT FRAME
# =================================

result_frame = tk.Frame(
    main_frame,
    height=350
)

result_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=10
)

result_frame.pack_propagate(False)


# =================================
# SCROLLBAR
# =================================

scrollbar = tk.Scrollbar(
    result_frame
)

scrollbar.pack(
    side="right",
    fill="y"
)


# =================================
# RESULT TEXT
# =================================

result_text = tk.Text(
    result_frame,
    font=("Courier New", 10),
    wrap="none",
    yscrollcommand=scrollbar.set
)

result_text.pack(
    side="left",
    fill="both",
    expand=True
)


# =================================
# CONNECT SCROLLBAR
# =================================

scrollbar.config(
    command=result_text.yview
)


# =================================
# ANALYZE FUNCTION
# =================================

def analyze_design():

    try:

        # =================================
        # GET INPUT
        # =================================

        diameter = float(
            diameter_entry.get()
        )

        torque = float(
            torque_entry.get()
        )

        required_fos = float(
            fos_entry.get()
        )

        length = float(
            length_entry.get()
        )


        # =================================
        # VALIDATE INPUT
        # =================================

        if (
            diameter <= 0
            or torque <= 0
            or required_fos <= 0
            or length <= 0
        ):

            raise ValueError


        # =================================
        # ML PREDICTION
        # =================================

        new_shaft = pd.DataFrame({

            "diameter_mm": [
                diameter
            ],

            "torque_nm": [
                torque
            ]

        })

        prediction = model.predict(
            new_shaft
        )[0]


        # =================================
        # ENGINEERING CALCULATION
        # =================================

        allowable_stress = 150

        torque_nmm = (
            torque * 1000
        )

        shear_stress = (
            16 * torque_nmm
        ) / (
            math.pi * diameter ** 3
        )

        factor_of_safety = (
            allowable_stress
            / shear_stress
        )


        if factor_of_safety >= required_fos:

            engineering_result = "PASS"

        else:

            engineering_result = "FAIL"


        # =================================
        # ML VS ENGINEERING
        # =================================

        if prediction == engineering_result:

            comparison = "MATCH"

        else:

            comparison = "DIFFER"


        # =================================
        # OPTIMIZATION
        # =================================

        recommended_diameter = None

        recommended_fos = None

        for test_diameter in range(10, 101):

            test_shear_stress = (
                16 * torque_nmm
            ) / (
                math.pi
                * test_diameter ** 3
            )

            test_fos = (
                allowable_stress
                / test_shear_stress
            )

            if test_fos >= required_fos:

                recommended_diameter = (
                    test_diameter
                )

                recommended_fos = (
                    test_fos
                )

                break


        # =================================
        # CHECK OPTIMIZATION
        # =================================

        if recommended_diameter is None:

            result_text.delete(
                "1.0",
                tk.END
            )

            result_text.insert(
                tk.END,
                "No suitable diameter found "
                "between 10 mm and 100 mm."
            )

            return


        # =================================
        # OPTIMIZED ML PREDICTION
        # =================================

        optimized_shaft = pd.DataFrame({

            "diameter_mm": [
                recommended_diameter
            ],

            "torque_nm": [
                torque
            ]

        })

        optimized_prediction = model.predict(
            optimized_shaft
        )[0]


        # =================================
        # OPTIMIZED ENGINEERING
        # =================================

        optimized_shear_stress = (
            16 * torque_nmm
        ) / (
            math.pi
            * recommended_diameter ** 3
        )

        optimized_fos = (
            allowable_stress
            / optimized_shear_stress
        )


        if optimized_fos >= required_fos:

            optimized_engineering_result = "PASS"

        else:

            optimized_engineering_result = "FAIL"


        # =================================
        # FINAL DESIGN
        # =================================

        if (
            optimized_prediction == "PASS"
            and optimized_engineering_result == "PASS"
        ):

            final_design = "PASS"

        else:

            final_design = "REVIEW REQUIRED"


        # =================================
        # GENERATE CAD
        # =================================

        cad_file = (
            PROJECT_ROOT
            / "shaft_design.dxf"
        )

        create_shaft_dxf(

            diameter=recommended_diameter,

            length=length,

            output_file=cad_file

        )


        # =================================
        # RESULT TEXT
        # =================================

        result = f"""
AI SHAFT ANALYSIS
========================================

INPUT PARAMETERS

Shaft Diameter:
{diameter:.2f} mm

Applied Torque:
{torque:.2f} N.m

Required FOS:
{required_fos:.2f}

Shaft Length:
{length:.2f} mm


AI PREDICTION
========================================

ML Prediction:
{prediction}


ENGINEERING VERIFICATION
========================================

Shear Stress:
{shear_stress:.2f} MPa

Factor of Safety:
{factor_of_safety:.2f}

Engineering Result:
{engineering_result}


AI vs ENGINEERING
========================================

Comparison:
{comparison}


OPTIMIZED DESIGN
========================================

Recommended Diameter:
{recommended_diameter} mm

Optimized Shear Stress:
{optimized_shear_stress:.2f} MPa

Optimized FOS:
{optimized_fos:.2f}

Engineering Result:
{optimized_engineering_result}


AI DESIGN CONFIRMATION
========================================

Optimized Diameter:
{recommended_diameter} mm

ML Prediction:
{optimized_prediction}

Engineering Result:
{optimized_engineering_result}

FINAL DESIGN:
{final_design}


CAD GENERATION
========================================

CAD Diameter:
{recommended_diameter} mm

CAD Length:
{length:.2f} mm

CAD File:
{cad_file}

CAD Status:
GENERATED


========================================
AI SHAFT ASSISTANT COMPLETE
========================================
"""


        # =================================
        # SHOW RESULT
        # =================================

        result_text.delete(
            "1.0",
            tk.END
        )

        result_text.insert(
            tk.END,
            result
        )


        # =================================
        # VISUALIZATION
        # =================================

        visualize_shaft(

            torque=torque,

            required_fos=required_fos,

            recommended_diameter=
            recommended_diameter,

            allowable_stress=
            allowable_stress

        )


        # =================================
        # SUCCESS MESSAGE
        # =================================

        messagebox.showinfo(

            "CAD Generated",

            f"CAD drawing generated successfully!\n\n"
            f"Diameter: {recommended_diameter} mm\n"
            f"Length: {length:.2f} mm\n\n"
            f"Saved to:\n{cad_file}"

        )


    except ValueError:

        messagebox.showerror(

            "Invalid Input",

            "Please enter valid positive numbers."

        )


    except Exception as error:

        messagebox.showerror(

            "Application Error",

            str(error)

        )


# =================================
# ANALYZE BUTTON
# =================================

analyze_button = tk.Button(

    main_frame,

    text="ANALYZE DESIGN + GENERATE CAD",

    font=("Arial", 14, "bold"),

    padx=30,

    pady=10,

    command=analyze_design

)

analyze_button.pack(
    pady=10
)


# =================================
# START APPLICATION
# =================================

window.mainloop()