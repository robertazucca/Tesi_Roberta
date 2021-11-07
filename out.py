import Lightning as LN
from datetime import datetime, date


channels_filename = 'edges.json'
nodes_filename = 'nodes.json'

#disegno grafo (relativo al primo dataset fornito_ 1-05-2021)
#ln=LN.LightningNetwork(channels_filename, nodes_filename) 
#ln.crea_grafo("output\grafi\multigrafo.gml")


#date in cui ho raccolto i dati
#dates = ["03-05-21", "10-05-21", "17-05-21", "24-05-21", "31-05-21", "07-06-21", "14-06-21", "21-06-21", "28-06-21", "05-07-21", "12-07-21", "19-07-21", "26-07-21", "02-08-21", "09-08-21", "16-08-21", "23-08-21", "30-08-21"]
dates = ["23-04-21", "24-04-21", "25-04-21", "26-04-21", "27-04-21", "28-04-21", "29-04-21", "30-04-21", "01-05-21", "02-05-21", "03-05-21", "04-05-21", "05-05-21", "06-05-21", "07-05-21",
"08-05-21", "09-05-21", "10-05-21"]

#costruisco i grafi
for data in dates:
    #ln = LN.LightningNetwork('datasetLun\ln_' + str(data)+ '.json__edges.json','datasetLun\ln_' + str(data)+ '.json__nodes.json')        
    ln = LN.LightningNetwork('datasetAprileMaggio\ln_' + str(data)+ '.json__edges.json','datasetLun\ln_' + str(data)+ '.json__nodes.json')        

    #ln.crea_grafo("output\grafi_all\multigrafo_" + str(data) +  ".gml")            
    ln.crea_grafo("output\grafi_AprileMaggio\multigrafo_" + str(data) +  ".gml")            

