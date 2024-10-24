# создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLabel,
)


app = QApplication([])


window = QWidget()
window.setWindowTitle("Memory Card")


"""Интерфейс приложения Memory Card"""
btn_ok = QPushButton("Ответить")  # кнопка ответа
lb_question = QLabel("Какой национальности не существует?")  # текст вопроса


radio_group_box = QGroupBox("Варианты ответов")  # группа ответов (выделяется визуально)

# радиальные переключатели с ответами
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чулымцы")
rbtn_4 = QRadioButton("Алеуты")

# вертикальные будут внутри горизонтального
layout_quest = QHBoxLayout()

# два ответа в первый столбец
layout_answer_column_1 = QVBoxLayout()
layout_answer_column_1.addWidget(rbtn_1)
layout_answer_column_1.addWidget(rbtn_2)

# два ответа во второй столбец
layout_answer_column_2 = QVBoxLayout()
layout_answer_column_2.addWidget(rbtn_3)
layout_answer_column_2.addWidget(rbtn_4)


layout_quest.addLayout(layout_answer_column_1)
layout_quest.addLayout(layout_answer_column_2)  # разместили столбцы в одной строке


radio_group_box.setLayout(layout_quest)  # готова "панель" с вариантами ответов


layout_line1 = QHBoxLayout()  # вопрос
layout_line2 = QHBoxLayout()  # варианты ответов или результат теста
layout_line3 = QHBoxLayout()  # кнопка "Ответить"


layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(radio_group_box)


layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)  # кнопка должна быть большой
layout_line3.addStretch(1)


# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # пробелы между содержимым


window.setLayout(layout_card)
window.show()
app.exec()
