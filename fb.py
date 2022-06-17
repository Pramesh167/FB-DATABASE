from tkinter import*
import sqlite3
light=Tk()
Label(light,text="Facebook",font="ariel 20 bold",bg="royal blue",fg="white").grid(row=0,column=2)
light.title("Facebook")
light.configure(bg='royal blue')
light.iconbitmap('facebuk.ico')
conn=sqlite3.connect('user_book.db')
c=conn.cursor()

# c.execute("""CREATE TABLE user(
#     first_name text,
#     last_name text,
#     address text,
#     age text,
#     password text,
#     fatherName text,
#     city text,
#     zipcode integer
#     )""")
# print("Table created successfully")
# conn.commit()
# conn.close()
from tkinter import messagebox
def submit():
    conn=sqlite3.connect('user_book.db')
    c=conn.cursor()
    c.execute("INSERT INTO user VALUES(:f_name,:l_name,:address,:age,:password,:fatherName,:city,:zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':l_name.get(),
        'age':age.get(),
        'password':password.get(),
        'fatherName':fatherName.get(),
        'city':city.get(),
        'zipcode':zipcode.get()
    })
    messagebox.showinfo('UserInfo Inserted Sucessfully')
    conn.commit()
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    age.delete(0,END)
    fatherName.delete(0,END)
    password.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)

def query():
    conn=sqlite3.connect('user_book.db')
    c=conn.cursor()
    c.execute('SELECT*, oid FROM user')
    records=c.fetchall()
    print(records)
    print_record=''
    for record in records:
        print_record+=str(record[0])+''+str(record[1])+''+'\t'+str(record[8])+'\n'
    qurey_label=Label(light,text=print_record)
    qurey_label.grid(row=8,column=0,columnspan=2)
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('user_book.db')
    c=conn.cursor()
    c.execute('DELETE FROM user WHERE oid='+delete_box.get())
    delete_box.delete(0,END)
    conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect('user_book.db')
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("""UPDATE user SET
        first_name=:first,
        last_name=:last,
        address=:address,
        age=:age,
        password=:password,
        fatherName=:fatherName,
        city=:city,
        zipcode=:zipcode
        WHERE oid=:oid""",
        {'first':f_name_editor.get(),
        'last':l_name_editor.get(),
        'address':address_editor.get(),
        'age':age_editor.get(),
        'password':password_editor.get(),
        'fatherName':fatherName_editor.get(),
        'city':city_editor.get(),
        'zipcode':zipcode_editor.get(),
        'oid':record_id
            }
    )
    conn.commit()
    conn.close()
    editor.destroy()







def edit():
    global editor
    editor=Toplevel()
    
    editor.title('Update Data')
    editor.iconbitmap('vsp.ico')
    editor.config(bg='royal blue')
    editor.geometry('400x400')
    conn=sqlite3.connect('user_book.db')
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute('SELECT* FROM user WHERE oid='+record_id)
    records=c.fetchall()


    global f_name_editor
    global l_name_editor
    global address_editor
    global age_editor
    global password_editor
    global fatherName_editor
    global city_editor
    global zipcode_editor


    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))

    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1)

    age_editor=Entry(editor,width=30)
    age_editor.grid(row=3,column=1,padx=20)

    password_editor=Entry(editor,width=30)
    password_editor.grid(row=4,column=1)

    fatherName_editor=Entry(editor,width=30)
    fatherName_editor.grid(row=5,column=1)

    city_editor=Entry(editor,width=30)
    city_editor.grid(row=6,column=1,padx=20)

    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=7,column=1)

    f_name_label=Label(editor,text='First Name',fg='white',bg='royal blue',font='tahoma')
    f_name_label.grid(row=0,column=0,pady=(10,0))

    l_name_label=Label(editor,text="Last Name",fg='white',bg='royal blue',font='tahoma')
    l_name_label.grid(row=1,column=0)

    address_label=Label(editor,text="Address",fg='white',bg='royal blue',font='tahoma')
    address_label.grid(row=2,column=0)

    age_label=Label(editor,text='Age',fg='white',bg='royal blue',font='tahoma')
    age_label.grid(row=3,column=0)

    password_label=Label(editor,text='Password',fg='white',bg='royal blue',font='tahoma')
    password_label.grid(row=4,column=0)

    fatherName_label=Label(editor,text='Father Name',fg='white',bg='royal blue',font='tahoma')
    fatherName_label.grid(row=5,column=0)



    city_lable=Label(editor,text="City",fg='white',bg='royal blue',font='tahoma')
    city_lable.grid(row=6,column=0)



    zipcode_label=Label(editor,text="Zipcode",fg='white',bg='royal blue',font='tahoma')
    zipcode_label.grid(row=7,column=0)

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        age_editor.insert(0,record[3])
        password_editor.insert(0,record[4])
        fatherName_editor.insert(0,record[5])

        city_editor.insert(0,record[6])
        
        zipcode_editor.insert(0,record[7])

    edit_btn=Button(editor,text="Save",command=update)
    edit_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=10)


    









f_name=Entry(light,width=30)
f_name.grid(row=0,column=1,padx=20)
f_name_Label=Label(light,text='First Name :',bg='royal blue',fg='white',font='tahoma')
f_name_Label.grid(row=0,column=0,pady=(10,0))

l_name=Entry(light,width=30)
l_name.grid(row=1,column=1)
l_name_label=Label(light,text='Last Name :',bg='royal blue',fg='white',font='tahoma')
l_name_label.grid(row=1,column=0)


address=Entry(light,width=30)
address.grid(row=2,column=1)
address_label=Label(light,text='Address :',bg='royal blue',fg='white',font='tahoma')
address_label.grid(row=2,column=0)



password=Entry(light,width=30,show='*')
password.grid(row=3,column=1)
password_label=Label(light,text='Password :',bg='royal blue',fg='white',font='tahoma')
password_label.grid(row=3,column=0)



age=Entry(light,width=30)
age.grid(row=4,column=1)
age_label=Label(light,text='Age :',bg='royal blue',fg='white',font='tahoma')
age_label.grid(row=4,column=0)




fatherName=Entry(light,width=30)
fatherName.grid(row=5,column=1)
fatherName_label=Label(light,text='Father Name :',bg='royal blue',fg='white',font='tahoma')
fatherName_label.grid(row=5,column=0)



city=Entry(light,width=30)
city.grid(row=6,column=1)
city_label=Label(light,text="City :",bg='royal blue',fg='white',font='tahoma')
city_label.grid(row=6,column=0)

zipcode=Entry(light,width=30)
zipcode.grid(row=7,column=1)
zipcode_label=Label(light,text='ZipCode :',bg='royal blue',fg='white',font='tahoma')
zipcode_label.grid(row=7,column=0)


delete_box=Entry(light,width=30)
delete_box.grid(row=11,column=1,pady=20)
delete_label=Label(light,text="Input ID",bg='royal blue',fg='white',font='tahoma')
delete_label.grid(row=11,column=0,pady=20)
# tasplab=Label(light,text='perform specific task click the button below*',fg='white',bg='royal blue')
# tasplab.grid(row=10,column=0)

sumbit_btn=Button(light,text='Add Records',command=submit)
sumbit_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=100)

query_btn=Button(light,text="Show Records",command=query)
query_btn.grid(row=9,column=1,columnspan=2,pady=10,padx=100)

delete_btn=Button(light,text='Delete',command=delete)
delete_btn.grid(row=14,column=0,columnspan=5,pady=10,padx=100,ipadx=1)

edit_btn=Button(light,text="Update",command=edit)
edit_btn.grid(row=14,column=2,columnspan=2,padx=10,pady=10,ipadx=10)

conn.commit()
conn.close()
light.mainloop()