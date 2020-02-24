def Home():
  print("")
  print("...............................")
  print("CHOOSE AN OPTION")
  print("...............................")
  print("(S) Add a student")
  print("(C) Add a course")
  print("(A) Assign Student to Course ")
  print("(G) Add a grade")
  print("(L) Student List")
  print("(O) Course List")
  print("")

def AddStudent(students):
  if len(students) > 0:
    print("Students:")
    for i in students:
      print(i)
  studentName = False
  while studentName == False:
    myName = input("Put the student's name in)> ")
    if myName == "":
      print("cannot be blank...try again...")
    else:
      studentName = True
      students[myName] = {
          "math": 0,
          "english": 0,
          "art":0
      }
      print("")
      print(str(myName) + " ADDED TO STUDENTS")
      print("")
      hesitate = input("press ENTER to continue...")
  return students

def AddCourse(courses):
  print(courses)
  course = True
  while course:
    courseName = input("Please enter the name of the course you wish to add)> ")
    if courseName == "":
      print("cannot be blank, please try again")
    else:
      courses.append(courseName)
      course = False
      print("")
      print(str(courseName) + " ADDED TO COURSES")
      print("")
      hesitate = input("press ENTER to continue...")
  return courses

def AssignCourse(student, students, courses):
  for i in students:
    print(i)
  print(courses)
  courseExists = False
  while courseExists == False:
    courseName = input("please enter the name of the course)> ")
    if courseName == "exit".lower():
      Home()
    if courseName in courses:
      students[student][courseName] = 0
      courseExists = True
      print("")
      print(str(courseName) + " ASSIGNED TO " + str(student))
      print("")
      hesitate = input("press ENTER to continue...")
    else:
      print("sorry that course does not exist...please try again")
  else:
    print("invalid selection. Please try again.  type 'exit' to exit, or 'home' to go to the home screen")
  return students

def SelectStudent(students):
  if len(students) == 0:
    print("there are no students yet! go back and add one!")
    return students
  for i in students:
    print(i)
  studentExists = False
  while studentExists == False:
    student = input("Please select a student by writing their name)> ")
    if student == "exit":
      break
    if student in students:
      studentExists = True
      return student
    else:
      print("sorry that student does not exist.  try again or type 'exit' to go to the home screen")
      

def AddGrade(student, students, courses):
  student = str(student)
  courseName = False
  while courseName == False:
    course = input("Please enter the name of the course you are grading)> ")
    if course in students[student]:
      courseName = True
      print(student + " " + str(students[student]))
      gradeInput = False
      while gradeInput == False:
        grade = input("Please enter the grade for the course)> ")
        try:
          grade = int(grade)
          gradeInput = True
          students[student][course] = grade
        except:
          print("not an integer.  Try using a number, dumb dumb...")
    else:
      print("invalid course...Try again")
  return students


students = {}
courses = ["math", "english", "art"]

# program loop
optionChosen = False
while optionChosen == False:
  Home()
  selection = input("Please make a selection)> ").lower()
  if selection == "S".lower():
    students = AddStudent(students)
  elif selection == "C".lower():
    courses = AddCourse(courses)
  elif selection == "G".lower():
    student = SelectStudent(students)
    students = AddGrade(student, students, courses)
  elif selection == "A".lower():
    student = SelectStudent(students)
    students = AssignCourse(student, students, courses)
  elif selection == "L".lower():
    print(students)
  elif selection == "O".lower():
    print(courses)
  else:
    print("invalid selection, please try again")

