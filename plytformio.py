import sys
import os
import time
import getpass

class plytformio(object):
    def __init__(self):
        print("Programa desenvolvido por Ronald Lopes - Versão 0.1")
        try:
            os.system("pip install platformio")
        except:
            pass
        self.gitUrl = str(sys.argv[1]).replace("https://","") #github.com/RonaldLopes/IOT-Trabalho-Final
        self.time = int(sys.argv[2]) * 60
    def start(self):
        self.userName = input("Informe o seu nome de usuario do git: ")
        try:
            self.password = getpass.getpass("Informe sua senha do git: ")
            # print(self.password)
        except:
            exit(0)
        while(True):
            self.updateCode()
            time.sleep(self.time)

    def updateCode(self):
        comando = "git pull https://"+str(self.userName)+":"+str(self.password)+"@"+self.gitUrl+" >> temp.txt"
        os.system(comando)
        file = open("temp.txt","r+")
        leitura = file.readline()
        if "Updating" in leitura:
            print("Codigo atualizado, iniciando o upload!")
            self.uploadCode()
        elif "Already up to date." in leitura:
            print("Codigo atualizado, não é necessário nenhuma ação!")
        file.close()
        file = open("temp.txt", "w")
        file.close()


    def uploadCode(self):
        try:
            os.system("platformio run -t upload")
        except Exception as erro:
            print("Erro: " + erro)
temp = plytformio()
# temp.uploadCode()
temp.start()