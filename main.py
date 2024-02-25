import tkinter as tk
import webbrowser
from pipeline import Pipeline
import tkinter as tk
from tkinter import ttk
import threading

def classify():
    html_content = html_text.get("1.0", "end-1c")
    # Start the progress bar in a new thread
    threading.Thread(target=progress_bar_start).start()

    x = threading.Thread(target = my_fn, args=(1, html_content)).start()

def my_fn(args, html_content):

    pp = Pipeline()
    htmls = pp.pipeline(html_content)
    page = ''.join(htmls)
    with open("temp.html", "w") as f:
        f.write(page)

    # Open browser after function is completed
    threading.Thread(target=open_browser_after_delay).start()

def progress_bar_start():
    # Start the progress bar
    progress_bar.start(10)

def open_browser_after_delay():

    webbrowser.open("temp.html")
    # Stop the progress bar
    progress_bar.stop()

root = tk.Tk()
root.title("MBTI Classification")

html_text = tk.Text(root, height=30, width=100)
html_text.pack(pady=10)


open_button = tk.Button(root, text="Calculate Results", command=classify)
open_button.pack(pady=5)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="indeterminate")
progress_bar.pack(pady=10)

root.mainloop()
