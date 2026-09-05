def agent_decision(prediction):
    failure, performance, test, security = prediction[0]

    if failure == 1:
        return "🚫 Stop Pipeline (Failure Risk)"

    elif security == 1:
        return "🔐 Trigger Security Scan"

    elif performance == 1:
        return "⚡ Optimize Performance"

    elif test == 1:
        return "🧪 Re-run Tests"

    else:
        return "✅ Safe Deployment"