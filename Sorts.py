from tkinter import *
from tkinter.ttk import *
from random import sample



def coordinates(tg, color):
    global a
    x_width = 650 / (len(a) + 1)
    x0 = tg * x_width + 30
    y0 = 200 - 20 * int(a[tg])
    x1 = (tg + 1) * x_width + 20
    y1 = 200
    xt = x0 + ((x1 - x0) / 2)
    box2.create_rectangle(x0, y0, x1, y1, fill=color)
    box2.create_text(xt, y0 - 10, text=a[tg])


def new_win():
    global box2, win2
    win2 = Toplevel()
    win2.geometry(f'+{round(win.winfo_screenwidth() / 2 - 120 - 660)}+200')
    win2.resizable(False, False)
    box2 = Canvas(win2, width=650, height=200)
    box2.grid(row=0, column=0)


def info():
    tl = Toplevel()
    tl.resizable(False, False)
    Label(tl, text='Visualization of different sorting algorithms', font=('Times New Roman', 15)).grid(row=0, column=0,
                                                                                                       columnspan=2,
                                                                                                       padx=15, pady=15)
    Label(tl, text='Created by Leontev A.', font=('Comic Sans MS', 10)).grid(row=1, column=0, pady=10, padx=5)
    Label(tl, text='version 2.4', font=('Arial', 10)).grid(row=1, column=1, pady=10, padx=5, sticky=SE)


def rand():
    global a
    g.delete(0, END)
    alphabet = '123456789'
    a = ''.join(sample(alphabet, k=len(alphabet)))
    g.insert(0, a)
    win.focus()


def auto():
    global sted
    sp = int(scale.get())
    but3.config(state=DISABLED)
    but1.config(state=DISABLED)
    rb1.config(state=DISABLED)
    rb2.config(state=DISABLED)
    check.config(state=DISABLED)
    if sted:
        finish()
    else:
        if rb_var.get() == 0:
            bubble_sort()
            win.after(sp, auto)
        if rb_var.get() == 1:
            selection_sort()
            win.after(sp, auto)

    win.focus()


def lines(x, y):
    box.create_line(x - 3, 65, x - 3, 80)
    box.create_line(y + 2, 65, y + 2, 80)
    box.create_line(x - 3, 80, y + 2, 80)
    box.create_text((x + y - 1) / 2, 85, text='swapped')


def stock():
    global a, nc, wh1, wh2, ak, box2
    box.delete('all')
    if check_var.get() == 1:
        box2.delete('all')
    win.update_idletasks()
    nc = win.winfo_width() / 2 - 12.7 * len(a) / 2
    pl = 0
    for i in range(0, len(a)):
        box.create_text(nc + pl, 50, text=a[i], font="Verdana 14", fill='black')
        if check_var.get() == 1:
            coordinates(i, 'black')
        if i == wh1:
            box.create_line(nc + pl, 40, nc + pl, 15)
            box.create_text(nc + pl, 8, text='max', font='Arial 8')
        if i == wh2:
            box.create_line(nc + pl, 40, nc + pl, 30)
            box.create_text(nc + pl, 23, text='min', font='Arial 8')
        pl += 14


def finish():
    global a, nc
    box.delete('all')
    check.config(state=ACTIVE)
    if check_var.get() == 1:
        box2.delete('all')
    pl = 0
    for i in range(0, len(a)):
        box.create_text(nc + pl, 50, text=a[i], font=("Verdana", 14), fill='green')
        if check_var.get() == 1:
            coordinates(i, 'green')
        pl += 14


def entr():
    global a, p, sted, box, wdth, wh1, wh2, iy, smallest, j, kvk, ak, win2
    box.config(width=200, height=200)

    sted = False
    kvk = False
    maxel = 0
    minel = 9
    p = 0
    j = 1
    iy = 0
    smallest = iy
    wh1 = 0
    wh2 = 0
    c = 0
    if check_var.get() == 1:
        try:
            win2.destroy()
            new_win()
        except NameError:
            new_win()
    else:
        try:
            win2.destroy()
        except NameError:
            pass
    try:
        box.delete("all")
        but1.config(text='Sort', state=ACTIVE)
        but3.config(text='Auto-sorting', state=ACTIVE)
        rb1.config(state=ACTIVE)
        rb2.config(state=ACTIVE)
        check.config(state=ACTIVE)
        a = g.get()
        a = [int(x) for x in a]
        if len(a) > 10:
            box.configure(width=win.winfo_screenwidth() / 2, height=200)
        for i in range(0, len(a)):
            if a[i] >= maxel:
                maxel = a[i]
                wh1 = i
            if a[i] <= minel:
                minel = a[i]
                wh2 = i
        stock()
        for e in range(0, len(a) - 1):
            if a[e] <= a[e + 1]:
                c += 1
        if c == len(a) - 1:
            finish()
            but1.config(text='Sorted!', state=DISABLED)
            but3.config(text='Sorted!', state=DISABLED)
            sted = True
    except ValueError:
        box.create_text(100, 50, text='Error! \nIncorrect data!', font='Arial 20')
        but1.config(state=DISABLED)
        but3.config(state=DISABLED)
    win.focus()


def bubble_sort():
    global a, p, nc, sted, wh1, wh2
    pl = 14
    c = 0
    k = False
    if a[p] > a[p + 1]:
        if p == wh1:
            wh1 += 1
        if p + 1 == wh2:
            wh2 += -1
        k = True
        a[p], a[p + 1] = a[p + 1], a[p]
    stock()
    box.create_text((nc + (pl * p)), 50, text=a[p], font="Verdana 14", fill='red')
    box.create_text((nc + (pl * (p + 1))), 50, text=a[p + 1], font="Verdana 14", fill='red')
    if check_var.get() == 1:
        coordinates(p, 'red')
        coordinates(p + 1, 'red')
    if k:
        lines(nc + (pl * p), nc + (pl * (p + 1)))
    p += 1
    if p == len(a) - 1:
        p = 0
        for e in range(0, len(a) - 1):
            if a[e] <= a[e + 1]:
                c += 1
        if c == len(a) - 1:
            win.after(1500, finish)
            but1.config(text='Sorted!', state=DISABLED)
            but3.config(text='Sorted!', state=DISABLED)
            sted = True

    win.focus()


def selection_sort():
    global a, j, wh1, wh2, iy, smallest, sted, kvk
    pl = 14
    c = 0
    if a[j] < a[smallest]:
        smallest = j
        kvk = True
    stock()
    box.create_text((nc + (pl * j)), 50, text=a[j], font="Verdana 14", fill='red')
    box.create_text((nc + (pl * iy)), 50, text=a[iy], font="Verdana 14", fill='red')
    if check_var.get() == 1:
        coordinates(j, 'red')
        coordinates(iy, 'red')
    j += 1
    if j == len(a):
        if kvk:
            box.create_text((nc + (pl * smallest)), 50, text=a[smallest], font="Verdana 14", fill='#7CFC00')
            if check_var.get() == 1:
                coordinates(smallest, '#7CFC00')
            if smallest == wh2:
                wh2 = iy
            if iy == wh1:
                wh1 = smallest
            a[iy], a[smallest] = a[smallest], a[iy]
            lines(nc + (pl * iy), nc + (pl * smallest))
        kvk = False
        iy += 1
        smallest = iy
        j = iy + 1
        for e in range(0, len(a) - 1):
            if a[e] <= a[e + 1]:
                c += 1
        if c == len(a) - 1:
            win.after(1500, finish)
            but1.config(text='Sorted!', state=DISABLED)
            but3.config(text='Sorted!', state=DISABLED)
            sted = True

    win.focus()


def main():
    if rb_var.get() == 0:
        bubble_sort()
    if rb_var.get() == 1:
        selection_sort()


win = Tk()
win.title('Sorts')
win.resizable(False, False)
win.geometry(f'+{round(win.winfo_screenwidth() / 2 - 120)}+200')
photo = PhotoImage(file = 'sort.png')
win.iconphoto(True, photo)
style = Style()
style.configure("BW.TLabel", foreground="grey", bd=0)
rb_var = IntVar()
rb_var.set(1)
check_var = BooleanVar()
check_var.set(0)
aus = LabelFrame(win, text='Automatic')
meh = LabelFrame(win, text='Manual')
rbs = Frame(win)
g = Entry(win)
check = Checkbutton(win, text='Rectangles', variable=check_var, offvalue=0, onvalue=1, command=win.focus)
rb1 = Radiobutton(rbs, text='Bubble sort', variable=rb_var, value=0, command=win.focus)
rb2 = Radiobutton(rbs, text='Selection sort', variable=rb_var, value=1, command=win.focus)
Label(win, text='Set of numbers:').grid(row=0, column=0, columnspan=2, padx=10, pady=5)
scale = Scale(aus, orient='horizontal', from_=2000, to_=100)
scale.set(800)
but1 = Button(meh, text='Sort', state=DISABLED, command=main)
but2 = Button(win, text='Enter', command=entr)
but3 = Button(aus, text='Auto-sorting', state=DISABLED, command=auto)
but4 = Button(win, text='Random numbers', command=rand)
Label(aus, text='Speed').grid(row=6, column=0)
Label(meh, text='Step by step:').grid(row=4, column=0, sticky=E, pady=5)
box = Canvas(win, width=200, height=200)
info = Button(win, text='About this', style='BW.TLabel', command=info)
aus.grid(row=6, column=0, columnspan=2, pady=5)
meh.grid(row=5, column=0, columnspan=2, pady=5)
rb1.grid(row=0, column=0, sticky=W)
rb2.grid(row=1, column=0, sticky=W)
g.grid(row=1, column=0, columnspan=2)
check.grid(row=2, column=0, pady=5, columnspan=2)
but2.grid(row=3, column=1, pady=5, stick='wens', padx=5)
but1.grid(row=4, column=1, pady=5, stick='wens', padx=3)
but3.grid(row=5, column=0, columnspan=2, pady=2, stick='wens', padx=5)
but4.grid(row=3, column=0, pady=5, padx=5, stick='wens')
scale.grid(row=6, column=1, padx=5)
rbs.grid(column=0, columnspan=2, row=4)
box.grid(row=7, column=0, columnspan=2)
info.grid(row=8, column=1, padx=5, pady=5, sticky=E)

mainloop()
