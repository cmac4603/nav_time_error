import os

print('Welcome to SPX Navigation Time Error v4.1')
print('This program was written to replace the V5 navigation time')
print('with the time from the GASGC3 time portion of the same string')
print('using 000000_SPX.backup files and saving as 000000_SPX.txt')

user_dir = input('Enter the full folder address containing SPX.backup files here --> ')
dir = os.chdir(user_dir)
cwd = os.getcwd()
user_firstfix = input('Enter the first fix number --> ')
user_lastfix = input('Enter the last fix number  --> ')
ff_str = user_firstfix.zfill(6)
ff_int = int(user_firstfix)
f_incint = int(ff_str)
lf = int(user_lastfix) + 1

for x in range(ff_int,lf):
    f_incstr = str(f_incint).zfill(6)
    nav = open(cwd+'/%s_SPX.backup' % f_incstr)
    nav_list = list(nav)
    nav_str = str(nav_list)
    nav_ele = list(nav_str)
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
    nav_filenum = str('%s_SPX.txt' % f_incstr)
    nav_string = open(nav_filenum, 'w')
    nav_string.write(good_nav[2:265]+"\n"+good_nav[271:296]+"\n")
    f_incint = int(f_incstr)
    f_incint += 1

__author__ = 'colinmacrae'