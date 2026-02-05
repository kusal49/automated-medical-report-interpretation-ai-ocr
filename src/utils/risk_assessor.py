def assess_medical_risk(analysis_text: str):
    text = analysis_text.lower()

    high_risk_keywords = [
        "critical",
        "very high",
        "severely",
        "immediately",
        "abnormal",
        "dangerous",
        "consult a doctor",
        "emergency"
    ]

    medium_risk_keywords = [
        "borderline",
        "slightly high",
        "monitor",
        "follow up",
        "elevated"
    ]

    if any(word in text for word in high_risk_keywords):
        return (
            "HIGH",
            "⚠️ The report suggests potentially serious findings. "
            "Please consult a qualified medical professional as soon as possible."
        )

    if any(word in text for word in medium_risk_keywords):
        return (
            "MEDIUM",
            "Some values may require monitoring or medical advice. "
            "Consider consulting a doctor if symptoms are present."
        )

    return (
        "LOW",
        "No urgent medical issues detected based on the report."
    )
