# самолёт

# ** Интерфейсы — Python: Абстракция с помощью данных
# ------------------------------------------------------------
# /courses/python-data-abstraction
#
# В IT широко распространен термин "Интерфейс", который по смыслу похож на то, как мы используем это слово в повседневной жизни. Например, пользовательский интерфейс представляет собой совокупность элементов управления сайтом, банкоматом, телефоном и так далее. Интерфейсом пульта управления от телевизора являются кнопки. Интерфейсом автомобиля можно назвать все рычаги управления, кнопки и руль. Резюмируя, можно сказать, что интерфейс определяет способ взаимодействия с системой.
#
# Создание грамотных интерфейсов не так уж просто, как может показаться на первый взгляд. Я бы даже сказал, что это крайне сложно. Каждый день мы встречаемся с неудобными интерфейсами, начиная от способов открывания дверей и заканчивая работой лифтов. Чем сложнее система (то есть, чем больше возможных состояний), тем сложнее сделать интерфейс. Даже в примитивном примере с кнопкой включения телевизора (два состояния — вкл/выкл), можно реализовать либо две кнопки, либо одну, которая ведет себя по разному в зависимости от текущего состояния.
#
# В программировании все устроено похожим образом. Интерфейсом называют набор функций (имена и их сигнатуры, то есть количество и типы входящих параметров, а также возвращаемое значение), не зависящих от конкретной реализации. Такое определение один в один совпадает с понятием абстрактного типа данных. Например, для точек интерфейсными являются все функции, которые мы реализовывали в практике, и которые описывались в теории.
#
# Как соотносятся между собой понятия абстракция и интерфейс? Абстракция — это слово, описывающее в первую очередь те данные, с которыми мы работаем. Например, почти каждое веб-приложение включает в себя абстракцию "пользователь". На Хекслете есть абстракция "курс", "проект" и многое другое. Интерфейсом же называется набор функций, с помощью которых можно взаимодействовать с данными.
#
# Но функции бывают не только интерфейсные, но и вспомогательные, которые не предназначены для вызывающего кода и используются исключительно внутри абстракции:
# # Функции make_user, get_age, is_adult — интерфейс абстракции User.
# # Они используются внешним (пользовательским, вызывающим) кодом.
# def make_user(name, birthday):
# return {
# "name": name,
# "birthday": birthday,
# }
#
# def get_age(user):
# return calculate_age(user["birthday"])
#
# def is_adult(user):
# return get_age(user) >= 18
#
# # Эта функция не является частью интерфейса абстракции User.
# # Она является "внутренней" и возвращает возраст пользователя.
# def calculate_age(birthday):
# ###
#
# В сложных абстракциях (которые могут быть представлены внешними библиотеками), количество неинтерфейсных функций значительно больше, чем интерфейсных. Вплоть до того, что интерфейсом библиотеки могут являться одна или две функции, но в самой библиотеке их сотни. То, насколько хороша ваша абстракция, определяется в том числе тем, насколько удобен ее интерфейс.
# ------------------------------------------------------------
#
#
# ** Дополнительные материалы
# ------------------------------------------------------------
# 1. Абстрактный тип данных (https://ru.wikipedia.org/wiki/Абстрактный_тип_данных)
#
# ------------------------------------------------------------
# Аватары экспертов Хекслета
#
#
# ** Остались вопросы? Задайте их в разделе «Обсуждение (https://help.hexlet.io/ru/articles/110020-kak-zadat-vopros-po-uroku) »
# ------------------------------------------------------------
#
# Вам ответят команда поддержки Хекслета или другие студенты.
#
# Об обучении на Хекслете
#
# * Статья «Как учиться и справляться с негативными мыслями (https://guides.hexlet.io/ru/learning?roistat_visit=4729987) »
# * Статья «Ловушки обучения (https://ru.hexlet.io/blog/posts/traps-learning) »
# * Статья «Сложные простые задачи по программированию (https://ru.hexlet.io/blog/posts/slozhnye-prostye-zadachi-po-programmirovaniyu) »
# * Урок «Как эффективно учиться на Хекслете (https://ru.hexlet.io/courses/introduction_to_programming/lessons/hexlet-flow/theory_unit) »
# * Вебинар «Как самостоятельно учиться (https://www.youtube.com/watch?v=dCYZppVgGww) »
#
#
# ** Для полного доступа к курсу нужен базовый план
# ------------------------------------------------------------
#
# Базовый план откроет полный доступ ко всем курсам, упражнениям и урокам Хекслета, проектам и пожизненный доступ к теории пройденных уроков. Подписку можно отменить в любой момент.
# Получить доступ (/subscription/new?nickname=professional_monthly_3900)
# ------------------------------------------------------------
# 130
# курсов (/courses)
# 1000
# упражнений
# 2000+
# часов теории
# 3200
# тестов