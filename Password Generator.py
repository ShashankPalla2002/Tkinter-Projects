from tkinter import *
import random

NUMBERS, SPECIAL_SYMBOLS, UPPER_CASE, LOWER_CASE = 0, 0, 0, 0
SpecialSymbols_list = ['@', '$', '&', '!', '%']
choice = ['u', 'l', 's', 'n']
pass_list = []
final_list = []

def window():
    global main_window
    main_window = Tk(className=" Random Password Generator ")
    main_window.geometry('800x600')

def Input():
    global input
    input = Entry(main_window, width=50, justify='center')

def click(*args):
    input.delete(0, 'end')

def clearFrame():
    for widget in main_window.winfo_children():
        widget.destroy()

window()
Input()

def first_step():
    input.insert(0, "How many letter password do you want?")
    input.bind("<Button-1>", click)
    input.pack(pady = 25,)

    def check1():
        global pass_length
        pass_length = input.get()
        if pass_length.isdigit():
            pass_length = int(pass_length)
            clearFrame()
            second_step()
        else:
            label = Label(main_window, text="NOTE - Entered value not numeric...Try again!")
            label.pack()


    button = Button(main_window, text="Enter", command=check1)
    button.pack(pady = 10)

first_step()

def second_step():
    drop_down1()
    def check2():
        if select == "Randomized Password":
            Randomized_Password()

        else:
            Specialized_Password()


    global button1
    button1 = Button(main_window, text="Enter", command=check2, state='disabled')
    button1.pack()
    label = Label(main_window, text='Randomized Password-> System generates a random password...').pack(pady=50)
    label1 = Label(main_window, text='Specialized Password-> You can customize your password...').pack()

def drop_down1():
    mainframe = Frame(main_window)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)
    variable = StringVar(main_window)

    choices = {'Randomized Password', 'Specialized Password'}
    variable.set('None')

    popupMenu = OptionMenu(mainframe, variable, *choices)
    Label(mainframe, text="What type of password do you want?").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):
        global select
        select = variable.get()
        if select!=None:
            button1['state'] = 'normal'

    variable.trace('w', change_dropdown)

def Randomized_Password():
    clearFrame()
    i = pass_length
    while i > 0:
        select = random.choice(choice)
        if select == 'u':
            pass_list.append(chr(random.randint(65, 90)))
            i = i-1
        elif select == 'n':
            pass_list.append(str(random.randint(0, 9)))
            i = i-1
        elif select == 'l':
            pass_list.append(chr(random.randint(97, 122)))
            i = i-1
        else:
            pass_list.append(random.choice(SpecialSymbols_list))
            i = i-1

    input = Entry(main_window, width=100, bg='systembuttonface', bd=0, justify='center', font=10)
    input.insert(0, pass_list)
    input['state'] = 'disable'
    input.pack(pady=50)

    def copy():
        main_window.clipboard_clear()
        main_window.clipboard_append(input.get())
        label = Label(main_window, text='Copied to Clipboard successfully!').pack(pady=30)

    button = Button(main_window, text='Copy to Clipboard', command=copy).pack()

def Specialized_Password():
    clearFrame()
    global input
    input = Entry(main_window, text='enter', state='disabled')

    def drop_down_2():

        mainframe = Frame(main_window)
        Label(mainframe, text=f'You opted for a password length of {pass_length}.').grid(row=0, column=1)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)
        variable = StringVar(main_window)
        choices = {'Uppercase Letters', 'Lowercase Letters', 'Numbers', 'Special Symbols'}
        variable.set('--None--')
        popupMenu = OptionMenu(mainframe, variable, *choices)

        Label(mainframe, text="Please select the option from the dropdown box below...").grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

        def change_dropdown(*args):
            global select
            select = variable.get()
            Question = select
            if select != '--None--':
                input['state'] = 'normal'

        variable.trace('w', change_dropdown)
    drop_down_2()
    label = Label(main_window, text='Please enter how characters many do you want...').pack()
    input.bind("<Button-1>", click)
    input.pack()
    button = Button(main_window, text='Enter', command=check3)
    button.pack()
    label = Label(main_window, text='After entering everything press "DONE" to generate password').pack(pady=45)
    button = Button(main_window, text='DONE', command=Specialized_func, width=15)
    button.pack(pady=30)

def check3():
    global input
    a = input.get()
    if a.isdigit():
        a = int(a)
        if select == 'Numbers':
            global NUMBERS
            NUMBERS = a
            clearFrame()
            Specialized_Password()
            # button = Button(main_window, text='Enter', command=check)
            # button.pack()
            # label = Label(main_window, text='After entering everything press "DONE" to generate password').pack(pady=45)
            # button = Button(main_window, text='DONE', command=func, width=15)
            # button.pack(pady = 30)

        elif select == 'Uppercase Letters':
            global UPPER_CASE
            UPPER_CASE = a
            clearFrame()
            Specialized_Password()
            # button = Button(main_window, text='Enter', command=check)
            # button.pack()
            # label = Label(main_window, text='After entering everything press "DONE" to generate password').pack(pady=45)
            # button = Button(main_window, text='DONE', command=func, width=15)
            # button.pack(pady=30)

        elif select == 'Lowercase Letters':
            global LOWER_CASE
            LOWER_CASE = a
            clearFrame()
            Specialized_Password()
            # button = Button(main_window, text='Enter', command=check)
            # button.pack()
            # label = Label(main_window, text='After entering everything press "DONE" to generate password').pack(pady=45)
            # button = Button(main_window, text='DONE', command=func, width=15)
            # button.pack(pady=30)

        elif select == 'Special Symbols':
            global SPECIAL_SYMBOLS
            SPECIAL_SYMBOLS = a
            clearFrame()
            Specialized_Password()
            # button = Button(main_window, text='Enter', command=check)
            # button.pack()
            # label = Label(main_window, text='After entering everything press "DONE" to generate password').pack(pady=45)
            # button = Button(main_window, text='DONE', command=func, width=15)
            # button.pack(pady=30)

    else:
        label = Label(main_window, text='NOTE - Entered value is not numeric...Try again!').pack()

def Specialized_func():
    global UPPER_CASE, NUMBERS, LOWER_CASE, SPECIAL_SYMBOLS
    if NUMBERS + SPECIAL_SYMBOLS + UPPER_CASE + LOWER_CASE > pass_length or NUMBERS + SPECIAL_SYMBOLS + UPPER_CASE + LOWER_CASE < pass_length:
        label = Label(main_window, text= 'NOTE - The sum of entered values does not match the password length...Try again!').pack()
    else:
        clearFrame()
        i = pass_length
        while i > 0:
            while UPPER_CASE > 0:
                pass_list.append(chr(random.randint(65, 90)))
                UPPER_CASE = UPPER_CASE - 1
                i = i - 1

            while LOWER_CASE > 0:
                pass_list.append(chr(random.randint(97, 122)))
                LOWER_CASE = LOWER_CASE - 1
                i = i - 1
            while NUMBERS > 0:
                pass_list.append(random.randint(0, 9))
                NUMBERS = NUMBERS - 1
                i = i - 1
            while SPECIAL_SYMBOLS > 0:
                pass_list.append(random.choice(SpecialSymbols_list))
                SPECIAL_SYMBOLS = SPECIAL_SYMBOLS - 1
                i = i - 1

    def print_password():
        j = pass_length
        if len(pass_list) == j:
            while j > 0:
                rand = random.choice(pass_list)
                final_list.append(rand)
                pass_list.remove(rand)
                j = j - 1

        else:
            print("NOTE - The sum of entered values does not match the password length...Try again!")



        input = Entry(main_window, width=100, bg= 'systembuttonface', bd=0, justify='center', font=10)
        input.insert(0, final_list)
        input['state'] = 'disabled'
        input.pack(pady = 50)

        def copy():
            main_window.clipboard_clear()
            main_window.clipboard_append(input.get())
            label = Label(main_window, text='Copied to Clipboard successfully!').pack(pady = 30)

        button = Button(main_window, text='Copy to Clipboard', command=copy).pack()

    print_password()

main_window.mainloop()

