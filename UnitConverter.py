import tkinter as foo
import tkinter.messagebox


class UnitConversion:
    def __init__(self):
        self.main_window = foo.Tk()
        self.main_window.title("Unit Conversion")

        self.top_frame = foo.Frame(self.main_window)
        self.bottom_frame = foo.Frame(self.main_window)

        self.radio_var = foo.IntVar()

        self.radio_var.set(1)

        self.rb1 = foo.Radiobutton(self.top_frame, text= 'Area', variable= self.radio_var, value= 1)
        self.rb2 = foo.Radiobutton(self.top_frame, text= 'Length', variable= self.radio_var, value= 2)
        self.rb3 = foo.Radiobutton(self.top_frame, text= 'Mass', variable= self.radio_var, value= 3)
        self.rb4 = foo.Radiobutton(self.top_frame, text= 'Volume', variable= self.radio_var, value= 4)
        self.rb5 = foo.Radiobutton(self.top_frame, text= 'Time', variable= self.radio_var, value= 5)
        self.rb6 = foo.Radiobutton(self.top_frame, text= 'Temperature', variable= self.radio_var, value= 6)
        self.rb7 = foo.Radiobutton(self.top_frame, text= 'Speed', variable= self.radio_var, value= 7)
        self.rb8 = foo.Radiobutton(self.top_frame, text= 'Pressure', variable= self.radio_var, value= 8)
        self.rb9 = foo.Radiobutton(self.top_frame, text= 'Energy', variable= self.radio_var, value= 9)
        self.rb10 = foo.Radiobutton(self.top_frame, text= 'Frequency', variable= self.radio_var, value= 10)

        self.rb1.pack(anchor=foo.W)
        self.rb2.pack(anchor=foo.W)
        self.rb3.pack(anchor=foo.W)
        self.rb4.pack(anchor=foo.W)
        self.rb5.pack(anchor=foo.W)
        self.rb6.pack(anchor=foo.W)
        self.rb7.pack(anchor=foo.W)
        self.rb8.pack(anchor=foo.W)
        self.rb9.pack(anchor=foo.W)
        self.rb10.pack(anchor=foo.W)

        self.ok_button = foo.Button(self.bottom_frame, text= 'Ok', command=self.show_choice)
        self.quit_button = foo.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()


    def show_choice(self):
        option = self.radio_var.get()
        if option == 1:
            self.area()
        elif option == 2:
            self.length()
        elif option == 3:
            self.mass()
        elif option == 4:
            self.volume()
        elif option == 5:
            self.time()
        elif option == 6:
            self.temperature()
        elif option == 7:
            self.speed()
        elif option == 8:
            self.pressure()
        elif option == 9:
            self.energy()
        elif option == 10:
            self.frequency()

# AREA WINDOW
    def area(self):
        self.area_window = foo.Tk()
        self.area_window.title("Area Conversion")

        self.top_frame = foo.Frame(self.area_window)
        self.middle_top_frame = foo.Frame(self.area_window)
        self.middle_frame = foo.Frame(self.area_window)
        self.middle_bottom_frame = foo.Frame(self.area_window)
        self.bottom_frame = foo.Frame(self.area_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Area Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Acre', 'Hectacre', 'Sq. Inch', 'Sq. Foot', 'Sq. Yard', 'Sq. Mile', 'Sq. Meter', 'Sq. Kilometer']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Area: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Area Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Acre', 'Hectacre', 'Sq. Inch', 'Sq. Foot', 'Sq. Yard', 'Sq. Mile', 'Sq. Meter', 'Sq. Kilometer']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.area_output_value = foo.StringVar()

        self.area_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        

        self.area_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.area_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_area)
        self.area_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.area_window.destroy)

        self.area_calc_button.pack(side='left')
        self.area_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()

# AREA CONVERSION FUNCTION
    def convert_area(self):
        self.orig_widget = self.original_unit
        self.orig_area_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_area_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        if self.orig_area_unit == self.new_area_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")

        elif self.orig_area_unit == 0 and self.new_area_unit == 1:            
            self.new_ammt = self.orig_ammt * 0.404686
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Acres is " + str(format(self.new_ammt, ',.2f')) + " Hectacres " \
                "or " +str(format(self.new_ammt, '.2e')) + " Hectacres.")

        elif self.orig_area_unit == 0 and self.new_area_unit == 2:
            self.new_ammt = self.orig_ammt * 6273000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Acres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Inches " \
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Inches.")

        elif self.orig_area_unit == 0 and self.new_area_unit == 3:
            self.new_ammt = self.orig_ammt * 43560
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Acres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Feet " \
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Feet.")

        elif self.orig_area_unit == 0 and self.new_area_unit == 4:
            self.new_ammt = self.orig_ammt * 4840
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Acres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Yards " \
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Yards.")

        elif self.orig_area_unit == 0 and self.new_area_unit == 5:
            self.new_ammt = self.orig_ammt * 0.0015625
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Acres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Miles " \
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Miles.")

        elif self.orig_area_unit == 0 and self.new_area_unit == 6:
            self.new_ammt = self.orig_ammt * 4046.86
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Acres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Meters " \
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Meters.")

        elif self.orig_area_unit == 0 and self.new_area_unit == 7:
            self.new_ammt = self.orig_ammt * 0.00404686
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Acres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Kilometers " \
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Kilometers.")

        elif self.orig_area_unit == 1 and self.new_area_unit == 0:
            self.new_ammt = self.orig_ammt * 2.47105
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hectacres is " + str(format(self.new_ammt, ',.2f')) + " Acres " \
                "or " +str(format(self.new_ammt, '.2e')) + " Acres.")

        elif self.orig_area_unit == 1 and self.new_area_unit == 2:
            self.new_ammt = self.orig_ammt * 15500000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hectacres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Inches.")

        elif self.orig_area_unit == 1 and self.new_area_unit == 3:
            self.new_ammt = self.orig_ammt * 107639
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hectacres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Feet.")

        elif self.orig_area_unit == 1 and self.new_area_unit == 4:
            self.new_ammt = self.orig_ammt * 11959.9
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hectacres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Yards.")

        elif self.orig_area_unit == 1 and self.new_area_unit == 5:
            self.new_ammt = self.orig_ammt * 0.00386102
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hectacres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Miles.")

        elif self.orig_area_unit == 1 and self.new_area_unit == 6:
            self.new_ammt = self.orig_ammt * 10000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hectacres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Meters.")

        elif self.orig_area_unit == 1 and self.new_area_unit == 7:
            self.new_ammt = self.orig_ammt * 0.01
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hectacres is " + str(format(self.new_ammt, ',.2f')) + " Sq. Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Kilometers.")

        elif self.orig_area_unit == 2 and self.new_area_unit == 0:
            self.new_ammt = self.orig_ammt * 0.00000015942
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Inches is " + str(format(self.new_ammt, ',.2f')) + " Acres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Acres.")

        elif self.orig_area_unit == 2 and self.new_area_unit == 1:
            self.new_ammt = self.orig_ammt * 0.000000064516
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Inches is " + str(format(self.new_ammt, ',.2f')) + " Hectacres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hectacres.")

        elif self.orig_area_unit == 2 and self.new_area_unit == 3:
            self.new_ammt = self.orig_ammt * 0.00694444
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Inches is " + str(format(self.new_ammt, ',.2f')) + " Sq. Feet " \
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Feet.")

        elif self.orig_area_unit == 2 and self.new_area_unit == 4:
            self.new_ammt = self.orig_ammt * 0.000771605
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Inches is " + str(format(self.new_ammt, ',.2f')) + " Sq. Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Yards.")

        elif self.orig_area_unit == 2 and self.new_area_unit == 5:
            self.new_ammt = self.orig_ammt * 0.0000000002491
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Inches is " + str(format(self.new_ammt, ',.2f')) + " Sq. Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Miles.")

        elif self.orig_area_unit == 2 and self.new_area_unit == 6:
            self.new_ammt = self.orig_ammt * 0.00064516
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Inches is " + str(format(self.new_ammt, ',.2f')) + " Sq. Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Meters.")

        elif self.orig_area_unit == 2 and self.new_area_unit == 7:
            self.new_ammt = self.orig_ammt * 0.00000000064516
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Inches is " + str(format(self.new_ammt, ',.2f')) + " Sq. Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Kilometers.")

        elif self.orig_area_unit == 3 and self.new_area_unit == 0:
            self.new_ammt = self.orig_ammt * 0.000022957
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Feet is " + str(format(self.new_ammt, ',.2f')) + " Acres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Acres.")

        elif self.orig_area_unit == 3 and self.new_area_unit == 1:
            self.new_ammt = self.orig_ammt * 0.0000092903
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Feet is " + str(format(self.new_ammt, ',.2f')) + " Hectacres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hectacres.")

        elif self.orig_area_unit == 3 and self.new_area_unit == 2:
            self.new_ammt = self.orig_ammt * 144
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Feet is " + str(format(self.new_ammt, ',.2f')) + " Sq. Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Inches.")

        elif self.orig_area_unit == 3 and self.new_area_unit == 4:
            self.new_ammt = self.orig_ammt * 0.111111
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Feet is " + str(format(self.new_ammt, ',.2f')) + " Sq. Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Yards.")

        elif self.orig_area_unit == 3 and self.new_area_unit == 5:
            self.new_ammt = self.orig_ammt * 0.00000003587
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Feet is " + str(format(self.new_ammt, ',.2f')) + " Sq. Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Miles.")

        elif self.orig_area_unit == 3 and self.new_area_unit == 6:
            self.new_ammt = self.orig_ammt * 0.092903
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Feet is " + str(format(self.new_ammt, ',.2f')) + " Sq. Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Meters.")

        elif self.orig_area_unit == 3 and self.new_area_unit == 7:
            self.new_ammt = self.orig_ammt * 0.000000092903
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Feet is " + str(format(self.new_ammt, ',.2f')) + " Sq. Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Kilometers.")

        elif self.orig_area_unit == 4 and self.new_area_unit == 0:
            self.new_ammt = self.orig_ammt * 0.000206612
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Yards is " + str(format(self.new_ammt, ',.2f')) + " Acres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Acres.")

        elif self.orig_area_unit == 4 and self.new_area_unit == 1:
            self.new_ammt = self.orig_ammt * 0.000083613
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Yards is " + str(format(self.new_ammt, ',.2f')) + " Hectacres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hectacres.")

        elif self.orig_area_unit == 4 and self.new_area_unit == 2:
            self.new_ammt = self.orig_ammt * 1296
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Yards is " + str(format(self.new_ammt, ',.2f')) + " Sq. Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Inches.")

        elif self.orig_area_unit == 4 and self.new_area_unit == 3:
            self.new_ammt = self.orig_ammt * 9
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Yards is " + str(format(self.new_ammt, ',.2f')) + " Sq. Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Feet.")

        elif self.orig_area_unit == 4 and self.new_area_unit == 5:
            self.new_ammt = self.orig_ammt * 0.00000032283
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Yards is " + str(format(self.new_ammt, ',.2f')) + " Sq. Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Miles.")

        elif self.orig_area_unit == 4 and self.new_area_unit == 6:
            self.new_ammt = self.orig_ammt * 0.836127
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Yards is " + str(format(self.new_ammt, ',.2f')) + " Sq. Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Meters.")

        elif self.orig_area_unit == 4 and self.new_area_unit == 7:
            self.new_ammt = self.orig_ammt * 0.00000083613
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Yards is " + str(format(self.new_ammt, ',.2f')) + " Sq. Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Kilometers.")

        elif self.orig_area_unit == 5 and self.new_area_unit == 0:
            self.new_ammt = self.orig_ammt * 640
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Miles is " + str(format(self.new_ammt, ',.2f')) + " Acres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Acres.")

        elif self.orig_area_unit == 5 and self.new_area_unit == 1:
            self.new_ammt = self.orig_ammt * 258.999
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Miles is " + str(format(self.new_ammt, ',.2f')) + " Hectacres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hectacres.")

        elif self.orig_area_unit == 5 and self.new_area_unit == 2:
            self.new_ammt = self.orig_ammt * 4014000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Miles is " + str(format(self.new_ammt, ',.2f')) + " Sq. Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Inches.")

        elif self.orig_area_unit == 5 and self.new_area_unit == 3:
            self.new_ammt = self.orig_ammt * 27880000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Miles is " + str(format(self.new_ammt, ',.2f')) + " Sq. Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Feet.")

        elif self.orig_area_unit == 5 and self.new_area_unit == 4:
            self.new_ammt = self.orig_ammt * 3098000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Miles is " + str(format(self.new_ammt, ',.2f')) + " Sq. Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Yards.")

        elif self.orig_area_unit == 5 and self.new_area_unit == 6:
            self.new_ammt = self.orig_ammt * 2590000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Miles is " + str(format(self.new_ammt, ',.2f')) + " Sq. Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Meters.")

        elif self.orig_area_unit == 5 and self.new_area_unit == 7:
            self.new_ammt = self.orig_ammt * 2.58999
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Miles is " + str(format(self.new_ammt, ',.2f')) + " Sq. Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Kilometers.")

        elif self.orig_area_unit == 6 and self.new_area_unit == 0:
            self.new_ammt = self.orig_ammt * 0.000247105
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Meters is " + str(format(self.new_ammt, ',.2f')) + " Acres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Acres.")

        elif self.orig_area_unit == 6 and self.new_area_unit == 1:
            self.new_ammt = self.orig_ammt * 0.0001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Meters is " + str(format(self.new_ammt, ',.2f')) + " Hectacres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hectacres.")

        elif self.orig_area_unit == 6 and self.new_area_unit == 2:
            self.new_ammt = self.orig_ammt * 1550
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Meters is " + str(format(self.new_ammt, ',.2f')) + " Sq. Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Inches.")

        elif self.orig_area_unit == 6 and self.new_area_unit == 3:
            self.new_ammt = self.orig_ammt * 10.7639
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Meters is " + str(format(self.new_ammt, ',.2f')) + " Sq. Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Feet.")

        elif self.orig_area_unit == 6 and self.new_area_unit == 4:
            self.new_ammt = self.orig_ammt * 1.19599
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Meters is " + str(format(self.new_ammt, ',.2f')) + " Sq. Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Yards.")

        elif self.orig_area_unit == 6 and self.new_area_unit == 5:
            self.new_ammt = self.orig_ammt * 0.0000003861
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Meters is " + str(format(self.new_ammt, ',.2f')) + " Sq. Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Miles.")

        elif self.orig_area_unit == 6 and self.new_area_unit == 7:
            self.new_ammt = self.orig_ammt * 0.000001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Meters is " + str(format(self.new_ammt, ',.2f')) + " Sq. Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers.")

        elif self.orig_area_unit == 7 and self.new_area_unit == 0:
            self.new_ammt = self.orig_ammt * 247.105
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Acres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Acres.")

        elif self.orig_area_unit == 7 and self.new_area_unit == 1:
            self.new_ammt = self.orig_ammt * 100
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Hectacres "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hectacres.")

        elif self.orig_area_unit == 7 and self.new_area_unit == 2:
            self.new_ammt = self.orig_ammt * 1550000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Sq. Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Inches.")

        elif self.orig_area_unit == 7 and self.new_area_unit == 3:
            self.new_ammt = self.orig_ammt * 10760000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Sq. Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Feet.")

        elif self.orig_area_unit == 7 and self.new_area_unit == 4:
            self.new_ammt = self.orig_ammt * 1196000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Sq. Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Yards.")

        elif self.orig_area_unit == 7 and self.new_area_unit == 5:
            self.new_ammt = self.orig_ammt * 0.386102
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Sq. Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Miles.")

        elif self.orig_area_unit == 7 and self.new_area_unit == 6:
            self.new_ammt = self.orig_ammt * 1000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Sq. Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Sq. Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Sq. Meters.")

# LENGTH WINDOW
    def length(self):
        self.leng_window = foo.Tk()
        self.leng_window.title("Length Conversion")

        self.top_frame = foo.Frame(self.leng_window)
        self.middle_top_frame = foo.Frame(self.leng_window)
        self.middle_frame = foo.Frame(self.leng_window)
        self.middle_bottom_frame = foo.Frame(self.leng_window)
        self.bottom_frame = foo.Frame(self.leng_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Length Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Inch', 'Foot', 'Yard', 'Mile', 'Millimeter', 'Centimeter', 'Meter', 'Kilometer']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Length: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Length Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Inch', 'Foot', 'Yard', 'Mile', 'Millimeter', 'Centimeter', 'Meter', 'Kilometer']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.leng_output_value = foo.StringVar()

        self.leng_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        

        self.leng_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.leng_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_leng)
        self.leng_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.leng_window.destroy)

        self.leng_calc_button.pack(side='left')
        self.leng_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()

# LENGTH CONVERSION FUNCTION
    def convert_leng(self):
        self.orig_widget = self.original_unit
        self.orig_leng_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_leng_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        if self.orig_leng_unit == self.new_leng_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")

        elif self.orig_leng_unit == 0 and self.new_leng_unit == 1:            
            self.new_ammt = self.orig_ammt * 0.0833333
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Inches is " + str(format(self.new_ammt, ',.2f')) + " Feet " \
                "or " +str(format(self.new_ammt, '.2e')) + " Feet.")

        elif self.orig_leng_unit == 0 and self.new_leng_unit == 2:
            self.new_ammt = self.orig_ammt * 0.0277778
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Inches is " + str(format(self.new_ammt, ',.2f')) + " Yards " \
                "or " +str(format(self.new_ammt, '.2e')) + " Yards.")

        elif self.orig_leng_unit == 0 and self.new_leng_unit == 3:
            self.new_ammt = self.orig_ammt * 0.000015783
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Inches is " + str(format(self.new_ammt, ',.2f')) + " Miles " \
                "or " +str(format(self.new_ammt, '.2e')) + " Miles.")

        elif self.orig_leng_unit == 0 and self.new_leng_unit == 4:
            self.new_ammt = self.orig_ammt * 25.4
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Inches is " + str(format(self.new_ammt, ',.2f')) + " Millimeters " \
                "or " +str(format(self.new_ammt, '.2e')) + " Millimeters.")

        elif self.orig_leng_unit == 0 and self.new_leng_unit == 5:
            self.new_ammt = self.orig_ammt * 2.54
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Inches is " + str(format(self.new_ammt, ',.2f')) + " Centimeters " \
                "or " +str(format(self.new_ammt, '.2e')) + " Centimeters.")

        elif self.orig_leng_unit == 0 and self.new_leng_unit == 6:
            self.new_ammt = self.orig_ammt * 0.0254
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Inches is " + str(format(self.new_ammt, ',.2f')) + " Meters " \
                "or " +str(format(self.new_ammt, '.2e')) + " Meters.")

        elif self.orig_leng_unit == 0 and self.new_leng_unit == 7:
            self.new_ammt = self.orig_ammt * 0.0000254
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Inches is " + str(format(self.new_ammt, ',.2f')) + " Kilometers " \
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers.")

        elif self.orig_leng_unit == 1 and self.new_leng_unit == 0:
            self.new_ammt = self.orig_ammt * 12
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet is " + str(format(self.new_ammt, ',.2f')) + " Inches " \
                "or " +str(format(self.new_ammt, '.2e')) + " Inches.")

        elif self.orig_leng_unit == 1 and self.new_leng_unit == 2:
            self.new_ammt = self.orig_ammt * 0.333333
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet is " + str(format(self.new_ammt, ',.2f')) + " Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Yards.")

        elif self.orig_leng_unit == 1 and self.new_leng_unit == 3:
            self.new_ammt = self.orig_ammt * 0.000189394
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet is " + str(format(self.new_ammt, ',.2f')) + " Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Miles.")

        elif self.orig_leng_unit == 1 and self.new_leng_unit == 4:
            self.new_ammt = self.orig_ammt * 304.8
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet is " + str(format(self.new_ammt, ',.2f')) + " Millimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Millimeters.")

        elif self.orig_leng_unit == 1 and self.new_leng_unit == 5:
            self.new_ammt = self.orig_ammt * 30.48
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet is " + str(format(self.new_ammt, ',.2f')) + " Centimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Centimeters.")

        elif self.orig_leng_unit == 1 and self.new_leng_unit == 6:
            self.new_ammt = self.orig_ammt * 0.3048
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet is " + str(format(self.new_ammt, ',.2f')) + " Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Meters.")

        elif self.orig_leng_unit == 1 and self.new_leng_unit == 7:
            self.new_ammt = self.orig_ammt * 0.0003048
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet is " + str(format(self.new_ammt, ',.2f')) + " Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers.")

        elif self.orig_leng_unit == 2 and self.new_leng_unit == 0:
            self.new_ammt = self.orig_ammt * 36
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Yards is " + str(format(self.new_ammt, ',.2f')) + " Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Inches.")

        elif self.orig_leng_unit == 2 and self.new_leng_unit == 1:
            self.new_ammt = self.orig_ammt * 3
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Yards is " + str(format(self.new_ammt, ',.2f')) + " Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Feet.")

        elif self.orig_leng_unit == 2 and self.new_leng_unit == 3:
            self.new_ammt = self.orig_ammt * 0.000568182
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Yards is " + str(format(self.new_ammt, ',.2f')) + " Miles " \
                "or " +str(format(self.new_ammt, '.2e')) + " Miles.")

        elif self.orig_leng_unit == 2 and self.new_leng_unit == 4:
            self.new_ammt = self.orig_ammt * 914.4
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Yards is " + str(format(self.new_ammt, ',.2f')) + " Millimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Millimeters.")

        elif self.orig_leng_unit == 2 and self.new_leng_unit == 5:
            self.new_ammt = self.orig_ammt * 91.44
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Yards is " + str(format(self.new_ammt, ',.2f')) + " Centimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Centimeters.")

        elif self.orig_leng_unit == 2 and self.new_leng_unit == 6:
            self.new_ammt = self.orig_ammt * 0.9144
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Yards is " + str(format(self.new_ammt, ',.2f')) + " Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Meters.")

        elif self.orig_leng_unit == 2 and self.new_leng_unit == 7:
            self.new_ammt = self.orig_ammt * 0.0009144
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Yards is " + str(format(self.new_ammt, ',.2f')) + " Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers.")

        elif self.orig_leng_unit == 3 and self.new_leng_unit == 0:
            self.new_ammt = self.orig_ammt * 63360
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles is " + str(format(self.new_ammt, ',.2f')) + " Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Inches.")

        elif self.orig_leng_unit == 3 and self.new_leng_unit == 1:
            self.new_ammt = self.orig_ammt * 5280
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles is " + str(format(self.new_ammt, ',.2f')) + " Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Feet.")

        elif self.orig_leng_unit == 3 and self.new_leng_unit == 2:
            self.new_ammt = self.orig_ammt * 1760
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles is " + str(format(self.new_ammt, ',.2f')) + " Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Yards.")

        elif self.orig_leng_unit == 3 and self.new_leng_unit == 4:
            self.new_ammt = self.orig_ammt * 1609000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles is " + str(format(self.new_ammt, ',.2f')) + " Millimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Millimeters.")

        elif self.orig_leng_unit == 3 and self.new_leng_unit == 5:
            self.new_ammt = self.orig_ammt * 160934
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles is " + str(format(self.new_ammt, ',.2f')) + " Centimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Centimeters.")

        elif self.orig_leng_unit == 3 and self.new_leng_unit == 6:
            self.new_ammt = self.orig_ammt * 1609.34
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles is " + str(format(self.new_ammt, ',.2f')) + " Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Meters.")

        elif self.orig_leng_unit == 3 and self.new_leng_unit == 7:
            self.new_ammt = self.orig_ammt * 1.60934
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles is " + str(format(self.new_ammt, ',.2f')) + " Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers.")

        elif self.orig_leng_unit == 4 and self.new_leng_unit == 0:
            self.new_ammt = self.orig_ammt * 0.0393701
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Millimeters is " + str(format(self.new_ammt, ',.2f')) + " Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Inches.")

        elif self.orig_leng_unit == 4 and self.new_leng_unit == 1:
            self.new_ammt = self.orig_ammt * 0.00328084
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Millimeters is " + str(format(self.new_ammt, ',.2f')) + " Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Feet.")

        elif self.orig_leng_unit == 4 and self.new_leng_unit == 2:
            self.new_ammt = self.orig_ammt * 0.00109361
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Millimeters is " + str(format(self.new_ammt, ',.2f')) + " Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Yards.")

        elif self.orig_leng_unit == 4 and self.new_leng_unit == 3:
            self.new_ammt = self.orig_ammt * 0.00000062137
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Millimeters is " + str(format(self.new_ammt, ',.2f')) + " Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Miles.")

        elif self.orig_leng_unit == 4 and self.new_leng_unit == 5:
            self.new_ammt = self.orig_ammt * 0.1
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Millimeters is " + str(format(self.new_ammt, ',.2f')) + " Centimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Centimeters.")

        elif self.orig_leng_unit == 4 and self.new_leng_unit == 6:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Millimeters is " + str(format(self.new_ammt, ',.2f')) + " Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Meters.")

        elif self.orig_leng_unit == 4 and self.new_leng_unit == 7:
            self.new_ammt = self.orig_ammt * 0.000001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Millimeters is " + str(format(self.new_ammt, ',.2f')) + " Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers.")

        elif self.orig_leng_unit == 5 and self.new_leng_unit == 0:
            self.new_ammt = self.orig_ammt * 0.393701
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Centimeters is " + str(format(self.new_ammt, ',.2f')) + " Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Inches.")

        elif self.orig_leng_unit == 5 and self.new_leng_unit == 1:
            self.new_ammt = self.orig_ammt * 0.0328084
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Centimeters is " + str(format(self.new_ammt, ',.2f')) + " Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Feet.")

        elif self.orig_leng_unit == 5 and self.new_leng_unit == 2:
            self.new_ammt = self.orig_ammt * 0.0109361
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Centimeters is " + str(format(self.new_ammt, ',.2f')) + " Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Yards.")

        elif self.orig_leng_unit == 5 and self.new_leng_unit == 3:
            self.new_ammt = self.orig_ammt * 0.0000062137
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Centimeters is " + str(format(self.new_ammt, ',.2f')) + " Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Miles.")

        elif self.orig_leng_unit == 5 and self.new_leng_unit == 4:
            self.new_ammt = self.orig_ammt * 10
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Centimeters is " + str(format(self.new_ammt, ',.2f')) + " Millimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Millimeters.")

        elif self.orig_leng_unit == 5 and self.new_leng_unit == 6:
            self.new_ammt = self.orig_ammt * 0.01
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Centimeters is " + str(format(self.new_ammt, ',.2f')) + " Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Meters.")

        elif self.orig_leng_unit == 5 and self.new_leng_unit == 7:
            self.new_ammt = self.orig_ammt * 0.00001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Centimeters is " + str(format(self.new_ammt, ',.2f')) + " Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers.")

        elif self.orig_leng_unit == 6 and self.new_leng_unit == 0:
            self.new_ammt = self.orig_ammt * 39.3701
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters is " + str(format(self.new_ammt, ',.2f')) + " Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Inches.")

        elif self.orig_leng_unit == 6 and self.new_leng_unit == 1:
            self.new_ammt = self.orig_ammt * 3.28084
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters is " + str(format(self.new_ammt, ',.2f')) + " Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Feet.")

        elif self.orig_leng_unit == 6 and self.new_leng_unit == 2:
            self.new_ammt = self.orig_ammt * 1.09361
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters is " + str(format(self.new_ammt, ',.2f')) + " Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Yards.")

        elif self.orig_leng_unit == 6 and self.new_leng_unit == 3:
            self.new_ammt = self.orig_ammt * 0.000621371
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters is " + str(format(self.new_ammt, ',.2f')) + " Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Miles.")

        elif self.orig_leng_unit == 6 and self.new_leng_unit == 4:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters is " + str(format(self.new_ammt, ',.2f')) + " Millimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Millimeters.")

        elif self.orig_leng_unit == 6 and self.new_leng_unit == 5:
            self.new_ammt = self.orig_ammt * 100
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters is " + str(format(self.new_ammt, ',.2f')) + " Centimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Centimeters.")

        elif self.orig_leng_unit == 6 and self.new_leng_unit == 7:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters is " + str(format(self.new_ammt, ',.2f')) + " Kilometers "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers.")

        elif self.orig_leng_unit == 7 and self.new_leng_unit == 0:
            self.new_ammt = self.orig_ammt * 39370.1
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Inches.")

        elif self.orig_leng_unit == 7 and self.new_leng_unit == 1:
            self.new_ammt = self.orig_ammt * 3280.84
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Feet.")

        elif self.orig_leng_unit == 7 and self.new_leng_unit == 2:
            self.new_ammt = self.orig_ammt * 1093.61
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Yards "\
                "or " +str(format(self.new_ammt, '.2e')) + " Yards.")

        elif self.orig_leng_unit == 7 and self.new_leng_unit == 3:
            self.new_ammt = self.orig_ammt * 0.621371
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Miles "\
                "or " +str(format(self.new_ammt, '.2e')) + " Miles.")

        elif self.orig_leng_unit == 7 and self.new_leng_unit == 4:
            self.new_ammt = self.orig_ammt * 1000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Millimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Millimeters.")

        elif self.orig_leng_unit == 7 and self.new_leng_unit == 5:
            self.new_ammt = self.orig_ammt * 100000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Centimeters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Centimeters.")

        elif self.orig_leng_unit == 7 and self.new_leng_unit == 6:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers is " + str(format(self.new_ammt, ',.2f')) + " Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Meters.")

# MASS WINDOW
    def mass(self):
        self.mass_window = foo.Tk()
        self.mass_window.title("Mass Conversion")

        self.top_frame = foo.Frame(self.mass_window)
        self.middle_top_frame = foo.Frame(self.mass_window)
        self.middle_frame = foo.Frame(self.mass_window)
        self.middle_bottom_frame = foo.Frame(self.mass_window)
        self.bottom_frame = foo.Frame(self.mass_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Mass Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Ounce', 'Pound', 'US Ton', 'Milligram', 'Gram', 'Kilogram', 'Metric Ton']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Mass: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Mass Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Ounce', 'Pound', 'US Ton', 'Milligram', 'Gram', 'Kilogram', 'Metric Ton']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.mass_output_value = foo.StringVar()

        self.mass_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        

        self.mass_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.mass_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_mass)
        self.mass_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.mass_window.destroy)

        self.mass_calc_button.pack(side='left')
        self.mass_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()

# MASS CONVERSION FUNCTION
    def convert_mass(self):
        self.orig_widget = self.original_unit
        self.orig_mass_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_mass_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        if self.orig_mass_unit == self.new_mass_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")

        elif self.orig_mass_unit == 0 and self.new_mass_unit == 1:            
            self.new_ammt = self.orig_ammt * 0.0625
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Pounds " \
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds.")

        elif self.orig_mass_unit == 0 and self.new_mass_unit == 2:
            self.new_ammt = self.orig_ammt * 0.00003125
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " US Tons " \
                "or " +str(format(self.new_ammt, '.2e')) + " US Tons.")

        elif self.orig_mass_unit == 0 and self.new_mass_unit == 3:
            self.new_ammt = self.orig_ammt * 28349.5
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Milligrams " \
                "or " +str(format(self.new_ammt, '.2e')) + " Milligrams.")

        elif self.orig_mass_unit == 0 and self.new_mass_unit == 4:
            self.new_ammt = self.orig_ammt * 28.3495
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Grams " \
                "or " +str(format(self.new_ammt, '.2e')) + " Grams.")

        elif self.orig_mass_unit == 0 and self.new_mass_unit == 5:
            self.new_ammt = self.orig_ammt * 0.0283495
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Kilograms " \
                "or " +str(format(self.new_ammt, '.2e')) + " Kilograms.")

        elif self.orig_mass_unit == 0 and self.new_mass_unit == 6:
            self.new_ammt = self.orig_ammt * 0.00002835
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Metric Tons " \
                "or " +str(format(self.new_ammt, '.2e')) + " Metric Tons.")

        elif self.orig_mass_unit == 1 and self.new_mass_unit == 0:
            self.new_ammt = self.orig_ammt * 16
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds is " + str(format(self.new_ammt, ',.2f')) + " Ounces " \
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_mass_unit == 1 and self.new_mass_unit == 2:
            self.new_ammt = self.orig_ammt * 0.0005
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds is " + str(format(self.new_ammt, ',.2f')) + " US Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " US Tons.")

        elif self.orig_mass_unit == 1 and self.new_mass_unit == 3:
            self.new_ammt = self.orig_ammt * 453592
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds is " + str(format(self.new_ammt, ',.2f')) + " Milligrams "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milligrams.")

        elif self.orig_mass_unit == 1 and self.new_mass_unit == 4:
            self.new_ammt = self.orig_ammt * 453.592
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds is " + str(format(self.new_ammt, ',.2f')) + " Grams "\
                "or " +str(format(self.new_ammt, '.2e')) + " Grams.")

        elif self.orig_mass_unit == 1 and self.new_mass_unit == 5:
            self.new_ammt = self.orig_ammt * 0.453592
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds is " + str(format(self.new_ammt, ',.2f')) + " Kilograms "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilograms.")

        elif self.orig_mass_unit == 1 and self.new_mass_unit == 6:
            self.new_ammt = self.orig_ammt * 0.000453592
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds is " + str(format(self.new_ammt, ',.2f')) + " Metric Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Metric Tons.")

        elif self.orig_mass_unit == 2 and self.new_mass_unit == 0:
            self.new_ammt = self.orig_ammt * 32000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " US Tons is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_mass_unit == 2 and self.new_mass_unit == 1:
            self.new_ammt = self.orig_ammt * 2000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " US Tons is " + str(format(self.new_ammt, ',.2f')) + " Pounds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds.")

        elif self.orig_mass_unit == 2 and self.new_mass_unit == 3:
            self.new_ammt = self.orig_ammt * 907200000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " US Tons is " + str(format(self.new_ammt, ',.2f')) + " Milligrams " \
                "or " +str(format(self.new_ammt, '.2e')) + " Milligrams.")

        elif self.orig_mass_unit == 2 and self.new_mass_unit == 4:
            self.new_ammt = self.orig_ammt * 907185
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " US Tons is " + str(format(self.new_ammt, ',.2f')) + " Grams "\
                "or " +str(format(self.new_ammt, '.2e')) + " Grams.")

        elif self.orig_mass_unit == 2 and self.new_mass_unit == 5:
            self.new_ammt = self.orig_ammt * 907.185
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " US Tons is " + str(format(self.new_ammt, ',.2f')) + " Kilograms "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilograms.")

        elif self.orig_mass_unit == 2 and self.new_mass_unit == 6:
            self.new_ammt = self.orig_ammt * 0.907185
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " US Tons is " + str(format(self.new_ammt, ',.2f')) + " Metric Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Metric Tons.")

        elif self.orig_mass_unit == 3 and self.new_mass_unit == 0:
            self.new_ammt = self.orig_ammt * 0.000035274
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milligrams is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_mass_unit == 3 and self.new_mass_unit == 1:
            self.new_ammt = self.orig_ammt * 0.0000022046
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milligrams is " + str(format(self.new_ammt, ',.2f')) + " Pounds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds.")

        elif self.orig_mass_unit == 3 and self.new_mass_unit == 2:
            self.new_ammt = self.orig_ammt * 0.0000000011023
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milligrams is " + str(format(self.new_ammt, ',.2f')) + " US Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " US Tons.")

        elif self.orig_mass_unit == 3 and self.new_mass_unit == 4:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milligrams is " + str(format(self.new_ammt, ',.2f')) + " Grams "\
                "or " +str(format(self.new_ammt, '.2e')) + " Grams.")

        elif self.orig_mass_unit == 3 and self.new_mass_unit == 5:
            self.new_ammt = self.orig_ammt * 0.000001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milligrams is " + str(format(self.new_ammt, ',.2f')) + " Kilograms "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilograms.")

        elif self.orig_mass_unit == 3 and self.new_mass_unit == 6:
            self.new_ammt = self.orig_ammt * 0.000000001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milligrams is " + str(format(self.new_ammt, ',.2f')) + " Metric Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Metric Tons.")

        elif self.orig_mass_unit == 4 and self.new_mass_unit == 0:
            self.new_ammt = self.orig_ammt * 0.035274
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Grams is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_mass_unit == 4 and self.new_mass_unit == 1:
            self.new_ammt = self.orig_ammt * 0.00220462
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Grams is " + str(format(self.new_ammt, ',.2f')) + " Pounds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds.")

        elif self.orig_mass_unit == 4 and self.new_mass_unit == 2:
            self.new_ammt = self.orig_ammt * 0.0000011023
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Grams is " + str(format(self.new_ammt, ',.2f')) + " US Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " US Tons.")

        elif self.orig_mass_unit == 4 and self.new_mass_unit == 3:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Grams is " + str(format(self.new_ammt, ',.2f')) + " Milligrams "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milligrams.")

        elif self.orig_mass_unit == 4 and self.new_mass_unit == 5:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Grams is " + str(format(self.new_ammt, ',.2f')) + " Kilograms "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilograms.")

        elif self.orig_mass_unit == 4 and self.new_mass_unit == 6:
            self.new_ammt = self.orig_ammt * 0.000001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Grams is " + str(format(self.new_ammt, ',.2f')) + " Metric Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Metric Tons.")

        elif self.orig_mass_unit == 5 and self.new_mass_unit == 0:
            self.new_ammt = self.orig_ammt * 35.274
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilograms is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_mass_unit == 5 and self.new_mass_unit == 1:
            self.new_ammt = self.orig_ammt * 2.20462
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilograms is " + str(format(self.new_ammt, ',.2f')) + " Pounds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds.")

        elif self.orig_mass_unit == 5 and self.new_mass_unit == 2:
            self.new_ammt = self.orig_ammt * 0.00110231
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilograms is " + str(format(self.new_ammt, ',.2f')) + " US Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " US Tons.")

        elif self.orig_mass_unit == 5 and self.new_mass_unit == 3:
            self.new_ammt = self.orig_ammt * 1000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilograms is " + str(format(self.new_ammt, ',.2f')) + " Milligrams "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milligrams.")

        elif self.orig_mass_unit == 5 and self.new_mass_unit == 4:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilograms is " + str(format(self.new_ammt, ',.2f')) + " Grams "\
                "or " +str(format(self.new_ammt, '.2e')) + " Grams.")

        elif self.orig_mass_unit == 5 and self.new_mass_unit == 6:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilowgrams is " + str(format(self.new_ammt, ',.2f')) + " Metric Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Metric Tons.")

        elif self.orig_mass_unit == 6 and self.new_mass_unit == 0:
            self.new_ammt = self.orig_ammt * 35274
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Metric Tons is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_mass_unit == 6 and self.new_mass_unit == 1:
            self.new_ammt = self.orig_ammt * 2204.62
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Metric Tons is " + str(format(self.new_ammt, ',.2f')) + " Pounds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds.")

        elif self.orig_mass_unit == 6 and self.new_mass_unit == 2:
            self.new_ammt = self.orig_ammt * 1.10231
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Metric Tons is " + str(format(self.new_ammt, ',.2f')) + " US Tons "\
                "or " +str(format(self.new_ammt, '.2e')) + " US Tons.")

        elif self.orig_mass_unit == 6 and self.new_mass_unit == 3:
            self.new_ammt = self.orig_ammt * 1000000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Metric Tons is " + str(format(self.new_ammt, ',.2f')) + " Milligrams "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milligrams.")

        elif self.orig_mass_unit == 6 and self.new_mass_unit == 4:
            self.new_ammt = self.orig_ammt * 1000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Metric Tons is " + str(format(self.new_ammt, ',.2f')) + " Grams "\
                "or " +str(format(self.new_ammt, '.2e')) + " Grams.")

        elif self.orig_mass_unit == 6 and self.new_mass_unit == 5:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Metric Tons is " + str(format(self.new_ammt, ',.2f')) + " Kilograms "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilograms.")

# VOLUME WINDOW
    def volume(self):
        self.vol_window = foo.Tk()
        self.vol_window.title("Volume Conversion")

        self.top_frame = foo.Frame(self.vol_window)
        self.middle_top_frame = foo.Frame(self.vol_window)
        self.middle_frame = foo.Frame(self.vol_window)
        self.middle_bottom_frame = foo.Frame(self.vol_window)
        self.bottom_frame = foo.Frame(self.vol_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Volume Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Gallon', 'Quart', 'Pint', 'Cup', 'Ounce', 'Tablespoon', 'Teaspoon', 'Liter', 'Milliliter', 'Cubic Ft.', 'Cubic In.', 'Cubic Meter']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Volume: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Volume Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Gallon', 'Quart', 'Pint', 'Cup', 'Ounce', 'Tablespoon', 'Teaspoon', 'Liter', 'Milliliter', 'Cubic Ft.', 'Cubic In.', 'Cubic Meter']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.vol_output_value = foo.StringVar()

        self.vol_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        

        self.vol_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.vol_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_vol)
        self.vol_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.vol_window.destroy)

        self.vol_calc_button.pack(side='left')
        self.vol_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()

# VOLUME CONVERSION FUNCTION
    def convert_vol(self):
        self.orig_widget = self.original_unit
        self.orig_vol_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_vol_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        if self.orig_vol_unit == self.new_vol_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 1:            
            self.new_ammt = self.orig_ammt * 4
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Quarts " \
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 8
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Pints " \
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 15.7725
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Cups " \
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 128
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Ounces " \
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 256
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons " \
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 768
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons " \
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 3.78541
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Liters " \
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 3785.41
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Milliliters " \
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.133681
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet " \
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 231
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches " \
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 0 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.00378541
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gallons is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters " \
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 0.25
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Gallons " \
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 2
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 3.94314
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Cups "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 32
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 64
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 192
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 0.946353
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 946.353
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.0334201
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 57.75
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 1 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.000946353
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Quarts is " + str(format(self.new_ammt, ',.2f')) + " Cubic meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 0.125
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 0.5
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 1.97157
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Cups " \
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 16
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 32
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 96
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 0.473176
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 473.176
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.0167101
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 28.875
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 2 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.000473176
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pints is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 0.0634013
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 0.253605
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 0.50721
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 8.11537
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 16.2307
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 48.6922
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 0.24
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 240
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.00847552
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 14.6457
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 3 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.00024
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cups is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 0.0078125
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 0.03125
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 0.0625
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 0.123223
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Cups "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 2
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 6
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 0.0295735
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 29.5735
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.00104438
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 1.80469
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 4 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.000029574
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Ounces is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 0.00390625
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 0.015625
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 0.03125
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 0.0616115
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Cups "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 0.5
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 3
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 0.0147868
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 14.7868
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.00052219
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 0.902344
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 5 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.000014787
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Tablespoons is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 0.00130208
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 0.00520833
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 0.0104167
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 0.0205372
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Cups "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 0.166667
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 0.333333
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 0.00492892
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 4.92892
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.000174063
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 0.300781
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 6 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.00000492891749
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Teaspoons is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 0.264172
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 1.05669
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 2.11338
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 4.16667
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Cups "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 33.814
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 67.628
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 202.884
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.0353147
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 61.0237
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 7 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Liters is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 0.000264172
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 0.00105669
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 0.00211338
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 0.00416667
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Cups "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 0.033814
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 0.067628
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 0.202884
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.000035315
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 0.0610237
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 8 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.000001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliliters is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 7.48052
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 29.9221
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 59.8442
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 117.987
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Cups "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 957.506
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 1915.01
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 5745.04
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 28.3168
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 28316.8
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 1728
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

        elif self.orig_vol_unit == 9 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.0283168
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Feet is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 0.004329
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 0.017316
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 0.034632
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 0.0682794
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Cups "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 0.554113
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 1.10823
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 3.32468
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 0.0163871
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 16.3871
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 0.000578704
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 10 and self.new_vol_unit == 11:
            self.new_ammt = self.orig_ammt * 0.000016387
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Inches is " + str(format(self.new_ammt, ',.2f')) + " Cubic Meters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Meters.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 0:
            self.new_ammt = self.orig_ammt * 264.172
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Gallons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gallons.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 1:
            self.new_ammt = self.orig_ammt * 1056.69
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Quarts "\
                "or " +str(format(self.new_ammt, '.2e')) + " Quarts.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 2:
            self.new_ammt = self.orig_ammt * 2113.38
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Pints "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pints.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 3:
            self.new_ammt = self.orig_ammt * 4166.67
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Cups "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cups.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 4:
            self.new_ammt = self.orig_ammt * 33814
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Ounces "\
                "or " +str(format(self.new_ammt, '.2e')) + " Ounces.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 5:
            self.new_ammt = self.orig_ammt * 67628
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Tablespoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Tablespoons.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 6:
            self.new_ammt = self.orig_ammt * 202884
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Teaspoons "\
                "or " +str(format(self.new_ammt, '.2e')) + " Teaspoons.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 7:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Liters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Liters.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 8:
            self.new_ammt = self.orig_ammt * 1000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Milliliters "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliliters.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 9:
            self.new_ammt = self.orig_ammt * 35.3147
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Cubic Feet "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Feet.")

        elif self.orig_vol_unit == 11 and self.new_vol_unit == 10:
            self.new_ammt = self.orig_ammt * 61023.7
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Cubic Meters is " + str(format(self.new_ammt, ',.2f')) + " Cubic Inches "\
                "or " +str(format(self.new_ammt, '.2e')) + " Cubic Inches.")

# TIME WINDOW
    def time(self):
        self.time_window = foo.Tk()
        self.time_window.title("Time Conversion")

        self.top_frame = foo.Frame(self.time_window)
        self.middle_top_frame = foo.Frame(self.time_window)
        self.middle_frame = foo.Frame(self.time_window)
        self.middle_bottom_frame = foo.Frame(self.time_window)
        self.bottom_frame = foo.Frame(self.time_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Time Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Year', 'Month', 'Week', 'Day', 'Hour', 'Minute', 'Second', 'Millisecond']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Time: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Time Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Year', 'Month', 'Week', 'Day', 'Hour', 'Minute', 'Second', 'Millisecond']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.time_output_value = foo.StringVar()

        self.time_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        

        self.time_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.time_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_time)
        self.time_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.time_window.destroy)

        self.time_calc_button.pack(side='left')
        self.time_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()

# TIME CONVERSION FUNCTION
    def convert_time(self):
        self.orig_widget = self.original_unit
        self.orig_time_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_time_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        if self.orig_time_unit == self.new_time_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")

        elif self.orig_time_unit == 0 and self.new_time_unit == 1:            
            self.new_ammt = self.orig_ammt * 12
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Years is " + str(format(self.new_ammt, ',.2f')) + " Months " \
                "or " +str(format(self.new_ammt, '.2e')) + " Months.")

        elif self.orig_time_unit == 0 and self.new_time_unit == 2:
            self.new_ammt = self.orig_ammt * 52.1429
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Years is " + str(format(self.new_ammt, ',.2f')) + " Weeks " \
                "or " +str(format(self.new_ammt, '.2e')) + " Weeks.")

        elif self.orig_time_unit == 0 and self.new_time_unit == 3:
            self.new_ammt = self.orig_ammt * 365
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Years is " + str(format(self.new_ammt, ',.2f')) + " Days " \
                "or " +str(format(self.new_ammt, '.2e')) + " Days.")

        elif self.orig_time_unit == 0 and self.new_time_unit == 4:
            self.new_ammt = self.orig_ammt * 8760
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Years is " + str(format(self.new_ammt, ',.2f')) + " Hours " \
                "or " +str(format(self.new_ammt, '.2e')) + " Hours.")

        elif self.orig_time_unit == 0 and self.new_time_unit == 5:
            self.new_ammt = self.orig_ammt * 525600
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Years is " + str(format(self.new_ammt, ',.2f')) + " Minutes " \
                "or " +str(format(self.new_ammt, '.2e')) + " Minutes.")

        elif self.orig_time_unit == 0 and self.new_time_unit == 6:
            self.new_ammt = self.orig_ammt * 31540000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Years is " + str(format(self.new_ammt, ',.2f')) + " Seconds " \
                "or " +str(format(self.new_ammt, '.2e')) + " Seconds.")

        elif self.orig_time_unit == 0 and self.new_time_unit == 7:
            self.new_ammt = self.orig_ammt * 31540000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Years is " + str(format(self.new_ammt, ',.2f')) + " Milliseconds " \
                "or " +str(format(self.new_ammt, '.2e')) + " Milliseconds.")

        elif self.orig_time_unit == 1 and self.new_time_unit == 0:
            self.new_ammt = self.orig_ammt * 0.0833334
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Months is " + str(format(self.new_ammt, ',.2f')) + " Years " \
                "or " +str(format(self.new_ammt, '.2e')) + " Years.")

        elif self.orig_time_unit == 1 and self.new_time_unit == 2:
            self.new_ammt = self.orig_ammt * 4.34524
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Months is " + str(format(self.new_ammt, ',.2f')) + " Weeks "\
                "or " +str(format(self.new_ammt, '.2e')) + " Weeks.")

        elif self.orig_time_unit == 1 and self.new_time_unit == 3:
            self.new_ammt = self.orig_ammt * 30.4167
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Months is " + str(format(self.new_ammt, ',.2f')) + " Days "\
                "or " +str(format(self.new_ammt, '.2e')) + " Days.")

        elif self.orig_time_unit == 1 and self.new_time_unit == 4:
            self.new_ammt = self.orig_ammt * 730.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Months is " + str(format(self.new_ammt, ',.2f')) + " Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hours.")

        elif self.orig_time_unit == 1 and self.new_time_unit == 5:
            self.new_ammt = self.orig_ammt * 43800
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Months is " + str(format(self.new_ammt, ',.2f')) + " Minutes "\
                "or " +str(format(self.new_ammt, '.2e')) + " Minutes.")

        elif self.orig_time_unit == 1 and self.new_time_unit == 6:
            self.new_ammt = self.orig_ammt * 2628000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Months is " + str(format(self.new_ammt, ',.2f')) + " Seconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Seconds.")

        elif self.orig_time_unit == 1 and self.new_time_unit == 7:
            self.new_ammt = self.orig_ammt * 2628000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Months is " + str(format(self.new_ammt, ',.2f')) + " Milliseconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliseconds.")

        elif self.orig_time_unit == 2 and self.new_time_unit == 0:
            self.new_ammt = self.orig_ammt * 0.0191781
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Weeks is " + str(format(self.new_ammt, ',.2f')) + " Years "\
                "or " +str(format(self.new_ammt, '.2e')) + " Years.")

        elif self.orig_time_unit == 2 and self.new_time_unit == 1:
            self.new_ammt = self.orig_ammt * 0.230137
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Weeks is " + str(format(self.new_ammt, ',.2f')) + " Months "\
                "or " +str(format(self.new_ammt, '.2e')) + " Months.")

        elif self.orig_time_unit == 2 and self.new_time_unit == 3:
            self.new_ammt = self.orig_ammt * 7
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Weeks is " + str(format(self.new_ammt, ',.2f')) + " Days " \
                "or " +str(format(self.new_ammt, '.2e')) + " Days.")

        elif self.orig_time_unit == 2 and self.new_time_unit == 4:
            self.new_ammt = self.orig_ammt * 168
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Weeks is " + str(format(self.new_ammt, ',.2f')) + " Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hours.")

        elif self.orig_time_unit == 2 and self.new_time_unit == 5:
            self.new_ammt = self.orig_ammt * 10080
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Weeks is " + str(format(self.new_ammt, ',.2f')) + " Minutes "\
                "or " +str(format(self.new_ammt, '.2e')) + " Minutes.")

        elif self.orig_time_unit == 2 and self.new_time_unit == 6:
            self.new_ammt = self.orig_ammt * 604800
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Weeks is " + str(format(self.new_ammt, ',.2f')) + " Seconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Seconds.")

        elif self.orig_time_unit == 2 and self.new_time_unit == 7:
            self.new_ammt = self.orig_ammt * 604800000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Weeks is " + str(format(self.new_ammt, ',.2f')) + " Milliseconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliseconds.")

        elif self.orig_time_unit == 3 and self.new_time_unit == 0:
            self.new_ammt = self.orig_ammt * 0.00273973
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Days is " + str(format(self.new_ammt, ',.2f')) + " Years "\
                "or " +str(format(self.new_ammt, '.2e')) + " Years.")

        elif self.orig_time_unit == 3 and self.new_time_unit == 1:
            self.new_ammt = self.orig_ammt * 0.0328767
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Days is " + str(format(self.new_ammt, ',.2f')) + " Months "\
                "or " +str(format(self.new_ammt, '.2e')) + " Months.")

        elif self.orig_time_unit == 3 and self.new_time_unit == 2:
            self.new_ammt = self.orig_ammt * 0.142857
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Days is " + str(format(self.new_ammt, ',.2f')) + " Weeks "\
                "or " +str(format(self.new_ammt, '.2e')) + " Weeks.")

        elif self.orig_time_unit == 3 and self.new_time_unit == 4:
            self.new_ammt = self.orig_ammt * 24
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Days is " + str(format(self.new_ammt, ',.2f')) + " Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hours.")

        elif self.orig_time_unit == 3 and self.new_time_unit == 5:
            self.new_ammt = self.orig_ammt * 1440
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Days is " + str(format(self.new_ammt, ',.2f')) + " Minutes "\
                "or " +str(format(self.new_ammt, '.2e')) + " Minutes.")

        elif self.orig_time_unit == 3 and self.new_time_unit == 6:
            self.new_ammt = self.orig_ammt * 86400
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Days is " + str(format(self.new_ammt, ',.2f')) + " Seconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Seconds.")

        elif self.orig_time_unit == 3 and self.new_time_unit == 7:
            self.new_ammt = self.orig_ammt * 86400000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Days is " + str(format(self.new_ammt, ',.2f')) + " Milliseconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliseconds.")

        elif self.orig_time_unit == 4 and self.new_time_unit == 0:
            self.new_ammt = self.orig_ammt * 0.000114155
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hours is " + str(format(self.new_ammt, ',.2f')) + " Years "\
                "or " +str(format(self.new_ammt, '.2e')) + " Years.")

        elif self.orig_time_unit == 4 and self.new_time_unit == 1:
            self.new_ammt = self.orig_ammt * 0.00136986
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hours is " + str(format(self.new_ammt, ',.2f')) + " Months "\
                "or " +str(format(self.new_ammt, '.2e')) + " Months.")

        elif self.orig_time_unit == 4 and self.new_time_unit == 2:
            self.new_ammt = self.orig_ammt * 0.00595238
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hours is " + str(format(self.new_ammt, ',.2f')) + " Weeks "\
                "or " +str(format(self.new_ammt, '.2e')) + " Weeks.")

        elif self.orig_time_unit == 4 and self.new_time_unit == 3:
            self.new_ammt = self.orig_ammt * 0.0416667
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hours is " + str(format(self.new_ammt, ',.2f')) + " Days "\
                "or " +str(format(self.new_ammt, '.2e')) + " Days.")

        elif self.orig_time_unit == 4 and self.new_time_unit == 5:
            self.new_ammt = self.orig_ammt * 60
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hours is " + str(format(self.new_ammt, ',.2f')) + " Minutes "\
                "or " +str(format(self.new_ammt, '.2e')) + " Minutes.")

        elif self.orig_time_unit == 4 and self.new_time_unit == 6:
            self.new_ammt = self.orig_ammt * 3600
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hours is " + str(format(self.new_ammt, ',.2f')) + " Seconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Seconds.")

        elif self.orig_time_unit == 4 and self.new_time_unit == 7:
            self.new_ammt = self.orig_ammt * 3600000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hours is " + str(format(self.new_ammt, ',.2f')) + " Milliseconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliseconds.")

        elif self.orig_time_unit == 5 and self.new_time_unit == 0:
            self.new_ammt = self.orig_ammt * 0.0000019026
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Minutes is " + str(format(self.new_ammt, ',.2f')) + " Years "\
                "or " +str(format(self.new_ammt, '.2e')) + " Years.")

        elif self.orig_time_unit == 5 and self.new_time_unit == 1:
            self.new_ammt = self.orig_ammt * 0.000022831
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Minutes is " + str(format(self.new_ammt, ',.2f')) + " Months "\
                "or " +str(format(self.new_ammt, '.2e')) + " Months.")

        elif self.orig_time_unit == 5 and self.new_time_unit == 2:
            self.new_ammt = self.orig_ammt * 0.000099206
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Minutes is " + str(format(self.new_ammt, ',.2f')) + " Weeks "\
                "or " +str(format(self.new_ammt, '.2e')) + " Weeks.")

        elif self.orig_time_unit == 5 and self.new_time_unit == 3:
            self.new_ammt = self.orig_ammt * 0.000694444
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Minutes is " + str(format(self.new_ammt, ',.2f')) + " Days "\
                "or " +str(format(self.new_ammt, '.2e')) + " Days.")

        elif self.orig_time_unit == 5 and self.new_time_unit == 4:
            self.new_ammt = self.orig_ammt * 0.0166667
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Minutes is " + str(format(self.new_ammt, ',.2f')) + " Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hours.")

        elif self.orig_time_unit == 5 and self.new_time_unit == 6:
            self.new_ammt = self.orig_ammt * 60
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Minutes is " + str(format(self.new_ammt, ',.2f')) + " Seconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Seconds.")

        elif self.orig_time_unit == 5 and self.new_time_unit == 7:
            self.new_ammt = self.orig_ammt * 60000 
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Minutes is " + str(format(self.new_ammt, ',.2f')) + " Milliseconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliseconds.")

        elif self.orig_time_unit == 6 and self.new_time_unit == 0:
            self.new_ammt = self.orig_ammt * 0.00000003171
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Seconds is " + str(format(self.new_ammt, ',.2f')) + " Years "\
                "or " +str(format(self.new_ammt, '.2e')) + " Years.")

        elif self.orig_time_unit == 6 and self.new_time_unit == 1:
            self.new_ammt = self.orig_ammt * 0.00000038052
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Seconds is " + str(format(self.new_ammt, ',.2f')) + " Months "\
                "or " +str(format(self.new_ammt, '.2e')) + " Months.")

        elif self.orig_time_unit == 6 and self.new_time_unit == 2:
            self.new_ammt = self.orig_ammt * 0.0000016534
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Seconds is " + str(format(self.new_ammt, ',.2f')) + " Weeks "\
                "or " +str(format(self.new_ammt, '.2e')) + " Weeks.")

        elif self.orig_time_unit == 6 and self.new_time_unit == 3:
            self.new_ammt = self.orig_ammt * 0.000011574
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Seconds is " + str(format(self.new_ammt, ',.2f')) + " Days "\
                "or " +str(format(self.new_ammt, '.2e')) + " Days.")

        elif self.orig_time_unit == 6 and self.new_time_unit == 4:
            self.new_ammt = self.orig_ammt * 0.000277778
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Seconds is " + str(format(self.new_ammt, ',.2f')) + " Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hours.")

        elif self.orig_time_unit == 6 and self.new_time_unit == 5:
            self.new_ammt = self.orig_ammt * 0.0166667
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Seconds is " + str(format(self.new_ammt, ',.2f')) + " Minutes "\
                "or " +str(format(self.new_ammt, '.2e')) + " Minutes.")

        elif self.orig_time_unit == 6 and self.new_time_unit == 7:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Seconds is " + str(format(self.new_ammt, ',.2f')) + " Milliseconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Milliseconds.")

        elif self.orig_time_unit == 7 and self.new_time_unit == 0:
            self.new_ammt = self.orig_ammt * 0.00000000003171
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliseconds is " + str(format(self.new_ammt, ',.2f')) + " Years "\
                "or " +str(format(self.new_ammt, '.2e')) + " Years.")

        elif self.orig_time_unit == 7 and self.new_time_unit == 1:
            self.new_ammt = self.orig_ammt * 0.00000000038052
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliseconds is " + str(format(self.new_ammt, ',.2f')) + " Months "\
                "or " +str(format(self.new_ammt, '.2e')) + " Months.")

        elif self.orig_time_unit == 7 and self.new_time_unit == 2:
            self.new_ammt = self.orig_ammt * 0.0000000016534
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliseconds is " + str(format(self.new_ammt, ',.2f')) + " Weeks "\
                "or " +str(format(self.new_ammt, '.2e')) + " Weeks.")

        elif self.orig_time_unit == 7 and self.new_time_unit == 3:
            self.new_ammt = self.orig_ammt * 0.000000011574
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliseconds is " + str(format(self.new_ammt, ',.2f')) + " Days "\
                "or " +str(format(self.new_ammt, '.2e')) + " Days.")

        elif self.orig_time_unit == 7 and self.new_time_unit == 4:
            self.new_ammt = self.orig_ammt * 0.00000027778
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliseconds is " + str(format(self.new_ammt, ',.2f')) + " Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hours.")

        elif self.orig_time_unit == 7 and self.new_time_unit == 5:
            self.new_ammt = self.orig_ammt * 0.000016667
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliseconds is " + str(format(self.new_ammt, ',.2f')) + " Minutes "\
                "or " +str(format(self.new_ammt, '.2e')) + " Minutes.")

        elif self.orig_time_unit == 7 and self.new_time_unit == 6:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Milliseconds is " + str(format(self.new_ammt, ',.2f')) + " Seconds "\
                "or " +str(format(self.new_ammt, '.2e')) + " Seconds.")



# TEMPERATURE WINDOW
    def temperature(self):
        self.temp_window = foo.Tk()
        self.temp_window.title("Temperature Conversion")

        self.top_frame = foo.Frame(self.temp_window)
        self.middle_top_frame = foo.Frame(self.temp_window)
        self.middle_frame = foo.Frame(self.temp_window)
        self.middle_bottom_frame = foo.Frame(self.temp_window)
        self.bottom_frame = foo.Frame(self.temp_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Temperature Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Fahrenheit', 'Celsius', 'Kelvin']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Temperature: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Temperature Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Fahrenheit', 'Celsius', 'Kelvin']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.temp_output_value = foo.StringVar()

        self.temp_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        
        self.temp_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.temp_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_temp)
        self.temp_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.temp_window.destroy)

        self.temp_calc_button.pack(side='left')
        self.temp_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()
##### ADD SCIENTIFIC NOTATION TO OUTPUT!!!!!!    
# TEMPERATURE CONVERSION FUNCTION
    def convert_temp(self):
        self.orig_widget = self.original_unit
        self.orig_temp_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_temp_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        
        if self.orig_temp_unit == self.new_temp_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")

        elif self.orig_temp_unit == 0 and self.new_temp_unit == 1:            
            self.new_ammt = (self.orig_ammt - 32) * 5/9
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Fahrenheit is " + str(format(self.new_ammt, ',.2f')) + " Celsius.")

        elif self.orig_temp_unit == 0 and self.new_temp_unit == 2:
            self.new_ammt = ((self.orig_ammt - 32) * 5/9) + 273.15
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Fahrenheit is " + str(format(self.new_ammt, ',.2f')) + " Kelvin.")
            
        elif self.orig_temp_unit == 1 and self.new_temp_unit == 0:
            self.new_ammt = ((self.orig_ammt) * 9/5) + 32
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Celsius is " + str(format(self.new_ammt, ',.2f')) + " Fahrenheit.")

        elif self.orig_temp_unit == 1 and self.new_temp_unit == 2:
            self.new_ammt = self.orig_ammt + 273.15
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Celsius is " + str(format(self.new_ammt, ',.2f')) + " Kelvin.")

        elif self.orig_temp_unit == 2 and self.new_temp_unit == 0:
            self.new_ammt = ((self.orig_ammt - 273.15) * 9/5) + 32
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kelvin is " + str(format(self.new_ammt, ',.2f')) + " Fahrenheit.")

        elif self.orig_temp_unit == 2 and self.new_temp_unit == 1:
            self.new_ammt = self.orig_ammt - 273.15
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kelvin is " + str(format(self.new_ammt, ',.2f')) + " Celsius.")


    def speed(self):
        self.speed_window = foo.Tk()
        self.speed_window.title("Speed Conversion")

        self.top_frame = foo.Frame(self.speed_window)
        self.middle_top_frame = foo.Frame(self.speed_window)
        self.middle_frame = foo.Frame(self.speed_window)
        self.middle_bottom_frame = foo.Frame(self.speed_window)
        self.bottom_frame = foo.Frame(self.speed_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Speed Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Miles Per Hour (MPH)', 'Feet Per Second (FPS)', 'Meters Per Second (MPS)', 'Kilometers Per Hour (KPH)', 'Knots (Kn)']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Speed: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Speed Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Miles Per Hour (MPH)', 'Feet Per Second (FPS)', 'Meters Per Second (MPS)', 'Kilometers Per Hour (KPH)', 'Knots (Kn)']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.speed_output_value = foo.StringVar()

        self.speed_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        

        self.speed_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.speed_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_speed)
        self.speed_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.speed_window.destroy)

        self.speed_calc_button.pack(side='left')
        self.speed_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()


    def convert_speed(self):
        self.orig_widget = self.original_unit
        self.orig_speed_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_speed_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        if self.orig_speed_unit == self.new_speed_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")

        elif self.orig_speed_unit == 0 and self.new_speed_unit == 1:            
            self.new_ammt = (self.orig_ammt * 5280) / 3600
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles Per Hour (MPH) is " + str(format(self.new_ammt, ',.2f')) + " Feet Per Second (FPS) " \
                "or " +str(format(self.new_ammt, '.2e')) + " Feet Per Second (FPS).")

        elif self.orig_speed_unit == 0 and self.new_speed_unit == 2:
            self.new_ammt = self.orig_ammt * .44704
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles Per Hour (MPH) is " + str(format(self.new_ammt, ',.2f')) + " Meters Per Second (MPS) " \
                "or " +str(format(self.new_ammt, '.2e')) + " Meters Per Second (MPS).")

        elif self.orig_speed_unit == 0 and self.new_speed_unit == 3:
            self.new_ammt = self.orig_ammt * 1.60934
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles Per Hour (MPH) is " + str(format(self.new_ammt, ',.2f')) + " Kilometers Per Hour (KPH) " \
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers Per Hour (KPH).")

        elif self.orig_speed_unit == 0 and self.new_speed_unit == 4:
            self.new_ammt = self.orig_ammt * 0.868976
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Miles Per Hour (MPH) is " + str(format(self.new_ammt, ',.2f')) + " Knots (Kn) " \
                "or " +str(format(self.new_ammt, '.2e')) + " Knots (Kn).")

        elif self.orig_speed_unit == 1 and self.new_speed_unit == 0:
            self.new_ammt = self.orig_ammt * 0.681818
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet Per Second (FPS) is " + str(format(self.new_ammt, ',.2f')) + " Miles Per Hour (MPH) " \
                "or " +str(format(self.new_ammt, '.2e')) + " Miles Per Hour (MPH).")

        elif self.orig_speed_unit == 1 and self.new_speed_unit == 2:
            self.new_ammt = self.orig_ammt * 0.3048
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet Per Second (FPS) is " + str(format(self.new_ammt, ',.2f')) + " Meters Per Second (MPS) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Meters Per Second (MPS).")

        elif self.orig_speed_unit == 1 and self.new_speed_unit == 3:
            self.new_ammt = self.orig_ammt * 1.09728
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet Per Second (FPS) is " + str(format(self.new_ammt, ',.2f')) + " Kilometers Per Hour (KPH) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers Per Hour (KPH).")

        elif self.orig_speed_unit == 1 and self.new_speed_unit == 4:
            self.new_ammt = self.orig_ammt * 0.592484
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Feet Per Second (FPS) is " + str(format(self.new_ammt, ',.2f')) + " Knots (Kn) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Knots (Kn).")

        elif self.orig_speed_unit == 2 and self.new_speed_unit == 0:
            self.new_ammt = self.orig_ammt * 2.23694
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters Per Second (MPS) is " + str(format(self.new_ammt, ',.2f')) + " Miles Per Hour (MPH) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Miles Per Hour (MPH).")

        elif self.orig_speed_unit == 2 and self.new_speed_unit == 1:
            self.new_ammt = self.orig_ammt * 3.28084
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters Per Second (MPS) is " + str(format(self.new_ammt, ',.2f')) + " Feet Per Second (FPS) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Feet Per Second (FPS).")

        elif self.orig_speed_unit == 2 and self.new_speed_unit == 3:
            self.new_ammt = self.orig_ammt * 3.6
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters Per Second (MPS) is " + str(format(self.new_ammt, ',.2f')) + " Kilometers Per Hour (KPH) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers Per Hour (KPH).")

        elif self.orig_speed_unit == 2 and self.new_speed_unit == 4:
            self.new_ammt = self.orig_ammt * 1.94384
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Meters Per Second (MPS) is " + str(format(self.new_ammt, ',.2f')) + " Knots (Kn) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Knots (Kn).")

        elif self.orig_speed_unit == 3 and self.new_speed_unit == 0:
            self.new_ammt = self.orig_ammt * 0.621371
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers Per Hour (KPH) is " + str(format(self.new_ammt, ',.2f')) + " Miles Per Hour (MPH) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Miles Per Hour (MPH).")

        elif self.orig_speed_unit == 3 and self.new_speed_unit == 1:
            self.new_ammt = self.orig_ammt * 0.911344
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers Per Hour (KPH) is " + str(format(self.new_ammt, ',.2f')) + " Feet Per Second (FPS) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Feet Per Second (FPS).")

        elif self.orig_speed_unit == 3 and self.new_speed_unit == 2:
            self.new_ammt = self.orig_ammt * 0.277778
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers Per Hour (KPH) is " + str(format(self.new_ammt, ',.2f')) + " Meters Per Second (MPS) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Meters Per Second (MPS).")

        elif self.orig_speed_unit == 3 and self.new_speed_unit == 4:
            self.new_ammt = self.orig_ammt * 0.539957
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilometers Per Hour (KPH) is " + str(format(self.new_ammt, ',.2f')) + " Knots (Kn) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Knots (Kn).")

        elif self.orig_speed_unit == 4 and self.new_speed_unit == 0:
            self.new_ammt = self.orig_ammt * 1.15078
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Knots (Kn) is " + str(format(self.new_ammt, ',.2f')) + " Miles Per Hour (MPH) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Miles Per Hour (MPH).")

        elif self.orig_speed_unit == 4 and self.new_speed_unit == 1:
            self.new_ammt = self.orig_ammt * 1.68781
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Knots (Kn) is " + str(format(self.new_ammt, ',.2f')) + " Feet Per Second (FPS) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Feet Per Second (FPS).")

        elif self.orig_speed_unit == 4 and self.new_speed_unit == 2:
            self.new_ammt = self.orig_ammt * 0.514444
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Knots (Kn) is " + str(format(self.new_ammt, ',.2f')) + " Meters Per Second (MPS) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Meters Per Second (MPS).")

        elif self.orig_speed_unit == 4 and self.new_speed_unit == 3:
            self.new_ammt = self.orig_ammt * 1.852
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Knots (Kn) is " + str(format(self.new_ammt, ',.2f')) + " Kilometers Per Hour (KPH) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilometers Per Hour (KPH).")

# PRESSURE WINDOW
    def pressure(self):
        self.press_window = foo.Tk()
        self.press_window.title("Pressure Conversion")

        self.top_frame = foo.Frame(self.press_window)
        self.middle_top_frame = foo.Frame(self.press_window)
        self.middle_frame = foo.Frame(self.press_window)
        self.middle_bottom_frame = foo.Frame(self.press_window)
        self.bottom_frame = foo.Frame(self.press_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Pressure Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Atmosphere (Atm)', 'Bar', 'Pascal (Pa)', 'Pounds Per Square Inch (PSI)', 'Torr']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Pressure: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Pressure Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Atmosphere (Atm)', 'Bar', 'Pascal (Pa)', 'Pounds Per Square Inch (PSI)', 'Torr']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.press_output_value = foo.StringVar()

        self.press_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        

        self.press_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.press_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_press)
        self.press_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.press_window.destroy)

        self.press_calc_button.pack(side='left')
        self.press_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()

# PRESSURE CONVERSION FUNCTION
    def convert_press(self):
        self.orig_widget = self.original_unit
        self.orig_press_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_press_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        if self.orig_press_unit == self.new_press_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")

        elif self.orig_press_unit == 0 and self.new_press_unit == 1:            
            self.new_ammt = self.orig_ammt * 1.01325
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Atmosphere (Atm) is " + str(format(self.new_ammt, ',.2f')) + " Bar " \
                "or " +str(format(self.new_ammt, '.2e')) + " Bar.")

        elif self.orig_press_unit == 0 and self.new_press_unit == 2:
            self.new_ammt = self.orig_ammt * 101325
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Atmosphere (Atm) is " + str(format(self.new_ammt, ',.2f')) + " Pascal (Pa) " \
                "or " +str(format(self.new_ammt, '.2e')) + " Pascal (Pa).")

        elif self.orig_press_unit == 0 and self.new_press_unit == 3:
            self.new_ammt = self.orig_ammt * 14.6959
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Atmosphere (Atm) is " + str(format(self.new_ammt, ',.2f')) + " Pounds Per Square Inch (PSI) " \
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds Per Square Inch (PSI).")

        elif self.orig_press_unit == 0 and self.new_press_unit == 4:
            self.new_ammt = self.orig_ammt * 760
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Atmosphere (Atm) is " + str(format(self.new_ammt, ',.2f')) + " Torr " \
                "or " +str(format(self.new_ammt, '.2e')) + " Torr.")

        elif self.orig_press_unit == 1 and self.new_press_unit == 0:
            self.new_ammt = self.orig_ammt * 0.986923
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Bar is " + str(format(self.new_ammt, ',.2f')) + " Atmosphere (Atm) " \
                "or " +str(format(self.new_ammt, '.2e')) + " Atmosphere (Atm).")

        elif self.orig_press_unit == 1 and self.new_press_unit == 2:
            self.new_ammt = self.orig_ammt * 100000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Bar is " + str(format(self.new_ammt, ',.2f')) + " Pascal (Pa) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pascal (Pa).")

        elif self.orig_press_unit == 1 and self.new_press_unit == 3:
            self.new_ammt = self.orig_ammt * 14.5038
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Bar is " + str(format(self.new_ammt, ',.2f')) + " Pounds Per Square Inch (PSI) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds Per Square Inch (PSI).")

        elif self.orig_press_unit == 1 and self.new_press_unit == 4:
            self.new_ammt = self.orig_ammt * 750.062
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Bar is " + str(format(self.new_ammt, ',.2f')) + " Torr "\
                "or " +str(format(self.new_ammt, '.2e')) + " Torr.")

        elif self.orig_press_unit == 2 and self.new_press_unit == 0:
            self.new_ammt = self.orig_ammt * 0.0000098692
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pascal (Pa) is " + str(format(self.new_ammt, ',.2f')) + " Atmosphere (Atm) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Atmosphere (Atm).")

        elif self.orig_press_unit == 2 and self.new_press_unit == 1:
            self.new_ammt = self.orig_ammt * 0.00001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pascal (Pa) is " + str(format(self.new_ammt, ',.2f')) + " Bar "\
                "or " +str(format(self.new_ammt, '.2e')) + " Bar.")

        elif self.orig_press_unit == 2 and self.new_press_unit == 3:
            self.new_ammt = self.orig_ammt * 0.000145038
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pascal (Pa) is " + str(format(self.new_ammt, ',.2f')) + " Pounds Per Square Inch (PSI) " \
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds Per Square Inch (PSI).")

        elif self.orig_press_unit == 2 and self.new_press_unit == 4:
            self.new_ammt = self.orig_ammt * 0.00750062
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pascal (Pa) is " + str(format(self.new_ammt, ',.2f')) + " Torr "\
                "or " +str(format(self.new_ammt, '.2e')) + " Torr.")

        elif self.orig_press_unit == 3 and self.new_press_unit == 0:
            self.new_ammt = self.orig_ammt * 0.068046
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds Per Square Inch (PSI) is " + str(format(self.new_ammt, ',.2f')) + " Atmosphere (Atm) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Atmosphere (Atm).")

        elif self.orig_press_unit == 3 and self.new_press_unit == 1:
            self.new_ammt = self.orig_ammt * 0.0689476
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds Per Square Inch (PSI) is " + str(format(self.new_ammt, ',.2f')) + " Bar "\
                "or " +str(format(self.new_ammt, '.2e')) + " Bar.")

        elif self.orig_press_unit == 3 and self.new_press_unit == 2:
            self.new_ammt = self.orig_ammt * 6894.76
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds Per Square Inch (PSI) is " + str(format(self.new_ammt, ',.2f')) + " Pascal (Pa) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pascal (Pa).")

        elif self.orig_press_unit == 3 and self.new_press_unit == 4:
            self.new_ammt = self.orig_ammt * 51.7149
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Pounds Per Square Inch (PSI) is " + str(format(self.new_ammt, ',.2f')) + " Torr "\
                "or " +str(format(self.new_ammt, '.2e')) + " Torr.")

        elif self.orig_press_unit == 4 and self.new_press_unit == 0:
            self.new_ammt = self.orig_ammt * 0.00131579
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Torr is " + str(format(self.new_ammt, ',.2f')) + " Atmosphere (Atm) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Atmosphere (Atm).")

        elif self.orig_press_unit == 4 and self.new_press_unit == 1:
            self.new_ammt = self.orig_ammt * 0.00133322
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Torr is " + str(format(self.new_ammt, ',.2f')) + " Bar "\
                "or " +str(format(self.new_ammt, '.2e')) + " Bar.")

        elif self.orig_press_unit == 4 and self.new_press_unit == 2:
            self.new_ammt = self.orig_ammt * 133.322
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Torr is " + str(format(self.new_ammt, ',.2f')) + " Pascal (Pa) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pascal (Pa).")

        elif self.orig_press_unit == 4 and self.new_press_unit == 3:
            self.new_ammt = self.orig_ammt * 0.0193368
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Torr is " + str(format(self.new_ammt, ',.2f')) + " Pounds Per Square Inch (PSI) "\
                "or " +str(format(self.new_ammt, '.2e')) + " Pounds Per Square Inch (PSI).")


    def energy(self):
        self.ener_window = foo.Tk()
        self.ener_window.title("Energy Conversion")

        self.top_frame = foo.Frame(self.ener_window)
        self.middle_top_frame = foo.Frame(self.ener_window)
        self.middle_frame = foo.Frame(self.ener_window)
        self.middle_bottom_frame = foo.Frame(self.ener_window)
        self.bottom_frame = foo.Frame(self.ener_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Energy Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Joule', 'Kilojoule', 'Gram Calorie', 'Kilocalorie', 'Watt Hour', 'Kilowatt Hour', 'BTU']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Energy: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Energy Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Joule', 'Kilojoule', 'Gram Calorie', 'Kilocalorie', 'Watt Hour', 'Kilowatt Hour', 'BTU']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.ener_output_value = foo.StringVar()

        self.ener_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        

        self.ener_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.ener_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_ener)
        self.ener_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.ener_window.destroy)

        self.ener_calc_button.pack(side='left')
        self.ener_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()


    def convert_ener(self):
        self.orig_widget = self.original_unit
        self.orig_ener_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_ener_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        if self.orig_ener_unit == self.new_ener_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")

        elif self.orig_ener_unit == 0 and self.new_ener_unit == 1:            
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Joules is " + str(format(self.new_ammt, ',.2f')) + " Kilojoules " \
                "or " +str(format(self.new_ammt, '.2e')) + " Kilojoules.")

        elif self.orig_ener_unit == 0 and self.new_ener_unit == 2:
            self.new_ammt = self.orig_ammt * 0.239006
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Joules is " + str(format(self.new_ammt, ',.2f')) + " Gram Calories " \
                "or " +str(format(self.new_ammt, '.2e')) + " Gram Calories.")

        elif self.orig_ener_unit == 0 and self.new_ener_unit == 3:
            self.new_ammt = self.orig_ammt * 0.000239006
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Joules is " + str(format(self.new_ammt, ',.2f')) + " Kilocalories " \
                "or " +str(format(self.new_ammt, '.2e')) + " Kilocalories.")

        elif self.orig_ener_unit == 0 and self.new_ener_unit == 4:
            self.new_ammt = self.orig_ammt * 0.000277778
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Joules is " + str(format(self.new_ammt, ',.2f')) + " Watt Hours " \
                "or " +str(format(self.new_ammt, '.2e')) + " Watt Hours.")

        elif self.orig_ener_unit == 0 and self.new_ener_unit == 5:
            self.new_ammt = self.orig_ammt * 0.00000027778
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Joules is " + str(format(self.new_ammt, ',.2f')) + " Kilowatt Hours " \
                "or " +str(format(self.new_ammt, '.2e')) + " Kilowatt Hours.")

        elif self.orig_ener_unit == 0 and self.new_ener_unit == 6:
            self.new_ammt = self.orig_ammt * 0.000947817
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Joules is " + str(format(self.new_ammt, ',.2f')) + " BTUs " \
                "or " +str(format(self.new_ammt, '.2e')) + " BTUs.")

        elif self.orig_ener_unit == 1 and self.new_ener_unit == 0:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilojoules is " + str(format(self.new_ammt, ',.2f')) + " Joules " \
                "or " +str(format(self.new_ammt, '.2e')) + " Joules.")

        elif self.orig_ener_unit == 1 and self.new_ener_unit == 2:
            self.new_ammt = self.orig_ammt * 239.006
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilojoules is " + str(format(self.new_ammt, ',.2f')) + " Gram Calories "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gram Calories.")

        elif self.orig_ener_unit == 1 and self.new_ener_unit == 3:
            self.new_ammt = self.orig_ammt * 0.239006
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilojoules is " + str(format(self.new_ammt, ',.2f')) + " Kilocalories "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilocalories.")

        elif self.orig_ener_unit == 1 and self.new_ener_unit == 4:
            self.new_ammt = self.orig_ammt * 0.277778
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilojoules is " + str(format(self.new_ammt, ',.2f')) + " Watt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Watt Hours.")

        elif self.orig_ener_unit == 1 and self.new_ener_unit == 5:
            self.new_ammt = self.orig_ammt * 0.000277778
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilojoules is " + str(format(self.new_ammt, ',.2f')) + " Kilowatt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilowatt Hours.")

        elif self.orig_ener_unit == 1 and self.new_ener_unit == 6:
            self.new_ammt = self.orig_ammt * 0.947817
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilojoules is " + str(format(self.new_ammt, ',.2f')) + " BTUs "\
                "or " +str(format(self.new_ammt, '.2e')) + " BTUs.")

        elif self.orig_ener_unit == 2 and self.new_ener_unit == 0:
            self.new_ammt = self.orig_ammt * 4.184
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gram Calorie is " + str(format(self.new_ammt, ',.2f')) + " Joules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Joules.")

        elif self.orig_ener_unit == 2 and self.new_ener_unit == 1:
            self.new_ammt = self.orig_ammt * 0.004184
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gram Calorie is " + str(format(self.new_ammt, ',.2f')) + " Kilojoules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilojoules.")

        elif self.orig_ener_unit == 2 and self.new_ener_unit == 3:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gram Calorie is " + str(format(self.new_ammt, ',.2f')) + " Kilocalories " \
                "or " +str(format(self.new_ammt, '.2e')) + " Kilocalories.")

        elif self.orig_ener_unit == 2 and self.new_ener_unit == 4:
            self.new_ammt = self.orig_ammt * 0.00116222
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gram Calorie is " + str(format(self.new_ammt, ',.2f')) + " Watt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Watt Hours.")

        elif self.orig_ener_unit == 2 and self.new_ener_unit == 5:
            self.new_ammt = self.orig_ammt * 0.0000011622
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gram Calorie is " + str(format(self.new_ammt, ',.2f')) + " Kilowatt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilowatt Hours.")

        elif self.orig_ener_unit == 2 and self.new_ener_unit == 6:
            self.new_ammt = self.orig_ammt * 0.00396567
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gram Calorie is " + str(format(self.new_ammt, ',.2f')) + " BTUs "\
                "or " +str(format(self.new_ammt, '.2e')) + " BTUs.")

        elif self.orig_ener_unit == 3 and self.new_ener_unit == 0:
            self.new_ammt = self.orig_ammt * 4184
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilocalories is " + str(format(self.new_ammt, ',.2f')) + " Joules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Joules.")

        elif self.orig_ener_unit == 3 and self.new_ener_unit == 1:
            self.new_ammt = self.orig_ammt * 4.184
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilocalories is " + str(format(self.new_ammt, ',.2f')) + " Kilojoules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilojoules.")

        elif self.orig_ener_unit == 3 and self.new_ener_unit == 2:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilocalories is " + str(format(self.new_ammt, ',.2f')) + " Gram Calories "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gram Calories.")

        elif self.orig_ener_unit == 3 and self.new_ener_unit == 4:
            self.new_ammt = self.orig_ammt * 1.16222
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilocalories is " + str(format(self.new_ammt, ',.2f')) + " Watt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Watt Hours.")

        elif self.orig_ener_unit == 3 and self.new_ener_unit == 5:
            self.new_ammt = self.orig_ammt * 0.00116222
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilocalories is " + str(format(self.new_ammt, ',.2f')) + " Kilowatt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilowatt Hours.")

        elif self.orig_ener_unit == 3 and self.new_ener_unit == 6:
            self.new_ammt = self.orig_ammt * 3.96567
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilocalories is " + str(format(self.new_ammt, ',.2f')) + " BTUs "\
                "or " +str(format(self.new_ammt, '.2e')) + " BTUs.")

        elif self.orig_ener_unit == 4 and self.new_ener_unit == 0:
            self.new_ammt = self.orig_ammt * 3600
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Watt Hours is " + str(format(self.new_ammt, ',.2f')) + " Joules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Joules.")

        elif self.orig_ener_unit == 4 and self.new_ener_unit == 1:
            self.new_ammt = self.orig_ammt * 3.6
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Watt Hours is " + str(format(self.new_ammt, ',.2f')) + " Kilojoules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilojoules.")

        elif self.orig_ener_unit == 4 and self.new_ener_unit == 2:
            self.new_ammt = self.orig_ammt * 860.421
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Watt Hours is " + str(format(self.new_ammt, ',.2f')) + " Gram Calories "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gram Calories.")

        elif self.orig_ener_unit == 4 and self.new_ener_unit == 3:
            self.new_ammt = self.orig_ammt * 0.860421
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Watt Hours is " + str(format(self.new_ammt, ',.2f')) + " Kilocalories "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilocalories.")

        elif self.orig_ener_unit == 4 and self.new_ener_unit == 5:
            self.new_ammt = self.orig_ammt * 0.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Watt Hours is " + str(format(self.new_ammt, ',.2f')) + " Kilowatt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilowatt Hours.")

        elif self.orig_ener_unit == 4 and self.new_ener_unit == 6:
            self.new_ammt = self.orig_ammt * 3.41214
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Watt Hours is " + str(format(self.new_ammt, ',.2f')) + " BTUs "\
                "or " +str(format(self.new_ammt, '.2e')) + " BTUs.")

        elif self.orig_ener_unit == 5 and self.new_ener_unit == 0:
            self.new_ammt = self.orig_ammt * 3600000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilowatt Hours is " + str(format(self.new_ammt, ',.2f')) + " Joules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Joules.")

        elif self.orig_ener_unit == 5 and self.new_ener_unit == 1:
            self.new_ammt = self.orig_ammt * 3600
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilowatt Hours is " + str(format(self.new_ammt, ',.2f')) + " Kilojoules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilojoules.")

        elif self.orig_ener_unit == 5 and self.new_ener_unit == 2:
            self.new_ammt = self.orig_ammt * 860421
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilowatt Hours is " + str(format(self.new_ammt, ',.2f')) + " Gram Calories "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gram Calories.")

        elif self.orig_ener_unit == 5 and self.new_ener_unit == 3:
            self.new_ammt = self.orig_ammt * 860.421
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilowatt Hours is " + str(format(self.new_ammt, ',.2f')) + " Kilocalories "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilocalories.")

        elif self.orig_ener_unit == 5 and self.new_ener_unit == 4:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilowatt Hours is " + str(format(self.new_ammt, ',.2f')) + " Watt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Watt Hours.")

        elif self.orig_ener_unit == 5 and self.new_ener_unit == 6:
            self.new_ammt = self.orig_ammt * 3412.14
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilowatt Hours is " + str(format(self.new_ammt, ',.2f')) + " BTUs "\
                "or " +str(format(self.new_ammt, '.2e')) + " BTUs.")

        elif self.orig_ener_unit == 6 and self.new_ener_unit == 0:
            self.new_ammt = self.orig_ammt * 1055.06
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " BTUs is " + str(format(self.new_ammt, ',.2f')) + " Joules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Joules.")

        elif self.orig_ener_unit == 6 and self.new_ener_unit == 1:
            self.new_ammt = self.orig_ammt * 1.05506
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " BTUs is " + str(format(self.new_ammt, ',.2f')) + " Kilojoules "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilojoules.")

        elif self.orig_ener_unit == 6 and self.new_ener_unit == 2:
            self.new_ammt = self.orig_ammt * 252.164
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " BTUs is " + str(format(self.new_ammt, ',.2f')) + " Gram Calories "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gram Calories.")

        elif self.orig_ener_unit == 6 and self.new_ener_unit == 3:
            self.new_ammt = self.orig_ammt * 0.252164
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " BTUs is " + str(format(self.new_ammt, ',.2f')) + " Kilocalories "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilocalories.")

        elif self.orig_ener_unit == 6 and self.new_ener_unit == 4:
            self.new_ammt = self.orig_ammt * 0.293071
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " BTUs is " + str(format(self.new_ammt, ',.2f')) + " Watt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Watt Hours.")

        elif self.orig_ener_unit == 6 and self.new_ener_unit == 5:
            self.new_ammt = self.orig_ammt * 0.000293071
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " BTUs is " + str(format(self.new_ammt, ',.2f')) + " Kilowatt Hours "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilowatt Hours.")


# FREQUENNCY WINDOW
    def frequency(self):
        self.freq_window = foo.Tk()
        self.freq_window.title("Frequency Conversion")

        self.top_frame = foo.Frame(self.freq_window)
        self.middle_top_frame = foo.Frame(self.freq_window)
        self.middle_frame = foo.Frame(self.freq_window)
        self.middle_bottom_frame = foo.Frame(self.freq_window)
        self.bottom_frame = foo.Frame(self.freq_window)

        # TOP FRAME

        self.prompt_label = foo.Label(self.top_frame, text="Original Frequency Unit: ")
        
        self.original_unit = foo.Listbox(self.top_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.scrollbar = foo.Scrollbar(self.top_frame, orient='vertical', command=self.original_unit.yview)

        
        for item in ['Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz']:
            self.original_unit.insert(foo.END, item)  

        self.original_unit.config(yscrollcommand=self.scrollbar)     

        self.prompt_label.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')
        self.original_unit.pack(side='left')

        # MIDDLE TOP FRAME

        self.middle_top_prompt_label = foo.Label(self.middle_top_frame, text="Enter the Frequency: ")
        self.middle_top_entry = foo.Entry(self.middle_top_frame, width="25")

        self.middle_top_prompt_label.pack(side='left')
        self.middle_top_entry.pack(side='left')

        # MIDDLE FRAME

        self.middle_prompt_label = foo.Label(self.middle_frame, text="New Frequency Unit: ")
        
        self.new_unit = foo.Listbox(self.middle_frame, selectmode="SINGLE", height="1", width="25", yscrollcommand=foo.Scrollbar.set, exportselection=0)
        self.middle_scrollbar = foo.Scrollbar(self.middle_frame, orient='vertical', command=self.new_unit.yview)

        
        for item in ['Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz']:
            self.new_unit.insert(foo.END, item)  

        self.new_unit.config(yscrollcommand=self.middle_scrollbar)

        self.middle_prompt_label.pack(side='left')
        self.middle_scrollbar.pack(side='right', fill='y')
        self.new_unit.pack(side='left')

        # MIDDLE BOTTOM FRAME

        self.freq_output_value = foo.StringVar()

        self.freq_desc_label = foo.Label(self.middle_bottom_frame, text='Be sure to click both scrollbar entries, then click "Convert".')
        

        self.freq_desc_label.pack(side='left')
        
        # BOTTOM FRAME

        self.freq_calc_button = foo.Button(self.bottom_frame, text='Convert', command=self.convert_freq)
        self.freq_quit_button = foo.Button(self.bottom_frame, text='Quit', command= self.freq_window.destroy)

        self.freq_calc_button.pack(side='left')
        self.freq_quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_top_frame.pack()
        self.middle_frame.pack()
        self.middle_bottom_frame.pack()
        self.bottom_frame.pack()

        foo.mainloop()

# FREQUENCY CONVERSION FUNCTION
    def convert_freq(self):
        self.orig_widget = self.original_unit
        self.orig_freq_unit = int(self.orig_widget.curselection()[0])
        self.new_widget = self.new_unit
        self.new_freq_unit = int(self.new_widget.curselection()[0])
        self.orig_ammt_widget = self.middle_top_entry
        self.orig_ammt = float(self.orig_ammt_widget.get())

        if self.orig_freq_unit == self.new_freq_unit:
            tkinter.messagebox.showinfo("Result", "You have selected the same unit, please try again.")
        elif self.orig_freq_unit == 0 and self.new_freq_unit == 1:            
            self.new_ammt = self.orig_ammt *.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hertz is " + str(format(self.new_ammt, ',.2f')) + " Kilohertz " \
                "or " +str(format(self.new_ammt, '.2e')) + " Kilohertz.")
        elif self.orig_freq_unit == 0 and self.new_freq_unit == 2:
            self.new_ammt = self.orig_ammt * .000001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hertz is " + str(format(self.new_ammt, ',.2f')) + " Megahertz " \
                "or " +str(format(self.new_ammt, '.2e')) + " Megahertz.")
        elif self.orig_freq_unit == 0 and self.new_freq_unit == 3:
            self.new_ammt = self.orig_ammt * .000000001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Hertz is " + str(format(self.new_ammt, ',.2f')) + " Gigahertz " \
                "or " +str(format(self.new_ammt, '.2e')) + " Gigahertz.")
        elif self.orig_freq_unit == 1 and self.new_freq_unit == 0:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilohertz is " + str(format(self.new_ammt, ',.2f')) + " Hertz " \
                "or " +str(format(self.new_ammt, '.2e')) + " Hertz.")
        elif self.orig_freq_unit == 1 and self.new_freq_unit == 2:
            self.new_ammt = self.orig_ammt *.001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilohertz is " + str(format(self.new_ammt, ',.2f')) + " Megahertz "\
                "or " +str(format(self.new_ammt, '.2e')) + " Megahertz.")
        elif self.orig_freq_unit == 1 and self.new_freq_unit == 3:
            self.new_ammt = self.orig_ammt *.000001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Kilohertz is " + str(format(self.new_ammt, ',.2f')) + " Gigahertz "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gigahertz.")
        elif self.orig_freq_unit == 2 and self.new_freq_unit == 0:
            self.new_ammt = self.orig_ammt * 1000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Megahertz is " + str(format(self.new_ammt, ',.2f')) + " Hertz "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hertz.")
        elif self.orig_freq_unit == 2 and self.new_freq_unit == 1:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Megahertz is " + str(format(self.new_ammt, ',.2f')) + " Kilohertz "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilohertz.")
        elif self.orig_freq_unit == 2 and self.new_freq_unit == 3:
            self.new_ammt = self.orig_ammt * .001
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Megahertz is " + str(format(self.new_ammt, ',.2f')) + " Gigahertz "\
                "or " +str(format(self.new_ammt, '.2e')) + " Gigahertz.")
        elif self.orig_freq_unit == 3 and self.new_freq_unit == 0:
            self.new_ammt = self.orig_ammt * 1000000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gigahertz is " + str(format(self.new_ammt, ',.2f')) + " Hertz "\
                "or " +str(format(self.new_ammt, '.2e')) + " Hertz.")
        elif self.orig_freq_unit == 3 and self.new_freq_unit == 1:
            self.new_ammt = self.orig_ammt * 1000000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gigahertz is " + str(format(self.new_ammt, ',.2f')) + " Kilohertz "\
                "or " +str(format(self.new_ammt, '.2e')) + " Kilohertz.")
        elif self.orig_freq_unit == 3 and self.new_freq_unit == 2:
            self.new_ammt = self.orig_ammt * 1000
            tkinter.messagebox.showinfo("Result", str(self.orig_ammt) + " Gigahertz is " + str(format(self.new_ammt, ',.2f')) + " Megahertz "\
                "or " +str(format(self.new_ammt, '.2e')) + " Megahertz.")
        

unitconversion = UnitConversion()

