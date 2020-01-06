class ComputerStudent:
    """This is a Python program that models a Computer Science Student. this program lets the user input the number of
    courses he/she is doing and be able to enter the courses and their respective units. it also gives the user the
    opportunity to calculate his/her grade point average."""



    def __init__(self,name,matric_no,num_courses,num_units,level= None):
        DEFAULT_NUM_COURSES = 5

        if level is None and self.num_courses < DEFAULT_NUM_COURSES and len(matric_no) != 6:
            print("please indicate your level and the correct number of courses you are doing.")
            print("matric number cannot be less than or greater than six")

        self.name = name
        self.num_courses = num_courses
        self.level = level
        self.num_units = int(num_units)
        self.matric_no = matric_no

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Computer Student: {}".format(self.name)

    def _add_courses(self):
        """this allows the user to input courses and respective unit"""
        my_courses = []
        my_units = []
        for courses in range(self.num_courses):
            course = input("enter course: ")
            unit = int(input("enter the respective unit: "))
            my_courses.append(course)
            my_units.append(unit)

        if sum(my_units) < self.num_units:
            print("Total number of units entered do not tally with the number of units added. ")
        elif sum(my_units) > self.num_units:
            print("Total number of units entered do not tally with the number of units added. ")

        if len(my_units) < len(my_courses):
            print("Number of courses and units do not correspond, please complete it.")

    def check_level(self):
        if self.level is 100:
            print("You are a Hundred level student.")
        elif self.level is 200:
            print("You are a Two Hundred level student.")
        elif self.level is 300:
            print("You are a Three Hundred level student.")
        elif self.level is 400:
            print("You are a Four Hundred level student.")

    def add_score(self):
        my_scores = []
        my_points = []
        print("Enter your scores in order you entered your courses.")
        for i in range(self.num_courses):
            score = int(input("enter Your score: "))
            my_scores.append(score)
            if score >= 70:
                point = 4
                my_points.append(point)
            elif score >= 60:
                point = 3
                my_points.append(point)
            elif score >= 50:
                point = 2
                my_points.append(point)
            elif score >= 45:
                point = 1
                my_points.append(point)
            else:
                point = 0
                my_points.append(point)

        def calculate_grade():
            """This is a local function enclosed in the add_score method."""
            my_units = []
            for j in range(len(my_points)):
                unit = int(input("Enter your units like before please: "))
                my_units.append(unit)

            total_points = 0
            for num in my_points:
                total_points += (my_points[num] * my_units[num])

            grade_point = total_points / self.num_units
            if grade_point >= 3.50:
                print("{} You are on First-Class.".format(self.name.split(" ")[-1]))
            elif grade_point >= 3.00:
                print("{} You are on Second-Class Upper.".format(self.name.split(" ")[-1]))
            elif grade_point >= 2.00:
                print("{} You are on Second-Class Lower.".format(self.name.split(" ")[-1]))
            elif grade_point >= 1.00:
                print("{} You are on Third-Class.".format(self.name.split(" ")[-1]))
            else:
                print("{} You are on Pass.".format(self.name.split(" ")[-1]))
            print("Your grade point is {}".format(grade_point))
        return calculate_grade


if __name__ == "__main__":
    comp = ComputerStudent("Ayodabo Tomisin","205537",15,48,100)
    comp.add_courses()
    my_score = comp.add_score()
    my_score()