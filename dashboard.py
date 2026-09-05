import streamlit as st
import plotly.graph_objects as go

from streamlit_autorefresh import st_autorefresh

from simulator import generate_pipeline_data
from predict import predict_risk
from rl_predict import get_action

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Live Autonomous CI/CD Agent",
    layout="wide"
)

st.title(
    "🚀 Live Autonomous CI/CD Monitoring"
)

st.markdown(
    "Real-time AI + RL powered "
    "CI/CD optimization system"
)

# =====================================
# AUTO REFRESH
# =====================================

st_autorefresh(
    interval=5000,
    key="refresh"
)

# =====================================
# GENERATE LIVE DATA
# =====================================

data = generate_pipeline_data()

input_num = [
    data["error_count"],
    data["duration"],
    0,
    data["coverage"],
    data["cpu_usage"],
    data["memory_usage"],
    data["past_failures"]
]

# =====================================
# PREDICTION
# =====================================

result = predict_risk(
    input_num,
    data["log_text"]
)

state = [
    result["Failure"]["probability"],
    result["Performance"]["probability"],
    result["Security"]["probability"],
    data["cpu_usage"] / 100,
    data["duration"] / 500
]

action, explanation = get_action(
    state
)

# =====================================
# HEALTH SCORE
# =====================================

avg_risk = (
    result["Failure"]["probability"] +
    result["Performance"]["probability"] +
    result["Security"]["probability"]
) / 3

health_score = int(
    (1 - avg_risk) * 100
)

# =====================================
# METRICS
# =====================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Pipeline Health",
    f"{health_score}%"
)

col2.metric(
    "CPU Usage",
    f"{data['cpu_usage']}%"
)

col3.metric(
    "Coverage",
    f"{data['coverage']}%"
)

col4.metric(
    "Duration",
    f"{data['duration']} sec"
)

st.divider()

# =====================================
# LOGS
# =====================================

st.subheader("📜 Live Pipeline Logs")

st.code(data["log_text"])

# =====================================
# RISK GRAPH
# =====================================

st.subheader("📊 Live Risk Analysis")

risks = [
    "Failure",
    "Performance",
    "Test",
    "Security"
]

probabilities = [
    result["Failure"]["probability"],
    result["Performance"]["probability"],
    result["Test"]["probability"],
    result["Security"]["probability"]
]

fig = go.Figure()

fig.add_trace(go.Bar(
    x=risks,
    y=probabilities,
    text=[
        f"{p:.2f}"
        for p in probabilities
    ],
    textposition='auto'
))

fig.update_layout(
    yaxis_title="Risk Probability",
    xaxis_title="Risk Type"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# RL DECISION
# =====================================

st.subheader(
    "🤖 Autonomous RL Decision"
)

st.success(action)

st.info(explanation)

# =====================================
# PIPELINE STATUS
# =====================================

st.subheader(
    "🛠 Pipeline Status"
)

if health_score > 75:

    st.success(
        "Pipeline Stable"
    )

elif health_score > 45:

    st.warning(
        "Pipeline Moderately Risky"
    )

else:

    st.error(
        "Pipeline Critical"
    )

# =====================================
# RAW DATA
# =====================================

with st.expander(
    "View Live Raw Data"
):

    st.json(data)