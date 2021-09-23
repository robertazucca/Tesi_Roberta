import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from collections import Counter
import pandas as pd
import json
from datetime import datetime, date


def htcl_distribution(data):
    #istogrammi distribuzione htcl canali

    plt.figure(figsize=(13,6))
    plt.tick_params(axis='x', labelsize=18)
    plt.tick_params(axis='y', labelsize=18)
    plt.xlabel('htcl(msat)', fontsize=20)
    plt.ylabel('channel count',fontsize=20)

    plt.yscale('symlog')
    plt.xscale('symlog')
    plt.hist(data, bins = [0,1,10,100,1000,10000,100000,1000000,10000000,100000000], alpha = 0.3, color = 'green',  label='minhtcl')

    plt.legend(loc='upper right')
    plt.tight_layout()

def feebase_distribution(data):

    plt.figure(figsize=(13,6))
    plt.tick_params(axis='x', labelsize=18)
    plt.tick_params(axis='y', labelsize=18)
    plt.xlabel('fee_base (msat)', fontsize=20)
    plt.ylabel('channel count',fontsize=20)

    plt.yscale('symlog')
    plt.xscale('symlog')
    plt.hist(data, bins = [0,1,10,100,1000,10000,100000,1000000,10000000,100000000], alpha = 0.3, color = 'purple',  label='fee_base')

    plt.legend(loc='upper right')
    plt.tight_layout()

def feerate_distribution(data):

    plt.figure(figsize=(13,6))
    plt.tick_params(axis='x', labelsize=18)
    plt.tick_params(axis='y', labelsize=18)
    plt.xlabel('fee_rate (msat)', fontsize=20)
    plt.ylabel('channel count',fontsize=20)

    plt.yscale('symlog')
    plt.xscale('symlog')
    plt.hist(data, bins = [0,1,10,100,1000,10000,100000,1000000,10000000,100000000], alpha = 0.3, color = 'pink',  label='fee_rate')

    plt.legend(loc='upper right')
    plt.tight_layout()