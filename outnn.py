import Lightningnn as LN
from datetime import datetime, date


channels_filename = 'edges.json'
nodes_filename = 'nodes.json'

#disegno grafo (relativo al primo dataset fornito_ 1-05-2021)
#ln=LN.LightningNetwork(channels_filename, nodes_filename) 
#ln.crea_grafo("output\grafi\multigrafo.gml")


#date in cui ho raccolto i dati
dates = ["03-05-21", "10-05-21", "17-05-21", "24-05-21", "31-05-21", "07-06-21", "14-06-21", "21-06-21", "28-06-21", "05-07-21", "12-07-21", "19-07-21", "26-07-21", "02-08-21", "09-08-21", "16-08-21", "23-08-21", "30-08-21"]

#costruisco i grafi
for data in dates:
    ln = LN.LightningNetworkNotNull('datasetLun\ln_' + str(data)+ '.json__edges.json','datasetLun\ln_' + str(data)+ '.json__nodes.json')        #per analisi
    #ln = LN.LightningNetwork(channels_filename, nodes_filename, day, month=10, mode='graph_file_graphia', attributes=None)   #per graphia

    ln.crea_grafo("output\grafi_notnull\multigrafo_" + str(data) +  ".gml")            #per analisi
    #ln.create_graph_gml("/home/emanuela/Documenti/Tirocinio/snapshots_cnr/graphs/graph_graphia_"+ dates[day] + ".gml")       per graphia

