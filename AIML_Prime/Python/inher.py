class Employer:
    start_time = "9:00 AM"
    end_time = "5:00 PM"

    def change_working_hours(self, start, end):
        self.start_time = start
        self.end_time = end


class Teacher(Employer):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

teacher1 = Teacher("Alice", "Math")
print(teacher1.name)  # Output: Alice

print(teacher1.start_time)  # Output: 9:00 AM
teacher1.change_working_hours("10:00 AM", "6:00 PM")
print(teacher1.start_time)  # Output: 10:00 AM