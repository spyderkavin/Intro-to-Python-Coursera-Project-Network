def scores(score):
    while score >=0:    
        if score >= 50:
            print("Pass")
        elif score < 50 and score >= 0:
            print("Fail")
        elif score < 0:
            print("Invalid score")
            break
        
scores(int(input("Enter your score: ")))  # Example usage