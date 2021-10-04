import Lightning as LN

channels_filename = 'edges.json'
nodes_filename = 'nodes.json'

#disegno grafo 
ln=LN.LightningNetwork(channels_filename, nodes_filename) 
ln.crea_grafo("output\grafi\multigrafo.gml")


