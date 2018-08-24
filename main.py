from classes import Prints, Human
from battle import Battle, IQcheck, STRcheck, CHAcheck
import random

# initializing variables
p1damage = 0
p2damage = 0
ross = Human("Ross", 100,1,100,50,50)
carlos = Human("Carlos", 100,1,75,50,75)
out = Prints(False)
out.line = carlos.description()
out.delay_print()
out.line = ross.description()
out.delay_print()




Battle(ross,carlos)


out.line = carlos.description()
out.delay_print()
out.line = ross.description()
out.delay_print()