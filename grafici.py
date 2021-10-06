import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from collections import Counter
import pandas as pd
import json
from datetime import datetime, date


def htlc_distribution(data):
    #istogrammi distribuzione htlc canali

    plt.figure(figsize=(13,6))
    plt.tick_params(axis='x', labelsize=18)
    plt.tick_params(axis='y', labelsize=18)
    plt.xlabel('htlc(msat)', fontsize=20)
    plt.ylabel('channel count',fontsize=20)

    plt.yscale('symlog')
    plt.xscale('symlog')
    plt.hist(data, bins = [0,1,10,100,1000,10000,100000,1000000,10000000,100000000], alpha = 0.5, edgecolor ='black', color = 'green')

    #plt.legend(loc='upper right')
    plt.tight_layout()

def feebase_distribution(data):

    plt.figure(figsize=(13,6))
    plt.tick_params(axis='x', labelsize=18)
    plt.tick_params(axis='y', labelsize=18)
    plt.xlabel('fee_base (msat)', fontsize=20)
    plt.ylabel('channel count',fontsize=20)

    plt.yscale('symlog')
    plt.xscale('symlog')
    plt.hist(data, bins = [0,1,10,100,1000,10000,100000,1000000,10000000,100000000], alpha = 0.5, edgecolor ='black', color = 'purple')

    #plt.legend(loc='upper right')
    plt.tight_layout()

def feerate_distribution(data):

    plt.figure(figsize=(13,6))
    plt.tick_params(axis='x', labelsize=18)
    plt.tick_params(axis='y', labelsize=18)
    plt.xlabel('fee_rate (msat)', fontsize=20)
    plt.ylabel('channel count',fontsize=20)

    plt.yscale('symlog')
    plt.xscale('symlog')
    plt.hist(data, bins = [0,1,10,100,1000,10000,100000,1000000,10000000,100000000], alpha = 0.5, edgecolor ='black', color = 'orange')

    #plt.legend(loc='upper right')
    plt.tight_layout()

def double_hist_fee(data1,data2):

    plt.figure(figsize=(13,6))
    a1 = plt.subplot(2,2,1)
    a1.tick_params(axis='x', labelsize=11)
    a1.tick_params(axis='y', labelsize=11)
    plt.xlabel('fee_base (msat)', fontsize=10)
    plt.ylabel('channel count',fontsize=10)
    #plt.yscale('log')
    plt.xscale('symlog')
    a1.hist(data1, bins = [0,1,10,100,1000,10000,100000,1000000,10000000,100000000], alpha = 0.5, edgecolor ='black', color = 'green')
    plt.tight_layout()


    a2=plt.subplot(2, 2, 2)
    a2.tick_params(axis='x', labelsize=11)
    a2.tick_params(axis='y', labelsize=11)
    plt.xlabel('fee_rate (msat)', fontsize=10)
    plt.ylabel('channel count',fontsize=10)
    #plt.yscale('log')
    plt.xscale('symlog')
    a2.hist(data2, bins = [0,1,10,100,1000,10000,100000,1000000,10000000,100000000], alpha = 0.5, edgecolor ='black', color = 'green')
    plt.tight_layout()
