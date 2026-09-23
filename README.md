# RiskCare — Health Risk Calculator

A Streamlit-based health risk assessment dashboard that demonstrates how patient parameters can be converted into a simple rule-based risk score.

## Project Overview

RiskCare is an educational Streamlit application designed to demonstrate interactive UI components and basic rule-based scoring.

Users can enter patient information and calculate a demonstration risk score from 0 to 100.

The application includes sliders dropdowns buttons containers sidebar components charts and export functionality.

## Features

- Age slider
- Gender dropdown
- Systolic blood pressure slider
- Glucose level slider
- BMI input
- Smoking status selection
- Physical activity selection
- Rule-based risk calculation
- Low Moderate and High risk levels
- Risk factor contribution analysis
- Interactive charts
- JSON export
- CSV export
- Reset assessment
- Responsive Streamlit layout
- Sidebar navigation and information panel

## Technology Stack

- Python
- Streamlit
- Pandas
- NumPy

## Project Structure

```text
Streamlit-Risk-Calculator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── components/
│   ├── __init__.py
│   ├── inputs.py
│   ├── results.py
│   └── charts.py
│
├── core/
│   ├── __init__.py
│   └── risk_engine.py
│
└── utils/
    ├── __init__.py
    └── export.py