class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience

    @property
    def name(self):
        return self._name

    @property
    def education(self):
        return self._education

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value



    def get_teacher_data(self):
        return f"{self.name}, {self.education}, {self.experience}"

    def add_mark(self, student_name, mark):

        return f"{self.name} поставил оценку {mark} студенту {student_name}"

    def remove_mark(self, student_name, mark):
        return f"{self.name} удалил оценку {mark} студенту {student_name}"

    def give_a_consultation(self, student_class):
        return f"{self.name} провел консультацию в классе {student_class}"


teacher = Teacher("Иван Петров","БГПУ","4 года")
print(teacher.get_teacher_data())
print(teacher.add_mark("Петр Сидоров", 4))
print(teacher.remove_mark("Дмитрий Степанов",3))
print(teacher.give_a_consultation("9Б"))