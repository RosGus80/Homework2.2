import json


def students_load():
    with open("students.json") as file:
        data = file.read()
        return json.loads(data)


def professions_load():
    with open("professions.json") as file:
        data = file.read()
        return json.loads(data)


def get_student(pk):
    with open("students.json") as file:
        data_json = file.read()
        data = json.loads(data_json)
        for student in data:
            if student["pk"] == pk:
                return student
                break


def get_profession(title):
    with open("professions.json") as file:
        data_json = file.read()
        data = json.loads(data_json)
        for profession in data:
            if profession["title"] == title:
                return profession
                break


def check_fitness(student, profession):
    student_skills = set(student["skills"])
    required_skills = set(profession["skills"])
    output = {"has": student_skills.intersection(required_skills),
              "lacks": required_skills.difference(student_skills)}
    output["fit"] = round(len(output["has"])/len(required_skills)*100)
    return output