import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from):
        dbx = dropbox.Dropbox(self.access_token)

        if os.path.exists:

            for root, dirs, files in os.walk(file_from):
                for file in files:
                    file_path = os.path.join(root, file)
                    print("Trying to move: " + file_path)
                    f = open(file_path, 'rb')
                    dbx.files_upload(f.read(), '/Dropbox/' + str(file))
        else:
            print("No folder found!")


def main():
    access_token = "aaY3yuHqLGQAAAAAAAAAARKPa9OWY-Qzya0LPS13JD8kR_dLWmjOC_hoMTJNe678"
    transferData = TransferData(access_token)

    file_from = input(
        "Enter the folder COMPLETE location to transfer (ex: C:\\Stuff\\Python\\Python2\\Projects): ")
    transferData.upload_file(file_from)
    print("Files have been moved!")


if __name__ == '__main__':
    main()
