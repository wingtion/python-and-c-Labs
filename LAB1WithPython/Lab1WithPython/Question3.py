name = input("What is your name?")
labGrade = float(input("What is your LAB GRADE?"))
midtermGrade = float(input("What is your MIDTERM GRADE?"))
finalGrade = float(input("What is your FINAL GRADE?"))

print(f"Name: {name}")
print(f"Lab: {labGrade}")
print(f"Midterm: {midtermGrade}")
print(f"Final: {finalGrade}")

labGrade = labGrade/4
midtermGrade = (midtermGrade*35)/100
finalGrade = (finalGrade*4)/10
lastGrade = labGrade + midtermGrade + finalGrade

print(f"Last Score: {lastGrade}")