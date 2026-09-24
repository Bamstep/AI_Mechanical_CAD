# AI Mechanical CAD Assistant

**AI-assisted mechanical shaft analysis, design optimization, visualization, and automated CAD generation.**

## Overview

The **AI Mechanical CAD Assistant** is an educational and research-oriented engineering prototype that combines classical mechanical engineering calculations, machine learning, design optimization, visualization, and automated CAD generation.

The current version focuses on the analysis and preliminary design optimization of **solid circular shafts subjected to torsional loading**.

The system allows a user to enter a shaft diameter, applied torque, required factor of safety, and shaft length. It then:

1. Uses a machine-learning model to predict whether the design passes or fails.
2. Independently verifies the design using classical torsion equations.
3. Compares the ML prediction with the engineering calculation.
4. Searches for a smaller shaft diameter that satisfies the required factor of safety.
5. Verifies the optimized design.
6. Generates a CAD drawing of the shaft.
7. Visualizes the shaft geometry.

---

## Project Workflow

```text
USER INPUT
     │
     ▼
AI/ML PREDICTION
     │
     ▼
ENGINEERING VERIFICATION
     │
     ▼
ML vs ENGINEERING COMPARISON
     │
     ▼
DESIGN OPTIMIZATION
     │
     ▼
OPTIMIZED DESIGN CONFIRMATION
     │
     ▼
CAD GENERATION
     │
     ▼
SHAFT VISUALIZATION
```

---

## Engineering Problem

For a solid circular shaft subjected to torque, the maximum shear stress is calculated using:

$$
\tau_{\max} = \frac{16T}{\pi d^3}
$$

where:

* $T$ = applied torque
* $d$ = shaft diameter
* $\tau_{\max}$ = maximum shear stress

The polar second moment of area for a solid circular shaft is:

$$
J = \frac{\pi d^4}{32}
$$

where:

* $J$ = polar second moment of area
* $d$ = shaft diameter

The general torsion relationship is:

$$
\tau = \frac{Tr}{J}
$$

where:

* $\tau$ = shear stress
* $T$ = applied torque
* $r$ = radial distance from the shaft center
* $J$ = polar second moment of area

For a solid circular shaft, the maximum shear stress occurs at the outer surface where:

$$
r = \frac{d}{2}
$$

Substituting the polar second moment of area gives:

$$
\tau_{\max} = \frac{16T}{\pi d^3}
$$

The factor of safety is calculated as:

$$
FOS = \frac{\text{Allowable Shear Stress}}{\text{Actual Shear Stress}}
$$

For this prototype, an allowable shear stress of **150 MPa** is used.

The design passes when:

$$
FOS \geq FOS_{\text{required}}
$$

---

## Machine Learning

The project uses a **Decision Tree Classifier** to predict whether a shaft design will pass or fail.

### Input Features

* Shaft diameter
* Applied torque

### Target

* `PASS`
* `FAIL`

The training dataset contains synthetic shaft designs generated using the classical torsion equation.

The model currently achieves high classification accuracy on the generated dataset.

However, this accuracy should **not** be interpreted as real-world engineering validation because the dataset is synthetic and the labels are generated from the same engineering relationship used for verification.

---

## Engineering Verification

The ML prediction is not treated as the final engineering authority.

Every design is independently checked using the mechanical engineering equations.

This creates an important separation:

```text
Machine Learning
      ↓
Prediction

Classical Engineering
      ↓
Verification
```

The engineering calculation provides an independent check of the ML prediction.

---

## Design Optimization

The optimization module searches through possible shaft diameters and identifies a smaller diameter that satisfies the required factor of safety.

The objective is not simply to make the shaft as small as possible.

Instead, the goal is to find a design that:

* satisfies the required safety factor
* remains within the simplified engineering constraints
* avoids unnecessary material usage

This reflects an important engineering principle:

> Use the required amount of material to safely perform the function rather than unnecessarily over-designing the component.

---

## Example

Example input:

```text
Shaft Diameter:       40 mm
Applied Torque:       650 N·m
Required FOS:         2
Shaft Length:         200 mm
```

Example analysis:

```text
ML Prediction:             PASS

Shear Stress:              51.73 MPa
Factor of Safety:           2.90
Engineering Verification:   PASS

ML vs Engineering:          MATCH

Optimized Diameter:         36 mm
Optimized Shear Stress:     70.95 MPa
Optimized FOS:               2.11

Final Design:               PASS
```

The optimized design is then used to generate the CAD representation.

---

## Automated CAD Generation

The project uses **ezdxf** to generate a DXF representation of the optimized shaft.

The CAD generator creates:

* Shaft outline
* Center line
* Diameter information
* Length information
* Engineering annotations
* Design title

The generated file is:

```text
shaft_design.dxf
```

The DXF file can be opened in compatible CAD software such as AutoCAD.

---

## Visualization

The project includes shaft visualization to provide a graphical representation of the analyzed design.

This creates a complete workflow from:

```text
Engineering Input
       ↓
Calculation
       ↓
Optimization
       ↓
CAD
       ↓
Visualization
```

---

## Project Structure

```text
AI_Mechanical_CAD/
│
├── .gitignore
├── README.md
│
├── data/
│   ├── shaft_dataset.csv
│   ├── generate_dataset.py
│   └── inspect_dataset.py
│
├── models/
│   ├── train_model.py
│   └── test_model.py
│
├── engineering/
│   ├── shaft_analyzer.py
│   └── shaft_visualization.py
│
├── optimization/
│   └── design_optimizer.py
│
├── app/
│   ├── ai_shaft_assistant.py
│   └── gui.py
│
├── cad/
│   └── shaft_dxf_generator.py
│
└── shaft_design.dxf
```

---

## Technologies Used

### Programming

* Python

### Machine Learning

* Scikit-learn
* Decision Tree Classification

### Engineering Computation

* NumPy

### Data Processing

* Pandas

### Visualization

* Matplotlib

### GUI

* Tkinter

### CAD Automation

* ezdxf

### Development

* Visual Studio Code
* Git
* GitHub

---

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project:

```bash
cd AI_Mechanical_CAD
```

Install the required Python packages:

```bash
pip install numpy pandas matplotlib scikit-learn ezdxf
```

---

## Running the Project

The main graphical interface can be started with:

```bash
python app/gui.py
```

Enter the required shaft parameters and select:

```text
ANALYZE DESIGN + GENERATE CAD
```

The application will perform the analysis, optimization, verification, visualization, and CAD generation.

---

## Current Limitations

This project is an **educational/research prototype** and should not be used as certified engineering design software.

The current model is limited because:

* The ML dataset is synthetic.
* The current engineering model focuses primarily on torsional loading.
* Material behavior is simplified.
* The allowable shear stress is fixed for the prototype.
* Fatigue loading is not currently modeled.
* Stress concentration effects are not currently modeled.
* Keyways and geometric discontinuities are not currently modeled.
* Combined bending and torsional loading is not currently modeled.
* Bearings, gears, vibration, and dynamic loading are not currently included.
* Finite Element Analysis is not currently included.
* The ML model has not been validated against laboratory or industrial datasets.

Therefore, the results should be treated as **preliminary engineering analysis and educational demonstration**, not as a replacement for detailed engineering calculations, simulation, testing, or applicable design standards.

---

## Future Development

### V2 — Advanced Mechanical Analysis

* Bending stress
* Shear force
* Deflection
* Combined bending and torsion
* Angle of twist
* Material selection
* More realistic safety constraints

### V3 — Advanced Design Optimization

* Weight optimization
* Material-cost optimization
* Multi-objective optimization
* Automated material selection
* Constraint-based optimization

### V4 — Engineering Simulation + AI

* Finite Element Analysis
* Simulation-generated training data
* ML surrogate models
* Stress prediction
* Deformation prediction
* Failure-risk prediction

### V5 — Predictive Engineering

Potential applications include:

* Predictive maintenance
* Mechanical component health monitoring
* Failure prediction
* Equipment diagnostics
* Engineering design assistance

---

## Engineering + AI

The long-term goal of this project is to explore how **artificial intelligence can assist mechanical engineers without replacing engineering fundamentals**.

The project follows an important principle:

```text
Engineering Fundamentals
          +
Data
          +
Machine Learning
          +
Optimization
          +
Automation
          =
AI-Assisted Engineering
```

The AI component is therefore treated as an assistant, while engineering theory remains essential for verification and responsible decision-making.

---

## Disclaimer

This project is intended for **educational, research, and portfolio purposes**.

It is not certified engineering software and should not be used as the sole basis for the design, manufacture, or operation of safety-critical mechanical components.

Professional engineering analysis, applicable standards, simulation, testing, and engineering review should be performed before using any design in a real-world application.

---

## Author

**Bamidele Stephen Omotayo**

Mechanical Engineering Student
Ekiti State University, Nigeria

Interests:

* Mechanical Engineering
* Artificial Intelligence
* Machine Learning
* Engineering Automation
* CAD
* Energy and Industrial Engineering

---

## Project Status

**Current status: Engineering Prototype**

The first version demonstrates the integration of:

**Mechanical Engineering + Machine Learning + Optimization + CAD Automation + Visualization**

Future versions will progressively incorporate more realistic engineering models, simulation data, advanced optimization, and additional mechanical engineering applications.
