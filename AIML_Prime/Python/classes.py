class Student:
    college="ABC College"
    student_count=0
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
        Student.student_count=Student.student_count+1


    @staticmethod
    def set_Marks_static(grade):
        if grade == "A":
            mark = 90
        elif grade == "B":
            mark = 80
        else:
            mark = 70
        return mark
    
    @classmethod
    def get_college(cls):
        return cls.college

    @staticmethod
    def get_student_count():
        return Student.student_count

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, college: {self.college}")

st1=Student("praveen",22,"A")
st2=Student("mari",21,"B")
print(st1.name)
print(st2.age)
print(Student.set_Marks_static(st1.grade))
print(Student.college)
st1.get_details()
print(Student.get_college())
print(Student.get_student_count())
st2=Student("mari",21,"B")
print(Student.get_student_count())

