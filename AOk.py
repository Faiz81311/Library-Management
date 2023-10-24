from tkinter import *
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
import datetime



class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        root.title("Library Managemnt System")
        root.geometry("1920x1080+0+0")


        #assign var to comm to the database
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()


























        #Title of the App
        lbltitle = Label(root,text = "LIBRARY MANAGEMENT SYSTEM", bg = "powder blue",fg = "green",bd = 20 ,relief="ridge"
                         ,font=("times new roman",50,"bold"),padx = 2, pady = 6)
        lbltitle.pack(side = TOP,fill = X)

        #The frame to hold Member and book details 
        frame = Frame(root,bd = 12 , relief=RIDGE,padx = 20 , bg = 'powder blue')
        frame.place(x = 0 , y =130 ,width = 1535,height = 400)

        #Data for the Membership info
        #============================================================================================================================================================================
        DataFrameLeft=LabelFrame(frame,text = "Library Membership Information", bg = "powder blue",fg = "green"
                                 ,bd = 12 ,relief="ridge",font=("times new roman",20,"bold"),padx = 2, pady = 6)
        DataFrameLeft.place(x = 0 , y = 5 , width = 900 , height = 360)

        #For the 'member type' written in black
        lblMember = Label(DataFrameLeft,text = "Member Type",bg = "powder blue",font=("times new roman",12,"bold"),padx = 2, pady = 6)
        lblMember.grid(row = 0 , column = 0,sticky=W)

        #For the combobox beside 'member type' in black
        comMember = ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.member_var,width =27,state = "readonly")
        comMember["value"] = ("Admin Staff","Student","Lecturer")
        comMember.grid(row = 0 , column = 1)

        #For the Label and Entries 

        #PRN_NO
        lblPRN_No = Label(DataFrameLeft,text = "PRN No:",bg = "powder blue",font=("arial",12,"bold"),padx = 2,pady = 5)
        lblPRN_No.grid(row = 1 , column = 0,sticky=W)
        textPRN_NO = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width = 29)
        textPRN_NO.grid(row=1 , column=1)

        #ID No
        lblTitle = Label(DataFrameLeft,text = "ID No:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblTitle.grid(row = 2 , column = 0,sticky=W)
        txtTitle = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width = 29)
        txtTitle.grid(row=2 , column=1)


        #Frist Name
        lblFirstName = Label(DataFrameLeft,text = "FirstName:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblFirstName.grid(row = 3 , column = 0,sticky=W)
        txtFirstName = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width = 29)
        txtFirstName.grid(row=3 , column=1)


        #Last name
        lblLastName = Label(DataFrameLeft,text = "LastName:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblLastName.grid(row = 4 , column = 0,sticky=W)
        txtLastName = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width = 29)
        txtLastName.grid(row=4 , column=1)



        #Address1
        lblAddress1 = Label(DataFrameLeft,text = "Address1:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblAddress1.grid(row = 5 , column = 0,sticky=W)
        txtAddress1 = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width = 29)
        txtAddress1.grid(row=5 , column=1)


        #Address2
        lblAddress2 = Label(DataFrameLeft,text = "Address2:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblAddress2.grid(row = 6 , column = 0,sticky=W)
        txtAddress2 = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width = 29)
        txtAddress2.grid(row=6 , column=1)


        #PostCode
        lblPostCode = Label(DataFrameLeft,text = "PostCode:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblPostCode.grid(row = 7 , column = 0,sticky=W)
        txtPostCode = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width = 29)
        txtPostCode.grid(row=7 , column=1)


        #Mobile
        lblMobile = Label(DataFrameLeft,text = "Mobile:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblMobile.grid(row = 8 , column = 0,sticky=W)
        txtMobile = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width = 29)
        txtMobile.grid(row=8 , column=1)



        #Book Id
        lblbookId = Label(DataFrameLeft,text = "Book ID:",bg = "powder blue",font=("arial",12,"bold"),padx = 2,pady = 5)
        lblbookId.grid(row = 0 , column = 2,sticky=W)
        textPRN_NO = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width = 29)
        textPRN_NO.grid(row=0 , column=3)

        #Book Title
        lblBookTitle = Label(DataFrameLeft,text = "Book Title:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblBookTitle.grid(row = 1 , column = 2,sticky=W)
        txlBookTitle = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width = 29)
        txlBookTitle.grid(row=1 , column=3)


        #Auther
        lblAuther = Label(DataFrameLeft,text = "Auther:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblAuther.grid(row = 2 , column = 2,sticky=W)
        txtAuther = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.auther_var,width = 29)
        txtAuther.grid(row=2 , column=3)


        #Date Borrowed
        lblDateBorrowed = Label(DataFrameLeft,text = "Date Borrowed:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblDateBorrowed.grid(row = 3 , column = 2,sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width = 29)
        txtDateBorrowed.grid(row=3 , column=3)



        #Date Due
        lblDateDue = Label(DataFrameLeft,text = "Date Due:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblDateDue.grid(row = 4 , column = 2,sticky=W)
        txtDateDue = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width = 29)
        txtDateDue.grid(row=4 , column=3)


        #Days On Book
        lblDaysOnBook = Label(DataFrameLeft,text = "Days On Book:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblDaysOnBook.grid(row = 5 , column = 2,sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook_var,width = 29)
        txtDaysOnBook.grid(row=5 , column=3)


        #Late Return Fine
        lblLateReturnFine = Label(DataFrameLeft,text = "Late Return Fine:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblLateReturnFine.grid(row = 6 , column = 2,sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lateratefine_var,width = 29)
        txtLateReturnFine.grid(row=6 , column=3)


        #Date Over Due
        lblDateOverDue = Label(DataFrameLeft,text = "Date Over Due:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblDateOverDue.grid(row = 7 , column = 2,sticky=W)
        txtDateOverDue = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable= self.dateoverdue_var,width = 29)
        txtDateOverDue.grid(row=7 , column=3)



        #Actual Price
        lblActualPrice = Label(DataFrameLeft,text = "Actual Price:",bg = "powder blue",font=("arial",12,"bold"),padx = 2, pady = 5)
        lblActualPrice.grid(row = 8 , column = 2,sticky=W)
        txtActualPrice = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice_var,width = 29)
        txtActualPrice.grid(row=8 , column=3)

        #============================================================================================================================================================================



        #Data for Book Details
        #============================================================================================================================================================================
 
        DataFrameright=LabelFrame(frame,text = "Book Details", bg = "powder blue",fg = "green",bd = 12 ,relief="ridge",font=("arial",20,"bold"),padx = 2, pady = 6)
        DataFrameright.place(x = 910 , y = 5 , width = 570 , height = 360 )

        #text box for all books names
        txtBox=Text(DataFrameright,font=("arial",12,"bold"),width = 32 , height = 15 , padx = 2 , pady = 6)
        txtBox.grid(row = 0 , column = 2)

        listScrollbar = Scrollbar(DataFrameright)
        listScrollbar.grid(row = 0,column=1,sticky="ns")

        #books names 
        listbooks = ['To Kill a Mockingbird', 'The Catcher in the Rye', 'Pride and Prejudice', '1984', 'The Great Gatsby', 'Brave New World',
                      'The Adventures of Huckleberry Finn', 'Animal Farm', 'The Picture of Dorian Gray', 'Fahrenheit 451']


        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value 
            if (x == "To Kill a Mockingbird"):
                self.bookid_var.set("MOCID35")
                self.booktitle_var.set("To Kill a Mockingbird")
                self.auther_var.set("Harper Lee")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")

            elif (x == "The Catcher in the Rye"):
                self.bookid_var.set("TCIT34ID")
                self.booktitle_var.set("The Catcher in the Rye")
                self.auther_var.set("J. D. Salinge")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")

            elif (x == "Pride and Prejudice"):
                self.bookid_var.set("PRAPR356ID")
                self.booktitle_var.set("Pride and Prejudice")
                self.auther_var.set("Jane Austen")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")

            elif (x == "1984"):
                self.bookid_var.set("NEF84ID")
                self.booktitle_var.set("1984")
                self.auther_var.set("George Orwell")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")

            elif (x == "The Great Gatsby"):
                self.bookid_var.set("TGG874ID")
                self.booktitle_var.set("The Great Gatsby")
                self.auther_var.set("F. Scott Fitzgerald")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")

            elif (x == "Brave New World"):
                self.bookid_var.set("BNW874ID")
                self.booktitle_var.set("Brave New World")
                self.auther_var.set("Aldous Huxley")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")

            elif (x == "The Adventures of Huckleberry Finn"):
                self.bookid_var.set("TAOHF74ID")
                self.booktitle_var.set("The Adventures of Huckleberry Finn")
                self.auther_var.set("Mark Twain")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")

            elif (x == "Animal Farm"):
                self.bookid_var.set("AF784ID")
                self.booktitle_var.set("Animal Farm")
                self.auther_var.set("George Orwell")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")

            elif (x == "The Picture of Dorian Gray"):
                self.bookid_var.set("TPODG47ID")
                self.booktitle_var.set("The Picture of Dorian Gray")
                self.auther_var.set("Oscar Wilde")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")

            elif (x == "Fahrenheit 451"):
                self.bookid_var.set("FF5839ID")
                self.booktitle_var.set("Fahrenheit 451")
                self.auther_var.set("Ray Bradbury")
                d1 =datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs788")



        listBox = Listbox(DataFrameright,font=("arial",12,"bold"),width = 20 , height = 15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row = 0 ,column = 0,padx = 4) 
        listScrollbar.config(command=listBox.yview)


        #inserting books into the text box

        for item in listbooks:
            listBox.insert(END,item)
        



        

        #Frames for buttons 
        #============================================================================================================================================================================
        Framebutton = Frame(root,bd = 12 , relief=RIDGE,padx = 20 , bg = 'powder blue')
        Framebutton.place(x = 0 , y =530 ,width = 1535,height = 70)


        btnAddData = Button(Framebutton,text="Add Data",font=("arial",12,"bold"),command=self.add_data,width = 23 , bg = 'blue',fg = 'white')
        btnAddData.grid(row = 0 , column = 0,padx = 20)


        btnShowData = Button(Framebutton,text="show Data",font=("arial",12,"bold"),width = 23 , bg = 'blue',fg = 'white')
        btnShowData.grid(row = 0 , column = 1,padx = 20)


        btnUpdateData = Button(Framebutton,text="Update",font=("arial",12,"bold"),width = 23 , bg = 'blue',fg = 'white')
        btnUpdateData.grid(row = 0 , column = 2,padx = 20)


        btnDeleteData = Button(Framebutton,text="Delete",font=("arial",12,"bold"),width = 23 , bg = 'blue',fg = 'white')
        btnDeleteData.grid(row = 0 , column = 3,padx = 20)


        btnResetData = Button(Framebutton,text="Reset",font=("arial",12,"bold"),width = 23 , bg = 'blue',fg = 'white')
        btnResetData.grid(row = 0 , column = 4,padx = 20)


        btnExitData = Button(Framebutton,text="Exit",font=("arial",12,"bold"),width = 23 , bg = 'blue',fg = 'white')
        btnExitData.grid(row = 0 , column = 4,padx = 20)




        #Frame for database
        #============================================================================================================================================================================
 
        FrameDetails = Frame(root,bd = 12 , relief=RIDGE,padx = 20 , bg = 'powder blue')
        FrameDetails.place(x = 0 , y =600 ,width = 1535,height = 240)

        #for the table
        Table_frame = Frame(FrameDetails,bd = 6,relief=RIDGE,bg = "powder blue")
        Table_frame.place(x = 0 , y = 2 , width = 1460 , height = 190)


        xscroll = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        library_table =ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname",
                                                        "address1","address2","postid","mobile","bookid",
                                                        "booktitle","auther","dateborrowed","datedue","days",
                                                        "latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side = BOTTOM,fill = X)
        yscroll.pack(side = RIGHT,fill = Y)

        xscroll.config(command=library_table.xview)
        yscroll.config(command=library_table.yview)

        library_table.heading("membertype",text="Member Type")
        library_table.heading("prnno",text="PRN NO")
        library_table.heading("title",text="Title")
        library_table.heading("firstname",text="First Name")
        library_table.heading("lastname",text="Last Name")
        library_table.heading("address1",text="Address1")
        library_table.heading("address2",text="Address2")
        library_table.heading("postid",text="Post ID")
        library_table.heading("mobile",text="Mobile Number")
        library_table.heading("bookid",text="Book ID")
        library_table.heading("booktitle",text="Book Title")
        library_table.heading("auther",text="Auther")
        library_table.heading("dateborrowed",text="Date Borrowed")
        library_table.heading("datedue",text="Date Due")
        library_table.heading("days",text="Days On Book")
        library_table.heading("latereturnfine",text="Late Return Fine")
        library_table.heading("dateoverdue",text="Date Over Due")
        library_table.heading("finalprice",text="Final Price")


        library_table["show"] = "headings"
        library_table.pack(fill=BOTH,expand = 1)

        #To make each column the size of 100 
        library_table.column("membertype",width = 100)
        library_table.column("prnno",width = 100)
        library_table.column("title",width = 100)
        library_table.column("firstname",width = 100)
        library_table.column("lastname",width = 100)
        library_table.column("address1",width = 100)
        library_table.column("address2",width = 100)
        library_table.column("postid",width = 100)
        library_table.column("mobile",width = 100)
        library_table.column("bookid",width = 100)
        library_table.column("booktitle",width = 100)
        library_table.column("auther",width = 100)
        library_table.column("dateborrowed",width = 100)
        library_table.column("datedue",width = 100)
        library_table.column("days",width = 100)
        library_table.column("latereturnfine",width = 100)
        library_table.column("dateoverdue",width = 100)
        library_table.column("finalprice",width = 100)




    
    def add_data(self):
        conn = mysql.connector.connect(host = "localhost",user ="root",password="1234",database ="test")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library (Member,PRN_NO,ID,FirstName,LastName,Address1,Address2,PostId,Mobile,BookId,Booktitle,Auther,Dateborrowed,datedue,dayasofbook,latereturnfine,dateoverdue,finalprice) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                       self.member_var.get(),
                                                        self.prn_var.get(),
                                                        self.id_var.get(),
                                                        self.firstname_var.get(),
                                                        self.lastname_var.get(),
                                                        self.address1_var.get(),
                                                        self.address2_var.get(),
                                                        self.postcode_var.get(),
                                                        self.mobile_var.get(),
                                                        self.bookid_var.get(),
                                                        self.booktitle_var.get(),
                                                        self.auther_var.get(),
                                                        self.dateborrowed_var.get(),
                                                        self.datedue_var.get(),
                                                        self.daysonbook_var.get(),
                                                        self.lateratefine_var.get(),
                                                        self.dateoverdue_var.get(),
                                                        self.finalprice_var.get() 
                                                                            ))
        conn.commit()
 
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

    



#main func
if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()        