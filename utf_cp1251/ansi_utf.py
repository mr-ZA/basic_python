import codecs
import os

path = os.getcwd() + "\\files\\"
path_out = os.getcwd() + "\\files\\result_files\\"
print(path)
print(path_out)

def primary():
  for filename in os.listdir(path):
    if filename == "result_files":
      continue
    print(filename)
    # read from folder
    fp = codecs.open(path + filename, 'r', encoding="utf-8-sig")
    try:
      s = fp.read()
    except UnicodeDecodeError:
      continue

    # with codecs.open(path + filename, 'w', encoding='cp1251') as file:
    #   try:
    #     s = file.read()
    #   except UnicodeDecodeError:
    #     continue

    #write output file
    with codecs.open(path_out+filename, 'w', encoding = 'cp1251') as file:
      try:
        file.write(s)
      except UnicodeEncodeError:
        continue

  # Check what files recorded with an error
  for filename in os.listdir(path_out):
    if os.path.getsize(path+filename) < 1:
      print("\nError in: {}".format(filename))

if __name__ == '__main__':
  primary()
