#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 22:04:57 2023

@author: guzhemeimao
"""

from wwyclass import *



def main():
     market=Market()
     users=[]  # initialize an empty list for users   
     days=int( input(" Please enter number of Days to simulate:"))
     if days<7:
         print("The number of Days to simulate is too small")
         days=int( input(" Please enter number of Days to simulate:"))
     num_users=int( input(" Please enter number of Users: "))
    
     for i in range(num_users):
        user_name=input(f"Please enter the name of User{i+1}: ")
        users.append(useraccount(user_name))
     run_blockchain=blockchain_system() 

     for day in range(1,days+1):
            print(f"====== Simulation Day {day} ======")
            market.generate_daily_price()
            
            market.visualize_SDPA_price()
            for user in users:
                user.visualize_asset(market)
                
            after_daily_add_machines=market.machines_num+(day-1)*10
            print(f"The price of SDPA is {market.SDPA_price}. Electricity unit cost {market.electricity_price}. Total number of ASIC machines {after_daily_add_machines}.")
            run_blockchain.SDPA_distribution(users)
            market.electricity_pay_market()
            for user in users:
                  if user.instance: # check if the user's machines are active
                      electricity_pay_user=user.mining_machines*market.electricity_price
                      user.GBP_capital-=electricity_pay_user
                      if electricity_pay_user!=0:
                          print(f"{user.user_name} pays {electricity_pay_user} electricity bill")

                  if user.GBP_capital<0:
                      print(f"{user.user_name} has gone bankrupt.")
                      market.machines_num-=user.mining_machines
                      user.mining_machines=0
                      user.SDPA_balance=0
                      users.remove(user)  
            for user in users:
                  handle_user_actions(user,users,market)
     visualization(market, users)
     print("game is over")
           


# run the main function
main()
              
              