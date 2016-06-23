'''
This is to hook all the classes and stuff for Sprak.dll for C#.
'''
import clr
started = 0
for started == 0:
    AddReferance('Sprak.dll')
    started = 1
    from Sprak.dll import *
    print('referance added!')