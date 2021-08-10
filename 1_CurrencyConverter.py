#Tkinter is the inbuilt python module that is used to create GUI applications
from tkinter import *   # * is used to import everything from that module

class CurrencyConverter:  # : helps in indenting the code
    def __init__(self):
        window = Tk() #tk() creates a top level window object to house our application.It is a component of the Tkinter module.
        window.title("Currency Converter")
        window.configure(bg="yellow")

        #Adding label widgets to application window
        Label(window,bg="yellow",font=("Helvetica 12 bold"),text="Amount to Convert").grid(row=1, column=1, sticky=W )
        Label(window,bg="yellow",font=("Helvetica 12 bold"),text="Conversion rate").grid(row=2, column=1, sticky=W)
        Label(window,bg="yellow",font=("Helvetica 12 bold"),text="Converted amount").grid(row=3, column=1, sticky=W)

        #Creating objects and add Entry function
        self.amounttoconvertvar=StringVar() #stringvar is a predefined class in tkinter module.Used to monitor changes in tkinter variable.
        Entry(window, textvariable= self.amounttoconvertvar,justify= RIGHT).grid(row= 1, column= 2) #Entry function is used to take input form the user
        self.conversionRateVar = StringVar()       
        Entry(window, textvariable= self.conversionRateVar,justify= RIGHT).grid(row= 2, column= 2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount = Label(window,bg="yellow",font=("Helvetica 12 bold"),textvariable=self.convertedAmountVar).grid(row= 3, column=2,sticky = E)

        #Creating Convert and clear buttons.When they will be clicked they will call their respective functions

        btConvertedAmount = Button(window,font=("Helvetica 12 bold"), text="Convert",bg="blue",fg="white",command= self.ConvertedAmount).grid(row=4,column=2,sticky= E)
        #fg stands for foreground color--means color of the text
        btdelete_all = Button(window, font=("Helvetica 12 bold"),text= "Clear",bg="red",fg="white",command = self.delete_all).grid(row=4,column=6,padx=25,pady=25,sticky=E)

        window.mainloop()  # Runs the application Program

    #Functions to do the conversion.Stores input and performs Conversion
    def ConvertedAmount(self):
        amt= float(self.conversionRateVar.get())
        convertedAmountVar = float(self.amounttoconvertvar.get())*amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f')) #setting value upto 2 decimal places

    #Function to clear inputs
    def delete_all(self):
        self.amounttoconvertvar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")

CurrencyConverter()
