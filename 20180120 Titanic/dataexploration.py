# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:06:25 2018

@author: Caio Martins Ramos de Oliveira
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pds

trset = []

with open("train.csv","r") as train:
    for line in train:
        trset += [line]

print (trset)