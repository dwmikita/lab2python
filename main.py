# Author: Daniel Mikita djm6907@psu.edu
# Collaborator: Jiahui Lin jzl6335@psu.edu
# Collaborator: Chen-Kuan Liao czl5899@psu.edu
# Collaborator: Yeman Xu ybx5148@psu.edu
# Section: 1
# Breakout: 8

grade = float(input("Enter your CMPSC 131 grade: "))

if grade >= 93.0:
 letter = "A"
elif grade >=90.0:
  letter = "A-"
elif grade >= 87.0:
  letter = "B+"
elif grade >= 83.0:
  letter = "B"
elif grade >= 80.0:
 letter = "B-"
elif grade >= 77.0:
  letter = "C+"
elif grade >= 70.0:
  letter = "C"
elif grade >= 60.0:
  letter = "D"
else:
  letter = "F"

print(f"Your letter grade for CMPSC 131 is  {letter}.")

#if_name_== "_main_"
#run()