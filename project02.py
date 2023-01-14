from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Mangment System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar
        self.Dose=StringVar
        self.Noooftablets=StringVar
        self.lot=StringVar
        self.Issuedate=StringVar
        self.ExpDate=StringVar
        self.DailyDose=StringVar
        self.SideEfect=StringVar
        self.FurtherInformation=StringVar
        self.Storage=StringVar
        self.DrivingUsingMachine=StringVar
        self.HowToUseMedication=StringVar
        self.PatientName=StringVar
        self.DateOfBirth=StringVar
        self.PatientAddress=StringVar
        self.BloodPressuer=StringVar
        self.PatientId=StringVar
        self.NhsNumber=StringVar


        lbltitle=Label(self.root, bd=20, relief=RIDGE, text="Hospital Mangment System", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP,fill=X)
        #================================================Data fream======================================================================================

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        Dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,font=("arial",10,"bold"),text="patient Information")
        Dataframeleft.place(x=0,y=5,width=980,height=350)

        DataframeRight= LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=20, font=("arial", 10, "bold"),
                                   text="Priescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        #=======================================================================================================================================================

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        #=======================================================================================================================================================

        Detailframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailframe.place(x=0, y=600, width=1530, height=190)
#=======================================================================================================================================================
        lblNameTablet=Label(Dataframeleft,text="Names Of Tablet",font=("time new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.Combobox(Dataframeleft,textvariable=self.Nameoftablets,state="readonly",font=("arial",12,"bold"),width=33)
        comNameTablet['value']=('nice','corona vacacine','acetaminophen','adderall','amlodipine','ativan')
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(Dataframeleft, font=("arial", 12, "bold"),text="Refernce No",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        texref=Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.ref,width=35)
        texref.grid(row=1, column=1)

        lblDose = Label(Dataframeleft, font=("arial", 12, "bold"), text="Dose", padx=2,pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        texDose = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.Dose, width=35)
        texDose.grid(row=2, column=1)

        lblNoOfTablets = Label(Dataframeleft, font=("arial", 12, "bold"), text="No Of Tablets", padx=2,pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        texNoOfTablets = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable= self.Noooftablets,width=35)
        texNoOfTablets.grid(row=3, column=1)

        lblLot = Label(Dataframeleft, font=("arial", 12, "bold"), text="Lot", padx=2,pady=8)
        lblLot.grid(row=4, column=0, sticky=W)
        texLot = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.lot, width=35)
        texLot.grid(row=4, column=1)

        lblIssueDate = Label(Dataframeleft, font=("arial", 12, "bold"), text="Issue Date", padx=2,pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        texIssueDate = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.Issuedate, width=35)
        texIssueDate.grid(row=5, column=1)

        lblExpDate = Label(Dataframeleft, font=("arial", 12, "bold"), text="Exp Date", padx=2,pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        texExpDate = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.ExpDate, width=35)
        texExpDate.grid(row=6, column=1)

        lblDailyDose = Label(Dataframeleft, font=("arial", 12, "bold"), text="Daily Dose", padx=2,pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        texDailyDose = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.DailyDose, width=35)
        texDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(Dataframeleft, font=("arial", 12, "bold"), text="Side Effect", padx=2,pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        texSideEffect = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.SideEfect, width=35)
        texSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(Dataframeleft, font=("arial", 12, "bold"), text="Further info", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        texFurtherinfo = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.FurtherInformation,width=35)
        texFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(Dataframeleft, font=("arial", 12, "bold"), text="Blood Pressure", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        texBloodPressure = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.BloodPressuer, width=35)
        texBloodPressure.grid(row=1, column=3)

        lblStorage = Label(Dataframeleft, font=("arial", 12, "bold"), text="Storage", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        texStorage= Entry(Dataframeleft, font=('arial', 13, 'bold'), width=35)
        texStorage.grid(row=2, column=3)

        lblMedicine = Label(Dataframeleft, font=("arial", 12, "bold"), text="Medicine", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        texMedicine = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.HowToUseMedication, width=35)
        texMedicine.grid(row=3, column=3)

        lblPatientId = Label(Dataframeleft, font=("arial", 12, "bold"), text="Patient Id", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        texPatientId= Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.PatientId, width=35)
        texPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(Dataframeleft, font=("arial", 12, "bold"), text="NhsNumber", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        texNhsNumber = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.NhsNumber, width=35)
        texNhsNumber.grid(row=5, column=3)

        lblPtieantName = Label(Dataframeleft, font=("arial", 12, "bold"), text="Ptieant Name", padx=2, pady=6)
        lblPtieantName.grid(row=6, column=2, sticky=W)
        texPtieantName = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.PatientName, width=35)
        texPtieantName.grid(row=6, column=3)

        lblDateOfBirth = Label(Dataframeleft, font=("arial", 12, "bold"), text="Date Of Birth", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        texDateOfBirth = Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.DateOfBirth, width=35)
        texDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(Dataframeleft, font=("arial", 12, "bold"), text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        texPatientAddress= Entry(Dataframeleft, font=('arial', 13, 'bold'),textvariable=self.PatientAddress, width=35)
        texPatientAddress.grid(row=8, column=3)


        self.texPrescription=Text(DataframeRight,font=("arial", 12, "bold"),width=45,height=16,padx=2,pady=6)
        self.texPrescription.grid(row=0,column=0)

        btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23)
        btnPrescription.grid(row=0,column=1)

        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=23)
        btnPrescriptionData.grid(row=0,column=2)

        btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23)
        btnUpdate.grid(row=0,column=3)

        btnDelete = Button(Buttonframe,command=self.idelete,text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=23)
        btnDelete.grid(row=0, column=4)

        btnReset = Button(Buttonframe,command=self.clear, text="Reset", bg="green", fg="white", font=("arial", 12, "bold"), width=23)
        btnReset.grid(row=0, column=5)

        btnExit = Button(Buttonframe,command=self.iExit, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23)
        btnExit.grid(row=0, column=6)


        Scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        Scroll_Y= ttk.Scrollbar(Detailframe, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailframe,columns=("nameoftable","ref",'dose','nooftablets','lot','issuedate'
                                                              ,'expdate','dailydose','storage','NHSnumber','pname','dob','address'),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_Y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_Y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading('nameoftable',text="Name Of Table")
        self.hospital_table.heading('ref',text='Reference No.')
        self.hospital_table.heading('dose',text='Dose')
        self.hospital_table.heading("nooftablets",text='No Of Tabletes')
        self.hospital_table.heading('lot',text='Lot')
        self.hospital_table.heading('issuedate',text='Issue Date')
        self.hospital_table.heading('expdate',text='exp Date')
        self.hospital_table.heading('dailydose',text='Daily Dose')
        self.hospital_table.heading('storage',text='Storage')
        self.hospital_table.heading('NHSnumber',text='NHS Number')
        self.hospital_table.heading('pname',text='Patient Name')
        self.hospital_table.heading('dob',text='DOB')
        self.hospital_table.heading('address',text='Address')

        self.hospital_table['show']='headings'

        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.column('nameoftable',width=100)
        self.hospital_table.column('ref',width=100)
        self.hospital_table.column('dose',width=100)
        self.hospital_table.column('nooftablets',width=100)
        self.hospital_table.column('lot',width=100)
        self.hospital_table.column('issuedate',width=100)
        self.hospital_table.column('expdate',width=100)
        self.hospital_table.column('dailydose',width=100)
        self.hospital_table.column('storage',width=100)
        self.hospital_table.column('NHSnumber',width=100)
        self.hospital_table.column('pname',width=100)
        self.hospital_table.column('dob',width=100)
        self.hospital_table.column('address',width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind('<ButtonRelease-1>',self.get_cursor)


        self.fatch_data()
#======================================================================================================================
    def iPrescriptionData(self):
        if self.Nameoftablets.get()==""or self.ref.get()=="":
            messagebox.showerror('Error','All fields are requried')
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='muydata')
            my_cursor=conn.cursor()
            my_cursor.execute('insert into Hospital value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                  self.Nameoftablets.get(),
                                                                                                  self.ref.get(),
                                                                                                  self.Dose.get(),
                                                                                                  self.Nameoftablets.get(),
                                                                                                  self.lot.get(),
                                                                                                  self.Issuedate.get(),
                                                                                                  self.ExpDate.get(),
                                                                                                  self.DailyDose.get(),
                                                                                                  self.Storage.get(),
                                                                                                  self.NhsNumber.get(),
                                                                                                  self.PatientName.get(),
                                                                                                  self.DateOfBirth.get(),
                                                                                                  self.PatientAddress.get()
                                                                                                  ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo('Sucess','Record has been inserted')


    def update(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='test@123', database='muydata')
        my_cursor = conn.cursor()
        my_cursor.execute('update hospital set Nameoftable=%s,Dose=%s,Nooftablets=%s,lot=%s,IssueDate=%s,ExpDate=%s,DailyDose=%s,Storage=%s,NhsNumber=%s,PatientName=%s,'
                          'DateOfBirth=%s,PatientAddress=%s'),(

                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.lot.get(),
                                                                                                    self.Issuedate.get(),
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.Storage.get(),
                                                                                                    self.NhsNumber.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.PatientAddress.get()
                                                                                                    )
        conn.commit()



    def fatch_data(self):

        conn=mysql.connector.connect(host='localhost',username='Hospital',password='Test@123',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("select=from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        curses_row=self.hospital_table.focus()
        content=self.hospital_table.item(curses_row)
        row=content['values']
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.Noooftablets.set(row[3])
        self.lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.Storage.set(row[8])
        self.NhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])


    def iprectioption(self):
        self.texPrescription.insert(END,'name of Tablets:\t\t\t'+self.Nameoftablets.get()+'\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')
        self.texPrescription.insert(END, 'name of Tablets:\t\t\t' + self.Nameoftablets.get() + '\n')

    def idelete(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='test@123', database='muydata')
        my_cursor = conn.cursor()
        query='delete from hospital where Refrence_No=%s'
        value=(self.ref.get(),)
        my_cursor.execute(query,value)


        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo('Delete','Patient has been deleted successfully')

    def clear(self):
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")
        self.Nameoftablets.set("")

    def iExit(self):
        iExit=messagebox.askyesno('Hospital mangment system','confirm yoy want to exit')
        if iexit>0:
            root.destroy()
            return




root=Tk()
O=Hospital(root)
root.mainloop()