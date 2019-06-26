# -*- coding: utf-8 -*-

import os
import shutil
import re

"""
def mkdir_cmd():												#making dir and file (not worked yet, lazyyy)
  if not os.path.exists(r"./folder_ips"):
    os.mkdir(r"./folder_ips")
    print(r'Dir made')
  os.chdir("folder_ips")
  my_file = open('snake.txt', 'w')
"""

def new_mass(addr_beg, addr_end):									# [all st], [all endd]
  #addr = ['11.53.128.0', '11.53.159.255']

  print ("[List of ip\'s: ]")

  for i in range(col):
    begin = list(map(int,addr_beg[i].split('.')))					# 5.1.20.0 -> split('.') -> '5','1','20','0' -> map(int) -> 5,1,20,0 -> list() -> [5, 1, 20, 0]
    end = list(map(int,addr_end[i].split('.')))						# 5.1.20.255 -> [5, 1, 20, 255]
    
    # obj"zip" -> to -> list required!
    res = list(zip(begin, end))										# begin = [5, 1, 20, 0] end = [5, 1, 20, 255] ----> zip(begin, end) ----> [(5, 5), (1, 1), (20, 20), (0, 255)]

    if (res[2][0] == res[2][1]):
      for k in range(res[0][0], res[0][1]+1):						# for .. in range ([5], [6])
          for L in range(res[1][0], res[1][1]+1):					# for .. in range ([1], [2])
              for m in range(res[2][0], res[2][1]+1):				# for .. in range ([20], [21])
                  for n in range(res[3][0], res[3][1]+1):			# for .. in range ([0], [255])
                     print('.'.join(list(map(str,[k,L,m,n]))))		# print [5,1,2,0] -> int made to (str) with map() -> '5,1,2,0' -> join with separator[.] at the beginning

    else:															# [(31, 31), (43, 43), (128, 154), (0, 255)]
      for k in range(res[0][0], res[0][1]+1):						# for .. in range ([31], [32])
          for L in range(res[1][0], res[1][1]+1):					# for .. in range ([43], [43])
              for m in range(res[2][0], res[2][1]+1):				# for .. in range ([128], [154])
                  for n in range(res[3][0], res[3][1]+1):			# for .. in range ([0], [255])
                     print('.'.join(list(map(str,[k,L,m,n]))))

def get_ips():                          			#sources
  print("Enter path to file with IP range: ")
  path = input()									#get directory
  regex_num = re.compile('(.*)\-')					#precompile regex expressions
  regex_num_end = re.compile('\-(.*)')

  with open(path, 'r') as p:						#read strings from file
    str_original = p.read()
    #print(type (str_original))

  print ("[start values]")
  print (regex_num.findall(str_original))
  print("\n")
  st = regex_num.findall(str_original)				#detect the start value with regex
  
  print("[length of massive of start values]")
  global col
  col = len(st)										#length of start values
  print (col)
  print("\n")

  print ("[end values]")
  print(regex_num_end.findall(str_original))
  print("\n")
  endd = regex_num_end.findall(str_original)

  print("[length of massive of end values]")
  col_end = len(endd)
  print (col_end)
  print("\n")

  new_mass(st, endd)


def main():
  get_ips()
  #mkdir_cmd()

if __name__ == '__main__':
  main()
