'''
Connect photogate with LED  between OD1 and GND and PhotoDiode between IN1 and GND

Use function print p.get_frequency(3) # to get frequency of square wave at at pin 3 
'''

import expeyes.eyemath as em
p = expeyes.eyesj.open()
p.set_state(10,1)   # sets OD1 at HIGH, Channel No for OD1 id 10
print p.get_frequency(3)

