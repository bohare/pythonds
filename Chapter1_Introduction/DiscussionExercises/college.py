class College:
    #Parent class describing a College
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

    def __str__(self):
        return 'Name: {}, Contact: {}'.format(str(self.name), str(self.contact))


class student(College):
    def __init__(self, name, age, contact, grade, email):
        College.__init__(self, name, age, contact)
        self.grade = grade
        self.email = email

    def register_for_exams(self):
        pass


Rahul = College('Rahul Bohare', '25', '0123456789')
print(Rahul)
