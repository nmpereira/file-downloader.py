from tkinter import *
from tkinter import ttk
from tqdm import tqdm
import sys
import requests
import threading
import time
import datetime

root = Tk()
root.title('File Downloader')
root.geometry("580x250")
root.resizable(False, True)

#requires url to file download
url = sys.argv[1]
#requires path to save file to
directory = sys.argv[2]
#requires True or False
autostart = sys.argv[3]

print(url)
print("Downloading..")

filename = url.split('/')[-1]
bar_format='{l_bar}{bar}''|{n_fmt}MB/{total:.2f}MB | [Time:{elapsed}<{remaining} {rate_fmt}{postfix}]'

complete = False
total_size=0
chunk_size = 1048576

label_url=Label(root,wraplength=500,justify=LEFT, text='URL: '+url)
label_destination=Label(root,wraplength=500,justify=LEFT, text='Dest: '+directory+'\\'+ filename)
label_percent_complete = Label(root, text='0'+'%')
label_total_size = Label(root, text=': '+'0'+'MB')
label_current_byte = Label(root, text='0'+'MB')
label_current_time = Label(root, text='00:00')
label_time_left = Label(root, text=': '+'00:00')
label_total_time = Label(root, text='Est. Time: '+'00:00')
label_download_speed = Label(root, text='Speed: '+'0'+'MB/s')

def update_label():
	label_percent_complete.config(text=str(done) + '%')
	label_total_size.config(text=': '+ str(int(total_size/chunk_size))+'MB')
	label_current_byte.config(text= str(int(current_byte)) +'MB')
	label_current_time.config(text=str(datetime.timedelta(seconds=int(current_time))))
	label_time_left.config(text=': '+str(datetime.timedelta(seconds=int(time_left))))
	label_total_time.config(text='Est. Time: '+str(datetime.timedelta(seconds=int(total_time))))
	label_download_speed.config(text='Speed: '+str(download_speed)+'MB/s')

def step():
	global stop
	global total_size
	stop=False
	chunk_size = 1048576
	r = requests.get(url, stream = True)

	filename = directory + '\\' + url.split('/')[-1]
	with open(filename, 'wb') as f:
		
		start_time = time.time()
		dl = 0
		
		total_size = int(r.headers.get('content-length'))
		
		for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'MB', bar_format=bar_format):
			global done
			global current_time 
			global current_byte
			global download_speed
			global total_time
			global time_left

			root.update_idletasks()

			dl += len(data)
			done= int(100 * dl / total_size)
			my_progress['value']=done
			f.write(data)
			current_time=int(time.time()- start_time)
			current_byte=dl/chunk_size
			download_speed=round(((dl//(time.time() - start_time) / 100000)*0.125)/1.3,2)
			total_time=round(total_size/((download_speed*100000)/0.125)/1.3,2)
			time_left=round(total_time-current_time,2)
			root.after(1,update_label())
			if stop == True:
				start_button.config(text="Restart")
				start_button.grid()
				stop_button.grid_remove()
				return
			else:
				start_button.grid_remove()
				stop_button.grid()
		return print("Download complete!"), root.after(5000, lambda: root.destroy()), Close_button.grid()

		
def stop():
	global stop
	stop =True
def close_window():
	root.destroy()

label_url.grid(column=0, row=0,columnspan=11,sticky=W,pady=1,padx=10)
label_destination.grid(column=0, row=1,columnspan=11,sticky=W,pady=1,padx=10)

my_progress =ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
my_progress.grid(column=0, row=2, columnspan=10,pady=10,padx=10)

label_percent_complete.grid(column=11, row=2)
label_current_byte.grid(column=2, row=3, sticky=E)
label_total_size.grid(column=3, row=3,sticky=W)
label_current_time.grid(column=4, row=3,sticky=E,pady=5)
label_time_left.grid(column=5, row=3,sticky=W)
label_total_time.grid(column=7, row=3)
label_download_speed.grid(column=8, row=3)

start_button =Button(root, text='Start',width=8, command=lambda: threading.Thread(target=step).start())
start_button.grid(column=6,row=4,pady=10)

stop_button =Button(root, text='Stop',width=8, command=stop)
stop_button.grid(column=6, row=4,pady=10)

Close_button =Button(root, text='Close',width=8, command=close_window)
Close_button.grid(column=6, row=4,pady=10)

start_button.grid_remove()
stop_button.grid_remove()
Close_button.grid_remove()

if autostart=="True":
	start_button.invoke()
	
	start_button.grid_remove()
	stop_button.grid()
else:
	start_button.grid()
	stop_button.grid_remove()
	
root.mainloop()