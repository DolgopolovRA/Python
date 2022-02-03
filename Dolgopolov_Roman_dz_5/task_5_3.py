tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А']


gen = ((tutors[i], classes[i]) if i < len(classes) else (tutors[i], None) for i in range(0, len(tutors)))

print(type(gen))

"""Далее проверяем работу вплоть до истощения """

for n in gen:
    print(n)  # получаем очередное значение

print(list(gen))  # преобразуем к списку, но он пуст