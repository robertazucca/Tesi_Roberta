import json
import pandas as pd
import networkx as nx


class LightningNetwork:
    def __init__(self, channels_file, nodes_file):

        with open("edges.json",'r') as edges_file:
            data = json.load(edges_file)

        df_data = pd.json_normalize(data)

        #per calcolare la percentuale dei canali in cui non conosco le policy di inoltro
        n=0
        for i in range(len(df_data)):
            if(df_data.loc[i,'node1_policy.min_htlc']) == None and df_data.loc[i,'node2_policy.min_htlc'] == None :
                n = n+1
        print("Percentuale canali in cui non conosco la policy: ", str(round(n*100/len(df_data),2)))

        
        self.G = nx.MultiGraph(data = True)

        #ispeziono ogni canale, se i campi delle policy hanno valore null, setto il valore del campo a -1
        for i in range(len(df_data)):
            
            self.G.add_edge(df_data.loc[i,'node1_pub'],df_data.loc[i,'node2_pub'], df_data.loc[i,'channel_id'], 
            MINHTLC1 =  -1 if (df_data.loc[i,'node1_policy.min_htlc']) == None else int(df_data.loc[i,'node1_policy.min_htlc']),
            MINHTLC2 = -1 if (df_data.loc[i,'node2_policy.min_htlc']) == None else int(df_data.loc[i,'node2_policy.min_htlc']),
            FEEBASE1 = -1 if (df_data.loc[i,'node1_policy.fee_base_msat']) == None else int(df_data.loc[i,'node1_policy.fee_base_msat']),
            FEEBASE2 = -1 if (df_data.loc[i,'node2_policy.fee_base_msat']) == None else int(df_data.loc[i,'node2_policy.fee_base_msat']),
            FEERATE1 = -1 if (df_data.loc[i,'node1_policy.fee_rate_milli_msat']) == None else int(df_data.loc[i,'node1_policy.fee_rate_milli_msat']),
            FEERATE2 = -1 if (df_data.loc[i,'node2_policy.fee_rate_milli_msat']) == None else int(df_data.loc[i,'node2_policy.fee_rate_milli_msat']),
            ROUTING1 = -1 if(df_data.loc[i,'node1_policy.disabled'] == None or df_data.loc[i,'node1_policy.disabled'] == false ) else 1,
            ROUTING2 = -1 if(df_data.loc[i,'node2_policy.disabled'] == None or df_data.loc[i,'node2_policy.disabled'] == false ) else 1,
            CAPACITY = int(df_data.loc[i,'capacity'])
            )


        for edge in self.G.edges():
          self.G.add_node(edge[0])
          self.G.add_node(edge[1])


    def crea_grafo(self,name):
        nx.write_gml(self.G,name)