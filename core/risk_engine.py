from dataclasses import dataclass


@dataclass
class RiskResult:
    score: int
    level: str
    factors: dict[str, int]


def calculate_risk(
    age: int,
    blood_pressure: int,
    glucose: int,
    gender: str,
    bmi: float,
    smoking: str,
    activity: str,
) -> RiskResult:
    """
    Calculate a simple rule-based health risk score.

    This is a demonstration score for the Streamlit application.
    It is not a medical diagnostic model.
    """

    factors = {
        "Age": 0,
        "Blood Pressure": 0,
        "Glucose": 0,
        "BMI": 0,
        "Smoking": 0,
        "Physical Activity": 0,
    }

    # Age
    if age >= 65:
        factors["Age"] = 20
    elif age >= 50:
        factors["Age"] = 15
    elif age >= 35:
        factors["Age"] = 8

    # Blood pressure
    if blood_pressure >= 140:
        factors["Blood Pressure"] = 20
    elif blood_pressure >= 130:
        factors["Blood Pressure"] = 12
    elif blood_pressure >= 120:
        factors["Blood Pressure"] = 6

    # Glucose
    if glucose >= 126:
        factors["Glucose"] = 20
    elif glucose >= 100:
        factors["Glucose"] = 12
    elif glucose >= 90:
        factors["Glucose"] = 5

    # BMI
    if bmi >= 30:
        factors["BMI"] = 15
    elif bmi >= 25:
        factors["BMI"] = 8
    elif bmi < 18.5:
        factors["BMI"] = 5

    # Smoking
    if smoking == "Current smoker":
        factors["Smoking"] = 15
    elif smoking == "Former smoker":
        factors["Smoking"] = 7

    # Physical activity
    if activity == "Low":
        factors["Physical Activity"] = 10
    elif activity == "Moderate":
        factors["Physical Activity"] = 4

    score = min(sum(factors.values()), 100)

    if score < 30:
        level = "Low Risk"
    elif score < 60:
        level = "Moderate Risk"
    else:
        level = "High Risk"

    return RiskResult(
        score=score,
        level=level,
        factors=factors,
    )