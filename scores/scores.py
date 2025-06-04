def scores(score): 
    if score >= 50:
        print("Pass")
        
    elif score < 50 and score >= 0:
        print("Fail")
    elif score < 0:
        print("Invalid score")

score = int(input("Enter your score: "))

while score >=0:
    scores(score)  # Example usage
    score = int(input("Enter your score: "))

    
