# -*- coding: utf-8 -*-

import os
import sys

# Globals
memory = {}

def dump_memory():
    global memory
    mem = open("memory_Bot.txt", "r")
    for i in mem.readlines():
        question, answer = i.strip().split(':')
        memory[question] = answer
    return memory
    mem.close()

def main():
    print('=' * 10 + "\n   MENU\n" + '=' * 10)
    print("1.Let's learn!")
    print("2.Let's talk")
    print("3.Diagnostic mode")
    print("4.Quitter")
    while True:
        choice = input("What would you like to do?: ")
        if choice not in ['1', '2', '3', '4']:
            print ("Error, choose the correct menu item")

        elif choice == '1':
            while True:
                mem = open ("memory_Bot.txt", "a+")
                print("Enseigne moi des mots!\n")

                print ("la question?")
                que = input()
                print("la réponse?")
                rep = input()

                mass_answ = [[que, rep]]
                dict_answ = dict(mass_answ)
                print("Je me souviens: {}".format(dict_answ))

                for question, answer in dict_answ.items():
                    mem.write('{}:{}\n'.format(question, answer))

                mem.close()
                main()

        elif choice == '2':
            print("Let's talk, ask me: ")
            while True:
                global memory
                mem = open("memory_Bot.txt", "r")
                print("Lecture de mémoire!\n")
                for i in mem.readlines():
                    question, answer = i.strip().split(':')
                    memory[question] = answer

                print("la question?")
                que = input()
                print(memory[que])

                main()

        elif choice == '3':
            pass

        elif choice == '4':
            print ("Goodbye.")
            sys.exit()

if __name__ == '__main__':
    main()
