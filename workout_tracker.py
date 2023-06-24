# Marshall Ferguson - 6/2023

# Imports

import tkinter as tk

window = tk.Tk()

window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

lbl_exercise_name = tk.Label(master=window, text='Exercise Name')
ent_exercise_name = tk.Entry()
exercise_name = ent_exercise_name.get()
lbl_exercise_name.grid(row=0, column=0, sticky='nsew')

frm_weight = tk.Frame(master=window)
frm_weight.grid(row=1, column=0)
frm_weight.rowconfigure([0, 1], minsize=50, weight=1)
frm_weight.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl_weight = tk.Label(master=frm_weight, text='Weight (lbs)')
lbl_weight.grid(row=0, column=1)

btn_decrease_weight = tk.Button(master=frm_weight, text='-')
btn_decrease_weight.grid(row=1, column=0, sticky='nsew')

lbl_weight_value = tk.Label(master=frm_weight, text='0')
lbl_weight_value.grid(row=1, column=1)

btn_increase_weight = tk.Button(master=frm_weight, text='+')
btn_increase_weight.grid(row=1, column=2, sticky='nsew')

frm_reps = tk.Frame(master=window)
frm_reps.grid(row=2, column=0)
frm_reps.rowconfigure([0, 1], minsize=50, weight=1)
frm_reps.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl_reps = tk.Label(master=frm_reps, text='Reps')
lbl_reps.grid(row=0, column=1)

btn_decrease_reps = tk.Button(master=frm_reps, text='-')
btn_decrease_reps.grid(row=1, column=0, sticky='nsew')

lbl_reps_value = tk.Label(master=frm_reps, text='0')
lbl_reps_value.grid(row=1, column=1)

btn_increase_reps = tk.Button(master=frm_reps, text='+')
btn_increase_reps.grid(row=1, column=2, sticky='nsew')

window.mainloop()
