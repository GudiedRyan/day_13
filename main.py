import tkinter

FONT = ("Arial", 12, "normal")

window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=20,pady=20)

# Label at grid(column=0, row=1)

equal_label = tkinter.Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

# entry box at (column=1, row=0)
input_miles = tkinter.Entry(width=15)
input_miles.grid(column=1, row=0)

# miles label at col 2 row 0
miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

# km label at col 2 row 1
km_label = tkinter.Label(text="km", font=FONT)
km_label.grid(column=2, row=1)

#conversion label at col 1 row 1
result_label = tkinter.Label(text="", font=FONT)
result_label.grid(column=1, row=1)

# calculate button at col 1 row 2

def converter():
    miles = input_miles.get()
    prepped_miles = float(miles)*1.60934
    result_label.config(text=f"{prepped_miles}")

calculate_button = tkinter.Button(text="Calculate", font=FONT, command=converter)
calculate_button.grid(column=1, row=2)

window.mainloop()