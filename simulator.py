import random

LOG_TEMPLATES = [

    # Safe
    {
        "log": "Build completed successfully",
        "risk": "safe"
    },

    {
        "log": "All tests passed successfully",
        "risk": "safe"
    },

    # Failure
    {
        "log": "Build failed due to segmentation fault",
        "risk": "failure"
    },

    {
        "log": "Pipeline timeout and memory overflow",
        "risk": "failure"
    },

    # Security
    {
        "log": "Critical vulnerability detected",
        "risk": "security"
    },

    {
        "log": "Unauthorized access attempt detected",
        "risk": "security"
    },

    # Performance
    {
        "log": "CPU overload and latency spike",
        "risk": "performance"
    },

    {
        "log": "Pipeline performance degradation observed",
        "risk": "performance"
    }
]

def generate_pipeline_data():

    sample = random.choice(
        LOG_TEMPLATES
    )

    risk = sample["risk"]

    # SAFE
    if risk == "safe":

        return {
            "error_count": random.randint(0, 1),
            "duration": random.randint(80, 150),
            "coverage": random.randint(80, 100),
            "cpu_usage": random.randint(20, 50),
            "memory_usage": random.randint(20, 50),
            "past_failures": random.randint(0, 1),
            "log_text": sample["log"]
        }

    # FAILURE
    elif risk == "failure":

        return {
            "error_count": random.randint(5, 10),
            "duration": random.randint(300, 500),
            "coverage": random.randint(40, 70),
            "cpu_usage": random.randint(80, 100),
            "memory_usage": random.randint(80, 100),
            "past_failures": random.randint(3, 8),
            "log_text": sample["log"]
        }

    # SECURITY
    elif risk == "security":

        return {
            "error_count": random.randint(2, 6),
            "duration": random.randint(150, 300),
            "coverage": random.randint(50, 80),
            "cpu_usage": random.randint(40, 70),
            "memory_usage": random.randint(40, 70),
            "past_failures": random.randint(1, 4),
            "log_text": sample["log"]
        }

    # PERFORMANCE
    else:

        return {
            "error_count": random.randint(1, 4),
            "duration": random.randint(250, 450),
            "coverage": random.randint(60, 85),
            "cpu_usage": random.randint(85, 100),
            "memory_usage": random.randint(70, 95),
            "past_failures": random.randint(1, 3),
            "log_text": sample["log"]
        }