def scores(score):
    if score >= 50:
        return "Pass"
    elif score < 50:
        return "Fail"
    
scores(int(input("Enter your score: ")))  # Example usage