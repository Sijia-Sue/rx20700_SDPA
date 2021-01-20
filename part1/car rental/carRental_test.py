# -*- coding: utf-8 -*-
"""
Title: Test part of a car rental system

Authour: Sijia Hou <Sijia at python.org>

Created: 10-Jan-2021
"""

import unittest
from carshop import carshop


class testshop(unittest.TestCase):
    
    def test_invalid_day(self): #this method tests outliers of the car rental days
        test_carshop=carshop(4,3,3)
        tday=test_carshop.rent_car('2030121', 'suv', 1)
        self.assertEqual(tday,True)
        tday=test_carshop.rent_car('2030123', 'suv', 10)
        self.assertEqual(tday,True)
        tday=test_carshop.rent_car('2030124', 'suv', 0)
        self.assertEqual(tday,False)
        tday=test_carshop.rent_car('2030124', 'suv', -1)
        self.assertEqual(tday,False)
        
    
    def test_cartype(self): #this method tests outliers of car type
        test_carshop=carshop(4,3,3)
        tcar_ty=test_carshop.rent_car('2030126', 'hatchback', 2)
        self.assertEqual(tcar_ty,True)
        tcar_ty=test_carshop.rent_car('2030127', 'sedan', 2)
        self.assertEqual(tcar_ty,True)
        tcar_ty=test_carshop.rent_car('2030128', 'suv', 2)
        self.assertEqual(tcar_ty,True)
        a=test_carshop.rent_car('2030129', 'Benz', 2)
        self.assertEqual(a,"Unlisted car type.")
        
        
    def test_return(self): #this method tests the outliers of returning cars
        test_carshop=carshop(4,3,3)
        test_carshop.rent_car('2030121', 'suv', 3)
        t_invalid_para=test_carshop.return_car('2030121')
        self.assertEqual(t_invalid_para[0],'suv')
        self.assertEqual(t_invalid_para[1],3)
        t_invalid_para=test_carshop.return_car('2030122')
        self.assertEqual(t_invalid_para,False)
        
        
if __name__ == '__main__':
	unittest.main()