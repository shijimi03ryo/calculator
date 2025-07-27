# # シンプルな電卓プログラム

# # 入力を受け取る
# num1 = int(input("1つ目の数を入力してください: "))
# op = input("演算子を入力してください（+ - * /）: ")
# num2 = int(input("2つ目の数を入力してください: "))

# # 演算と出力
# if op == "+":
#     print("結果:", num1 + num2)
# elif op == "-":
#     print("結果:", num1 - num2)
# elif op == "*":
#     print("結果:", num1 * num2)
# elif op == "/":
#     if num2 != 0:
#         print("結果:", num1 / num2)
#     else:
#         print("0で割ることはできません")
# else:
#     print("無効な演算子です")

import tkinter as tk

# 計算直後フラグ
just_calculated = False

def click(event):
    global just_calculated
    val = str(event.widget["text"])
    current = entry.get()

    if just_calculated:
        # 計算直後なら、新しい数字からスタート
        entry.delete(0, tk.END)
        just_calculated = False

    entry.insert(tk.END, val)

def clear_all():
    global just_calculated
    entry.delete(0, tk.END)
    just_calculated = False
    
def clear():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    global just_calculated
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        just_calculated = True
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "エラー")
        just_calculated = True

# メインウィンドウ作成
root = tk.Tk()
root.title("電卓")

entry = tk.Entry(root, width=20, font=('Arial', 24), bd=10, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ["AC", "C", "", ""],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for i, row in enumerate(buttons):
    for j, val in enumerate(row):
        btn = tk.Button(root, text=val, width=5, height=2, font=('Arial', 24))
        btn.grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)

        if val == "":
            continue
        elif val == "C":
            btn.config(command=clear)
        elif val == "AC":
            btn.config(command=clear_all)
        elif val == "=":
            btn.config(command=calculate)
        else:
            btn.bind("<Button-1>", click)

root.mainloop()