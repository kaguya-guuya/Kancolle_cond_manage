import tkinter
from tkinter import ttk


def Count_cond():       # cond値を増減, 場合分け
    cond = 0
    # 旗艦はcond値を加算
    if kikan_CheckButton_value.get() == True:       # 旗艦か選択
        if win_lose_RadioButton_value.get() == 0 or 1 or 2 or 3:
            cond = cond + 3

    # MVPはcond値を加算
    if MVP_CheckButton_value.get() == True:
        cond = cond + 10

    # 戦績でcond値を加算
    if win_lose_RadioButton_value.get() == 0:       # 戦績Sの時に処理
            cond = cond + 4
    elif win_lose_RadioButton_value.get() == 1:     # 戦績Aの時に処理
            cond = cond + 3
    elif win_lose_RadioButton_value.get() == 2:     # 戦績Bの時に処理
            cond = cond + 2
    elif win_lose_RadioButton_value.get() == 3:     # 戦績Cの時に処理
            cond = cond + 1

    # 昼戦突入でcond値を減算
    if Tyuusen_CheckButton_value.get() == True:
        cond = cond - 3

    # 夜戦突入でcond値を減算
    if Yasen_CheckButton_value.get() == True:
        cond = cond - 2

    # 撤退、帰還でcond値を減算
    if Tettai_CheckButton_value.get() == True:
        cond = cond - 15

    return cond


def hanei():
    Cond_Label["text"] = Count_cond()


def kasan():
    Final_Cond_Label["text"] = Final_Cond_Label["text"] + Cond_Label["text"]


def Reset():
    Final_Cond_Label["text"] = 49


window = tkinter.Tk()
window.title("艦これ cond値 管理")
window.geometry("250x250")


# 最終cond値
Final_Cond_Label = tkinter.Label(window, text = 49, font = ("", "20"))
Final_Cond_Label.grid(row = 0, column = 0)

Cond_Text_Label = tkinter.Label(window, text = "cond値", relief = "ridge")
Cond_Text_Label.grid(row = 1, column = 0)


# 加減cond値
Cond_Label = tkinter.Label(window, text = "", font = ("", "20"))
Cond_Label.grid(row = 0, column = 1)

Cond_Text_Label = tkinter.Label(window, text = "加減cond値", relief = "ridge")
Cond_Text_Label.grid(row = 1, column = 1)


# 旗艦チェックボックス
kikan_CheckButton_value = tkinter.BooleanVar()
kikan_CheckButton_value.set(True)

kikan_CheckButton = tkinter.Checkbutton(window, text = "旗艦", variable = kikan_CheckButton_value)

kikan_CheckButton.grid(row = 2, column = 0)


# MVPチェックボックス
MVP_CheckButton_value = tkinter.BooleanVar()
MVP_CheckButton_value.set(True)

MVP_CheckButton = tkinter.Checkbutton(window, text = "MVP", variable = MVP_CheckButton_value)

MVP_CheckButton.grid(row = 2, column = 1)


# 戦績ラジオボタン
win_lose_RadioButton_value = tkinter.IntVar()
win_lose_RadioButton_value.set(0)

win_lose_S = tkinter.Radiobutton(window, text = "勝利S", value = 0, variable = win_lose_RadioButton_value)
win_lose_A = tkinter.Radiobutton(window, text = "勝利A", value = 1, variable = win_lose_RadioButton_value)
win_lose_B = tkinter.Radiobutton(window, text = "勝利B", value = 2, variable = win_lose_RadioButton_value)
win_lose_C = tkinter.Radiobutton(window, text = "敗北C", value = 3, variable = win_lose_RadioButton_value)
win_lose_D = tkinter.Radiobutton(window, text = "敗北D", value = 4, variable = win_lose_RadioButton_value)
win_lose_E = tkinter.Radiobutton(window, text = "敗北E", value = 5, variable = win_lose_RadioButton_value)

win_lose_S.grid(row = 3, column = 0)
win_lose_A.grid(row = 3, column = 1)
win_lose_B.grid(row = 3, column = 2)
win_lose_C.grid(row = 4, column = 0)
win_lose_D.grid(row = 4, column = 1)
win_lose_E.grid(row = 4, column = 2)


# 昼戦チェックボックス
Tyuusen_CheckButton_value = tkinter.BooleanVar()
Tyuusen_CheckButton_value.set(True)

Tyuusen_CheckButton = tkinter.Checkbutton(window, text = "昼戦", variable = Tyuusen_CheckButton_value)

Tyuusen_CheckButton.grid(row = 5, column = 0)


# 夜戦チェックボックス
Yasen_CheckButton_value = tkinter.BooleanVar()

Yasen_CheckButton = tkinter.Checkbutton(window, text = "夜戦", variable = Yasen_CheckButton_value)

Yasen_CheckButton.grid(row = 5, column = 1)


# 帰還, 撤退チェックボックス
Tettai_CheckButton_value = tkinter.BooleanVar()
Tettai_CheckButton_value.set(False)

Tettai_CheckButton = tkinter.Checkbutton(window, text = "帰還 / 撤退", variable = Tettai_CheckButton_value)

Tettai_CheckButton.grid(row = 5, column = 2)


# 反映ボタン
Hanei_Button = tkinter.Button(window, text = "反映", command = hanei)

Hanei_Button.grid(row = 6, column = 0)


# 加算ボタン
Kasan_Button = tkinter.Button(window, text = "加算", command = kasan)

Kasan_Button.grid(row = 6, column = 1)


# リセットボタン
Reset_Button = tkinter.Button(window, text = "リセット", command = Reset)

Reset_Button.grid(row = 6, column = 2)


window.mainloop()