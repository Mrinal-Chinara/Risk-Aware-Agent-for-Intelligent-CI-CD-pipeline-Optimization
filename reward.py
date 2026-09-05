def calculate_reward(state, action):

    failure_risk = state[0]
    performance_risk = state[1]
    security_risk = state[2]
    cpu_usage = state[3]
    duration = state[4]

    reward = 0

    # ACTION 0 = DEPLOY
    if action == 0:

        if failure_risk < 0.3:
            reward += 15

        else:
            reward -= 20

    # ACTION 1 = RUN TESTS
    elif action == 1:

        if failure_risk > 0.5:
            reward += 8

    # ACTION 2 = ROLLBACK
    elif action == 2:

        if failure_risk > 0.8:
            reward += 12

    # ACTION 3 = SECURITY SCAN
    elif action == 3:

        if security_risk > 0.6:
            reward += 10

    # ACTION 4 = ALLOCATE RESOURCES
    elif action == 4:

        if performance_risk > 0.5:
            reward += 7

        if cpu_usage > 0.8:
            reward += 5

    # ACTION 5 = DELAY DEPLOYMENT
    elif action == 5:

        if failure_risk > 0.7:
            reward += 6

    # Penalty for long pipeline
    if duration > 0.8:
        reward -= 3

    return reward