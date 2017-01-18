from graph import DiGraph
import algorithms

source = "s175"
sink = "s555"
rank = "13"

# Load the graph
G = DiGraph("net5")    
# Get the painting object and set its properties.
paint = G.painter()
paint.set_source_sink(source, sink)    
# Generate the graph using the painter we configured.
G.export(False, paint)
i=int(rank)
iRank = i
# Get shortest paths from the graph.
items = algorithms.ksp_yen(G, source, sink, i)
print(items)
#for path in items:
#   sCost = path['cost']
#    sPath = ", ".join(path['path'])               
#    response.content_type='application/json'
#    if i==1:
#        return { "Cost": sCost, "Path": sPath, "BusChange": result.busChanger(source,sink,iRank) }
#    else:
#        i=i-1
#        continue