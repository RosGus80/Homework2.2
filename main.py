from functions import *


#Создаю списки, в которых будут храниться валидные порядковые номера студентов и названия профессий (чтобы не проверять валидность итерацией по списку после ввода числа пользователем)
students = students_load()
valid_pk = []
for student in students:
    valid_pk.append(student["pk"])

professions = professions_load()
valid_professions = []
for profession in professions:
    valid_professions.append(profession["title"])


student_num = int(input("Введите номер студента: "))
student_data = get_student(student_num) #Тут будет храниться вся информация о студенте, которого выбрал пользователь

if student_num in valid_pk:
    print(f"Студент {student_data['full_name']}")
    student_skillss = ", ".join(student_data["skills"])
    print(f"Знает {', '.join(student_data['skills'])}")
else:
    print("У нас нет такого студента")
    quit()

profession_title = input(f"Выберите специальность для оценки студента {student_data['full_name']}: ")

if profession_title in valid_professions:
    profession_dic = get_profession(profession_title)
    output_dic = check_fitness(student_data, profession_dic)

    print(f"Пригодность {output_dic['fit']}%")
    # Делаю эти два условия, чтобы программа не выводила "Студент не знает set(). Можно выводить какое-нибудь альтернативное сообщение через else("Например, у студента нет навыков в этой профессии")
    if len(output_dic['has']) != 0:
        print(f"{student_data['full_name']} знает {output_dic['has']}")
    if len(output_dic['lacks']) != 0:
        print(f"{student_data['full_name']} не знает: {', '.join(output_dic['lacks'])}")
else:
    print("У нас нет такой специальности")
    quit()


