import random

from django.core.exceptions import ObjectDoesNotExist
from datacenter import models


COMMENDATIONS = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]



def fix_marks(schoolkid):
    bad_grades = models.Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    bad_grades.update(points=5)
    print('Готово!')


def remove_chastisements(schoolkid):
    chastisements = models.Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()
    print('Готово!')


def create_commendation(kid_name, subject_name):
    try:
        schoolkid = models.Schoolkid.objects.get(full_name=kid_name)
    except ObjectDoesNotExist:
        if kid_name:
            print(f'Ученик "{kid_name}" не найден в базе. Вероятно, ФИО ученика написаны с ошибкой.')
        else:
            print('Ошибка: не указаны Фамилия Имя Отчество ученика.')
        return
    try:
        subject = models.Subject.objects.get(title=subject_name, year_of_study=schoolkid.year_of_study)
    except ObjectDoesNotExist:
        if subject_name:
            print(f'Предмет "{subject_name}" не найден в базе. Вероятно, название предмета написано с ошибкой.')
        else:
            print('Ошибка: не указано название предмета.')
        return
    lessons = models.Lesson.objects.filter(group_letter=schoolkid.group_letter, subject=subject)
    last_lesson = lessons.order_by('-date').first()
    text = random.choice(COMMENDATIONS)
    models.Commendation.objects.create(
        text=text,
        created=last_lesson.date,
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )
    print('Готово!')
