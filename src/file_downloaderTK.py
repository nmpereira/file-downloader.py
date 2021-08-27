from tkinter import *
from tkinter import ttk

root = Tk()

root.title('File Downloader')
root.geometry("600x160")

def step():
	my_progress.start(10)

def stop():
	my_progress.stop()

my_progress =ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
my_progress.pack(pady=20)



start_button =Button(root, text='start', command=step)
start_button.pack(pady=10)


stop_button =Button(root, text='stop', command=stop)
stop_button.pack(pady=10)




root.mainloop()