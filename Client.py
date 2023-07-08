import socket
import sys
import time
from Ceasar import MasterList
"""f = open("Shift.txt","r")
sh = f.read()
Shift = int(sh)
Shift = 5"""
s = socket.socket()
host = input("please enter host name: ")
port = 1234
s.connect((host,port))
print("connected to server")
while 1:
    incoming_shift = s.recv(1024)
    incoming_message = s.recv(1024)
    inc_shift = incoming_shift.decode()
    inc_msg = incoming_message.decode()
    Shift = int(inc_shift)
    MyList = list(inc_msg.strip(" "))
    DecryptedText=""
    for i in range(len(MyList)):
        CurrentPosition = MasterList.index(MyList[i])
        NewPosition = CurrentPosition - Shift
        if NewPosition < len(MasterList):
           encrypted_text = ''.join(MasterList[NewPosition])
           DecryptedText =DecryptedText+encrypted_text

        else:
           CurrentPosition = NewPosition - len(MasterList)
           encrypted_text = ''.join(MasterList[CurrentPosition])
           DecryptedText = DecryptedText+encrypted_text

    print("Server: " + DecryptedText)
    message = input("Client: ")
    # Encryption
    def Encryption(Message, Shift, MasterList):
        MyList = list(Message.strip(" "))
        EncryptedText = ""
        for i in range(len(MyList)):
            CurrentPosition = MasterList.index(MyList[i])
            NewPosition = CurrentPosition + Shift
            if NewPosition < len(MasterList):
                encrypted_text = ''.join(MasterList[NewPosition])
                EncryptedText = EncryptedText + encrypted_text
            else:
                CurrentPosition = NewPosition - len(MasterList)
                encrypted_text = ''.join(MasterList[CurrentPosition])
                EncryptedText = EncryptedText + encrypted_text
        return EncryptedText
    message = Encryption(message, Shift, MasterList)
    #print("message: " + message)
    #print("Shift: ", Shift)
    Msg = message.encode()
    Sh = str(Shift)
    sh = Sh.encode()
    s.send(sh)
    s.send(Msg)
#tbp = ""
#tbp = Decryption(Incoming_message, sh, MasterList)