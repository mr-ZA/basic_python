# -*- coding: utf-8 -*-

import os
import sys
import time

# Globals
memory = {}

class Curie_brain():
    def __init__(self):
        self.memory = self.dump_memory()                # no need to read file again by the recall
        print('=' * 10 + "\n   MENU\n" + '=' * 10)
        print("1.Let's learn!")
        print("2.Let's talk")
        print("3.Diagnostic mode")
        print("4.Quitter")

        choice = input("What would you like to do?: ")
        if choice not in ['1', '2', '3', '4']:
            print("Error, choose the correct menu item")

        elif choice == '1':
            self.learn()

        elif choice == '2':
            self.talk()

        elif choice == '3':
            print ("\nYou choosed diagnostic mode, let me check my memory...")
            time.sleep(5)
            print("In memory i've got:\n {}\n".format(self.dump_memory()))
            Curie_brain()

        elif choice == '4':
            print("Goodbye.")
            sys.exit()

    #### realization ####
    def learn(self):
        mem = open("memory_Curie.txt", "a+")
        print("Enseigne moi des mots!\n")

        while True:
            i = input("Press <ENTER> (if end press <q>)\n")
            if not i:
                print("la question?")
                que = input()
                print("la réponse?")
                rep = input()

                mass_answ = [que, rep]
                dict_answ = dict([mass_answ])
                print("Je me souviens: {}".format(dict_answ))

                for question, answer in dict_answ.items():
                    mem.write('{}:{}\n'.format(question, answer))
            else:
                mem.close()
                Curie_brain()

    def talk(self):
        print("\nLet's talk dear, ask me: ")
        while True:
            i = input("Press <ENTER> (if end press <q>)\n")

            if not i:
            #     mem = open("memory_Curie.txt", "r")
            #     print("Lecture de mémoire!\n")

                # Assign block, don't needed exactly, just for test
                #for i in mem.readlines():
                    #question, answer = i.strip().split(':')
                    #memory[question] = answer

                print("Qu'est-ce que tu voudrais savoir?")
                que = input()
                print("\n...")
                try:
                    print(memory[que])
                except KeyError:
                    print("Question doesn't exist in memory, try to teach me again..")
                print("\n")
            else:
                Curie_brain()

    def dump_memory(self):
        global memory

        mem = open("memory_Curie.txt", "r")
        for i in mem.readlines():
            question, answer = i.strip().split(':')
            memory[question] = answer
        return memory
        mem.close()

Curie = Curie_brain()   # obj