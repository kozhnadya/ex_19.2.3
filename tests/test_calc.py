# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 09:40:36 2022

@author: zbookuser
"""

import pytest


from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator
        
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6
    
    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2) == 3
    
    def test_substraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 8, 4) == 4
        
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 5) == 10
        