from tkinter import *
import sqlite3


root = Tk()
root.title("Reading Tracker")
root.geometry("260x120")


def update_finished():
    global top
    top = Toplevel()
    top.title("Updating")
    conn = sqlite3.connect("Reading_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT *, oid FROM books Where oid = " + updatefrecord.get())
    record = cursor.fetchall()
    global l1top_name
    global l2top_author
    global l3top_genre
    global l4top_language
    global l5top_page
    global l6top_status
    l1top = Label(top, text="Book Name ->")
    l1top.grid(row=1, column=0)
    l1top_name = Entry(top, width=30)
    l1top_name.insert(0, record[0][0])
    l1top_name.grid(row=1, column=1, padx=20)
    l2top = Label(top, text="Authors Name ->")
    l2top.grid(row=2, column=0)
    l2top_author = Entry(top, width=30)
    l2top_author.insert(0, record[0][1])
    l2top_author.grid(row=2, column=1)
    l3top = Label(top, text="Address ->")
    l3top.grid(row=3, column=0)
    l3top_genre = Entry(top, width=30)
    l3top_genre.insert(0, record[0][2])
    l3top_genre.grid(row=3, column=1)
    l4top = Label(top, text="City ->")
    l4top.grid(row=4, column=0)
    l4top_language = Entry(top, width=30)
    l4top_language.insert(0, record[0][3])
    l4top_language.grid(row=4, column=1)
    l5top = Label(top, text="State->")
    l5top.grid(row=5, column=0)
    l5top_page = Entry(top, width=30)
    l5top_page.insert(0, record[0][4])
    l5top_page.grid(row=5, column=1)
    l6top = Label(top, text="Zipcode->")
    l6top.grid(row=6, column=0)
    l6top_status = Entry(top, width=30)
    l6top_status.insert(0, record[0][5])
    l6top_status.grid(row=6, column=1)
    adding_btn = Button(top, text="Update", command=adding)
    adding_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    conn.commit()
    conn.close()


def adding():
    conn = sqlite3.connect("Reading_info.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = ?, author = ?, genre = ?, language = ?, page = ?, status = ? "
                   "WHERE oid = ?",
                    [l1top_name.get(), l2top_author.get(), l3top_genre.get(), l4top_language.get(), l5top_page.get(),
                     l6top_status.get(), updatefrecord.get()])
    conn.commit()
    conn.close()
    top.destroy()


def show_all():
    conn = sqlite3.connect("Reading_info.db")
    cursor = conn.cursor()
    show_records = Toplevel()
    show_records.title("Records")
    cursor.execute("SELECT *, oid FROM books")
    records = cursor.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(show_records, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)
    conn.commit()
    conn.close()
    return


def insert():
    conn = sqlite3.connect("Reading_info.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books VALUES (:b_name, :a_name, :genre, :language, :page, :status)",
                   {'b_name': bf_name.get(),
                    'a_name': af_name.get(),
                    'genre': genref.get(),
                    'language': languagef.get(),
                    'page': pagef.get(),
                    'status': statusf.get()
                    })
    conn.commit()
    conn.close()
    bf_name.delete(0, END)
    af_name.delete(0, END)
    genref.delete(0, END)
    languagef.delete(0, END)
    pagef.delete(0, END)
    statusf.delete(0, END)
    return


def delete_finished():
    conn = sqlite3.connect("Reading_info.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE oid = " + delfrecord.get())
    conn.commit()
    conn.close()
    delfrecord.delete(0, END)
    return


def finish():
    conn = sqlite3.connect("Reading_info.db")
    cursor = conn.cursor()
    global bf_name
    global af_name
    global genref
    global languagef
    global pagef
    global statusf
    global delfrecord
    global updatefrecord
    finished_records = Toplevel()
    finished_records.title("Finished books")
    finished_records.geometry("400x450")
    finish_show_btn = Button(finished_records, text="Show all books", command=show_all)
    finish_show_btn.grid(row=7, column=0, columnspan=2, pady=20, padx=100, ipadx=50)
    finish_insert_btn = Button(finished_records, text="Insert book", command=insert)
    finish_insert_btn.grid(row=6, column=0, columnspan=2, pady=20, padx=50, ipadx=60)
    l1 = Label(finished_records, text="Book Name ->")
    l1.grid(row=0, column=0)
    bf_name = Entry(finished_records, width=30)
    bf_name.grid(row=0, column=1, padx=20)
    l2 = Label(finished_records, text="Author's Name ->")
    l2.grid(row=1, column=0)
    af_name = Entry(finished_records, width=30)
    af_name.grid(row=1, column=1, padx=20)
    l3 = Label(finished_records, text="Genre ->")
    l3.grid(row=2, column=0)
    genref = Entry(finished_records, width=30)
    genref.grid(row=2, column=1, padx=20)
    l4 = Label(finished_records, text="Language ->")
    l4.grid(row=3, column=0)
    languagef = Entry(finished_records, width=30)
    languagef.grid(row=3, column=1, padx=20)
    l5 = Label(finished_records, text="Pages ->")
    l5.grid(row=4, column=0)
    pagef = Entry(finished_records, width=30)
    pagef.grid(row=4, column=1, padx=20)
    l6 = Label(finished_records, text="Status ->")
    l6.grid(row=5, column=0)
    statusf = Entry(finished_records, width=30)
    statusf.grid(row=5, column=1, padx=20)
    finish_del_btn = Button(finished_records, text="Insert the ID to delete below", command=delete_finished)
    finish_del_btn.grid(row=8, column=0, columnspan=2, pady=20, padx=50, ipadx=16)
    delfrecord = Entry(finished_records, width=30)
    delfrecord.grid(row=9, column=0, columnspan=2, padx=20)
    finish_update_btn = Button(finished_records, text="Insert the ID you want to Update", command=update_finished)
    finish_update_btn.grid(row=10, column=0, columnspan=2, pady=20, padx=50, ipadx=8)
    updatefrecord = Entry(finished_records, width=30)
    updatefrecord.grid(row=11, column=0, columnspan=2, padx=20)
    conn.commit()
    conn.close()


finish_btn = Button(root, text="Books", command=finish)
finish_btn.grid(row=0, column=0, columnspan=3, pady=20, padx=50, ipadx=42, ipady=30)

root.mainloop()
