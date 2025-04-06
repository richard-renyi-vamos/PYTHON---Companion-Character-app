import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageSequence

class AvatarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF Avatar")
        self.root.geometry("250x250")
        self.root.configure(bg='black')
        self.root.overrideredirect(False)  # allows dragging
        self.root.attributes('-topmost', False)

        # Avatar GIF path
        self.gif_path = "avatar.gif"  # Replace with your default gif

        # Load and display the GIF
        self.label = tk.Label(self.root, bg='black')
        self.label.pack(expand=True)

        self.frames = []
        self.load_gif(self.gif_path)
        self.current_frame = 0
        self.play_gif()

        # Right-click menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Toggle Always on Top", command=self.toggle_always_on_top)
        self.menu.add_command(label="Settings", command=self.open_settings)
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=root.quit)

        self.root.bind("<Button-3>", self.show_menu)

    def show_menu(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    def load_gif(self, path):
        img = Image.open(path)
        self.frames = [ImageTk.PhotoImage(frame.copy().convert('RGBA')) for frame in ImageSequence.Iterator(img)]

    def play_gif(self):
        if self.frames:
            self.label.config(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.root.after(100, self.play_gif)

    def toggle_always_on_top(self):
        is_topmost = self.root.attributes('-topmost')
        self.root.attributes('-topmost', not is_topmost)

    def open_settings(self):
        settings = tk.Toplevel(self.root)
        settings.title("Settings")
        settings.geometry("300x200")

        def change_gif():
            new_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
            if new_path:
                self.gif_path = new_path
                self.load_gif(new_path)

        ttk.Button(settings, text="Change Avatar GIF", command=change_gif).pack(pady=10)
        ttk.Label(settings, text="More settings coming soon... 😺").pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = AvatarApp(root)
    root.mainloop()
