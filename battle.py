import random
from classes import Prints
out = Prints(False)
def Battle(p1,p2):
  global out, p1damage,p2damage
  p1damage = 0
  p2damage = 0
  IQcheck(p1,p2)
  STRcheck(p1,p2)
  CHAcheck(p1,p2)
  Critical(p1,p2)
  p1.hp = p1.hp- p2damage
  p2.hp = p2.hp- p1damage
  return p1.hp,p2.hp
def IQcheck(p1,p2):
  global p1damage,p2damage
  if p1.iq > p2.iq:
    p1damage = p1damage + (p1.iq - p2.iq)
    out.line = ("{}'s IQ is larger than {}'s. {} takes {} damage.\n".format(p1.name,p2.name, p2.name,(p1.iq-p2.iq)))
    out.slow_print()
  if p1.iq < p2.iq:
    p2damage = p2damage + (p2.iq - p1.iq)
    out.line = ("{}'s STR is larger than {}'s. {} takes {} damage.\n".format(p2.name,p1.name, p1.name,(p2.iq-p1.iq)))
    out.slow_print()
  return p1damage,p2damage
def STRcheck(p1,p2):
  global p1damage,p2damage
  if p1.strength > p2.strength:
    p1damage = p1damage + (p1.strength - p2.strength)
    out.line = ("{}'s STR is larger than {}'s. {} takes {} damage.\n".format(p1.name,p2.name, p2.name,(p1.strength-p2.strength)))
  if p1.strength < p2.strength:
    p2damage = p2damage + (p2.strength - p1.strength)
    out.line = ("{}'s STR is larger than {}'s. {} takes {} damage.\n".format(p2.name,p1.name, p1.name,(p2.strength-p1.strength)))
    
    out.slow_print()
    
  
def CHAcheck(p1,p2):
  global p1damage,p2damage
  if p1.charisma > p2.charisma:
    p1damage = p1damage + (p1.charisma - p2.charisma)

    out.line = ("{}'s CHA is larger than {}'s. {} takes {} damage.\n".format(p1.name,p2.name, p2.name,(p1.charisma-p2.charisma)))
    out.slow_print()
  if p1.charisma < p2.charisma:
    p2damage = p2damage + (p2.charisma - p1.charisma)
    out.line = ("{}'s STR is larger than {}'s. {} takes {} damage.\n".format(p2.name,p1.name, p1.name,(p2.charisma-p1.charisma)))
    out.slow_print()
  return p1damage,p2damage
def Critical(p1,p2):
  global p1damage,p2damage
  hit = random.randint(1,5)
  multiplier = int(random.random()*10) / 10.0+1
  if hit == 1:
    p1damage = p1damage*multiplier
    out.line = "{}'s attack was critical! His damage got a {}x multiplier!\n".format(p1.name,multiplier)
    out.slow_print()
  if hit ==5:
    p2damage = p2damage*multiplier
    out.line = "{}'s attack was critical! His damage got a {}x multiplier!\n".format(p2.name,multiplier)
    out.slow_print()
  return p1damage, p2damage