import tkinter as tk

class KeyboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard TextInput GUI")

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.grid(row=0, column=0, columnspan=10)

        self.create_keyboard()

    def create_keyboard(self):
        buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', 'Clear'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.root, text=button, width=5, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 9:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'Clear':
            self.text_entry.delete(0, tk.END)
        else:
            current_text = self.text_entry.get()
            new_text = current_text + char
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(0, new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyboardApp(root)
    root.mainloop()
