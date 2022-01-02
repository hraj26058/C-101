import dropbox
class CloudStorage:
	def __init__(self, access_token):
		self.access_token = access_token
	def upload_file(self,file_from,file_to):
		dbx = dropbox.Dropbox(self.access_token)
		f = open(file_from,'rb')
		dbx.files_upload(f.read(),file_to)
def main():
	access_token='bssSOBkyHBwAAAAAAAAAASpb3GFxjNCNrfYkPOC5Qnu0U6cylN7sFa74XyKPsUdd'
	transferdata=CloudStorage(access_token)

	file_from=input("Enter the file path to transfer")
	file_to=input("Enter the full dropbox path")
	transferdata.upload_file(file_from, file_to)
	print("File Moved Successfully")
main()

