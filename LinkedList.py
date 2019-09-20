# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:37:38 2019

@author: Mikef
"""

from Node import Node

class LinkedList(object):
    head = Node
    length = 0
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def setHead(self, head):
        iter = None
        if self.head.hasNext():
            iter = self.head.getNext()
        self.head = Node(head, 1, None)
        self.head.setNext(iter)
    
    def getHead(self):
        return self.head

    def getLength(self):
        return self.length

    def addData(self, password):
        newHead = Node(password, 1, self.head)
        self.head = newHead
        temp = self.length
        temp = temp + 1
        self.length = temp
    
    def contains(self, key):
        node = self.head
        for i in range(self.length):
            if node.getPassword() == key:
                return i
            node = node.getNext()
        return -1
            
    
    def printContents(self):
        iter = self.head
        while iter != None:
            iter.printContents()
            iter = iter.getNext()
            
    def checkAndStore(self, key):
        if self.length == 0:
            self.addData(key)
        iter = None
        check = self.contains(key)
        if check == -1:
            self.addData(key)
        else:
            iter = self.head
            while check > 0:
                iter = iter.getNext()
                check = check - 1
            iter.bump()