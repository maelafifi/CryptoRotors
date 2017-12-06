from rotor import Rotor
from machine import Machine
from reflector import Reflector



EN1_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
EN1_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
EN1_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

M3A_1 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
M3A_2 = "VZBRGITYUPSDNHLXAWMJQOFECK"

R = "EJMZALYXVBWFCRQUONTSPIKHGD"



EN11 = Rotor(EN1_1)
EN12 = Rotor(EN1_2)
EN13 = Rotor(EN1_3)
M3A1 = Rotor(M3A_1)
M3A2 = Rotor(M3A_2)

MVEN11 = Rotor(EN1_1)
MVEN12 = Rotor(EN1_2)
MVEN13 = Rotor(EN1_3)
MVM3A1 = Rotor(M3A_1)
MVM3A2 = Rotor(M3A_2)

D_MVEN11 = Rotor(EN1_1)
D_MVEN12 = Rotor(EN1_2) 
D_MVEN13 = Rotor(EN1_3)
D_MVM3A1 = Rotor(M3A_1)
D_MVM3A2 = Rotor(M3A_2)

rf = Reflector(R)


def main():
	choice = int(raw_input("Enter 1 for \"1930 Enigma I,\" 2 for \"1938 M3 Army,\" or 3 for Mohamed/Vincent Rotor: "))
	encode_decode = int(raw_input("Encipher (1) or decipher (2)? "))
	cipherText = raw_input("What would you like to encipher? ")
	if choice == 1:
		machine = Machine([EN11, EN12, EN13], rf)
		print machine.encipher(cipherText)
	elif choice == 2:
		machine = Machine([EN11, EN12, EN13, M3A1, M3A2], rf)
		print machine.encipher(cipherText)
	else:
		if encode_decode == 1:
			machine = Machine([MVEN11, MVEN12, MVEN13], rf)
			c_1 = machine.encipher(cipherText)
			machine2 = Machine([MVM3A1, MVM3A2], rf)
			print machine2.encipher(c_1)
		else:
			machine = Machine([D_MVM3A1, D_MVM3A2], rf)
			c_1 = machine.encipher(cipherText)
			machine2 = Machine([D_MVEN11, D_MVEN12, D_MVEN13], rf)
			print machine2.encipher(c_1)

if __name__ == "__main__":
	main()
