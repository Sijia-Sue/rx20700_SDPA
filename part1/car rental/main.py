# -*- coding: utf-8 -*-
"""
Title: A car rental system

Authour: Sijia Hou <Sijia at python.org>

Created: 10-Jan-2021
"""

import sys
from carshop import carshop
from customer import customer
from VIP import VIP

newshop=carshop(4,3,3) #Initialize the carshop

"""
Determine whether the user is a VIP.

"""
level=input("Are you a VIP? If yes, please enter Y, if not, please enter N"+"\n")
if level=='N':
    newcustomer=customer()
elif level=='Y':
    newcustomer=VIP()
else:
    print("Invalid input.")
    sys.exit()
    
    
"""
This is the function selection part.
"""
while True:
    
    print("Select the desired function:")
    print("1.Check car inventory and price")
    print("2.Rent a car")
    print("3.Return a car")
    print("4.Exit")
    option=int(input("input your choice:"))
    
    
    #Display car rental information according to whether customer is a vip
    if option==1:
        if level=='N':
            newshop.show()
        elif level=='Y':
            newshop.show_VIP()
            
    #Rent a car and customer could only choose 3 types of cars         
    elif option==2:
        customer_id=input("Please input your customer id:")
        print("What type of car do you want to rent?")
        print("1.hatchback"+"\n"+"2.sedan"+"\n"+"3.suv")
        car=int(input("input your choice:"))
        day=input("How many days do you want to rent?")
        if level=='N':
            if car==1:
                rent_cartype='hatchback'
                newshop.rent_car(customer_id, rent_cartype, day)
            elif car==2:
                rent_cartype='sedan'
                newshop.rent_car(customer_id, rent_cartype, day)
            elif car==3:
                rent_cartype='suv'
                newshop.rent_car(customer_id, rent_cartype, day)
            else:
                print("unlisted car type.")
                break
        elif level=='Y':
            if car==1:
                rent_cartype='hatchback'
                newshop.rent_car_VIP(customer_id, rent_cartype, day)
            elif car==2:
                rent_cartype='sedan'
                newshop.rent_car_VIP(customer_id, rent_cartype, day)
            elif car==3:
                rent_cartype='suv'
                newshop.rent_car_VIP(customer_id, rent_cartype, day)
            else:
                print("Unlisted car type.")
                break
            
    #The customer can only return the car if there is a car rental record        
    elif option==3:
        customer_id=input("Please input your customer id:")
        carty_time=newshop.return_car(customer_id)  
        if carty_time==False:   #This customer does not have a car rental record
            break
        else:
            cartype=carty_time[0]
            days=carty_time[1]
            print("Your bill is as follows:")
        if cartype=='hatchback' and level=='N':
            newcustomer.fee(customer_id, cartype, days)
        elif cartype=='sedan' and level=='N':
            newcustomer.fee(customer_id, cartype, days)
        elif cartype=='suv' and level=='N':
            newcustomer.fee(customer_id, cartype, days)
        elif cartype=='hatchback' and level=='Y':
            newcustomer.fee_VIP(customer_id, cartype, days)
        elif cartype=='sedan' and level=='Y':
            newcustomer.fee_VIP(customer_id, cartype, days)
        elif cartype=='suv' and level=='Y':
            newcustomer.fee_VIP(customer_id, cartype, days)
            
            
    elif option==4:
        print("Exit successfully!")
        break
            
        
                    



    
        
        
        
        
        

