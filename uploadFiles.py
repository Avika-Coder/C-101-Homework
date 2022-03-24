import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_Token):
        self.access_Token =  access_Token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_Token)      
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_Token='sl.BEYUaKcOftUAnBPNFKR-8Hca5kW3kgfUkv6ZCryr6lBDCViMyx9GbJx8n0V48Mkz76ATBdJAfbEWseGYcy3ctDz8m2V_JsdnjmR8yi1GWKVE5hkQtGD7W311AZOZbISkTJimzfO-84O2'  
    transferData = TransferData(access_Token)
    file_from=input("Enter the file that you want to transfer : ")
    file_to=input("Enter the path to upload file in the dropbox : ")
    transferData.upload_file(file_from,file_to)
    print("File has been moved")

main()
