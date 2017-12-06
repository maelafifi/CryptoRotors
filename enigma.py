from rotor import Rotor
from machine import Machine
from reflector import Reflector

I = "VEADTQRWUFZNLHYPXOGKJIMCSB"
II = "WNYPVJXTOAMQIZKSRFUHGCEDBL"
III = "DJYPKQNOZLMGIHFETRVCBXSWAU"
R = "EJMZALYXVBWFCRQUONTSPIKHGD"

r1 = Rotor(I, 1)
r1_2 = Rotor(I, 1)
r2 = Rotor(II, 2)
r2_2 = Rotor(II, 2)
r3 = Rotor(III, 3)
rf = Reflector(R)

def readfile(filename):
	with open(filename, 'r') as f:
		return f.readlines()

def main():
	choice = int(raw_input("Enter 1 for \"1930 Enigma I,\" 2 for \"Spring 1942 M4 R2,\" or 3 for Mohamed/Vincent Rotor: "))
	encode_decode = int(raw_input("Encipher (1) or decipher (2)? "))
	cipherText = raw_input("What would you like to encipher? ")
	if choice == 1:
		machine = Machine([r1, r2], rf)
		print machine.encipher(cipherText)
	elif choice == 2:
		machine = Machine([r1, r2], rf)
		print machine.encipher(cipherText)
	else:
		if encode_decode == 1:
			machine = Machine([r1, r2], rf)
			c_1 = machine.encipher(cipherText)
			print c_1
			machine2 = Machine([r2_2, r1_2], rf)
			print machine2.encipher(c_1)
		else:
			machine = Machine([r2, r1], rf)
			c_1 = machine.encipher(cipherText)
			print c_1
			machine2 = Machine([r1_2, r2_2], rf)
			print machine2.encipher(c_1)

if __name__ == "__main__":
	main()
