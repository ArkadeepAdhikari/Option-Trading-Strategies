#importing the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
sns.set()
os.chdir(r"F:\Option Trading Strategies\Call Options") #setting work directory

def call_profit(S, X, P):
    """This function takes the Spot price (S),Strike Price of call option(X), and call premium(P) 
    as inputs and returns the profit from call option exercise"""
    callpf = np.where(S > X, S - X, 0)    
    return (callpf-P)


def long_call(S, strike, premium):
    """ This funtion takes  Spot price range (S),Strike Price of call option(strike), and call premium 
    as inputs and gives us the profit profile for long position"""
    longcall_profit = call_profit(S, strike, premium)
    # Plot the long call graph
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(S,longcall_profit,label='Long Call profit')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit')
    plt.legend()
    plt.savefig("longcall_profit.png")

def short_call(S, strike, premium):
    """ This funtion takes  Spot price range (S),Strike Price of call option(strike), and call premium 
    as inputs and gives us the profit profile for short position"""
    shortcall_profit = call_profit(S, strike, premium)*(-1.0)
    # Plot the short call graph
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(S,shortcall_profit,label='Short Call profit')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit')
    plt.legend()
    plt.savefig("shortcall_profit.png")

#setting our parameter values
spot = 45 
S = np.arange(0.8*spot,1.2*spot) 
# generating a range to spot prices to study variations in call profit with stock prices

strike = 45 
premium = 2.5

#Generating the profit profile on long position on the call option
long_call(S,strike, premium)

#Generating the profit profile on short position on the call option
short_call(S,strike, premium)

