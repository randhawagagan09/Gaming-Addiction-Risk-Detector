import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Gaming Addiction Detector", layout="wide")

# -----------------------------
# Dark Theme Styling
# -----------------------------

st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #061826;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0B2239;
    border-right: 1px solid #12395B;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Graph Cards */
.card {
    background-color: #102B46;
    padding: 15px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.35);
    border: 1px solid #1E4D78;
}

/* Tabs */
button[data-baseweb="tab"] {
    font-size: 17px;
    color: white;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #00B4DB, #0083B0);
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    height: 45px;
    width: 100%;
}

/* Progress Bar */
.stProgress > div > div > div > div {
    background-color: #00C2FF;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("🎮 Gaming Addiction Risk Detector")
st.markdown("### Analyze your gaming behavior and mental health risk")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("📝 Enter Your Details")

daily_gaming_hours = st.sidebar.slider("Daily Gaming Hours", 0, 12, 4)
social_isolation_score = st.sidebar.slider("Social Isolation Score", 0, 10, 5)
withdrawal_symptoms = st.sidebar.slider("Withdrawal Symptoms", 0, 10, 5)
sleep_disruption = st.sidebar.slider("Sleep Disruption Frequency", 0, 10, 5)
mood_swings = st.sidebar.slider("Mood Swing Frequency", 0, 10, 5)
continued_despite = st.sidebar.slider("Continue Despite Problems", 0, 10, 5)
exercise_hours = st.sidebar.slider("Exercise Hours Weekly", 0, 10, 3)
academic_perf = st.sidebar.slider("Academic Performance", 0, 10, 5)

# -----------------------------
# Functions
# -----------------------------
def calculate_mental_analysis(data):
    score = (
        data['daily_gaming_hours'] * 0.25 +
        data['social_isolation_score'] * 0.15 +
        data['withdrawal_symptoms'] * 0.15 +
        data['sleep_disruption_frequency'] * 0.10 +
        data['mood_swing_frequency'] * 0.10 +
        data['continued_despite_problems'] * 0.10 -
        data['exercise_hours_weekly'] * 0.15 -
        data['academic_work_performance'] * 0.15
    )
    return max(score, 0)

def categorize(score):
    if score <= 2:
        return "Low"
    elif score <= 5:
        return "Moderate"
    elif score <= 8:
        return "High"
    else:
        return "Severe"

# -----------------------------
# Tabs Layout
# -----------------------------
tab1, tab2 = st.tabs(["📊 Prediction", "📘 About Project"])

# =====================================================
# TAB 1 : PREDICTION
# =====================================================
with tab1:

    if st.button("🔍 Predict Risk Level"):

        # -----------------------------
        # Input Data
        # -----------------------------
        data = {
            'daily_gaming_hours': daily_gaming_hours,
            'social_isolation_score': social_isolation_score,
            'withdrawal_symptoms': withdrawal_symptoms,
            'sleep_disruption_frequency': sleep_disruption,
            'mood_swing_frequency': mood_swings,
            'continued_despite_problems': continued_despite,
            'exercise_hours_weekly': exercise_hours,
            'academic_work_performance': academic_perf
        }

        # -----------------------------
        # Prediction
        # -----------------------------
        score = calculate_mental_analysis(data)
        risk = categorize(score)

        st.subheader("📊 Result")

        st.write(f"**Mental Analysis Score:** {round(score,2)}")

        st.progress(int(score * 10))

        # -----------------------------
        # Risk Output
        # -----------------------------
        if risk == "Low":
            st.success("🟢 Low Risk")
            st.write("You have a balanced gaming lifestyle. Keep it up!")

        elif risk == "Moderate":
            st.warning("🟡 Moderate Risk")
            st.write("Try reducing gaming time and improve daily routine.")

        elif risk == "High":
            st.error("🟠 High Risk")
            st.write("Gaming is affecting your lifestyle. Consider limiting usage.")

        else:
            st.error("🔴 Severe Risk")
            st.write("Strong signs of addiction. Professional guidance is recommended.")

        # =====================================================
        # FEATURE-WISE ANALYSIS
        # =====================================================
        st.markdown("## 📊 Feature-wise Analysis")

        categories = [
            "Daily Gaming Hours",
            "Social Isolation Score",
            "Withdrawal Symptoms",
            "Sleep Disruption Frequency",
            "Mood Swing Frequency",
            "Continue Despite Problems",
            "Exercise Hours Weekly",
            "Academic Performance"
        ]

        values = [
            daily_gaming_hours,
            social_isolation_score,
            withdrawal_symptoms,
            sleep_disruption,
            mood_swings,
            continued_despite,
            exercise_hours,
            academic_perf
        ]

        ideal_values = [2, 3, 2, 3, 3, 2, 5, 7]

        # =====================================================
        # GRID GRAPH LAYOUT
        # =====================================================
        for i in range(0, len(categories), 2):

            col1, col2 = st.columns(2)

            # -----------------------------
            # First Graph
            # -----------------------------
            with col1:

                st.markdown('<div class="card">', unsafe_allow_html=True)

                fig1 = go.Figure()

                fig1.add_trace(go.Bar(
                    x=["Your Value", "Ideal"],
                    y=[values[i], ideal_values[i]],
                    marker_color=["#4DA8FF", "#00FFD1"]
                ))

                fig1.update_layout(
                    title=categories[i],
                    paper_bgcolor="#112240",
                    plot_bgcolor="#112240",
                    font=dict(color="white"),
                    yaxis=dict(range=[0, 10])
                )

                st.plotly_chart(
                    fig1,
                    use_container_width=True,
                    key=f"chart_{i}"
                )

                st.markdown('</div>', unsafe_allow_html=True)

            # -----------------------------
            # Second Graph
            # -----------------------------
            if i + 1 < len(categories):

                with col2:

                    st.markdown('<div class="card">', unsafe_allow_html=True)

                    fig2 = go.Figure()

                    fig2.add_trace(go.Bar(
                        x=["Your Value", "Ideal"],
                        y=[values[i+1], ideal_values[i+1]],
                        marker_color=["#4DA8FF", "#00FFD1"]
                    ))

                    fig2.update_layout(
                        title=categories[i+1],
                        paper_bgcolor="#112240",
                        plot_bgcolor="#112240",
                        font=dict(color="white"),
                        yaxis=dict(range=[0, 10])
                    )

                    st.plotly_chart(
                        fig2,
                        use_container_width=True,
                        key=f"chart_{i+1}"
                    )

                    st.markdown('</div>', unsafe_allow_html=True)

        # =====================================================
        # FINAL COMPARISON GRAPH
        # =====================================================
        st.markdown("## 📊 Overall Comparison")

        fig_final = go.Figure()

        fig_final.add_trace(go.Bar(
            x=categories,
            y=values,
            name="Your Score",
            marker_color="#4DA8FF"
        ))

        fig_final.add_trace(go.Bar(
            x=categories,
            y=ideal_values,
            name="Ideal Score",
            marker_color="#00FFD1"
        ))

        fig_final.update_layout(
            barmode='group',
            paper_bgcolor="#112240",
            plot_bgcolor="#112240",
            font=dict(color="white")
        )

        st.plotly_chart(
            fig_final,
            use_container_width=True,
            key="final_chart"
        )

# =====================================================
# TAB 2 : ABOUT PROJECT
# =====================================================
with tab2:

    st.markdown("## 🧠 How it Works")

    st.write("""
    This system evaluates gaming addiction risk using behavioral and lifestyle factors.

    It calculates a mental health score based on:

    - Gaming hours
    - Social isolation
    - Sleep disruption
    - Mood swings
    - Exercise and academic performance

    The score is then categorized into:

    - Low Risk
    - Moderate Risk
    - High Risk
    - Severe Risk
    """)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("👨‍💻 Developed by Gagan Randhawa | BTech CSE Project")