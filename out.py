import Lightning as LN

channels_filename = 'edges.json'
nodes_filename = 'nodes.json'

#disegno grafo per visualizzazione con graphia
ln=LN.LightningNetwork(channels_filename, nodes_filename) 
ln.crea_grafo("grafonew.gml")

G = nx.Graph()

for edge in ln.edges(data=True):

    u = edge[0]
    v = edge[1]
    k = edge[2]

    if not G.has_edge(u,v):

        G.add_edge(u,v)
        htlc1 = mean(d.get('HTLC1',-1) for d in ln.get_edge_data(u,v).values())
        htlc2 = mean(d.get('HTLC2',-1) for d in ln.get_edge_data(u,v).values())
        feebase1 = mean(d.get('FEEBASE1',-1) for d in ln.get_edge_data(u,v).values())
        feebase2 = mean(d.get('FEEBASE2',-1) for d in ln.get_edge_data(u,v).values())
        feerate1 = mean(d.get('FEERATE1',-1) for d in ln.get_edge_data(u,v).values())
        #feerate2 = mean(d.get('FEERATE2',-1) for d in ln.get_edge_data(u,v).values())

        G[u][v]['ID'] = k
        G[u][v]['HTLC1'] = htlc1
        G[u][v]['HTLC2'] = htlc2
        G[u][v]['FEEBASE1'] = feebase1
        G[u][v]['FEEBASE2'] = feebase2
        G[u][v]['FEERATE1'] = feerate1
        #G[u][v]['FEERATE2'] = feerate2


