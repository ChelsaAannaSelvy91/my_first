import tkinter as tk


# Writing functions for each button
def get_number():
    global str_txt, strlen
    str_txt = txt_box1.get()
    strlen = len(str_txt)
    return strlen


def do_fun(result):
    str_txt = txt_box1.get()
    strlen = len(str_txt)
    txt_box1.delete(0, strlen)
    txt_box1.insert(0, result)


def b1_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '1')


def b2_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '2')


def b3_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '3')


def b4_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '4')


def b5_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '5')


def b6_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '6')


def b7_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '7')


def b8_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '8')


def b9_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '9')


def b0_fun():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '0')


def bclear():
    strlen = int(get_number())
    txt_box1.delete(0, strlen)
    txt_box1.insert(0, " ")


def bplus():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '+')


def bminus():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '-')


def bmul():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '*')


def bdiv():
    strlen = int(get_number())
    txt_box1.insert(strlen + 1, '/')


def bequal():
    str_txt = txt_box1.get()
    str_txt = str_txt.replace(' ', '')
    active_operator = []
    operand = []
    temp1 = []
    sub_string = ""
    operator = ['+', '-', '*', '/']
    num_list = []
    # separating operators and operands into two list
    for item in str_txt:
        if item.isdigit():
            sub_string = sub_string + item
            temp1.append(sub_string)
        elif item in operator:
            operand.append(sub_string)
            sub_string = ""
            active_operator.append(item)
    count = len(temp1)
    for i in range(count):
        if i == count - 1:
            operand.append(temp1[i])
    print(operand)
    print(active_operator)
    plus_no = active_operator.count('+')
    minus_no = active_operator.count('-')
    mul_no = active_operator.count('*')
    div_no = active_operator.count('/')
    # performing operations according to priority
    while div_no != 0:
        x = active_operator.index('/')
        y = x + 1
        count = len(operand)
        for i in range(count):
            num1 = operand[x]
            num2 = operand[y]
            if num1.isdigit():
                num1 = int(num1)
                if num2.isdigit():
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            else:
                num1 = float(num1)
                if num2.isdigit():
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            operation = str(num1 / num2)
            operand.pop(x)
            operand.insert(x, operation)
            operand.pop(y)
            active_operator.pop(x)
            break
        div_no = div_no - 1
        print(operand)
        print(active_operator)
    while mul_no != 0:
        x = active_operator.index('*')
        y = x + 1
        count = len(operand)
        for i in range(count):
            num1 = operand[x]
            num2 = operand[y]
            if num1.isdigit():
                num1 = int(num1)
                if num2.isdigit():
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            else:
                num1 = float(num1)
                if num2.isdigit():
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            operation = str(num1 * num2)
            operand.pop(x)
            operand.insert(x, operation)
            operand.pop(y)
            active_operator.pop(x)
            break
        mul_no = mul_no - 1
        print(operand)
        print(active_operator)

    while minus_no != 0:
        x = active_operator.index('-')
        y = x + 1
        count = len(operand)
        for i in range(count):
            num1 = operand[x]
            num2 = operand[y]
            if num1.isdigit():
                num1 = int(num1)
                if num2.isdigit():
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            else:
                num1 = float(num1)
                if num2.isdigit():
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            operation = str(num1 - num2)
            operand.pop(x)
            operand.insert(x, operation)
            operand.pop(y)
            active_operator.pop(x)
            break
        minus_no = minus_no - 1
        print(operand)
        print(active_operator)
    while plus_no != 0:
        x = active_operator.index('+')
        y = x + 1
        count = len(operand)
        for i in range(count):
            num1 = operand[x]
            num2 = operand[y]
            if num1.isdigit():
                num1 = int(num1)
                if num2.isdigit():
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            else:
                num1 = float(num1)
                if num2.isdigit():
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            operation = str(num1 + num2)
            operand.pop(x)
            operand.insert(x, operation)
            operand.pop(y)
            active_operator.pop(x)
            break
        plus_no = plus_no - 1
        # print(operand)
        # print(active_operator)
    # print result
    for i in operand:
        do_fun(i)
        print(abs(i))


# Create a new tkinter window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x500")
# Create two input fields and a button
txt_box1 = tk.Entry(window, width=32)
txt_box1.pack()
txt_box1.place(x=100, y=100)
b1 = tk.Button(window, text=" 1 ", command=b1_fun)
b1.pack()
b1.place(x=110, y=150)
b2 = tk.Button(window, text=" 2 ", command=b2_fun)
b2.pack()
b2.place(x=160, y=150)
b3 = tk.Button(window, text=" 3 ", command=b3_fun)
b3.pack()
b3.place(x=210, y=150)
b_plus = tk.Button(window, text=" + ", command=bplus)
b_plus.pack()
b_plus.place(x=260, y=150)
b4 = tk.Button(window, text=" 4 ", command=b4_fun)
b4.pack()
b4.place(x=110, y=200)
b5 = tk.Button(window, text=" 5 ", command=b5_fun)
b5.pack()
b5.place(x=160, y=200)
b6 = tk.Button(window, text=" 6 ", command=b6_fun)
b6.pack()
b6.place(x=210, y=200)
b_minus = tk.Button(window, text=" -  ", command=bminus)
b_minus.pack()
b_minus.place(x=260, y=200)
b7 = tk.Button(window, text=" 7 ", command=b7_fun)
b7.pack()
b7.place(x=110, y=250)
b8 = tk.Button(window, text=" 8 ", command=b8_fun)
b8.pack()
b8.place(x=160, y=250)
b9 = tk.Button(window, text=" 9 ", command=b9_fun)
b9.pack()
b9.place(x=210, y=250)
b_mul = tk.Button(window, text=" *  ", command=bmul)
b_mul.pack()
b_mul.place(x=260, y=250)
b_clr = tk.Button(window, text=" C ", command=bclear)
b_clr.pack()
b_clr.place(x=110, y=300)
b0 = tk.Button(window, text=" 0 ", command=b0_fun)
b0.pack()
b0.place(x=160, y=300)
b_div = tk.Button(window, text=" / ", command=bdiv)
b_div.pack()
b_div.place(x=210, y=300)
b_eq = tk.Button(window, text=" = ", command=bequal)
b_eq.pack()
b_eq.place(x=260, y=300)

window.mainloop()
