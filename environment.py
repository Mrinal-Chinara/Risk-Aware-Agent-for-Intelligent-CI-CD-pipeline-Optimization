import gymnasium as gym
from gymnasium import spaces
import numpy as np

from reward import calculate_reward

class CICDEnv(gym.Env):

    def __init__(self):

        super(CICDEnv, self).__init__()

        # Actions
        self.action_space = spaces.Discrete(6)

        # Observation space
        self.observation_space = spaces.Box(
            low=0,
            high=1,
            shape=(5,),
            dtype=np.float32
        )

        self.state = None

        self.steps = 0

    def generate_state(self):

        # Simulate realistic CI/CD conditions

        failure_risk = np.random.beta(2, 5)

        performance_risk = np.random.beta(2, 4)

        security_risk = np.random.beta(1.5, 5)

        cpu_usage = np.clip(
            performance_risk +
            np.random.normal(0, 0.1),
            0,
            1
        )

        duration = np.clip(
            failure_risk +
            performance_risk +
            np.random.normal(0, 0.1),
            0,
            1
        )

        return np.array([
            failure_risk,
            performance_risk,
            security_risk,
            cpu_usage,
            duration
        ], dtype=np.float32)

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.state = self.generate_state()

        self.steps = 0

        return self.state, {}

    def step(self, action):

        reward = calculate_reward(
            self.state,
            action
        )

        current_failure = self.state[0]

        # Simulate impact of actions

        if action == 1:
            current_failure *= 0.8

        elif action == 2:
            current_failure *= 0.4

        elif action == 3:
            self.state[2] *= 0.5

        elif action == 4:
            self.state[1] *= 0.7

        next_state = self.generate_state()

        next_state[0] = current_failure

        self.state = next_state

        self.steps += 1

        terminated = self.steps >= 30

        truncated = False

        return (
            next_state,
            reward,
            terminated,
            truncated,
            {}
        )