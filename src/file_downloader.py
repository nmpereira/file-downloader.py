from tqdm import tqdm
import requests
import sys

chunk_size = 1048576

url = sys.argv[1]

r = requests.get(url, stream = True)

total_size = int(r.headers['content-length'])
filename = url.split('/')[-1]

print(url)
print("Downloading..")
with open(filename, 'wb') as f:
	for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'MB'):
		f.write(data)


print("Download complete!")


