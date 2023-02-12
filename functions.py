import json


def students_load():
    """Загружает информацию из файла студентов в переменную"""
    with open("students.json") as file:
        data = file.read()
        return json.loads(data)


def professions_load():
    """Загружает информацию из файла профессий в переменную"""
    with open("professions.json") as file:
        data = file.read()
        return json.loads(data)


def get_student(data, pk):
    """Находит студента по порядковому номеру и возвращает его. data - загруженная в переменную информация из файла студентов"""
    for student in data:
        if student["pk"] == pk:
            return student
    else:
        print("У нас нет такого студента")
        quit()


def get_profession(data, title):
    """Находит профессию по названию и возвращает ее. data - загруженная в переменную информация из файла профессий"""
    for profession in data:
        if profession["title"] == title:
            return profession
    else:
        print("У нас нет такой профессии")
        quit()


def check_fitness(student, profession):
    student_skills = set(student["skills"])
    required_skills = set(profession["skills"])
    output = {"has": student_skills.intersection(required_skills),
              "lacks": required_skills.difference(student_skills)}
    output["fit"] = round(len(output["has"])/len(required_skills)*100)
    return output