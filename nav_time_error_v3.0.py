import os

f = 100
s = 100

dir = os.chdir('/Users/colinmacrae/Documents/Programming/untitled_tests_py3/nav_time_error/051PA060')
cwd = os.getcwd()
nav = open(cwd+'/000%i_SPX.backup' % s)
nav_list = list(nav)
nav_str = str(nav_list)
nav_ele = list(nav_str)

for x in range(100,932):
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

    good_nav = (''.join(nav_ele))
    nav_filenum = str('000%i_SPX.txt' % f)
    nav_string = open(nav_filenum, 'w')
    nav_string.write(good_nav[2:265]+"\n"+good_nav[271:296]+"\n")
    f += 1
    s += 1

__author__ = 'colinmacrae'