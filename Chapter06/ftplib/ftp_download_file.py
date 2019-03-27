#!/usr/bin/env python3

import ftplib

FTP_SERVER_URL = 'ftp.free.fr'
DOWNLOAD_DIR_PATH = '/mirrors/ftp.kernel.org/linux/kernel/Historic/'
DOWNLOAD_FILE_NAME = 'linux-0.01.tar.gz'

def ftp_file_download(path, username):
	# open ftp connection
	ftp_client = ftplib.FTP(path, username)
	print("Welcome:", ftp_client.getwelcome())
	# list the files in the download directory
	ftp_client.cwd(DOWNLOAD_DIR_PATH)
	print("Current working directory:", ftp_client.pwd())
	print("File list at %s:" %path)
	files = ftp_client.dir()
	print(files)
	# download a file
	try:
		file_handler = open(DOWNLOAD_FILE_NAME, 'wb')
		ftp_cmd = 'RETR %s' %DOWNLOAD_FILE_NAME
		ftp_client.retrbinary(ftp_cmd,file_handler.write)
		ftp_client.retrlines('LIST')
		file_handler.close()
		ftp_client.quit()
	except Exception as exception:
		print('File could not be downloaded:',exception)

if __name__ == '__main__':
	ftp_file_download(path=FTP_SERVER_URL,username='anonymous')
