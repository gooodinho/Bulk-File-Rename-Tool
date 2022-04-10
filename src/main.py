import tkinter as tk
from tkinter import ttk

from service import load_files, rename


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Renamer")
        self.geometry("840x720")
        self.resizable(False, False)

        s = ttk.Style()
        s.configure('Yellow.TFrame', background='yellow')


class DirectoryFrame(ttk.Frame):
    def __init__(self, master: ttk.Frame, fill_area: tk.Text, *args, **kwargs):
        super().__init__(master=master, style='Yellow.TFrame', *args, **kwargs)

        self.lbl_dir = ttk.Label(self, text="Last Source Directory:", font=("Arial", 20),
                                 foreground='black',
                                 background="yellow")
        self.temp_var_dir = tk.StringVar()
        self.entry_dir_path = ttk.Entry(self,
                                        textvariable=self.temp_var_dir,
                                        width=105,
                                        state='disable',
                                        font=("Arial", 10),
                                        foreground='black')
        self.btn_load = ttk.Button(self,
                                   text="Load Files",
                                   command=lambda: load_files(self.temp_var_dir, fill_area))

        self.lbl_dir.grid(column=0, row=0, sticky='w')
        self.entry_dir_path.grid(column=0, row=1)
        self.btn_load.grid(column=1, row=1)


class FilesFrame(ttk.Frame):
    def __init__(self, master: ttk.Frame, **kwargs):
        super().__init__(master=master, style="Yellow.TFrame", **kwargs)

        self.lbl_to_rename = ttk.Label(self,
                                       text="Files to rename:",
                                       font=("Arial", 20),
                                       background="yellow")
        self.lbl_renamed = ttk.Label(self,
                                     text="Renamed files:",
                                     font=("Arial", 20),
                                     background="yellow")
        self.text_to_rename = tk.Text(self,
                                      width=50,
                                      height=30)

        self.text_to_rename.configure(state='disabled')
        self.text_renamed = tk.Text(self,
                                    width=50,
                                    height=30)
        self.text_renamed.configure(state='disabled')

        self.lbl_to_rename.grid(column=0, row=0)
        self.lbl_renamed.grid(column=1, row=0)
        self.text_to_rename.grid(column=0, row=1)
        self.text_renamed.grid(column=1, row=1, padx=10)


class PrefixFrame(ttk.Frame):
    def __init__(self, master: ttk.Frame, to_rename: tk.Text, to_fill: tk.Text, **kwargs):
        super().__init__(master=master, style="Yellow.TFrame", **kwargs)

        self.lbl_prefix = ttk.Label(self, text="Filename prefix:", font=("Arial", 20), background="yellow")
        self.temp_var_prefix = tk.StringVar()
        self.entry_prefix = ttk.Entry(self, textvariable=self.temp_var_prefix, width=123)
        self.btn_rename = ttk.Button(self, text="Rename",
                                     command=lambda: rename(to_rename, to_fill,
                                                            self.temp_var_prefix,
                                                            self.progress_bar))
        self.progress_bar = ttk.Progressbar(self, orient='horizontal', mode='determinate')

        self.lbl_prefix.grid(column=0, row=0)
        self.entry_prefix.grid(column=0, row=1)
        self.btn_rename.grid(column=1, row=1)
        self.progress_bar.grid(column=0, row=3, sticky='we', columnspan=2)


class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, style="Yellow.TFrame")
        file_frame = FilesFrame(self)

        dir_frame = DirectoryFrame(self, file_frame.text_to_rename)
        prefix_frame = PrefixFrame(self, file_frame.text_to_rename, file_frame.text_renamed)

        dir_frame.grid(column=0, row=0, padx=10, pady=10)
        file_frame.grid(column=0, row=1, padx=10, pady=10)
        prefix_frame.grid(column=0, row=2, padx=10, pady=10)


if __name__ == "__main__":
    app = App()

    main = MainFrame(app)
    main.grid()

    app.mainloop()
