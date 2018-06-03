#importing the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
sns.set()
os.chdir(r"F:\Option Trading Strategies\Put Options") #setting work directory

def put_profit(S, X, P):
    """This function takes the Spot price (S),Strike Price of put option(X), and put premium(P) 
    as inputs and returns the profit from put option exercise"""
    putpf = np.where(S < X, X-S, 0)    
    return (putpf-P)


def long_put(S, strike, premium):
    """ This funtion takes  Spot price range (S),Strike Price of put option(strike), and put premium 
    as inputs and gives us the profit profile for long position"""
    longput_profit = put_profit(S, strike, premium)
    # Plot the long put graph
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(S,longput_profit,label='Long Put profit')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit')
    plt.legend()
    plt.savefig("longput_profit.png")

def short_put(S, strike, premium):
    """ This funtion takes  Spot price range (S),Strike Price of put option(strike), and put premium 
    as inputs and gives us the profit profile for short position"""
    shortput_profit = put_profit(S, strike, premium)*(-1.0)
    # Plot the short put graph
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(S,shortput_profit,label='Short Put profit')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit')
    plt.legend()
    plt.savefig("shortput_profit.png")

#setting our parameter values
spot = 55 
S = np.arange(0.8*spot,1.2*spot) 
# generating a range of spot prices to study variations in put profit with stock prices

strike = 55 
premium = 4.5

#Generating the profit profile on long position on the put option
long_put(S,strike, premium)

#Generating the profit profile on short position on the put option
short_put(S,strike, premium)

