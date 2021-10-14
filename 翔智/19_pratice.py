# 問答程式
from question import Question  # 代表從question.py檔案單純引入Question類別 不引入additional變數
# import question 代表引入整個模組 這裡不適合

test = [
    "1 + 3 = ? \n(a)  2\n(b)  3\n(c)  4\n\n",
    "How many centimeters is 1 meter ?\n(a)  10\n(b)  100\n(c)  1000\n\n",
    "What is the color of bananas ? \n(a)  red\n(b)  blue\n(c)  yellow\n\n"
]  # 一個問題有 描述 答案 兩個資訊，可定義為一個資料型態

questions = [  # 串建一個questions變數 存放問題與答案
    Question(test[0], "c"),
    Question(test[1], "b"),
    Question(test[2], "c")
]


def run_test(questions):  # 該函式要匯入什麼
    score = 0
    for question in questions:  # 用來自動匯入題目
        answer = input(question.description)  # 顯示題目 使用者的回答存放為answer
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "points. in total " +
          str(len(questions)) + "questions. ")


run_test(questions)
