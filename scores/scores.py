def scores(score):
    if score >= 50:
        print("Pass")
    elif score < 50:
        print("Fail")
    
scores(int(input("Enter your score: ")))  # Example usage