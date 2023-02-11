students = int(input("Сколько учеников в клвссе? Введите число: "))
counter_4 = 0
counter_5 = 0
counter_3 = 0
for classman in range(1, students+1):
<<<<<<< HEAD
    scores = int(input(f"Какю ОТМЕТКУ получил студент {classman}? "))
=======
    scores = int(input(f"Какю оценку получил студент сегодня {classman}? "))
>>>>>>> a92120bb63978821f8df90ba4251cbe7b0a26dd6
    if scores == 4:
        counter_4 += 1
    elif scores == 3:
        counter_3 += 2
    elif scores == 5:
        counter_5 += 1
if counter_5 < counter_4 > counter_3:
    print("Хорошистов сегодня больше")
elif counter_3 < counter_5 > counter_4:
    print("Отличников сегодня больше")
    print('new insert')
else:
    print("троечников сегодня больше ВСЕХ")
    print('Добавленная строка')

print()