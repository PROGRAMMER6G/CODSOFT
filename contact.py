import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to add a new contact to the contact list
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        contact_list.insert("", tk.END, values=(name, phone))
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Both name and phone number are required!")

# Function to delete the selected contact from the contact list
def delete_contact():
    selected_contact = contact_list.selection()
    if selected_contact:
        contact_list.delete(selected_contact)

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.configure(bg='#1874CD')
root.resizable(0,0)

# Create and configure a style for ttk widgets
style = ttk.Style()
style.configure("TButton", background="#4CAF50", font=("Helvetica", 14))
style.configure("Delete.TButton", background="#F44336")
style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))

# Create and configure input fields and labels
name_label = ttk.Label(root, text="Name:",font=14,background="#1874CD")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = ttk.Entry(root,font=('Arial',16))
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = ttk.Label(root, text="Phone:",font=14,background="#1874CD")
phone_label.grid(row=1, column=0, padx=10, pady=5)
phone_entry = ttk.Entry(root,font=('Arial',16))
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# Create buttons for adding and deleting contacts
delete_button = ttk.Button(root, text="Delete Contact", style="Delete.TButton", command=delete_contact)
delete_button.grid(row=2, column=0, pady=10, padx=10, sticky="we")

add_button = ttk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=1, pady=10, padx=10, sticky="we")

# Create and configure the contact list
contact_list = ttk.Treeview(root, columns=("Name", "Phone"), show="headings", selectmode="extended")
contact_list.heading("Name", text="Name")
contact_list.heading("Phone", text="Phone")
contact_list.column("Name", width=200)
contact_list.column("Phone", width=150)
contact_list.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

# Add a vertical scrollbar to the contact list
scrollbar = ttk.Scrollbar(root, orient="vertical", command=contact_list.yview)
scrollbar.grid(row=4, column=2, sticky="ns")
contact_list.configure(yscrollcommand=scrollbar.set)

# Start the GUI main loop
root.mainloop()
