from tkinter import *
from tkinter import ttk
from tqdm import tqdm
import requests
import sys

root = Tk()

root.title('File Downloader')
root.geometry("600x200")

chunk_size = 1048576

url = "http://speedtest.tele2.net/100MB.zip"

r = requests.get(url, stream = True)

total_size = int(r.headers['content-length'])
filename = url.split('/')[-1]
#bar_format=None

bar_format='{l_bar}{bar}''|{n_fmt}MB/{total:.2f}MB | [Time:{elapsed}<{remaining} {rate_fmt}{postfix}]'
iterable = r.iter_content(chunk_size = chunk_size) 
total = total_size/chunk_size

unit = 'MB' 
bar_format=bar_format

print(url)
print("Downloading..")
# with open(filename, 'wb') as f:
# 	for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'MB', bar_format=bar_format):
# 		f.write(data)


print("Download complete!")

total_length = r.headers.get('content-length')

def step():

	with open(filename, 'wb') as f:
		dl = 0
		total_length = r.headers.get('content-length')
		total_length = int(total_length)
		for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'MB', bar_format=bar_format):
			#my_progress.start()
			dl += len(data)
			done = int(100 * dl / total_length)
			my_progress['value']=done
			root.update_idletasks()
			f.write(data)

			#my_label.config(text=data)


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
	my_progress.stop()

my_progress =ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
my_progress.pack(pady=20)



start_button =Button(root, text='start', command=step)
start_button.pack(pady=10)


stop_button =Button(root, text='stop', command=stop)
stop_button.pack(pady=10)

my_label =Label(root, text='')
my_label.pack(pady=10)


root.mainloop()