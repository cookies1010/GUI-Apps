import tkinter as tk
from tkinter import filedialog


class NotesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notes App")
        self.geometry("400x300")

        self.text_area = tk.Text(self, wrap="word")
        self.text_area.pack(expand=True, fill="both")

        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.open_note)
        self.file_menu.add_command(label="Open", command=self.open_note)
        self.file_menu.add_command(label="Save", command=self.save_note)
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menu_bar)

        self.current_file = None

    def new_note(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None

    def open_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.current_file = file_path

    def save_note(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
            )
            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.current_file = file_path


if __name__ == "__main__":
    app = NotesApp()
    app.mainloop()
