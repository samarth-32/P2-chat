import string
import random
#Shift = random.randint(1,36)
#print(Shift)
MasterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","0","1","2","3","4","5","6","7","8","9","~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|","'",'"',",",".","<",">","/","?",":",";"]
global shift
Shift = random.randint(0,len(MasterList))
shift = Shift
f = open("Shift.txt","w")
f.write(str(shift))
f.close()