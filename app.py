from predict import predict_risk
from rl_predict import get_action


def main():

    # Sample CI/CD pipeline input
    input_num = [
        5,      # error count
        250,    # duration
        1,      # test failed
        60,     # coverage
        90,     # cpu usage
        80,     # memory usage
        3       # past failures
    ]

    input_text = (
        "Build failed due to "
        "security vulnerability "
        "and high CPU usage"
    )

    # ML Risk Prediction
    result = predict_risk(
        input_num,
        input_text
    )

    # Create RL State
    state = [

        # Failure Risk
        result["Failure"]["probability"],

        # Performance Risk
        result["Performance"]["probability"],

        # Security Risk
        result["Security"]["probability"],

        # CPU Usage normalized
        input_num[4] / 100,

        # Duration normalized
        input_num[1] / 300
    ]

    # RL Decision
    action, explanation = get_action(state)

    print("\n========== RESULTS ==========")

    print("\nRisk Predictions:\n")

    for risk_name, values in result.items():

        print(
            f"{risk_name}: "
            f"{values['probability']:.2f} "
            f"({values['severity']})"
        )

    print("\nAutonomous RL Decision:\n")

    print(action)

    print("\nReason:\n")

    print(explanation)


if __name__ == "__main__":
    main()