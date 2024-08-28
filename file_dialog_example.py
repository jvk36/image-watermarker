import tkinter as tk
from tkinter import filedialog

def open_file():
    # Open the file dialog
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("All files", "*.*")
        ]
    )
    
    # If a file was selected (i.e., the user didn't cancel)
    if file_path:
        # Update the label with the selected file path
        selected_file_label.config(text=f"Selected file: {file_path}")
        
        # Here you can add code to read or process the file
        # For example:
        # with open(file_path, 'r') as file:
        #     content = file.read()
        #     print(content)

# Create the main window
root = tk.Tk()
root.title("File Open Dialog Example")
root.geometry("400x200")

# Create and pack a button to open the file dialog
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=20)

# Create and pack a label to display the selected file
selected_file_label = tk.Label(root, text="No file selected", wraplength=380)
selected_file_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
