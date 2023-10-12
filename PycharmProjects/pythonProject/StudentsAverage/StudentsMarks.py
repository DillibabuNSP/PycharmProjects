from abc import ABC


class abstractStudents(ABC):
    def __init__(self):
        self.number_students = {}
        self.Marks = []
        self.number_Marks = []
        self.sorted_list = []
        # self.swappeddict = {}

    def student_marks(self):
        pass

    def second_highest(self):
        pass

    def compareAverage(self):
        pass


class PrivateSchool(abstractStudents):

    def student_marks(self):
        students = int(input("Enter Number Of Students: "))
        num = int(input("Enter number of subjects: "))

        for stud in range(students):
            print("Enter the marks of Student" + str(stud + 1) + ":")
            self.Marks.clear()
            for mark in range(num):
                self.Marks.append(int(input("Mark " + str(mark + 1) + ": ")))
            average = sum(self.Marks) / num
            self.number_Marks.append(average)

    def second_highest(self):
        student = 0
        for average_mark in self.number_Marks:
            student += 1
            self.number_students["Student" + str(student)] = average_mark

        # for key, value in self.number_students.items():
        #     self.swappeddict[value] = key

    def compareAverage(self):
        global lst
        for value in sorted(self.number_students):
            lst = (self.number_students[value], value)
            self.sorted_list.append(lst)

        lst1 = sorted(self.sorted_list)
        print(f'Second Highest Average: {lst1[-2]}')

    def studentsList(self):
        self.student_marks()
        self.second_highest()
        self.compareAverage()


class GovtSchool(abstractStudents):

    def student_marks(self):
        students = int(input("Enter Number Of Students: "))
        num = int(input("Enter number of subjects: "))

        for stud in range(students):
            print("Enter the marks of Student" + str(stud + 1) + ":")
            self.Marks.clear()
            for mark in range(num):
                self.Marks.append(int(input("Mark " + str(mark + 1) + ": ")))
            average = sum(self.Marks) / num
            self.number_Marks.append(average)

    def second_highest(self):
        student = 0
        for average_mark in self.number_Marks:
            student += 1
            self.number_students["Student" + str(student)] = average_mark

    def compareAverage(self):
        global lst
        for value in sorted(self.number_students):
            lst = (self.number_students[value], value)
            self.sorted_list.append(lst)

        lst1 = sorted(self.sorted_list)
        print(f'Second Highest Average: {lst1[-2]}')

    def studentsList(self):
        self.student_marks()
        self.second_highest()
        self.compareAverage()


class StudentsMarks:
    print("Please Select any one School")
    print("====================")
    print("   Private    ")
    print("   Govt           ")
    print("====================")

    select_school = input("Select the school to enter marks ")
    match select_school:
        case "Private":
            marks = PrivateSchool()
            marks.studentsList()

        case "Govt":
            marks = GovtSchool()
            marks.studentsList()
