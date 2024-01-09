# SDPA_coursework
https://github.com/whydddq/SDPA_coursework

In Part 1 of the coursework, I need to utilize object-oriented design principles in Python to create a simulation game about a virtual currency called SDPACoin.

In the game, users participate in can operate various activities such as buying and selling SDPACoins and mining machines, and turning their mining machines on or off. Initially, we need to set the number of days to simulate, which must be more than seven days, the simulator will print “The number of Days to simulate is too small” when a shorter duration is input. Besides, users also determine the number of participants and their names. On each simulated day, the system generates random market information, such as the daily price of SDPACoins and electricity fees. Furthermore, the system will produce 100 SDPACoins daily, distributing them among users and the market based on the proportion of their mining machines. According to current market information and their insights, users choose their actions to gain the most profits. After simulating all the set days, the system will generate two plots: one is a line graph of daily SDPACoins’ price and another one is a line graph of users’ total assets for comparison. The users’ asset value includes the GBP cash, holding SDPA market value, and holding machine value. In detail, due to the game's settings, if users do not sell their machines, the machines can run indefinitely. Therefore, it can be assumed that there is no depreciation for the mining machines. Thus, I can use 300 GBP which is the same price as selling one to calculate the value of each machine.

As for the file of “wwyclass”. Firstly, I defined a class named “useraccount” to store users’ basic information like name, GBP balance, SDPACoins balance, and the number of holding mining machines. This class also includes functions for buying and selling SDPACoins and mining machines.

Second, the “blockchain_system” class was created to manage the distribution of SDPACoins every day between the users and the market based on the proportion of holding mining machines.

Following that, I initialized the “Market” class about some market-related aspects such as the price of SDPACoin and the cost of electricity, which are generated randomly. Then, it defined a function to calculate the daily electricity expenses for users and market based on the current price of electricity and the number of  their holding machines.

Then, I created a function for visualization which lets users check the trend of daily SDPACoins price, aiding users to choose the right actions. Users can also observe a line graph indicating the present users’ asset value.

Lastly, the “handle_user_actions” function was established to receive and execute various actions combined with invoking the previously defined functions. The part also included error and exception handling. When incorrect data is entered, it shows “invalid input, input again”.

Regarding the “SDPA_main_1223” file, it starts with defining some useful variables to store simulation days, the number of users, and users’ names. Then, there is a loop to store names of users. All above operations includes the error and exception handling to deal with the special situations. Subsequently, it invokes various functions from “wwyclass” such as the “blockchain_system” class, followed by another loop to simulate the set days. Besides, there is also a function to monitor if the users reach bankruptcy, which occurs when users’ GBP balances are insufficient to cover their daily electricity costs. In order to simplify, the mining machines still belong to the bankrupt user, the system still distributes a specific amount of SDPACoins to bankrupt user, but they no longer actively participate in the game, so we will ignore the parts of SDPACoins. Finally, after simulating all the set simulation days, there are two plots helping us to visualize and find the winner who has the most asset value.

In order to keep an accurate assets value comparison, the game has no limited length of decimals to make data seems more apparent.

Bonus question:
1. From running my simulation game, I observed that once users choose to purchase the mining machines, they would almost end up with losing money when the set simulation days are short. Only in sufficiently long time simulation days, users can earn money in the system. Therefore, I think that we should be cautious about the decision whether to buy the mining machines, and it is better to hold them for the long term once buying them.
2. I found that individuals’ actions have a limited influence on the whole virtual currency market.
3. The cryptocurrency market is highly unpredictable with significant investing risk. For example, the daily price of virtual currencies and electricity costs are all randomly generated, which makes it impossible to make a reliable prediction about the market.

For Part 2, users need to install the yfinance library through typing and executing "pip install yfinance" in the Command Line Interface first.
