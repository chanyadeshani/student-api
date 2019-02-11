import datetime


class Student:
    birthday = datetime.datetime(1988, 1, 1)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_student(self):
        print("Id : " + self.id + ", Name : " + self.name + ", Birthday : " + self.birthday.strftime('%Y-%m-%d'))
