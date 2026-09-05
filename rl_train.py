from stable_baselines3 import DQN

from environment import CICDEnv

env = CICDEnv()

model = DQN(
    "MlpPolicy",
    env,
    learning_rate=0.0005,
    buffer_size=50000,
    learning_starts=2000,
    batch_size=64,
    gamma=0.99,
    exploration_fraction=0.3,
    verbose=1
)

model.learn(total_timesteps=100000)

model.save("model/rl_agent")

print("\nImproved RL Agent Trained")