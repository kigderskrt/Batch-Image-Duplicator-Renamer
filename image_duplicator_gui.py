# file: image_duplicator_gui.py

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageDuplicatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Image Duplicator and Renamer")
        self.image_paths = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.upload_btn = tk.Button(self.frame, text="Upload Images", command=self.upload_images)
        self.upload_btn.grid(row=0, column=0, pady=5)

        self.images_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.BROWSE)
        self.images_listbox.grid(row=1, column=0, pady=5)

        self.code_label = tk.Label(self.frame, text="Enter Codes (comma or newline separated):")
        self.code_label.grid(row=2, column=0, sticky="w")

        self.code_text = tk.Text(self.frame, height=6, width=50)
        self.code_text.grid(row=3, column=0, pady=5)

        self.rename_btn = tk.Button(self.frame, text="Duplicate and Rename", command=self.duplicate_and_rename)
        self.rename_btn.grid(row=4, column=0, pady=10)

        self.preview_btn = tk.Button(self.frame, text="Preview Output Filenames", command=self.preview_output)
        self.preview_btn.grid(row=5, column=0, pady=5)

        self.move_up_btn = tk.Button(self.frame, text="Move Up", command=self.move_up)
        self.move_up_btn.grid(row=7, column=0, pady=5, sticky="w")

        self.move_down_btn = tk.Button(self.frame, text="Move Down", command=self.move_down)
        self.move_down_btn.grid(row=7, column=0, pady=5, sticky="e")

    def upload_images(self):
        paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
        if paths:
            self.image_paths = list(paths)
            self.images_listbox.delete(0, tk.END)
            for path in self.image_paths:
                self.images_listbox.insert(tk.END, os.path.basename(path))

    def get_codes(self):
        raw = self.code_text.get("1.0", tk.END).strip()
        split_codes = [line.strip().replace(',', '') for line in raw.replace(',', '\n').splitlines() if line.strip()]
        return split_codes

    def preview_output(self):
        codes = self.get_codes()
        if not self.image_paths:
            messagebox.showerror("Error", "Please upload images first.")
            return
        if not codes:
            messagebox.showerror("Error", "Please enter code(s).")
            return

        preview = []
        for code in codes:
            for idx in range(len(self.image_paths)):
                suffix = f"_{idx}" if idx else ""
                filename = f"04-{code}{suffix}.jpg"
                preview.append(filename)

        messagebox.showinfo("Preview Filenames", "\n".join(preview))

    def duplicate_and_rename(self):
        codes = self.get_codes()
        if not self.image_paths:
            messagebox.showerror("Error", "Please upload images first.")
            return
        if not codes:
            messagebox.showerror("Error", "Please enter code(s).")
            return

        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        for code in codes:
            for idx, img_path in enumerate(self.image_paths):
                suffix = f"_{idx}" if idx else ""
                new_filename = f"04-{code}{suffix}.jpg"
                output_path = os.path.join(output_dir, new_filename)
                shutil.copy(img_path, output_path)

        messagebox.showinfo("Success", f"Duplicated and renamed images saved in '{output_dir}' folder.")

    def move_up(self):
        selected = self.images_listbox.curselection()
        if not selected:
            return
        index = selected[0]
        if index > 0:
            self.image_paths[index], self.image_paths[index - 1] = self.image_paths[index - 1], self.image_paths[index]
            self.update_listbox()
            self.images_listbox.select_set(index - 1)

    def move_down(self):
        selected = self.images_listbox.curselection()
        if not selected:
            return
        index = selected[0]
        if index < len(self.image_paths) - 1:
            self.image_paths[index], self.image_paths[index + 1] = self.image_paths[index + 1], self.image_paths[index]
            self.update_listbox()
            self.images_listbox.select_set(index + 1)

    def update_listbox(self):
        self.images_listbox.delete(0, tk.END)
        for path in self.image_paths:
            self.images_listbox.insert(tk.END, os.path.basename(path))

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageDuplicatorGUI(root)
    root.mainloop()
