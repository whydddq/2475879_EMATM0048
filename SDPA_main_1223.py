from wwyclass import *



def main():
     market=Market()
     users=[]  # initialize an empty list for users   
     user_names=[]
     while True:
         try:
            days = int(input("Please enter the number of Days to simulate: "))
            if days < 7:
                print("The number of Days to simulate is too small. Please try again.")
                continue
            else:
                break  
          except ValueError:
            print("Invalid input. Please enter a number.")
     while True:
           try:
              num_users = int(input("Please enter number of Users: "))
              break
           except ValueError:
              print("Invalid input. Please enter a number.")
     
    
     for i in range(num_users):
           while True:
            user_name_raw=input(f"Please enter the name of User{i+1}: ")
            if user_name_raw in user_names:
                print("invalid input, input again")
            else:
                user_names.append(user_name_raw)
                users.append(useraccount(user_name_raw))
                break
     run_blockchain=blockchain_system() 

     for day in range(1,days+1):
            print(f"====== Simulation Day {day} ======")
            market.generate_daily_price(day)  # add "day" to help to run the data
            
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
     for user in users:
        user.visualize_asset(market)        # add the code to ensure the plot of users' asset is right, or the result will not be the end of the last day, it will be the begin of the last day
     visualization(market, users)
     print("game is over")
           


# run the main function
main()
              
              
