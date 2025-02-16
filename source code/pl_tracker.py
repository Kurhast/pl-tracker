import tkinter as tk
from tkinter import messagebox

def copy_to_clipboard():
    formatted_texts = []
    for i in range(len(name_entries)):
        name = name_entries[i].get().strip()
        num1 = num1_entries[i].get().strip()
        num2 = num2_entries[i].get().strip()
        
        if name and num1.isdigit() and num2.isdigit():
            if 0 <= int(num1) <= 10 and 0 <= int(num2) <= 10:
                formatted_texts.append(f"{name} {num1}/{num2} - ")
            else:
                messagebox.showerror("ERREUR", "Nombre entre 0 et 10!")
                return
        elif name:
            messagebox.showerror("ERREUR", "Nombre entre 0 et 10!")
            return
    
    if formatted_texts:
        formatted_text = "\n".join(formatted_texts)
        root.clipboard_clear()
        root.clipboard_append(formatted_text)
        root.update()
        messagebox.showinfo("SUCCES", "Copier !")

def clear_entries():
    for entry in name_entries + num1_entries + num2_entries:
        entry.delete(0, tk.END)

def increment_num1():
    payers = []
    for i in range(len(num1_entries)):
        if num1_entries[i].get().isdigit() and num2_entries[i].get().isdigit():
            num1 = int(num1_entries[i].get())
            num2 = int(num2_entries[i].get())
            if num1 < 10:
                num1 += 1
                num1_entries[i].delete(0, tk.END)
                num1_entries[i].insert(0, str(num1))
            if num1 == num2:
                payers.append(name_entries[i].get())
                clear_row(i)
    
    if payers:
        messagebox.showinfo("PAIEMENT", ", ".join(payers) + " doit payer")

def clear_row(index):
    name_entries[index].delete(0, tk.END)
    num1_entries[index].delete(0, tk.END)
    num2_entries[index].delete(0, tk.END)

def delete_row(index):
    clear_row(index)

root = tk.Tk()
root.title("PL Tracker")
root.geometry("500x400")

frame = tk.Frame(root)
frame.pack(pady=10)

name_entries = []
num1_entries = []
num2_entries = []
delete_buttons = []

for i in range(7):
    row_frame = tk.Frame(frame)
    row_frame.pack(pady=2)
    
    name_entry = tk.Entry(row_frame, width=20)
    name_entry.pack(side=tk.LEFT, padx=5)
    name_entries.append(name_entry)
    
    num1_entry = tk.Entry(row_frame, width=5)
    num1_entry.pack(side=tk.LEFT, padx=5)
    num1_entries.append(num1_entry)
    
    num2_entry = tk.Entry(row_frame, width=5)
    num2_entry.pack(side=tk.LEFT, padx=5)
    num2_entries.append(num2_entry)
    
    delete_button = tk.Button(row_frame, text="X", command=lambda i=i: delete_row(i))
    delete_button.pack(side=tk.LEFT, padx=5)
    delete_buttons.append(delete_button)

copy_button = tk.Button(root, text="Copier texte", command=copy_to_clipboard)
copy_button.pack(pady=5)

clear_button = tk.Button(root, text="Tout effacer", command=clear_entries)
clear_button.pack(pady=5)

increment_button = tk.Button(root, text="+1 combat", command=increment_num1)
increment_button.pack(pady=5)

root.mainloop()

