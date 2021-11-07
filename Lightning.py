import json
import pandas as pd
import networkx as nx


class LightningNetwork:

    def __init__(self, channels_file, nodes_file):

        with open(channels_file,'r') as edges_file:
            data = json.load(edges_file)

        df_data = pd.json_normalize(data)


        edges = []
        nodes_set = set()


        #calcolare la percentuale dei canali di cui non conosco le policy di routing
        n=0
        m=0
        for i in range(len(df_data)):
            if(df_data.loc[i,'node1_policy.min_htlc'] == None and df_data.loc[i,'node2_policy.min_htlc'] == None) :
                n = n+1
            elif(df_data.loc[i,'node1_policy.min_htlc'] == None and df_data.loc[i,'node2_policy.min_htlc'] != None):
                m += 1
        print("Percentuale canali di cui non conosco la policy di nessun nodo: ", str(round(n*100/len(df_data),2)), "%")
        print("Percentuale canali di cui conosco la policy di un solo nodo: ", str(round(m*100/len(df_data),2)), "%")

        #calcolare percentuale dei canali su cui possono essere inoltrati pagamenti 
        j=0
        k=0
        for i in range(len(df_data)):
            if(df_data.loc[i,'node1_policy.disabled'] is True and df_data.loc[i,'node2_policy.disabled'] is True):
                j += 1
            elif(df_data.loc[i,'node1_policy.disabled'] == True or df_data.loc[i,'node2_policy.disabled'] == True):
                k += 1  
        print("Percentuale canali su cui entrambi i nodi non consentono il routing: ", str(round(j*100/len(df_data),2)), "%")
        print("Percentuale canali su cui un solo nodo non consente il routing: ", str(round(k*100/len(df_data),2)), "%")


        
        #self.G = nx.MultiGraph(data = True)

        #ispeziono ogni canale, se i campi delle policy hanno valore null, setto il valore del campo a -1
        #per i campi ROUTING setto a -1 anche nel caso in cui il campo disabled sia true altrimenti 1
        #for i in range(len(df_data)):
            
        #    self.G.add_edge(df_data.loc[i,'node1_pub'],df_data.loc[i,'node2_pub'], 
        #    CHANNELID = df_data.loc[i,'channel_id'], 
        #    MINHTLC1 =  -1 if df_data.loc[i,'node1_policy.min_htlc'] == None else int(df_data.loc[i,'node1_policy.min_htlc']),
        #    MINHTLC2 = -1 if df_data.loc[i,'node2_policy.min_htlc'] == None else int(df_data.loc[i,'node2_policy.min_htlc']),
        #    FEEBASE1 = -1 if df_data.loc[i,'node1_policy.fee_base_msat'] == None else int(df_data.loc[i,'node1_policy.fee_base_msat']),
        #    FEEBASE2 = -1 if df_data.loc[i,'node2_policy.fee_base_msat'] == None else int(df_data.loc[i,'node2_policy.fee_base_msat']),
        #    FEERATE1 = -1 if df_data.loc[i,'node1_policy.fee_rate_milli_msat'] == None else int(df_data.loc[i,'node1_policy.fee_rate_milli_msat']),
        #    FEERATE2 = -1 if df_data.loc[i,'node2_policy.fee_rate_milli_msat'] == None else int(df_data.loc[i,'node2_policy.fee_rate_milli_msat']),
        #    ROUTING1 = -1 if df_data.loc[i,'node1_policy.disabled'] == None else 0 if df_data.loc[i,'node1_policy.disabled'] == True else 1,
        #    ROUTING2 = -1 if df_data.loc[i,'node2_policy.disabled'] == None else 0 if df_data.loc[i,'node2_policy.disabled'] == True else 1,
        #    CAPACITY = int(df_data.loc[i,'capacity'])
        #    )


        for i in range(len(df_data)):

            edges.append((df_data.loc[i,'node1_pub'],df_data.loc[i,'node2_pub'],
            {   
                'CHANNELID' : df_data.loc[i,'channel_id'],
                'MINHTLC1' :  -1 if df_data.loc[i,'node1_policy.min_htlc'] == None else int(df_data.loc[i,'node1_policy.min_htlc']),
                'MINHTLC2' : -1 if df_data.loc[i,'node2_policy.min_htlc'] == None else int(df_data.loc[i,'node2_policy.min_htlc']),
                'FEEBASE1' : -1 if df_data.loc[i,'node1_policy.fee_base_msat'] == None else int(df_data.loc[i,'node1_policy.fee_base_msat']),
                'FEEBASE2' : -1 if df_data.loc[i,'node2_policy.fee_base_msat'] == None else int(df_data.loc[i,'node2_policy.fee_base_msat']),
                'FEERATE1' : -1 if df_data.loc[i,'node1_policy.fee_rate_milli_msat'] == None else int(df_data.loc[i,'node1_policy.fee_rate_milli_msat']),
                'FEERATE2' : -1 if df_data.loc[i,'node2_policy.fee_rate_milli_msat'] == None else int(df_data.loc[i,'node2_policy.fee_rate_milli_msat']),
                'ROUTING1' : -1 if df_data.loc[i,'node1_policy.disabled'] == None else 0 if df_data.loc[i,'node1_policy.disabled'] == True else 1,
                'ROUTING2' : -1 if df_data.loc[i,'node2_policy.disabled'] == None else 0 if df_data.loc[i,'node2_policy.disabled'] == True else 1,
                'CAPACITY' : int(df_data.loc[i,'capacity'])  
            }))

        for edge in edges:
            nodes_set.add(edge[0])
            nodes_set.add(edge[1])
        nodes = list(nodes_set)

        self.G = nx.MultiGraph(data=True)
        self.G.add_edges_from(edges)
        self.G.add_nodes_from(nodes)

      
        #for edge in self.G.edges():
        #  self.G.add_node(edge[0])
        #  self.G.add_node(edge[1])





    def crea_grafo(self,name):
        nx.write_gml(self.G,name)