# ----------------------------------------------------------
# День 1. Создание интерфейса: форма вопроса
# ----------------------------------------------------------


# 1.1.1) Подключи нужные модули (QtCore и QtWidgets и их элементы).
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QButtonGroup,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)
from random import shuffle


# 1.1.2) Создай объект-приложение, окно приложения. Задай заголовок и размеры.
app = QApplication([])

window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(400, 200)


# 1.1.3) Создай виджет-вопрос и виджет-кнопку «Ответить».
lb_question = QLabel("Какой национальности не существует?")
btn_ok = QPushButton("Ответить")


# 1.1.4) Создай набор переключателей с вариантами ответов. Расположи их по лэйаутам и объедини в группу.
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чулымцы")
rbtn_4 = QRadioButton("Алеуты")

# два ответа в первый столбец
layout_answer_column_1 = QVBoxLayout()
layout_answer_column_1.addWidget(rbtn_1)
layout_answer_column_1.addWidget(rbtn_2)

# два ответа во второй столбец
layout_answer_column_2 = QVBoxLayout()
layout_answer_column_2.addWidget(rbtn_3)
layout_answer_column_2.addWidget(rbtn_4)

# вертикальные будут внутри горизонтального
layout_quest = QHBoxLayout()
layout_quest.addLayout(layout_answer_column_1)
layout_quest.addLayout(layout_answer_column_2)

# группа ответов (выделяется визуально)
question_group_box = QGroupBox("Варианты ответов")
question_group_box.setLayout(layout_quest)


# 1.1.5) Расположи вопрос, группу переключателей и кнопку по лэйаутам.
# 1.1.6) При необходимости, добавь пробелы между виджетами и выровняй их по краю/центру.
layout_line1 = QHBoxLayout()  # вопрос
layout_line2 = QHBoxLayout()  # варианты ответов или результат теста
layout_line3 = QHBoxLayout()  # кнопка "Ответить"

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(question_group_box)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)  # кнопка должна быть большой
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # пробелы между содержимым

window.setLayout(layout_card)


# ----------------------------------------------------------
# День 1. Создание интерфейса: форма правильного ответа
# ----------------------------------------------------------


# 1.2.2) Создай виджет-результат «Правильно» (или «Неправильно») и виджет для правильного ответа.
lb_result = QLabel("прав ты или нет?")  # надпись "правильно" или "неправильно"
lb_correct = QLabel("ответ будет тут!")  # текст правильного ответа

# 1.2.3) Расположи новые виджеты по лэйаутам и объедини их в группу.
layout_result = QVBoxLayout()
layout_result.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
answer_group_box = QGroupBox("Результат теста")
answer_group_box.setLayout(layout_result)

layout_line2.addWidget(answer_group_box)

# Скроем панель с ответом
answer_group_box.hide()


# ----------------------------------------------------------
# День 2. Обработка событий кнопки «Ответить»/«Следующий вопрос»
# ----------------------------------------------------------


# 2.1.1. Напиши функцию show_result(), обрабатывающую нажатие на «Ответить».
# – скрывать форму вопроса;
# – отображать форму правильного ответа;
# – менять надпись на кнопке на «Следующий вопрос».
def show_result():
    """Показать панель ответов."""
    question_group_box.hide()
    answer_group_box.show()
    btn_ok.setText("Следующий вопрос")


# 2.1.2. Напиши функцию-обработчик show_question(), обрабатывающую нажатие на «Следующий вопрос». Она должна:
# – скрывать форму ответа;
# – показывать форму вопроса;
# – менять надпись «Следующий вопрос» на «Ответить»;
# – сбрасывать все переключатели.
radio_group = QButtonGroup()
radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)


def show_question():
    """Показать панель вопросов."""
    question_group_box.show()
    answer_group_box.hide()
    btn_ok.setText("Ответить")

    # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    radio_group.setExclusive(False)

    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)

    # вернули ограничения, теперь только одна радиокнопка может быть выбрана
    radio_group.setExclusive(True)


# 2.1.3. Напиши функцию-обработчик start_test(). Она должна:
# – проверять надпись на кнопке;
# – если надпись –– «Ответить», то вызывать show_result();
# – если надпись –– «Следующий вопрос», то вызывать show_question().
def start_test():
    """Временная функция, которая позволяет нажатием на кнопку вызывать по очереди `show_result()` либо `show_question()`."""
    if "Ответить" == btn_ok.text():
        show_result()
    else:
        show_question()


# проверяем, что панель ответов показывается при нажатии на кнопку
# btn_ok.clicked.connect(start_test)


# ----------------------------------------------------------
# День 2. Обработка событий кнопки «Ответить»/«Следующий вопрос»
# ----------------------------------------------------------


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# Чтобы задать конкретный вопрос и обработать ответ на него, напиши три функции:


# 2.2.1. Функция ask() должна:
# – передаваемые ей данные располагать в соответствующих виджетах;
# – перемешивать варианты ответов (переключатели);
# – в форму ответа заранее размещать правильный ответ (пригодится в show_correct());
# – отображать форму вопроса.
def ask(question: str, right_answer: str, wrong_answers: tuple[str, str, str]):
    """Обновляет вопрос и случайным образом размещает ответы на него.

    Параметры:
    - question (`str`): Текст вопроса.
    - right_answer (`str`): Правильный ответ на вопрос.
    - wrong_answers (`tuple`): Неправильные ответы на вопрос.
    """
    shuffle(answers)

    answers[0].setText(right_answer)
    answers[1].setText(wrong_answers[0])
    answers[2].setText(wrong_answers[1])
    answers[3].setText(wrong_answers[2])

    lb_question.setText(question)
    lb_correct.setText(right_answer)

    show_question()


# 2.2.2. Функция check_answer() должна проверять правильность данного ответа при нажатии на «Ответить»:
# – если выбран переключатель answers[0], то вызывать функцию show_correct с аргументом «Правильно»;
# – если выбран любой другой переключатель, то вызывать функцию show_correct с аргументом «Неверно».
def show_correct(res: str):
    """Показать результат - установим переданный текст в надпись "результат" и покажем нужную панель."""
    lb_result.setText(res)
    show_result()


# 2.2.3. Функция show_correct() должна:
# – устанавливать текст-результат в форме ответа;
# – отображать форму ответа.
def check_answer():
    """Если выбран какой-то вариант ответа, то показать соответствующую ему панель ответа."""
    if answers[0].isChecked():
        show_correct("Правильно!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно!")


btn_ok.clicked.connect(check_answer)  # Устанавливаем обработчик на кнопку


ask(
    "Государственный язык Бразилии",
    "Португальский",
    ("Бразильский", "Испанский", "Итальянский"),
)


# ----------------------------------------------------------
# Отрисовка и запуск приложения:
# ----------------------------------------------------------


window.show()
app.exec()
