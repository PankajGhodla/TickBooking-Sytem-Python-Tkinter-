import tkinter as tk                # impoting tkinter as tk into the program
from tkinter import *               # impoting tkinter into the program
from tkinter import font  as tkfont # importing fonts into the program
import re                           # importing re into the program
from tkinter import messagebox      # importing messagebox into the program


    
class SampleApp(tk.Tk): 

    def __init__(self):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame("StartPage")#StartPage is displayed when the program is opened

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame): #StartPage class contains content of the first page
            
    def __init__(self, parent, controller):
        
        def check():    #checks the number of seats available 
            txtdisplay1.configure(state='normal')   #allows the text to input/output
            for k,v in flight_Number.items():
                v=70-v
                flight=str(k)+' Available: '  + str(v)
                txtdisplay1.insert(tk.END,'\n'+flight)
            txtdisplay1.configure(state='disabled') #disallows the text to input/output
            
        def clear1():    #clears all the text in the textdisplay1 field
            txtdisplay1.configure(state='normal')   #allows the text to input/output
            txtdisplay1.delete('1.0', tk.END)
            txtdisplay1.configure(state='disabled') #disallows the text to input/output

            
        def Validation():   #validate the data entered by the user
            
            valid = False

            if len(entry_FN.get()) == 0:    #checks whether first name entry box is empty or not
                messagebox.showinfo("Error", "Please enter First Name") #notifies the user if the first name entry box is empty
            elif  entry_FN.get().isalpha() == False:
                messagebox.showinfo("Error", "First name can only contain Alphabets")   #notifies the use if the first name don't contain only alphabets
                
            if len(entry_LN.get()) == 0:    #checks whether last name entry box is empty or not
                messagebox.showinfo("Error", "Please enter Last Name")  #notifies the user if the last name entry box is empty
            elif  entry_LN.get().isalpha() == False:
                messagebox.showinfo("Error", "Last name can only contain Alphabets")   #notifies the use if the lastname name don't contain only alphabets

            if re.search("[@]", entry_Email.get()): #checks whether there is the symbal '@' in the email address
                if re.search("[.]", entry_Email.get()): #checks whether there is the symbal '.' in the email address
                    valid = True    #valid is set to True if the entered email is valid
                else:
                    messagebox.showinfo("Error", "Please enter an valid Email address") #notifies the user if the email doesn't contain symbol  "." , i.e the emial is invalid
            else:
                messagebox.showinfo("Error", "Please enter an valid Email address") #notifies the user if the email doesn't contain symbol "@" or "." or both , i.e the emial is invalid
                
            if len(flightvar.get()) == 0:   #checks whether the user has selected an flight or not
                messagebox.showinfo("Error", "Please Choose Flight")    #notifies  the user if they hasn't selected a flight

            if len(passengervar.get()) == 0:    #checks whether the user has selected the number of passenger or not
                messagebox.showinfo("Error", "Please select the Number of Passenger(s)")   #notifies  the user if they hasn't selected the number of passengers

            if len(passengervar.get()) != 0 and len(flightvar.get()) != 0:
                if (flight_Number[flightvar.get()])+ int(passengervar.get()) > 70: #checks whether the number of seats/passengers booked are over 70 or not
                    messagebox.showinfo("Error", "This many tickets are Not Available. \n"+ str( 70 - flight_Number[flightvar.get()]) +" seat(s) is/are available for the flight: "+ str(flightvar.get())) #notifes the user if the number of seats/passenger booked exceed 70 


            if len(entry_FN.get()) != 0 and entry_FN.get().isalpha() == True and entry_LN.get().isalpha() == True and len(entry_LN.get()) != 0 and valid != False and len(flightvar.get()) != 0 and len(passengervar.get()) != 0 and (flight_Number[flightvar.get()])+ int(passengervar.get()) <= 70:
                buttonToPageTwo.invoke() #involes the Button 'buttonToPageTwo', if the user has enerted all the fields data correctly

                
        tk.Frame.__init__(self, parent)
        self.controller = controller        

        global entry_FN
        global entry_LN
        global entry_Email
        global flightvar
        global passengervar
        global txtdisplay1
        global flight_Number

        
        
        frameHeading = tk.Frame(self)   #makes the header for the heading
        frameHeading.grid(row=0, columnspan=3)  
        heading = tk.Label(frameHeading, text="Flight Booking System", fg="white", bg="#2a69c9", height="2", width="22")    #Label for the header of the program    
        heading.config(font=("",30))    #sets the font for heading
        heading.grid(row=0,columnspan=2)    #add the header label into the frame 
        
        
        label_FN = tk.Label(self, text="First Name: ",font=("",15)) #Label for first name   
        label_FN.grid(row=1, column=0, pady=6)  #add the first name label to the of the page one
        entry_FN = tk.Entry(self, font=("",15)) #Entry box forFirst name 
        entry_FN.grid(row=1, column=1, pady=6)
        entry_FN.focus_force()  #sets the focus on the first name entry box


        label_LN = tk.Label(self, text="Last Name: ",font=("",15))  #label for last name
        label_LN.grid(row=2, column=0, pady=6)
        entry_LN = tk.Entry(self, font=("",15)) #Entry box for last name
        entry_LN.grid(row=2, column=1, pady=6)

        label_Email = tk.Label(self, text="Email Address: ",font=("",15))   #label for Email
        label_Email.grid(row=3, column=0, pady=6)
        entry_Email = tk.Entry(self, font=("",15))  #Entry box for email
        entry_Email.grid(row=3, column=1, pady=6)
            
        label_flight = tk.Label(self, text="Choose flight: ",font=("",15))  #label for flight Number
        label_flight.grid(row=4, column=0, pady=6)    
        flight_Number = {'NZ345':0, 'NZ346':0, 'NZ347':0, 'NZ348':0} #Array of flight available
        flightvar = tk.StringVar(self)  #flightvar is set as a string
        flightvar.set('') # set the default option
        popupMenu_Flight = tk.OptionMenu(self, flightvar, *flight_Number)   #popup menu for the entry of the flight number
        popupMenu_Flight.configure(font=("",15), width=17)  #configuring the width and the font of the popup menu
        popupMenu_Flight.grid(row=4, column=1, pady=6)

        label_passenger = tk.Label(self, text="No of Passenger(s): ",font=("",15))    #label for the number of passenger(s)
        label_passenger.grid(row=5, column=0, pady=6)
        passenger_Number = {1,2,3,4,5,6,7,8,9,10}   #list for the nuber of passenger(s)
        passengervar = tk.StringVar(self)   #sets the passengervar as string
        passengervar.set('') # set the default option
        popupMenu_passenger = tk.OptionMenu(self, passengervar, *passenger_Number) #popup menu for the entry of the passenger(s)
        popupMenu_passenger.configure(font=("",15), width=17)  #configuring the width and the font of the popup menu
        popupMenu_passenger.grid(row=5, column=1, pady=6)
        
        Button_Status= tk.Button(self, text="Flight Status",width="10",height="1", font=("",15), command=check) #Button to check the status of flights
        Button_Status.grid(row=6, column=0, pady=10,  padx=4)
        Button_Clear= tk.Button(self, text="Clear",width="7",height="1", font=("",15), command=clear1)   #Button to clear the text in the text field
        Button_Clear.grid(row=6, column=1, pady=10, sticky='E')
        
        txtdisplay1= tk.Text(self, width=57, height=15)   #text display to show the number of seats availabel in each flight
        txtdisplay1.grid(row=7, column=0, columnspan=3)
        txtdisplay1.configure(state='disabled') #configures the status of text display to disabled, so that the user can't enter data in the text field

        Button_next= tk.Button(self, text="Next",width="7",height="1", font=("",15), command = Validation)  #Button to go to the next and validates the inputed fileds 
        Button_next.grid(row=8, column=1, pady=10, sticky='E')

        Page_One = tk.Label(self, text="Page 1", font=("",10)).grid(row=9, column=1, sticky='E')    #label shows the page number
        buttonToPageTwo = tk.Button(self, text="", command=lambda: controller.show_frame("PageTwo"))    #Button when called opens the  frame 'PageTwo'
     
        

        
class PageTwo(tk.Frame):


    def __init__(self, parent, controller): 
        def Calc(): #Calculates the price for the ticket, for the selected numnber of passenger and it also validates the fields

            txtdisplay2.configure(state='normal')   #configures the status of text display to normal, so that the text field can be edited
           
            if int(Adultvar.get()) == 0:
                messagebox.showinfo("Error", "Please select atleast one Adult") #shows error message if the number of adult entered is zero
            else:
                if int(passengervar.get()) == ( int(Adultvar.get()) + int(Childrenvar.get()) + int(Infantvar.get())):  #check whether the number of passenger adds up to adult(s)+ children(s) + infant(s)
                    
                    txtdisplay2.insert(tk.END,"\n==============================================")
                    txtdisplay2.insert(tk.END, "\nNumber of Pasenger:" + str(passengervar.get()))  #Prints the number of passengers onto the text fiels
                    txtdisplay2.insert(tk.END,"\nNumber of Adult(s):" + str(Adultvar.get()))   #Prints the number of Adult(s) onto the text fiels
                    txtdisplay2.insert(tk.END,"\nNumber of Children(s):" + str(Childrenvar.get()))  #Prints the number of children(s) onto the text fiels
                    txtdisplay2.insert(tk.END,"\nNumber of Infant(s):" + str(Infantvar.get()))  #Prints the number of Infant(s) onto the text fiels
                    
                    cost = (int(Adultvar.get())*84*1.15) + (int(Childrenvar.get())*40*1.15) #calculates the cost for the ticket
                    txtdisplay2.insert(tk.END,"\n==============================================")
                    txtdisplay2.insert(tk.END,"\nCost: $" +str(round(cost,2)))  #prints the cost in the text field
                    txtdisplay2.insert(tk.END,"\n==============================================")
                    txtdisplay2.insert(tk.END,"\nCost for Adult: $ 96.6 *Including GST")    #prints the cost for adults in the text field
                    txtdisplay2.insert(tk.END,"\nCost for Children: $ 46 *Including GST")   #prints the cost for children in the text field
                    txtdisplay2.insert(tk.END,"\nCost for Infant: Free")                    #prints the cost for infant in the text field
                elif int(passengervar.get()) > ( int(Adultvar.get()) + int(Childrenvar.get()) + int(Infantvar.get())):     #check whether the number of passengers(s) is greater than  adult(s)+ children(s) + infant(s)
                     messagebox.showinfo("Error", "You have choosen less passengers than selected. \n") #shows the message if the able statement is true
                else:
                    messagebox.showinfo("Error", "You have choosen more passengers than selected. \n")  #show this message if the both above statement is false
                
            txtdisplay2.configure(state='disabled') #configures the status of text display to disabled, so the user cannot enter data in the text field

            
        def Confirm():  #Confirm the ticker and takes the user to the next page(PageThree)

            if int(Adultvar.get()) == 0:    #checks whether the number of adult equal zero or not
                messagebox.showinfo("Error", "Please select atleast one Adult")
            else:
                if int(passengervar.get()) == ( int(Adultvar.get()) + int(Childrenvar.get()) + int(Infantvar.get())):  #check whether the number of passenger adds up to adult(s)+ children(s) + infant(s)
                    loadPageThree = 1
                    buttonToPageThree.invoke()
                    
                elif int(passengervar.get()) > ( int(Adultvar.get()) + int(Childrenvar.get()) + int(Infantvar.get())): #check whether the number of passengers(s) is greater than  adult(s)+ children(s) + infant(s)
                     messagebox.showinfo("Error", "You have choosen less passengers than you selected on the page one. \n") #shows the message if the able statement is true
                else:
                    messagebox.showinfo("Error", "You have choosen more passengers than you selected on the page one. \n")  #show this message if the both above statement is false
        def clear2():    #clears all the text in the textdisplay1 field
            txtdisplay2.configure(state='normal')   #allows the text to input/output
            txtdisplay2.delete('1.0', tk.END)
            txtdisplay2.configure(state='disabled') #disallows the text to input/output

            
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global Adultvar
        global Childrenvar
        global Infantvar
        global txtdisplay2

        frameHeading = tk.Frame(self)   #makes the header for the heading
        frameHeading.grid(row=0, columnspan=3)  
        heading = tk.Label(frameHeading, text="Flight Booking System", fg="white", bg="#2a69c9", height="2", width="22")    #Label for the header of the program    
        heading.config(font=("",30))    #sets the font for heading
        heading.grid(row=0,columnspan=2)    #add the header label into the frame


        label_Adult = tk.Label(self, text="Number of Adults: ",font=("",15))    #label for number of adult(s)
        label_Adult.grid(row=5, column=0, pady=6)
        Adult_Number = {0,1,2,3,4,5,6,7,8,9,10} #list of number of adult(s)
        Adultvar = tk.StringVar(self)   #sets the adultvar as string
        Adultvar.set(0) #sets the default number of adult to zero
        popupMenu_Adult = tk.OptionMenu(self, Adultvar, *Adult_Number)  #popup menu to enter the number of adult
        popupMenu_Adult.configure(font=("",15), width=17)   #configures the font and width of the popup menu
        popupMenu_Adult.grid(row=5, column=1, pady=6)
        Adultlimit = tk.Label(self, text="*Adult should be above 14 years old")
        Adultlimit.grid(row=6, column=1, sticky='W')
        popupMenu_Adult.focus_force()

        label_Children = tk.Label(self, text="Number of Childrens: ",font=("",15))  #label for the number of children(s)
        label_Children.grid(row=7, column=0, pady=6)
        Children_Number = {0,1,2,3,4,5,6,7,8,9,10}  #list for the number of children(s)
        Childrenvar = tk.StringVar(self)    #sets the childrenvar as string
        Childrenvar.set(0)  #sets the default number of children to zero 
        popupMenu_Children = tk.OptionMenu(self,Childrenvar, *Children_Number)  #popup menu to enter the number of children(s)
        popupMenu_Children.configure(font=("",15), width=17)    #configures the font and width of the popup menu
        popupMenu_Children.grid(row=7, column=1, pady=6)
        Childrenlimit = tk.Label(self, text="*Children are between 2 and 14 years old inclusive")
        Childrenlimit.grid(row=8, column=1, sticky='W')

        label_Infants = tk.Label(self, text="Number of Infants: ",font=("",15)) #label for the number of infant(s)
        label_Infants.grid(row=9, column=0, pady=6)
        Infant_Number = {0,1,2,3,4,5,6,7,8,9,10}    #list for the number of infant(s)
        Infantvar = tk.StringVar(self)   #sets the infantvar as string
        Infantvar.set(0)    #sets the default number of infant to zero
        popupMenu_Infant = tk.OptionMenu(self, Infantvar, *Infant_Number)   #popup menu to enter the number of infant(s)
        popupMenu_Infant.configure(font=("",15), width=17)  #configures the font and width of the popup menu
        popupMenu_Infant.grid(row=9, column=1, pady=6)
        Infantlimit = tk.Label(self, text="*Infant are below 2 years old")
        Infantlimit.grid(row=10, column=1, sticky='W')

        Button_Clear= tk.Button(self, text="Clear",width="7",height="1", font=("",15), command=clear2)
        Button_Clear.grid(row=11, column=0, pady=6, padx=50, sticky='W')
        
        Button_Calculate = tk.Button(self, text="Calculate",width="8",height="1", font=("",15),
                                     command=Calc).grid(row=11, column=1, pady=6, padx=15, sticky='E')   #button calculates the price for the selected number of passenger(s)

        txtdisplay2=tk.Text(self,width=57,height=15)    #text field to show the price 
        txtdisplay2.grid(row=12, column=0, columnspan=3)
        txtdisplay2.configure(state='disabled')     #configures the status of text display to disabled, so the user cannot enter data in the text field

        Button_back = tk.Button(self, text="Back", width="7",height="1", font=("",15), command=lambda: controller.show_frame("StartPage"))
        Button_back.grid(row=13, column=0, pady=6, padx=50, sticky='W')  #Button that takes the user back to the start page, if they want to change something or entered soemthing wrong
        Button_Confirm = tk.Button(self, text="Confirm",width="8",height="1", font=("",15), command=Confirm)
        Button_Confirm.grid(row=13, column=1, pady=6, padx=15, sticky='E') #Confirm the ticket and takes the user to the next page, if there are no errors

        buttonToPageThree = tk.Button(self, text="", command=lambda: controller.show_frame("PageThree"))    #takes the uer to the next page(pageThree) when the button is invoked 

        Page_Two = tk.Label(self, text="Page 2", font=("",10)).grid(row=14, column=1, sticky='E')   #label shows the page number

class PageThree(tk.Frame):

    def __init__(self, parent, controller):

        def PrintTicket():  #prints the ticket and the price paid
            
            txtdisplay3.configure(state='normal')
            txtdisplay3.insert(tk.END,"\n==============================================")
            txtdisplay3.insert(tk.END,"\nFull Name: " + entry_FN.get() + " " + entry_LN.get()) #print first and last name in the text field
            txtdisplay3.insert(tk.END,"\nEmail: " + entry_Email.get())                          #print email address in the text field
            txtdisplay3.insert(tk.END,"\nNumber of Passengers: " + passengervar.get()) #print number of passenger(s) in the text field
            txtdisplay3.insert(tk.END,"\nNumber of Adult(s): " + Adultvar.get())             #print number of Adult(s) in the text fied
            txtdisplay3.insert(tk.END,"\nNumber of Children(s): " + Childrenvar.get())       #print number of children(s) in the text fied
            txtdisplay3.insert(tk.END,"\nNumber of Infant(s): " + Infantvar.get())           #print number of infant(s) in the text fied
            txtdisplay3.insert(tk.END,"\n==============================================")
            
            CostWIthoutGST = int(Adultvar.get())*84 + int(Childrenvar.get())*40   #calclates the cost for ticket without the GST
            GST = int(Adultvar.get())*84*0.15 + int(Childrenvar.get())*40*0.15    #calculates the GST
            TotalCost = CostWIthoutGST + GST                    #calculates the total cost

            txtdisplay3.insert(tk.END,"\nFlight number: " + flightvar.get())
            txtdisplay3.insert(tk.END,"\nCost: $" + str(CostWIthoutGST))    #prints the cost without GST
            txtdisplay3.insert(tk.END,"\nGST: $" + str(GST))                #prints the GST
            txtdisplay3.insert(tk.END,"\nTotal Cost: $" + str(TotalCost))   #prints the cost with GST
            txtdisplay3.insert(tk.END,"\n==============================================")
            txtdisplay3.configure(state='disabled') #configures the status of text display to disabled, so the user cannot enter data in the text field
            
        def BackToHomePage():

            flight_Number[flightvar.get()] = flight_Number[flightvar.get()]+ int(passengervar.get())

            txtdisplay1.configure(state='normal')   #configures the status of text display to normal, so that the text field can be edited
            txtdisplay2.configure(state='normal')   #configures the status of text display to normal, so that the text field can be edited
            txtdisplay3.configure(state='normal')   #configures the status of text display to normal, so that the text field can be edited
            
            entry_FN.delete(0, 'end')   #delets all the data in the all the field(s)
            entry_LN.delete(0, 'end')
            entry_Email.delete(0, 'end')
            flightvar.set('')
            passengervar.set('')
            txtdisplay1.delete('1.0', tk.END)
            Adultvar.set(0)
            Childrenvar.set(0)
            Infantvar.set(0)
            txtdisplay2.delete('1.0', tk.END)
            txtdisplay3.delete('1.0', tk.END)
            entry_FN.focus_force()  #sets the focus on the first name entry box

            
            txtdisplay1.configure(state='disabled') #configures the status of text display to disabled, so the user cannot enter data in the text field
            txtdisplay2.configure(state='disabled') #configures the status of text display to disabled, so the user cannot enter data in the text field
            txtdisplay3.configure(state='disabled') #configures the status of text display to disabled, so the user cannot enter data in the text field
            

            ToHomePage.invoke()
            
        tk.Frame.__init__(self, parent) 
        self.controller = controller

        frameHeading = tk.Frame(self)   #makes the header for the heading
        frameHeading.grid(row=0, columnspan=3)  
        heading = tk.Label(frameHeading, text="Flight Booking System", fg="white", bg="#2a69c9", height="2", width="22")    #Label for the header of the program    
        heading.config(font=("",30))    #sets the font for heading
        heading.grid(row=0,columnspan=2)    #add the header label into the frame
        

        txtdisplay3=tk.Text(self,width=57,height=30)    #text field to print the ticket
        txtdisplay3.grid(row=5, column=0, columnspan=3)
        txtdisplay3.configure(state='disabled') #configures the status of text display to disabled, so the user cannot enter data in the text field

        ButtonPrint = tk.Button(self, text="Click to Print the Ticket" ,width="20",height="2", font=("",15),
                                command=PrintTicket).grid(row=6, column=0, pady=6, padx=15, sticky='W') #prints the ticker in the text field


        ButtonToHomePage = tk.Button(self, text="Click to go back\n to the home page" ,width="20",height="2", font=("",15),
                                     command=BackToHomePage).grid(row=6, column=1, pady=6, padx=15, sticky='W') #takes the user back to the start page after deleting all the fields

        ToHomePage = tk.Button(self, text="" , command=lambda: controller.show_frame("StartPage"))  #takes the user the start page

        Page_Three = tk.Label(self, text="Page 3", font=("",10), padx= 20).grid(row=7, column=1, sticky='E')    #label shows the page number
        
if __name__ == "__main__":
    app = SampleApp()
    app.geometry("512x750")
    app.title("Flight Booking System")  #title of the program 
    app.mainloop()
