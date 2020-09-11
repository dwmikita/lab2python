# Author: Daniel Mikita djm6907@psu.edu
# Collaborator: Jiahui Lin jzl6335@psu.edu
# Collaborator: Chen-Kuan Liao czl5899@psu.edu
# Collaborator: Yeman Xu ybx5148@psu.edu
# Section: 1
# Breakout: 8

def getLetterGrade(grade):
  if (grade >= 93.0):
    return "A"
  elif (grade >=90.0) :
      return "A-"
  elif (grade >=87.0) :
    return "B+"
  elif (grade >=83.0) :
    return "B"
  elif (grade >=80.0) :
    return "B-"
  elif (grade >=73.0) :
    return "C+"
  elif (grade >=70.0) :
    return "C"
  elif (grade>= 60.0) :
    return "D"
  else:
    return "F"

def run():
    ignore = input("Enter your CMPSC 131 grade: ")

grade = float(input("Enter your CMPSC 131 grade: "))
if (grade >= 93.0):
  letter = "A"
elif (grade >=90.0) :
  letter = "A-"
elif (grade >=87.0) :
  letter = "B+"
elif (grade >=83.0) :
  letter = "B"
elif (grade >=80.0) :
  letter = "B-"
elif (grade >=73.0) :
  letter = "C+"
elif (grade >=70.0) :
  letter = "C"
elif (grade>= 60.0) :
  letter = "D"
else:
  letter = "F"

print(f"Your letter grade for CMPSC 131 is {letter}.")

if __name__== "__main__":
  run()