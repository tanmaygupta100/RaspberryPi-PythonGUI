# /usr/bin/python3
# form_tkinter.py by Tanmay Gupta
# This is a lab file that creates a feedback form, incorporating the following:
    # Dropdown menu: 5 country choices
    # Free-text field
    # Checkbox answers
    # Radiobutton answers
    # Clear button to clear form
    # Submit button to dump user responses in console


from tkinter import *
from tkinter import ttk


#Storing the window in a variable and creating it:
root = Tk()
root.title("Feedback Form") # setting a title for the feedback window.


#Function for creating empty lines:
def emptyline(root):
    empty_space = ttk.Label(root, text='')
    empty_space.pack()


#Top label
feedback_label = ttk.Label(root, text = 'Hi, friend!' + '\n' + 'Please fill give us feedback on our services!', justify="center")
feedback_label.pack()



#Label to display the connection message:
emptyline(root)
connection_label = ttk.Label(root, text="") # Description is initialized as empty
connection_label.pack(anchor="center")
#Function that will insert the received user input for country into pop-up label:
def update_connection_label():
    selected_country = country.get()
    if selected_country:
        connection_message = f"[You are now connected to our {selected_country} branch...]"
        connection_label.config(text=connection_message)


#Selecting country, with drop-down list:
emptyline(root) # empty line
country_question = ttk.Label(root, text = 'Which country are you located in?')
country_question.pack(anchor="w")
# COMBOBOX WIDGET:
country = StringVar() # 'country' string.
combobox = ttk.Combobox(root, textvariable = country)
combobox.pack(anchor="w")
combobox.config(values = ('USA', 'Canada', 'Spain', 'India',
                          'China', 'France', 'Russia', 'Egypt'))
combobox.bind("<<ComboboxSelected>>", lambda event: update_connection_label())
    # update the connection_label once a selection is made.


#Entering email, with free-text field:
name_question = ttk.Label(root, text = 'What is your email?')
name_question.pack(anchor="w")
# ENTRY WIDGET:
name = StringVar() # 'name' string.
entry = ttk.Entry(root, width = 30, textvariable = name) # field is 30 characters wide.
entry.pack(anchor="w")


#Sharing if you'd recommend the service, with checkbuttons:
emptyline(root) # empty line
rec_question = ttk.Label(root, text = 'Would you recommend us to others?')
rec_question.pack(anchor="w")
# CHECKBUTTON WIDGET:
rec = StringVar() # 'rec' string.
checkbutton = ttk.Checkbutton(root, text = 'Would recommend', variable = rec,
                              onvalue = "Would recommend", offvalue = "Would not recommend")
checkbutton.pack(anchor="w")


#Selecting satisfaction level, with radiobuttons:
emptyline(root) # empty line
rate_question = ttk.Label(root, text = 'How satisfied were you?')
rate_question.pack(anchor="w")
# RADIOBUTTON WIDGET:
rate = StringVar() # 'rate' string.
ttk.Radiobutton(root, text = 'Satisfied', variable = rate,
                value = 'Satisfied').pack(anchor="w")
ttk.Radiobutton(root, text = 'Neutral', variable = rate,
                value = 'Neutral').pack(anchor="w")
ttk.Radiobutton(root, text = 'Dissatisfied', variable = rate,
                value = 'Dissatisfied').pack(anchor="w")


emptyline(root) # empty line

#Clearing the form:
clear_button = ttk.Button(root, text="Clear form",
                          command=lambda: (country.set(''),
                                           name.set(''),
                                           rec.set(''),
                                           rate.set(''),
                                           connection_label.config(text="")
                                           ))
clear_button.pack()


#Submitting the form and printing the values:
print_submit_button = ttk.Button(root, text = "Submit form",
                          command=lambda: print('Your country:', country.get()
                                                + '\n'
                                                + 'Your email:', name.get()
                                                + '\n'
                                                + 'Your recommendation:', rec.get()
                                                + '\n'
                                                + 'Your rating:', rate.get()
                                                ))
print_submit_button.pack()


root.mainloop()

'''
SAMPLE OUTPUT:
____________________________________
Your country: Canada
Your email: tqg5283@psu.edu
Your recommendation: Would recommend
Your rating: Satisfied
____________________________________
'''
