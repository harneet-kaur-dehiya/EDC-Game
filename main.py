from IPython.display import Image 
from IPython.display import display


questionbank={'A JFET is a ______ driven device': 'Voltage', 
              'The MOSFET stands for': 'Metal Oxide Semiconductor field Effect Transistor', 
              'In which region does FET act as voltage-controlled resistor?': 'Ohmic Region',
              'For zero temperature drift FET, Vp=-2.5V. Find Vgs':'-1.872',
              'A certain E-MOSFET has ID(on) = 6mA, VGS(on) = 8V and VGS(TH) = 3V The value of kn is ______':'0.24 mA/V2',
              'For a FET when will maximum current flow':'Vgs = 0V, Vds >= |Vp|',
              'What is the value of drain current for gate-to-source voltage (VGS) of about 6V of E-MOSFET along with ID(ON) = 2mA at VGS & VGS (threshold) of about 12V & 4V respectively?':'2mA',
              'In a certain CS JFET amplifier, RD= 1kΩ, RS= 560 Ω, VDD=10V and gm= 4500 μS. If the source resistor is completely bypassed, the voltage gain is ___________':'4.5',
              'A MOSFET has _____________ terminals':'three',
              'If a JFET has IDSS = 10 mA and VP = 2 V, then RDS equals':'200 ohm',
              'FET has ______ input impedance':'high',
              'A certain D-MOSFET is biased at VGS = 0 V. Its data sheet specifies IDSS = 20mA and VGS(off) = -5 V. The value of the drain current is _________':'20 mA',
              'Transconductance is measured in _______':'Siemens',
              'A FET is a ______ transitor':'Unipolar',
              'A certain p-channel E-MOSFET has VGS(th) =-2V. If VGS= 0V, the drain current is ____':'0 mA',
              'A CS JFET amplifier has a load resistance of 10 kΩ, RD= 820Ω. If gm= 5mS and Vin= 500 mV, the output signal voltage is _____':'1.89 V',
              'Determine the voltage gain for a n channel JFET where VDD = 16V, R1 = 2.1MΩ, R2 = 270kΩ, RD = 2.4kΩ, RS = 1.5kΩ, C1 = 5µΩ, C2 = 10µΩ, CS = 20µΩ, IDSS = 8mA and VP = -4V':'-5.28'}
import random
def hangman():
    select = random.choice(list(questionbank.items()))
    word = select[1]
    question = select[0]
    print(question)
    print("Try to guess the answer in less than 7 attempts\n")
    validLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ1234567890.-/,|<>='
    turns = 7
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print('\n'+main)
            print("\nCorrect Answer!! \nYou win!")
            break

        print('\n')
        print("Enter a letter / number:" + main + '\n')
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("\nEnter a valid character")
            guess = input()
            
        if guess not in word:
            turns = turns - 1
            if turns == 6:
                print("Wrong guess!")
                print('6 turns left')
                display(Image(filename='images1.jpg'))
            if turns == 5:
                print("Wrong guess!")
                print('5 turns left')
                display(Image(filename='images2.jpg'))
            if turns == 4:
                print("Wrong guess!")
                print('4 turns left')
                display(Image(filename='images3.jpg'))
            if turns == 3:
                print("Wrong guess!")
                print('3 turns left')
                display(Image(filename='images4.jpg'))
            if turns == 2:
                print("Wrong guess!")
                print('2 turns left')
                display(Image(filename='images5.jpg'))
            if turns == 1:
                print("Wrong guess!")
                print('1 turn left')
                print("Last breaths counting, Take care!")
                display(Image(filename='images6.jpg'))
            if turns == 0:
                print("\nYou lose")
                print("You let a kind man die")
                display(Image(filename='images7.jpg'))
                break
                
name = input("Enter your Name:  ")
print("Welcome: " , name)
print("\n____________________\n")
hangman()
