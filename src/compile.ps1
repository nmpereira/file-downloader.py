python -m venv build_env

.\build_env\Scripts\activate.ps1

start-sleep 5

pip install -r requirements.txt

start-sleep 5

pyinstaller --noconfirm --onefile --windowed --name "FileDownloader.exe" "C:/gitpersonal/file-downloader.py/src/file_downloaderTK.py"

pause