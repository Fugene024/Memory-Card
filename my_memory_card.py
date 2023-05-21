#создай приложение для запоминания информации
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QButtonGroup,
    QHBoxLayout, QVBoxLayout, QRadioButton, QGroupBox, QMessageBox
)
from random import (randint, shuffle)

app = QApplication([])
window = QWidget()
window.resize(400, 200)

lbl_question = QLabel('Какой национальности не существует?')
rbtn_1 = QRadioButton('Волгиетяне')
rbtn_2 = QRadioButton('Чеченцы')
rbtn_3 = QRadioButton('Юги')
rbtn_4 = QRadioButton('Евреи')
btn_skip = QPushButton('Ответить')
grpbox_answers = QGroupBox('Варианты ответов')
grpbox_result = QGroupBox('Результат')
lbl_result = QLabel('Это правильный ответ!')

vline_add = QVBoxLayout()
vline_add.addWidget(lbl_result)

grpbox_result.setLayout(vline_add)
grpbox_result.hide()

vline_main = QVBoxLayout()
hline_main1 = QHBoxLayout()
hline_main2 = QHBoxLayout()
hline_main3 = QHBoxLayout()

hline_grpbox = QHBoxLayout()
vline_grpbox1 = QVBoxLayout()
vline_grpbox2 = QVBoxLayout()

hline_main1.addWidget(lbl_question)
hline_main2.addWidget(grpbox_answers)
hline_main2.addWidget(grpbox_result)
hline_main3.addWidget(btn_skip)

vline_grpbox1.addWidget(rbtn_1)
vline_grpbox1.addWidget(rbtn_2)
vline_grpbox2.addWidget(rbtn_3)
vline_grpbox2.addWidget(rbtn_4)

hline_grpbox.addLayout(vline_grpbox1)
hline_grpbox.addLayout(vline_grpbox2)

vline_main.addLayout(hline_main1)
vline_main.addLayout(hline_main2)
vline_main.addLayout(hline_main3)

btn_grp = QButtonGroup()
btn_grp.addButton(rbtn_1)
btn_grp.addButton(rbtn_2)
btn_grp.addButton(rbtn_3)
btn_grp.addButton(rbtn_4)

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

grpbox_answers.setLayout(hline_grpbox)
window.setLayout(vline_main)

cur_question = 0
score = 0
buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [
    Question('Как звали Петра I?', 'Пётр I', 'Петр 1', 'Пётр 1', 'Петр I'),
    Question('Что из перечисленного не является ритм-игрой?', 'Geometry Dash', 'osu!', 'Friday Night Funkin', 'Beat Saber'),
    Question('Дополни строчку: Ретроград Меркурий...', 'Сидим, кальяны курим?', 'Сидим, Колянов дурим?', 'Сидим, баранов жмурим?', 'Сидим, скважины бурим?'), 
    Question('Какого зачарования для меча не существует?', 'Эффективность', 'Острота', 'Бич членистоногих', 'Заговор огня'),
    Question('Какой пластинки в Minecraft не существует?', '12', '5', '11', '13'),
    Question('1000-7?', '993', '933', '1007', 'Я угль'),
    Question('Самый маленький штат в Америке?', 'Род-Айленд', 'Огайо', 'Оклахома', 'Нью-Джерси')
]

def show_result():
    if is_all_checked():
        if buttons[0].isChecked():
            global score
            score += 1
            lbl_result.setText('Вы ответили правильно!')
        else:
            lbl_result.setText('Неправильно, попробуй еще раз.')
        grpbox_answers.hide()
        grpbox_result.show()
        btn_skip.setText('Следующий вопрос')

def is_all_checked():
    flag = False
    for btn in buttons:
        if btn.isChecked():
            flag = True
    return flag

def show_questions():
    grpbox_answers.show()
    grpbox_result.hide()
    btn_skip.setText('Ответить')
    btn_grp.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    btn_grp.setExclusive(True)

def next_question():
    global cur_question, score
    cur_question += 1
    if cur_question >= len(questions):
        msg = QMessageBox()
        msg.setText(get_percent(score))
        msg.setWindowTitle('Результат')
        msg.exec()
        cur_question = 0
        score = 0
    ask(questions[cur_question])

def click_skip():
    if btn_skip.text() == 'Ответить':
        show_result()
    else:
        next_question()

btn_skip.clicked.connect(click_skip)

def ask(question):
    shuffle(buttons)
    buttons[0].setText(question.right_answer)
    buttons[1].setText(question.wrong1)
    buttons[2].setText(question.wrong2)
    buttons[3].setText(question.wrong3)
    lbl_question.setText(question.question)
    lbl_result.setText(question.right_answer)
    show_questions()

def get_percent(score):
    percent = score / len(questions) * 100
    percent = round(percent, 1)
    result = 'Вы ответили на ' + str(score) + ' вопросов из ' + str(len(questions)) + '.' + ' Процент верных ответов: ' + str(percent)
    return result

shuffle(questions)
ask(questions[cur_question])

window.show()
app.exec()