import pandas as pd
import streamlit as st

from core.risk_engine import RiskResult


def render_risk_chart(result: RiskResult):
    """Display risk score analytics and factor contribution chart."""

    st.subheader("Risk Analytics")

    st.caption(
        "Visual analysis of the factors contributing "
        "to the calculated demonstration score."
    )

    # =====================================================
    # SCORE OVERVIEW
    # =====================================================

    st.markdown("#### Risk Score Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Risk Score",
            f"{result.score}/100",
        )

    with col2:
        st.metric(
            "Risk Level",
            result.level,
        )

    with col3:
        active_factors = sum(
            value > 0
            for value in result.factors.values()
        )

        st.metric(
            "Active Factors",
            active_factors,
        )

    st.progress(
        result.score / 100,
        text=f"Overall Score: {result.score}/100",
    )

    st.divider()

    # =====================================================
    # FACTOR DATA
    # =====================================================

    factor_data = pd.DataFrame(
        {
            "Factor": list(result.factors.keys()),
            "Points": list(result.factors.values()),
        }
    )

    active_factors = factor_data[
        factor_data["Points"] > 0
    ].copy()

    # =====================================================
    # FACTOR CONTRIBUTION CHART
    # =====================================================

    st.markdown("#### Factor Contribution")

    if active_factors.empty:

        st.info(
            "No risk factors are currently contributing "
            "to the calculated score."
        )

        return

    active_factors = active_factors.sort_values(
        by="Points",
        ascending=False,
    )

    chart_data = active_factors.set_index(
        "Factor"
    )

    st.bar_chart(
        chart_data,
        y="Points",
        horizontal=True,
        height=350,
    )

    st.caption(
        "Higher bars indicate a larger contribution "
        "to the demonstration risk score."
    )

    st.divider()

    # =====================================================
    # FACTOR DETAILS
    # =====================================================

    st.markdown("#### Factor Details")

    for _, row in active_factors.iterrows():

        factor = row["Factor"]
        points = int(row["Points"])

        col1, col2 = st.columns([5, 1])

        with col1:

            st.markdown(
                f"**{factor}**"
            )

            st.progress(
                min(points / 20, 1.0)
            )

        with col2:

            st.metric(
                "Points",
                f"+{points}",
            )

    st.divider()

    # =====================================================
    # CONTRIBUTION TABLE
    # =====================================================

    st.markdown("#### Contribution Summary")

    display_data = active_factors.copy()

    display_data["Contribution"] = (
        display_data["Points"]
        .apply(lambda x: f"+{x} points")
    )

    display_data = display_data[
        ["Factor", "Contribution"]
    ]

    st.dataframe(
        display_data,
        width="stretch",
        hide_index=True,
    )

    # =====================================================
    # DISCLAIMER
    # =====================================================

    st.caption(
        "This visualization represents the rule-based "
        "logic used by this educational demonstration."
    )