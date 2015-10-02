import os

cwd = os.getcwd()
nav = open(cwd+'/000101_SPX_orig.backup')
nav_list = list(nav)
nav_str = str(nav_list)
nav_ele = [c for c in nav_str]

print(nav_ele[19])




__author__ = 'colinmacrae'
