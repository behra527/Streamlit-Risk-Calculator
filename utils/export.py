import json


def create_result_json(inputs: dict, result) -> str:
    """Create a JSON representation of the risk assessment."""

    data = {
        "assessment": {
            "risk_score": result.score,
            "risk_level": result.level,
        },
        "patient_inputs": {
            "age": inputs["age"],
            "blood_pressure": inputs["blood_pressure"],
            "glucose": inputs["glucose"],
            "gender": inputs["gender"],
            "bmi": inputs["bmi"],
            "smoking": inputs["smoking"],
            "physical_activity": inputs["activity"],
        },
        "risk_factors": result.factors,
    }

    return json.dumps(
        data,
        indent=4,
    )


def create_result_csv(inputs: dict, result) -> str:
    """Create a CSV representation of the risk assessment."""

    rows = [
        "Field,Value",
        f"Risk Score,{result.score}",
        f"Risk Level,{result.level}",
        f"Age,{inputs['age']}",
        f"Blood Pressure,{inputs['blood_pressure']}",
        f"Glucose,{inputs['glucose']}",
        f"Gender,{inputs['gender']}",
        f"BMI,{inputs['bmi']}",
        f"Smoking Status,{inputs['smoking']}",
        f"Physical Activity,{inputs['activity']}",
    ]

    return "\n".join(rows)