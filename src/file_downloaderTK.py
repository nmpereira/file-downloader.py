from tkinter import *
from tkinter import ttk
from tqdm import tqdm
import requests
import sys
import threading
import time
import os

root = Tk()

root.title('File Downloader')
root.geometry("600x300")

chunk_size = 1048576

url = "http://speedtest.tele2.net/1GB.zip"
directory = "C:\\gitpersonal\\file-downloader.py\\src"

r = requests.get(url, stream = True)

total_size = int(r.headers['content-length'])
filename = url.split('/')[-1]
#bar_format=None

bar_format='{l_bar}{bar}''|{n_fmt}MB/{total:.2f}MB | [Time:{elapsed}<{remaining} {rate_fmt}{postfix}]'
# iterable = r.iter_content(chunk_size = chunk_size) 
# total = total_size/chunk_size
global done
global current_time
global current_byte
global download_speed
global total_time
global time_left
complete = False

def reset_params():
	#global complete
	global done
	global current_time
	global current_byte
	global download_speed
	global total_time
	global time_left
	done=0
	current_time=0
	current_byte=0
	download_speed=0
	total_time=0
	time_left=0
	

	update_label()

# unit = 'MB' 
# bar_format=bar_format

print(url)
print("Downloading..")
# with open(filename, 'wb') as f:
# 	for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'MB', bar_format=bar_format):
# 		f.write(data)


print("Download complete!")

#total_size = int(r.headers.get('content-length'))
label_percent_complete = Label(root, text='Complete: '+'0'+'%')
label_total_size = Label(root, text='total_size: '+'0'+'MB')
label_current_byte = Label(root, text='current_byte: '+'0'+'MB')
label_time_left = Label(root, text='time_left: '+'00:00')
label_total_time = Label(root, text='time_left: '+'00:00')
label_current_time = Label(root, text='current_time: '+'00:00')
label_download_speed = Label(root, text='download_speed: '+'0'+'MB/s')

def update_label():
	global label_percent_complete
	global label_current_time
	label_percent_complete.config(text='Complete: '+ str(done) + '%')
	label_total_size.config(text='total_size: '+ str(total_size/chunk_size)+'MB')
	label_current_byte.config(text='current_byte: '+ str(current_byte) +'MB')
	label_time_left.config(text='time_left: '+str(int(time_left)))
	label_total_time.config(text='total_time: '+str(int(total_time)))
	label_current_time.config(text=f'current_time: '+str(int(current_time)))
	label_download_speed.config(text='download_speed: '+str(download_speed)+'MB/s')
	#print("done", done)

	#pass

def step():
	global stop
	
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
			#my_progress.start()
			dl += len(data)
			done= int(100 * dl / total_size)
			my_progress['value']=done
			#label_percent_complete.text=done
			#print("done", done)
			f.write(data)
			#print("\n")
			#print(int(time.time() - start_time))
			current_time=int(time.time()- start_time)
			current_byte=dl/chunk_size
			download_speed=round(((dl//(time.time() - start_time) / 100000)*0.125)/1.3,2)
			total_time=round(total_size/((download_speed*100000)/0.125)/1.3,2)
			time_left=round(total_time-current_time,2)
			#tqdm.update()
			root.after(1,update_label())
			if stop == True:
				break
		
		
		


			


	# with open(filename, "wb") as f:
	# 	print("Downloading %s" % filename)
	# 	response = requests.get(url, stream=True)
	# 	total_size = response.headers.get('content-length')

	# 	if total_size is None: # no content length header
	# 		f.write(response.content)
	# 	else:
	# 		dl = 0
	# 		total_size = int(total_size)
	# 		for data in response.iter_content(chunk_size=1024):
	# 			dl += len(data)
	# 			f.write(data)
	# 			done = int(100 * dl / total_size)
	# 			#sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (100-done)) ) 
	# 			my_progress['value']=done   
	# 			root.update_idletasks()
				#sys.stdout.flush()
	#my_progress.stop()

def stop():
	global stop
	stop =True

my_progress =ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
my_progress.pack(pady=20)

label_percent_complete.pack()
label_current_byte.pack()
label_total_size.pack()
label_current_time.pack()
label_time_left.pack()
label_total_time.pack()
label_download_speed.pack()


start_button =Button(root, text='start', command=lambda: threading.Thread(target=step).start())
start_button.pack(pady=10)


stop_button =Button(root, text='stop', command=stop)
stop_button.pack(pady=10)





root.mainloop()