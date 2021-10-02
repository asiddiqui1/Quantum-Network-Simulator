# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:51:55 2018

@author: User
"""

from vpython import box,color

class Testing:
    
    def test(self):
        
        ball1 = sphere(pos=vector(0,0,0), radius=0.5, color=color.cyan)
        ball2 = sphere(pos=vector(0,5,0),radius=0.5, color = color.cyan)
        v1 = vector(0,0,0)
        v2 = vector(0,5,0)
        c = curve(v1,v2)