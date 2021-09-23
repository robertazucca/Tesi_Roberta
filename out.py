import Lightning as LN

channels_filename = 'edges.json'
nodes_filename = 'nodes.json'

#grafo.gml per analisi
#ln=LN.LightningNetwork(channels_filename, nodes_filename,mode='analisi_graph')
#ln.crea_grafo("grafo.gml")

#graphia.gml per visualizzazione con graphia
ln1=LN.LightningNetwork(channels_filename, nodes_filename) 
ln1.crea_grafo("grafodef.gml")

