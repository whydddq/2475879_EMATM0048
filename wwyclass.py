"""
name: wenying wang
section: Part 1. class
There are all the classes and functions i will need in the main product.
"""
"""
Firstly, create my class include user account, blockchain system and market
"""
"""
define the user account class
"""
class useraccount:
    
    def __init__(self, user_name, GBP_capital=10000, SDPA_balance=0, mining_machines=0):  #Managing user name, GBP capital, SDPA balance, and mining machines.

        self.users_asset=[] 
        self.user_name=user_name
        self.GBP_capital=GBP_capital
        self.SDPA_balance=SDPA_balance
        self.mining_machines=mining_machines
        self.instance=True
    def visualize_asset(self, market):  #calculate and record the asset value of user to help visualize.

        asset_value=self.GBP_capital+self.SDPA_balance*market.SDPA_price+300*self.mining_machines
# Due to the game's settings, if users do not sell their machines, the machines can run indefinitely. 
# Therefore, it can be assumed that there is no depreciation for the machines. 
# So, I can use 300 GBP to calculate the value of each machine.
        self.users_asset.append(asset_value)
  
    def buy_SDPA_trade(self,market):

   # Executes a buying transaction for SDPA using GBP capital in the user's account.  


        num_action_buy=float(input(">>> Enter number of SDPA to buy:"))
        total_cost=num_action_buy*market.SDPA_price

        if self.GBP_capital>=total_cost:
            self.GBP_capital-=total_cost
            self.SDPA_balance+=num_action_buy
           
        else:
         print("GBP is insufficient,fail to buy")
    def sell_SDPA_trade(self,market):

    # Executes a selling transaction for SDPA using GBP capital in the user's account.  
     
        num_action_sell=float(input(">>> Enter number of SDPA to sell:"))
        total_profit =num_action_sell*market.SDPA_price

        if self.SDPA_balance>=num_action_sell:   
         self.GBP_capital+=total_profit
         self.SDPA_balance-=num_action_sell
       
  

        else:
         print("SDPA is insufficient,fail to sell")
    def buy_machine_trade(self,market):

    # Executes a buying transaction for mining machines using GBP capital in the user's account.  
  
        num_action_buy_ASIC=int(input(">>> Enter number of ASIC to buy:"))
        total_cost=num_action_buy_ASIC*600

        if self.GBP_capital>=total_cost:
         self.mining_machines+=num_action_buy_ASIC
         self.GBP_capital-=total_cost
         market.num_market_machine-=num_action_buy_ASIC
 
    
        else:
           print("GBP is insufficient,fail to buy")
       
    def sell_machine_trade(self,market):

   # Executes a selling transaction for mining machines using GBP capital in the user's account.  
 
       num_action_sell_ASIC=int(input(">>> Enter number of ASIC to sell:"))
       total_profit=num_action_sell_ASIC*300

       if self.mining_machines>=num_action_sell_ASIC:
        self.mining_machines-=num_action_sell_ASIC
        self.GBP_capital+=total_profit
   
        market.num_market_machine+=num_action_sell_ASIC
    
      
       else:
          print("ASIC is insufficient,fail to sell")
    # edit the code to correct the logic
    def instance_status(self):
        self.instance=not self.instance
        print(f"{self.user_name} change the status of the instance")
        


class blockchain_system:    # define the Blockchain System class
  
      def __init__(self):
        # self.transactions=[]
        self.machines=1000  # the number of machines of market


          
       # It distributes the daily SDPA among miners and market 
      def SDPA_distribution(self,users):   #users represent user1,user2,user3……
      # calculate the number of mining machines of all the users in the game
      # calculate the number of active machine
          on_machine=self.machines
          for user in users:
              if user.instance:
                 on_machine+=user.mining_machines

         
          if on_machine>0:   
      # calculate the number of SDPA each machine will be allocated
              SDPA_distri_num=100/on_machine
      # calculate and print the number of SDPA which is distributed to market
              market_distri=1000*SDPA_distri_num
              print(f"{market_distri}SDPA distributed to Market")
      # calculate the number of SDPA which is distributed to users
              for user in users:
                 if user.instance:
                     user_allo_SDPA=SDPA_distri_num*user.mining_machines
                     user.SDPA_balance+=user_allo_SDPA
                     if user_allo_SDPA>0:
                         print(f"{user_allo_SDPA} SDPA distributed to {user.user_name}")
                    
          else:
              print("No mining machines available for SDPA distribution.")

                 
        

import random


class Market:
    # Market: Generates daily SDPA price, electricity price, 
    # acts as the counterparty for users to trade SDPA, and maintains the special status with 1000 ASIC machines.
    def __init__(self):
        self.record_SDPA_price=[] # create a empty list to record the history of SDPA price to visualize
        self.SDPA_price=40
        self.electricity_price=round(random.uniform(1.9,2.1),2)
        self.num_market_machine=1000
        # Give the market a huge initial balance of GBP and SDPA.
        self.market_GBP=float('inf')
        self.market_SDPA=float('inf')
        # define the number of machines of all the users and market
        self.machines_num=1000

    def visualize_SDPA_price(self):

        self.record_SDPA_price.append(self.SDPA_price)
        
    def generate_daily_price(self,day):
        # daily return is draw from normal distribution N(0.003,0.0016)
        if day==1:
            self.SDPA_price=40
        else:
            mean=0.003
            gen=0.0016**0.5  # correct the code:  N(0.003,0.0016) ,the "0.0016" is the variance not the standard variance
            self.daily_return=random.gauss(mean,gen)
            self.t_price=self.SDPA_price
            self.SDPA_price=round(self.SDPA_price+self.t_price*self.daily_return,1)
        self.electricity_price=round(random.uniform(1.9,2.1),2)   # Let the electricity bill remain two decimal places to simplyfy the game


  
    def electricity_pay_market(self):
        electricity_pay=self.electricity_price*self.num_market_machine
        print(f"market pays {electricity_pay} electricity bill.")
     


import matplotlib.pyplot as plt

def visualization(market, users):
    plt.figure(figsize=(10,20))
    plt.plot(market.record_SDPA_price,label='SDPA Price')
    plt.title('SDPA Price Trend')
    plt.xlabel('Day')
    plt.ylabel('SDPA Price')
    plt.show()

    for user in users:
        plt.plot(user.users_asset,label=f'{user.user_name} Assets')
    plt.title('User Asset Value')
    plt.xlabel('Day')
    plt.ylabel('Asset Value')
    plt.legend()    # Add a legend to identify the value asset belongs to whitch user
    plt.show()




     
def handle_user_actions(user,users,market):
    
    while True:
        print(f"{user.user_name}'s action: current balance {user.GBP_capital} GBP, {user.SDPA_balance} SDPA, {user.mining_machines} ASIC.")
        print("1 to buy SDPA, 2 to sell SDPA, 3 to buy ASIC miners, 4 to end the turn, 5 to turn off/on the mining machines, 6 to sell ASIC miners, 7 to visualize the SDPA price and users' asset")
        action = input(">>> Enter your action: ")
        if  action=='1':  
            try:
               user.buy_SDPA_trade(market)
            except ValueError:
                   print("invalid input, input again")

        elif action=='2': 
            try:
               user.sell_SDPA_trade(market)
            except ValueError:
                 print("invalid input, input again")
            
        elif action=='3':
            try:
                user.buy_machine_trade(market)    
            
            except ValueError:
                   print("invalid input, input again")
                   
        elif action=='4':
                break
            
        elif action=='5':
            try:
                   user.instance_status()    
            except ValueError:
                      print("invalid input, input again")
        elif action=='6':
            try:
                 user.sell_machine_trade(market)    
            except ValueError:
                   print("invalid input, input again")
        elif action=='7':
            try:
                  visualization(market, users)
            except ValueError:
                   print("invalid input, input again")
        else:
            print("invalid input, input again")
        
        
        
        
        
        
        
        
        
