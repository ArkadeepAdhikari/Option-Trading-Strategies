# -*- coding: utf-8 -*-
"""
@author: ARKADEEP
"""
"""Covered Call strategy is used when we have a mildly bullish view on the market. 
   Here the strategy is to sell a call option on a stock owned by the option writer."""

#importing the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
sns.set()
os.chdir(r"F:\Option Trading Strategies\Covered Call") #setting work directory

def call_profit(S, X, P):
    """This function takes the Spot price (S),Strike Price of call option(X), and call premium(P) 
    as inputs and returns the profit from call option exercise"""
    callpf = np.where(S > X, S - X, 0)    
    return (callpf-P)


def stock_payoff(S,PP):
    """This function takes Spot price range(S), and purchase price(PP) of the stock as inputs
    and returns stock payoff """
    return (S-PP)

def covered_call(S, strike, premium ,PP):
    """ This funtion takes  Spot price range (S),Strike Price of call option(strike), call premium(premium)
    and stock purchase price (PP) as inputs and gives us the profit profile for covered call position"""
    st_payoff=stock_payoff(S,PP)  # calls and stores stock payoff in a variable
    call_pro=call_profit(S, strike, premium)*(-1)  # calls and stores written call profit in a variable
    covcall_profit = call_pro+st_payoff
    # Plot the covered call graph
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(S,st_payoff,'--',label='Stock Payoff',color='g')
    ax.plot(S,call_pro,'--',label='Written Call',color='r')
    ax.plot(S,covcall_profit,label='Covered Call')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit')
    plt.legend()
    plt.savefig("covered_call.png")

#setting our parameter values
spot = 45 
S = np.arange(0.8*spot,1.2*spot) 
# generating a range of spot prices to study variations in covered call profit with stock prices

PP=45
strike = 45 
premium = 2.5

#Generating the profit profile on the covered call position
covered_call(S,strike, premium,PP)



