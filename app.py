import pandas as pd
import streamlit as st

from components.inputs import render_inputs
from components.results import render_results
from components.charts import render_risk_chart
from core.risk_engine import calculate_risk
from utils.export import create_result_csv, create_result_json


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="RiskCare | Health Risk Calculator",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# GLOBAL UI STYLING
# =========================================================

st.markdown(
    """
    <style>

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.18);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }

    section[data-testid="stSidebar"] h1 {
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -0.4px;
        margin-bottom: 0.2rem;
    }

    h1 {
        font-size: 2.5rem;
        font-weight: 700;
        letter-spacing: -0.8px;
        margin-bottom: 0.3rem;
    }

    h2 {
        font-weight: 650;
        letter-spacing: -0.4px;
    }

    h3 {
        font-weight: 650;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 14px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        padding: 0.4rem;
    }

    div.stButton > button {
        width: 100%;
        min-height: 46px;
        border-radius: 10px;
        font-weight: 600;
        border: 1px solid rgba(128, 128, 128, 0.25);
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
    }

    div.stDownloadButton > button {
        width: 100%;
        min-height: 46px;
        border-radius: 10px;
        font-weight: 600;
    }

    div[data-baseweb="select"] > div {
        border-radius: 9px;
    }

    div[data-testid="stNumberInput"] input {
        border-radius: 9px;
    }

    div[data-testid="stMetric"] {
        border: 1px solid rgba(128, 128, 128, 0.18);
        border-radius: 12px;
        padding: 1rem;
        background: rgba(128, 128, 128, 0.035);
    }

    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem;
    }

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 10px;
        overflow: hidden;
    }

    hr {
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

    @media (max-width: 900px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        h1 {
            font-size: 2rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("RiskCare")

    st.caption("Health Risk Assessment Dashboard")

    st.divider()

    st.subheader("Calculator")

    st.caption(
        "Adjust patient parameters and calculate "
        "a rule-based demonstration risk score."
    )

    st.divider()

    st.markdown("#### Risk Scale")

    st.write("🟢 **Low Risk**")
    st.caption("Score: 0–29")

    st.write("🟡 **Moderate Risk**")
    st.caption("Score: 30–59")

    st.write("🔴 **High Risk**")
    st.caption("Score: 60–100")

    st.divider()

    st.markdown("#### System")

    st.caption("Scoring Method")
    st.write("Rule-Based")

    st.caption("Score Range")
    st.write("0–100")

    st.caption("Application Type")
    st.write("Educational Demo")

    st.divider()

    if st.button(
        "↻ Reset Assessment",
        width="stretch",
    ):
        st.session_state.pop("risk_result", None)
        st.session_state.pop("risk_inputs", None)
        st.rerun()

    st.divider()

    st.caption(
        "This application is an educational demonstration "
        "and is not a medical diagnostic system."
    )


# =========================================================
# PAGE HEADER
# =========================================================

with st.container(border=True):

    st.caption("RULE-BASED HEALTH ASSESSMENT")

    st.title("Health Risk Calculator")

    st.write(
        "Explore how common health-related factors can "
        "contribute to a simple demonstration risk score."
    )


# =========================================================
# PATIENT INFORMATION
# =========================================================

st.write("")

st.subheader("Patient Information")

st.caption(
    "Enter the available patient parameters below."
)

with st.container(border=True):

    inputs = render_inputs()


# =========================================================
# RISK CALCULATION
# =========================================================

st.write("")

st.subheader("Risk Assessment")

st.caption(
    "Review the selected parameters and run the "
    "rule-based assessment."
)

calculate_button = st.button(
    "Calculate Risk Score",
    type="primary",
    width="stretch",
)


# =========================================================
# CALCULATE RISK
# =========================================================

if calculate_button:

    result = calculate_risk(
        age=inputs["age"],
        blood_pressure=inputs["blood_pressure"],
        glucose=inputs["glucose"],
        gender=inputs["gender"],
        bmi=inputs["bmi"],
        smoking=inputs["smoking"],
        activity=inputs["activity"],
    )

    st.session_state["risk_result"] = result
    st.session_state["risk_inputs"] = inputs


# =========================================================
# RESULTS
# =========================================================

if "risk_result" in st.session_state:

    result = st.session_state["risk_result"]

    saved_inputs = st.session_state["risk_inputs"]

    # -----------------------------------------------------
    # RESULT SUMMARY
    # -----------------------------------------------------

    st.write("")

    with st.container(border=True):

        render_results(result)

    # -----------------------------------------------------
    # ANALYTICS
    # -----------------------------------------------------

    st.write("")

    with st.container(border=True):

        render_risk_chart(result)

    # -----------------------------------------------------
    # DIRECT FACTOR CHART
    # -----------------------------------------------------

    st.write("")

    with st.container(border=True):

        st.subheader("Factor Contribution Chart")

        st.caption(
            "Direct visualization of the points contributed "
            "by each risk factor."
        )

        chart_data = pd.DataFrame(
            {
                "Factor": list(result.factors.keys()),
                "Points": list(result.factors.values()),
            }
        )

        chart_data = chart_data[
            chart_data["Points"] > 0
        ].copy()

        if not chart_data.empty:

            chart_data = chart_data.sort_values(
                by="Points",
                ascending=False,
            )

            st.bar_chart(
                chart_data,
                x="Factor",
                y="Points",
                height=350,
                width="stretch",
            )

        else:

            st.info(
                "No risk factors are currently contributing "
                "to the calculated score."
            )

    # -----------------------------------------------------
    # EXPORT
    # -----------------------------------------------------

    st.write("")

    with st.container(border=True):

        st.subheader("Export Assessment")

        st.caption(
            "Save the current assessment for later reference."
        )

        json_data = create_result_json(
            saved_inputs,
            result,
        )

        csv_data = create_result_csv(
            saved_inputs,
            result,
        )

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name="risk_assessment.json",
                mime="application/json",
                width="stretch",
            )

        with col2:

            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name="risk_assessment.csv",
                mime="text/csv",
                width="stretch",
            )


# =========================================================
# EMPTY STATE
# =========================================================

else:

    st.write("")

    with st.container(border=True):

        st.subheader("Ready for Assessment")

        st.caption(
            "Complete the patient information above "
            "to generate a demonstration risk assessment."
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Input Categories",
                "3",
            )

        with col2:

            st.metric(
                "Risk Factors",
                "6",
            )

        with col3:

            st.metric(
                "Score Range",
                "0–100",
            )

        st.write("")

        st.info(
            "Complete the patient information above and "
            "select Calculate Risk Score when ready."
        )


# =========================================================
# FOOTER
# =========================================================

st.write("")

st.divider()

st.caption(
    "RiskCare • Rule-Based Health Risk Calculator • "
    "Educational Demonstration"
)