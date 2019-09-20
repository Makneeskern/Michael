# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:17:31 2019

@author: Mikef
"""

from LinkedList import LinkedList

def main ():
    passwords = LinkedList()
    file = open("10-million-combos.txt", 'r')
    uncollected = file.readlines()
    i = 0
    for line in uncollected:
        print(i)
        seperated = line.strip().split()
        passwords.checkAndStore(seperated[len(seperated) - 1])
        i = i + 1
    
    print(passwords.getLength())
        
main()