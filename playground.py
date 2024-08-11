# playground.py
#Open GNOMEX
import tkinter as tk
from tkinter import scrolledtext
from core import execute_code

class PythonPlayground:
    def __init__(self, root):
        self.root = root
        self.root.title("Open GnomeX Playground")
        
        # Create code input area
        self.code_input = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=20, width=70)
        self.code_input.pack(pady=10)
        
        # Create a button to run the code
        self.run_button = tk.Button(self.root, text="Run Code", command=self.run_code)
        self.run_button.pack(pady=5)
        
        # Create output display area
        self.output_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=10, width=70, state='disabled')
        self.output_display.pack(pady=10)
        self.output_display.pack(padx=10) 
        
        
        # Automatically run code on input change
        self.code_input.bind("<KeyRelease>", self.run_code)

    def run_code(self, event=None):
        # Get the code from the input area
        code = self.code_input.get("1.0", tk.END)
        
        # Execute the code and capture output
        output = execute_code(code)
        
        # Display the output
        self.output_display.config(state='normal')
        self.output_display.delete("1.0", tk.END)
        self.output_display.insert(tk.END, output)
        self.output_display.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    playground = PythonPlayground(root)
    root.mainloop()
