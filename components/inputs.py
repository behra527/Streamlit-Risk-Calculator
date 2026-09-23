import streamlit as st


def render_inputs():
    """Render patient input controls and return their values."""

    # =====================================================
    # BASIC INFORMATION
    # =====================================================

    st.markdown("#### Basic Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider(
            "Age",
            min_value=18,
            max_value=100,
            value=35,
            step=1,
            help="Select the patient's age.",
        )

    with col2:
        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
                "Other",
            ],
            help="Select the patient's gender.",
        )

    st.write("")

    # =====================================================
    # CLINICAL MEASUREMENTS
    # =====================================================

    st.markdown("#### Clinical Measurements")

    col1, col2, col3 = st.columns(3)

    with col1:
        blood_pressure = st.slider(
            "Systolic Blood Pressure",
            min_value=80,
            max_value=200,
            value=120,
            step=1,
            help="Systolic blood pressure in mmHg.",
        )

    with col2:
        glucose = st.slider(
            "Glucose Level",
            min_value=50,
            max_value=250,
            value=100,
            step=1,
            help="Glucose level used for the demonstration score.",
        )

    with col3:
        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=60.0,
            value=22.0,
            step=0.1,
            help="Body Mass Index.",
        )

    st.write("")

    # =====================================================
    # LIFESTYLE FACTORS
    # =====================================================

    st.markdown("#### Lifestyle Factors")

    col1, col2 = st.columns(2)

    with col1:
        smoking = st.selectbox(
            "Smoking Status",
            [
                "Never smoker",
                "Former smoker",
                "Current smoker",
            ],
            help="Select the patient's smoking status.",
        )

    with col2:
        activity = st.select_slider(
            "Physical Activity",
            options=[
                "Low",
                "Moderate",
                "High",
            ],
            value="Moderate",
            help="Select the general physical activity level.",
        )

    # =====================================================
    # INPUT VALIDATION
    # =====================================================

    validation_messages = []

    if blood_pressure >= 180:
        validation_messages.append(
            "Systolic blood pressure is very high."
        )

    if glucose >= 200:
        validation_messages.append(
            "Glucose level is very high."
        )

    if bmi >= 40:
        validation_messages.append(
            "BMI is in the very high range."
        )

    if validation_messages:
        st.warning(
            " | ".join(validation_messages)
        )

    # =====================================================
    # RETURN INPUTS
    # =====================================================

    return {
        "age": age,
        "blood_pressure": blood_pressure,
        "glucose": glucose,
        "gender": gender,
        "bmi": bmi,
        "smoking": smoking,
        "activity": activity,
    }