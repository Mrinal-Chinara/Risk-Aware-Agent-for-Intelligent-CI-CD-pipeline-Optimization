from stable_baselines3 import DQN
import numpy as np

model = DQN.load("model/rl_agent")

ACTIONS = {
    0: "Deploy",
    1: "Run Tests",
    2: "Rollback",
    3: "Security Scan",
    4: "Allocate Resources",
    5: "Delay Deployment"
}

EXPLANATIONS = {
    0: "Pipeline considered safe for deployment",

    1: "Additional testing required due to risk",

    2: "Rollback initiated to prevent failure",

    3: "Security vulnerabilities detected",

    4: "Resource optimization needed",

    5: "Deployment delayed due to instability"
}

def get_action(state):

    state = np.array(
        state,
        dtype=np.float32
    )

    action, _ = model.predict(
        state,
        deterministic=True
    )

    action = int(action)

    return (
        ACTIONS[action],
        EXPLANATIONS[action]
    )