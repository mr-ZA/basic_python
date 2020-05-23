import os

class FileHandler():
    def __init__(self):
        self.path_fullList = os.path.join(os.path.dirname(__file__), "payload_program", "full")
        self.path_userFiles = os.path.join(os.path.dirname(__file__), "payload_program", "tres")

    def file_appender(self, path) -> list:
        self.arrFile = []

        files = os.listdir(path)
        for file in files:
            self.arrFile.append(file)

        print("[INFO] Files append to the array successfully")
        return self.arrFile

fh = FileHandler()
userArray = (fh.file_appender(fh.path_userFiles))
fullArray = (fh.file_appender(fh.path_fullList))

print(f"\nUser .tres files quantity: {len(userArray)}")
for u in userArray:
    if u == "acaa170_en.tres":
        print(u)
print(f"Full list of .tres files quantity: {len(fullArray)}")

print("\n")
#print(fullArray)
