# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 02:25:37 2018

@author: ARKADEEP
"""
"""Protective put strategy is used to limit downside risk at the cost of Put Premium. 
   Here we combine an at-the-money long put position with the underlying stock."""

#importing the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
sns.set()
os.chdir(r"F:\Option Trading Strategies\Protective Put") #setting work directory

def put_profit(S, X, P):
    """This function takes the Spot price (S),Strike Price of put option(X), and put premium(P) 
    as inputs and returns the profit from put option exercise"""
    putpf = np.where(S < X, X-S, 0)    
    return (putpf-P)


def stock_payoff(S,PP):
    """This function takes Spot price range(S), and purchase price(PP) of the stock as inputs
    and returns stock payoff """
    return (S-PP)

def protective_put(S, strike, premium ,PP):
    """ This funtion takes  Spot price range (S),Strike Price of put option(strike), put premium(premium)
    and stock purchase price (PP) as inputs and gives us the profit profile for protective put position"""
    st_payoff=stock_payoff(S,PP)  # calls and stores stock payoff in a variable
    put_pro=put_profit(S, strike, premium)  # calls and stores put profit in a variable
    protput_profit = put_pro+st_payoff
    # Plot the short put graph
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(S,st_payoff,'--',label='Stock Payoff',color='g')
    ax.plot(S,put_pro,'--',label='Long Put',color='r')
    ax.plot(S,protput_profit,label='Protective Put')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit')
    plt.legend()
    plt.savefig("protective_put.png")

#setting our parameter values
spot = 55 
S = np.arange(0.8*spot,1.2*spot) 
# generating a range of spot prices to study variations in put profit with stock prices

PP=55
strike = 55 
premium = 4.5

#Generating the profit profile on long position on the put option
protective_put(S,strike, premium,PP)


