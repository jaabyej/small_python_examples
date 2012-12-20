# -*- coding: utf-8 -*-
'''
Created on 05/12/2012

@author: Maria
'''
#Kun små bokstaver og tal

import random
import string

char_set = string.ascii_lowercase + string.digits
print(''.join(random.sample(char_set,8)))
      
