Score = int(input("Enter Student's Score : "))

if Score >= 95 and Score <= 100:
    print("Excellent")

elif Score <= 94 and Score >= 90:
    print("Very Good")

elif Score <= 89 and Score >= 80:
    print("Good")

elif Score <= 79 and Score >= 75:
    print("Passed")

elif Score <= 74 and Score >= 60:
    print("Failed Better Luck Next Time")