from tkinter import *
from tkinter import ttk
from tqdm import tqdm
import requests
import sys
import threading

root = Tk()

root.title('File Downloader')
root.geometry("600x300")

chunk_size = 1048576

url = "http://speedtest.tele2.net/100MB.zip"
directory = "C:\\gitpersonal\\file_downloader.py\\src"

r = requests.get(url, stream = True)

total_size = int(r.headers['content-length'])
filename = url.split('/')[-1]
#bar_format=None

bar_format='{l_bar}{bar}''|{n_fmt}MB/{total:.2f}MB | [Time:{elapsed}<{remaining} {rate_fmt}{postfix}]'
# iterable = r.iter_content(chunk_size = chunk_size) 
# total = total_size/chunk_size
global done
done=0
# unit = 'MB' 
# bar_format=bar_format

print(url)
print("Downloading..")
# with open(filename, 'wb') as f:
# 	for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'MB', bar_format=bar_format):
# 		f.write(data)


print("Download complete!")

total_length = r.headers.get('content-length')
label_percent_complete = Label(root, text='Complete: '+'0'+'%')
label_total_byte = Label(root, text='total_byte: '+'0'+'MB')
label_current_byte = Label(root, text='current_byte: '+'0'+'MB')
label_total_time = Label(root, text='total_time: '+'00:00')
label_current_time = Label(root, text='current_time: '+'00:00')
label_download_speed = Label(root, text='download_speed: '+'0'+'MB/s')

def update_label():
	global label_percent_complete
	label_percent_complete.config(text='Complete: '+ str(done) + '%')
	label_total_byte = Label(root, text='total_byte: '+'0'+'MB')
	label_current_byte = Label(root, text='current_byte: '+'0'+'MB')
	label_total_time = Label(root, text='total_time: '+'00:00')
	label_current_time = Label(root, text='current_time: '+'00:00')
	label_download_speed = Label(root, text='download_speed: '+'0'+'MB/s')
	#print("done", done)

	#pass

def step():
	global stop
	stop=False
	chunk_size = 1048576
	r = requests.get(url, stream = True)

	total_size = int(r.headers['content-length'])
	filename = directory + '\\' + url.split('/')[-1]
	with open(filename, 'wb') as f:
		dl = 0
		
		total_length = r.headers.get('content-length')
		total_length = int(total_length)
		for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'MB', bar_format=bar_format):
			global done
			root.update_idletasks()
			#my_progress.start()
			dl += len(data)
			done= int(100 * dl / total_length)
			my_progress['value']=done
			#label_percent_complete.text=done
			#print(data)
			#print("done", done)
			f.write(data)
			root.after(1,update_label())
			
			if stop == True:
				break


			


	# with open(filename, "wb") as f:
	# 	print("Downloading %s" % filename)
	# 	response = requests.get(url, stream=True)
	# 	total_length = response.headers.get('content-length')

	# 	if total_length is None: # no content length header
	# 		f.write(response.content)
	# 	else:
	# 		dl = 0
	# 		total_length = int(total_length)
	# 		for data in response.iter_content(chunk_size=1024):
	# 			dl += len(data)
	# 			f.write(data)
	# 			done = int(100 * dl / total_length)
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
label_total_byte.pack()
label_current_time.pack()
label_total_time.pack()
label_download_speed.pack()


start_button =Button(root, text='start', command=lambda: threading.Thread(target=step).start())
start_button.pack(pady=10)


stop_button =Button(root, text='stop', command=stop)
stop_button.pack(pady=10)





root.mainloop()