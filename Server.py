import socket
import sys
import time
import random
from Ceasar import MasterList
f = open("Shift.txt","r")
sh = f.read()
Shift = int(sh)
s = socket.socket()
host = socket.gethostname()
print("server will start on: "+host)
port = 1234
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
print("server is bound successfully")
s.listen(1)
conn,addr = s.accept()
print(addr, "has connected")
while 1:
    message = input("Server: ")
    #Encryption
    def Encryption(Message,Shift,MasterList):
        MyList = list(Message.strip(" "))
        EncryptedText=""
        for i in range(len(MyList)):
            CurrentPosition = MasterList.index(MyList[i])
            NewPosition = CurrentPosition + Shift
            if NewPosition < len(MasterList):
               encrypted_text = ''.join(MasterList[NewPosition])
               EncryptedText=EncryptedText+encrypted_text
            else:
               CurrentPosition = NewPosition - len(MasterList)
               encrypted_text = ''.join(MasterList[CurrentPosition])
               EncryptedText=EncryptedText+encrypted_text
        return EncryptedText


    message = Encryption(message, Shift, MasterList)
    #print("message: "+message)
    #print("Shift: ", Shift)
    Msg = message.encode()
    Sh = str(Shift)
    sh = Sh.encode()
    conn.send(sh)
    conn.send(Msg)

    incoming_shift = conn.recv(1024)
    incoming_message = conn.recv(1024)
    inc_shift = incoming_shift.decode()
    inc_msg = incoming_message.decode()
    Shift = int(inc_shift)
    MyList = list(inc_msg.strip(" "))
    DecryptedText = ""
    for i in range(len(MyList)):
        CurrentPosition = MasterList.index(MyList[i])
        NewPosition = CurrentPosition - Shift
        if NewPosition < len(MasterList):
            encrypted_text = ''.join(MasterList[NewPosition])
            DecryptedText = DecryptedText + encrypted_text

        else:
            CurrentPosition = NewPosition - len(MasterList)
            encrypted_text = ''.join(MasterList[CurrentPosition])
            DecryptedText = DecryptedText + encrypted_text

    print("Client: " + DecryptedText)