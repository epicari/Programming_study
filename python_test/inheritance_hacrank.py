#
# HackerRank Tutorials Day 12: Inheritance
# 
#

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber) #부모클래스 내 함수 사용하고 싶을 때 super() 사용함
        self.scores = scores    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        grade = ''

        if avg >= 90 and avg <= 100:
            grade = 'O'
        elif avg >= 80 and avg < 90:
            grade = 'E'
        elif avg >= 70 and avg < 80:
            grade = 'A'
        elif avg >= 55 and avg < 70:
            grade = 'P'
        elif avg >= 40 and avg < 55:
            grade = 'D'
        elif avg < 40:
            grade = 'T'
        
        return grade
        
if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    #numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())