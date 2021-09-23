import json
import pandas as pd
import networkx as nx


class LightningNetwork:
    def __init__(self, channels_file, nodes_file):

        with open("edges.json",'r') as edges_file:
            data = json.load(edges_file)

        df_data = pd.json_normalize(data)

        nodes_set = set()

        n=0
        for i in range(len(df_data)):
            if(df_data.loc[i,'node1_policy.min_htlc']) == None and df_data.loc[i,'node2_policy.min_htlc'] == None :
                n = n+1

        print("Percentuale canali in cui non conosco la policy: ", str(round(n*100/len(df_data),2)))

        
        self.G = nx.MultiGraph(data = True)

        for i in range(len(df_data)):
            
            self.G.add_edge(df_data.loc[i,'node1_pub'],df_data.loc[i,'node2_pub'],df_data.loc[i,'channel_id'], 
            MINHTLC1 =  -1 if (df_data.loc[i,'node1_policy.min_htlc']) == None else int(df_data.loc[i,'node1_policy.min_htlc']),
            MINHTLC2 = -1 if (df_data.loc[i,'node2_policy.min_htlc']) == None else int(df_data.loc[i,'node2_policy.min_htlc']),
            FEEBASE1 = -1 if (df_data.loc[i,'node1_policy.fee_base_msat']) == None else int(df_data.loc[i,'node1_policy.fee_base_msat']),
            FEEBASE2 = -1 if (df_data.loc[i,'node2_policy.fee_base_msat']) == None else int(df_data.loc[i,'node2_policy.fee_base_msat']),
            FEERATE1 = -1 if (df_data.loc[i,'node1_policy.fee_rate_milli_msat']) == None else int(df_data.loc[i,'node1_policy.fee_rate_milli_msat']),
            FEERATE2 = -1 if (df_data.loc[i,'node2_policy.fee_rate_milli_msat']) == None else int(df_data.loc[i,'node2_policy.fee_rate_milli_msat'])
            )
        #elif mode == 'analisi_graph':
         #   for i in range(len(df_data)):
                #edges.append((df_data.loc[i,'node1_pub'],df_data.loc[i,'node2_pub'],df_data.loc[i,'channel_id'],{
         #       self.G.add_edge(df_data.loc[i,'node1_pub'],df_data.loc[i,'node2_pub'],df_data.loc[i,'channel_id']) #{
                    #'MINHTLC_1' : 0 if (df_data.loc[i,'node1_policy.min_htlc']) == None else int(df_data.loc[i,'node1_policy.min_htlc']),
                    #'MINHTLC_2' : 0 if (df_data.loc[i,'node2_policy.min_htlc']) == None else int(df_data.loc[i,'node2_policy.min_htlc']),
                    #'FEEBASE_1' : 0 if (df_data.loc[i,'node1_policy.fee_base_msat']) == None else int(df_data.loc[i,'node1_policy.fee_base_msat']),
                    #'FEEBASE_2' : 0 if (df_data.loc[i,'node2_policy.fee_base_msat']) == None else int(df_data.loc[i,'node2_policy.fee_base_msat']),
                    #'FEERATE_1' : 0 if (df_data.loc[i,'node1_policy.fee_rate_milli_msat']) == None else int(df_data.loc[i,'node1_policy.fee_rate_milli_msat']),
                    #'FEERATE_2' : 0 if (df_data.loc[i,'node2_policy.fee_rate_milli_msat']) == None else int(df_data.loc[i,'node2_policy.fee_rate_milli_msat'])
                #})


        for edge in self.G.edges():
          #self.G.add_node(edge[0])
          #self.G.add_node(edge[1])

            nodes_set.add(edge[0])
            nodes_set.add(edge[1])

        nodes = list(nodes_set)

        


        #self.G = nx.MultiGraph(data = True)
        self.G.add_nodes_from(nodes)
        #self.G.add_edgesllll_from(edges)


    def crea_grafo(self,name):
        nx.write_gml(self.G,name)