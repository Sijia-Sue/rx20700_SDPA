# -*- coding: utf-8 -*-

"""
Title: Carshop class of a car rental system

Authour: Sijia Hou <Sijia at python.org>

Created: 10-Jan-2021
"""
import pandas as pd

class carshop:
    """
    use df_record to record car rental information
    df_record will be used to verfity whether this customer rent a car
    use stock to update the inventory of the car 
    """
    def __init__(self,hatchbackNum,sedanNum,suvNum):
        self.df_record=pd.DataFrame(columns=['customer_id', 'cartype', 'days'])
        self.stock={'hatchback':{'in_stock':hatchbackNum},
                    'sedan':{'in_stock':sedanNum},
                    'suv':{'in_stock':suvNum}
                    }
        
    #List car information sheets to non-VIP customers through df_show   
    def show(self):
        df_show= pd.DataFrame([['hatchback',self.stock.get('hatchback').get('in_stock'),'£30','£25'],
                            ['sedan',self.stock.get('sedan').get('in_stock'),'£50','£40'],
                            ['suv',self.stock.get('suv').get('in_stock'),'£100','£90']],
                            columns=['cartype','stock','daily price for less than 7 days',
                                     'daily price for longer period'])
        print(df_show)
    
    #List car information sheets to VIP customers through df_show
    def show_VIP(self):
        df_showVIP=pd.DataFrame([['hatchback',self.stock.get('hatchback').get('in_stock'),'£20'],
                            ['sedan',self.stock.get('sedan').get('in_stock'),'£35'],
                            ['suv',self.stock.get('suv').get('in_stock'),'£80']],
                            columns=['cartype','stock','Daily price'])
        print(df_showVIP)
     
    # This method implements the car rental operation
    def rent_car(self,customer_id,rent_cartype,day):
        day=int(day)
        c=str(rent_cartype)
        typelist=['hatchback','sedan','suv']
        d1={'hatchback':'£30','sedan':'£50','suv':'£100'}
        d2={'hatchback':'£25','sedan':'£40','suv':'£90'}
        
        #Get the customer id in df_record and if the customer has a record then the car cannot be rented
        customer_columns=self.df_record['customer_id'].values.tolist()
        
        if customer_id in customer_columns:
            print("Sorry,each account can only rent one car at most, so you cannot rent another car"+"\n")
            return False
        
        
        elif rent_cartype in typelist:
            #Determine whether the car is still in stock
            if self.stock.get(rent_cartype).get('in_stock')>0:
                    
                #Car has been rented and the inventory of the corresponding model is reduced by one
                self.stock.get(rent_cartype).update({'in_stock':self.stock.get(rent_cartype).get('in_stock')-1})
                    
                #Create a rental car record and add it to df_record
                new=pd.Series({'customer_id':customer_id,'cartype':rent_cartype,'days':day})
                self.df_record=self.df_record.append(new,ignore_index=True)
                    
                    
                if day>0 and day<7:
                    print("You have rented a "+rent_cartype+"car for",day,"days. You will be charged",
                          d1[c],"per day, We hope that you enjoy our service"+"\n")
                    return True
                elif day>=7:
                    print("You have rented a "+rent_cartype+"car for",day,"days. You will be charged",
                          d2[c],"per day, We hope that you enjoy our service"+"\n")
                    return True
                else:
                    return False
            else:
                print("Sorry,this type of car is not in stock now. Please change your choice."+"\n")
                return False
        else:
            d="Unlisted car type."
            return d
            
            
    def rent_car_VIP(self,customer_id,rent_cartype,day):
        c=rent_cartype
        typelist=['hatchback','sedan','suv']
        d3={'hatchback':'£20','sedan':'£35','suv':'£80'}
        
        #List the customer id in df_record and if the customer has a record then the car cannot be rented
        customer_columns=self.df_record['customer_id'].values.tolist()
        if customer_id in customer_columns:
            print("Sorry,each account can only rent one car at most, so you cannot rent another car"+"\n")
            return False
        
        elif rent_cartype in typelist:
            
            if self.stock.get(rent_cartype).get('in_stock')>0:
                #Car has been rented and the inventory of the corresponding model is reduced by one
                self.stock.get(rent_cartype).update({'in_stock':self.stock.get(rent_cartype).get('in_stock')-1})
                    
                #Create a rental car record and add it to df_record
                new=pd.Series({'customer_id':customer_id,'cartype':rent_cartype,'days':day})
                self.df_record=self.df_record.append(new,ignore_index=True)
                
                print("You have rented a "+rent_cartype+"car for",day,"days. You will be charged",
                      d3[c],"per day, We hope that you enjoy our service"+"\n")
                return True
                
            else:
                print("Sorry,this type of car is not in stock now. Please change your choice."+"\n")
                return False
                
        else:
            d="Unlisted car type."
            return d
            
    # This method implements the return operation    
    def return_car(self,customer_id):
        
        #List the customer id in df_record and verfity whether the customer rented a car
        customer_columns=self.df_record['customer_id'].values.tolist()
        if customer_id in customer_columns:
            
            a=customer_columns.index(customer_id)   #index the row number of customer's row 
            
            #Use row number and column number to index the car type and rent time
            return_type=self.df_record.iloc[int(a),1]   
            day=self.df_record.iloc[int(a),2]
            
            #Car has been returned and the inventory of the corresponding model is increased by one
            self.stock.get(return_type).update({"in_stock":self.stock.get(return_type).get("in_stock")+1})
            return return_type,int(day)
        
        else:
            print("Sorry,you have no car rental record."+"\n")
            return False