# -*- coding: utf-8 -*-
"""
Title: VIP class of a car rental system

Authour: Sijia Hou <Sijia at python.org>

Created: 10-Jan-2021
"""

import pandas as pd
from customer import customer

class VIP(customer):
    def __init__(self):
        super().__init__()
        self.isVIP=0
    
    # This method is used to calculate the VIP car rental fee
    def fee_VIP(self,CusmoterID,cartype,days):
        
        if int(days)>0:
            
            if cartype=='hatchback':
                fee=int(days)*20
                
                #Create the bill information and add it into df
                new=pd.Series({'CusmoterID':CusmoterID,'cartype':cartype,'days':days,'fee':fee})
                self.df=self.df.append(new,ignore_index=True)
                print(self.df)
                return True
            
            elif cartype=='sedan':
                fee=int(days)*35
                new=pd.Series({'CusmoterID':CusmoterID,'cartype':cartype,'days':days,'fee':fee})
                self.df=self.df.append(new,ignore_index=True)
                print(self.df)
                return True
            
            elif cartype=='suv':
                fee=int(days)*80
                new=pd.Series({'CusmoterID':CusmoterID,'cartype':cartype,'days':days,'fee':fee})
                self.df=self.df.append(new,ignore_index=True)
                print(self.df)
                return True
            
            else:
                print("The type of car is invalid")
                return False
            
        else:
            print("The rental time is invalid")
            return False

