from tqdm import tqdm
import requests
import sys

chunk_size = 1048576

url = sys.argv[1]
directory = sys.argv[2]

r = requests.get(url, stream = True)

total_size = int(r.headers['content-length'])
filename = directory +'/'+ url.split('/')[-1]
#bar_format=None
bar_format='{l_bar}{bar}''|{n_fmt}MB/{total:.2f}MB | [Time:{elapsed}<{remaining} {rate_fmt}{postfix}]'
print(url)
print("Downloading..")
with open(filename, 'wb') as f:
	for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'MB', bar_format=bar_format):
		f.write(data)


print("Download complete!")


