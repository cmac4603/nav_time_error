import os

f = 101


cwd = os.getcwd()
nav = open(cwd+'/000101_SPX.backup')
nav_list = list(nav)
nav_str = str(nav_list)
nav_ele = [c for c in nav_str]

nav_ele[14] = nav_ele[143]
nav_ele[15] = nav_ele[144]
nav_ele[16] = nav_ele[146]
nav_ele[17] = nav_ele[147]
nav_ele[18] = nav_ele[149]
nav_ele[19] = nav_ele[150]
nav_ele[21] = nav_ele[152]
nav_ele[22] = nav_ele[153]
nav_ele[23] = nav_ele[154]
nav_ele[24] = nav_ele[155]
nav_ele[25] = nav_ele[156]
nav_ele[26] = nav_ele[157]

fix_filenum = str('000%i_SPX.txt' % f)
fix = open(fix_filenum, 'w')
nav_fixed = str(nav_ele)
fix.write(nav_fixed)

__author__ = 'colinmacrae'