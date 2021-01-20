# -*- coding: utf-8 -*-
"""
Title: Customer class of a car rental system

Authour: Sijia Hou <Sijia at python.org>

Created: 10-Jan-2021
"""

import pandas as pd


class customer:
    def __init__(self):
        #use df to display the bill
        self.df=pd.DataFrame(columns=['CusmoterID','cartype','days','fee'])
        
    # This method is used to calculate the non VIP car rental fee    
    def fee(self,CusmoterID,cartype,days):
        
        if int(days)>0 and int(days)<7:
            
            if cartype=='hatchback':
                fee=int(days)*30
                
                #Create the bill information and add it into df
                new=pd.Series({'CusmoterID':CusmoterID,'cartype':cartype,'days':days,'fee':fee})
                self.df=self.df.append(new,ignore_index=True)
                print(self.df)
                print("\n")
                return True
            
            elif cartype=='sedan':
                fee=int(days)*50
                new=pd.Series({'CusmoterID':CusmoterID,'cartype':cartype,'days':days,'fee':fee})
                self.df=self.df.append(new,ignore_index=True)
                print(self.df)
                print("\n")
                return True
            
            elif cartype=='suv':
                fee=int(days)*100
                new=pd.Series({'CusmoterID':CusmoterID,'cartype':cartype,'days':days,'fee':fee})
                self.df=self.df.append(new,ignore_index=True)
                print(self.df)
                print("\n")
                return True
            
            else:
                print("The type of car is invalid")
                return False
            
    
        elif int(days)>=7:
            
            if cartype=='hatchback':
                fee=int(days)*25
                new=pd.Series({'CusmoterID':CusmoterID,'cartype':cartype,'days':days,'fee':fee})
                self.df=self.df.append(new,ignore_index=True)
                print(self.df)
                print("\n")
                return True
            
            elif cartype=='sedan':
                fee=int(days)*40
                new=pd.Series({'CusmoterID':CusmoterID,'cartype':cartype,'days':days,'fee':fee})
                self.df=self.df.append(new,ignore_index=True)
                print(self.df)
                print("\n")
                return True
            
            elif cartype=='suv':
                fee=int(days)*90
                new=pd.Series({'CusmoterID':CusmoterID,'cartype':cartype,'days':days,'fee':fee})
                self.df=self.df.append(new,ignore_index=True)
                print(self.df)
                print("\n")
                return True
            
            else:
                print("The type of car is invalid")
                return False
            
        else:
            print("The rental time is invalid")
            return False
