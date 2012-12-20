# -*- coding: utf-8 -*-
'''
Created on 05/12/2012

@author: Maria
'''
#Uppercase først

import random
import string

chara_set = string.ascii_uppercase
char_set = string.ascii_lowercase + string.digits
print((''.join(random.sample(chara_set,1)))+''.join(random.sample(char_set,9)))
   
