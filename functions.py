import json


def students_load():
    with open("students.json") as file:
        data = file.read()
        return json.loads(data)


def professions_load():
    with open("professions.json") as file:
        data = file.read()
        return json.loads(data)


def get_student(data, pk):
        for student in data:
            if student["pk"] == pk:
                return student
        else:
            print("У нас нет такого студента")
            quit()


def get_profession(data, title):
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