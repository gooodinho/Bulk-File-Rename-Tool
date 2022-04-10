import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showinfo
import time
import threading
from pathlib import Path

from logging_setup import base_logger


class AsyncFill(threading.Thread):
    def __init__(self, to_rename: tk.Text, files: tuple):
        super().__init__()
        self.to_rename = to_rename
        self.files = files
        self.name = "Thread-2"

    def run(self):
        self.to_rename.configure(state="normal")
        for file in self.files:
            self.to_rename.insert("end", f"{file}\n")
        self.to_rename.configure(state="disabled")


class Renamer(threading.Thread):
    def __init__(self, paths, to_rename: tk.Text, to_fill: tk.Text,
                 prefix: tk.StringVar, progress_bar: ttk.Progressbar):
        super().__init__()
        self.paths = paths
        self.to_rename = to_rename
        self.to_fill = to_fill
        self.prefix = prefix.get()
        self.progress_bar = progress_bar
        self.name = "Thread-3"

    def run(self):
        self.to_rename.configure(state="normal")
        self.to_fill.configure(state="normal")
        step = 100 / len(self.paths)
        for num, path in enumerate(self.paths, start=1):
            time.sleep(0.1)
            file = Path(path)
            new_file = file.parent.joinpath(f'{self.prefix}FIle{num}{file.suffix}')
            file.rename(new_file)
            self.to_rename.delete("1.0", "2.0")
            self.to_fill.insert("end", f"{new_file}\n")
            self.progress_bar['value'] += step
            # base_logger.info(f"Renaming and deleting: {path}\nFill: {new_file}")
        self.to_rename.configure(state="disabled")
        self.to_fill.configure(state="disabled")
        self.progress_bar['value'] = 0


def monitor(thread: threading.Thread, _):
    if thread.is_alive():
        _.after(100, lambda: monitor(thread, _))
    else:
        base_logger.info(f'Thread {thread.name} has finished')


def load_files(var: tk.StringVar, to_rename: tk.Text):
    files = askopenfilenames()
    path = files[0].split('/')[:-1]
    var.set('\\'.join(path))
    files = tuple([file.replace('/', '\\') for file in files])

    download_thread = AsyncFill(to_rename, files)
    download_thread.start()

    monitor(download_thread, to_rename)


def rename(to_rename: tk.Text, to_fill: tk.Text, prefix: tk.StringVar, progress_bar: ttk.Progressbar):
    for thread in threading.enumerate():
        if Renamer.__instancecheck__(thread):
            showinfo(title="Warning", message="Wait until the renaming process is finished!")
            return
    paths = to_rename.get("1.0", "end").split("\n")
    no_empty_paths = [path for path in paths if path != ""]
    if len(no_empty_paths) == 0:
        showinfo(title="Error", message="You didn't load any file!")
    else:
        rename_thread = Renamer(no_empty_paths, to_rename, to_fill, prefix, progress_bar)
        rename_thread.start()

        monitor(rename_thread, to_rename)
