# file-downloader.py
A simple CommandLine based file downloader GUI that uses the python modules Tkinter, tqdm and requests. The intended purpose behind creating this tool was to have a GUI based progressbar when scripting/PowerShell automations. It can also be automatically started, paused and restarted, all of which are lacking from powerShell's built in tools.


[FileDownloader.exe](https://github.com/nmpereira/file-downloader.py/releases/) contains a progressbar and is called from the CommandLine.

The program can be called using the following command.

`.\FileDownloader.exe "URL of file to be downloaded" "DestinationPath" "True"` where `"True"` is autostarting the download. `"False"` will not autostart the download, letting the user start click on the button to initate download.

Examples:

`.\FileDownloader.exe "http://speedtest.tele2.net/100MB.zip" "C:\\temp" "True"`

`.\FileDownloader.exe "http://speedtest.tele2.net/1GB.zip" ".\" "False"`

![File Downloader without command](https://github.com/nmpereira/file-downloader.py/blob/master/src/images/FileDownloader.PNG?raw=true)

![File Downloader with command](https://github.com/nmpereira/file-downloader.py/blob/master/src/images/FileDownloaderFull.PNG?raw=true)



