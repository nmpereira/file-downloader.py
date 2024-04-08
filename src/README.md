To build, use `compile.ps1` which will create a python virtual environment, pip install all the required modules from requirements.txt and build a exe into `/dist` using pyinstaller.

`example/file_downloader.py` is a very basic implementation of tqdm and requests module that can be called by using `Python file_downloader.py "http://speedtest.tele2.net/1GB.zip" "DestinationPath"`. This is just an example of how to use tqdm, and is separate from the main implementation.


`file_downloaderTK.py` is the main python file that builds the exe. It uses Tkinter, in addtion to tqdm and requests. It also uses some helper modules like threading, datetime etc. It can be called by using `Python file_downloaderTK.py "http://speedtest.tele2.net/100MB.zip" "DestinationPath" "True"`










