def calculate_health_score(income, expenses):

    if income <= 0:
        return {
            "score": 0,
            "status": "No Income",
            "savings_rate": 0,
            "recommendation": "Add your income to calculate your financial health."
        }

    savings = income - expenses
    savings_rate = (savings / income) * 100

    if savings_rate >= 50:
        score = 95
        status = "🟢 Excellent"
        recommendation = (
            "Excellent! You are saving more than 50% of your income. "
            "Keep maintaining these spending habits."
        )

    elif savings_rate >= 30:
        score = 80
        status = "🟡 Good"
        recommendation = (
            "Good job! Your savings rate is healthy. "
            "Try increasing it a little more."
        )

    elif savings_rate >= 10:
        score = 60
        status = "🟠 Average"
        recommendation = (
            "You are saving some money, but there is room for improvement. "
            "Review your unnecessary expenses."
        )

    else:
        score = 30
        status = "🔴 Poor"
        recommendation = (
            "Your expenses are consuming most of your income. "
            "Create a budget and reduce non-essential spending."
        )

    return {
        "score": score,
        "status": status,
        "savings_rate": round(savings_rate, 2),
        "recommendation": recommendation
    }