import tkinter as tk
from tkinter import ttk



def book_appointment():
    print("starting bookings .... ")

def show_menu(oldFrame:tk.Frame = None):   # basic menu
    if oldFrame is not None:
        oldFrame.destroy()
    root = tk.Tk()
    root.geometry('600x400')   # decide the size of the main frame
    root.title('Notebook Menu Demo')  # give it a title
    note = ttk.Notebook(root)

    b = ttk.Button(root, text="help")  # demo how to use a button
    b.pack()

    tab1 = ttk.Frame(note, width=400, height=300)
    tab2 = ttk.Frame(note, width=400, height=300)
    tab3 = ttk.Frame(note, width=400, height=300)
    tab4 = ttk.Button(root, text="Exit Application?", command=root.destroy)

    note.add(tab1, text="Accounts")
    note.add(tab2, text="Bookings")
    note.add(tab3, text="Display")
    note.add(tab4, text="Exit")
    note.pack(expand=True, fill=tk.BOTH)
    root.mainloop()


def show_customised_menu():    # customised menu
    # using pack() method, go to https://www.pythontutorial.net/tkinter/tkinter-pack/
    root = tk.Tk()
    root.geometry('600x400')  # decide the size of the main frame
    root.title('Notebook Menu Demo')  # give it a title
    my_style = ttk.Style()   # define a style
    my_style.map("TNotebook.Tab", foreground=[("selected", "blue")])   # blue selected tab
    my_style.configure('TNotebook.Tab', font=('default', 10))  # default size is 10
    my_style.configure("TNotebook", tabposition="top")  # tab position at the top
    my_style.configure("TNotebook.Tab", padding=[20, 5], background="lightgray")  # bg colour
    my_style.configure("TNotebook.Separator", background="red", borderwidth=2)  # border
    notebook = ttk.Notebook(root)
    account_button = ttk.Button(root, text="help")  # demo how to use a button
    account_button.pack(expand=False, fill=tk.BOTH)
    account_tab = ttk.Frame(notebook)
    booking_tab = ttk.Frame(notebook)
    display_tab = ttk.Frame(notebook)
    notebook.add(account_tab, text='Account')
    notebook.add(booking_tab, text='Bookings')
    notebook.add(display_tab, text='Display')

    # adding button in account tab
    account_text = ttk.Label(account_tab, text="Demo Title", font=("Arial", 15))
    textbox_label = ttk.Label(account_tab, text="Staff Name:", font=("Arial", 12, "bold"))

    textbox = ttk.Entry(account_tab, font=("Arial", 10, "italic"))
    textbox.insert(tk.END, "enter staff name here ...")
    tab_button = ttk.Button(account_tab, text="Exit?", command=root.destroy)

    account_text.pack(padx=10, pady=10, anchor="w")
    textbox_label.pack(padx=10, pady=10, anchor="w")
    textbox.pack(pady=10, anchor="w")
    tab_button.pack(pady=10, anchor="w")
    tab_button.pack(padx=10, pady=10, anchor="w")
    notebook.pack(expand=True, fill='both')

    # adding button in booking tab (demo only)
    booking_button = ttk.Button(booking_tab, text="Book", command= lambda: book_appointment())
    booking_button.pack(padx=10, pady=10, anchor="w")

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(300, 200))


    #root.eval('tk::PlaceWindow . center')  # centres the window on the screen (not accurate!)
    root.mainloop()


if __name__ == '__main__':

    #show_menu()
    show_customised_menu()
