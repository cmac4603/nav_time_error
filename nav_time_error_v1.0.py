import os

cwd = os.getcwd()
nav = open(cwd+'/000101_SPX.backup')
nav_list = list(nav)
nav_str = str(nav_list)

print(nav_str[15])




__author__ = 'colinmacrae'
