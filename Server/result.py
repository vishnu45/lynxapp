from graph import DiGraph
import algorithms
import stopRouteData

def busChanger(source, sink, rank):
	#source = "s175"
	#sink = "s555"
	#rank = "2"	
	# Load the graph
	G = DiGraph("net5")    
	# Get the painting object and set its properties.
	paint = G.painter()
	paint.set_source_sink(source, sink)    
	# Generate the graph using the painter we configured.
	G.export(False, paint)
	iRank = int(rank)
	# Get shortest paths from the graph.
	items = algorithms.ksp_yen(G, source, sink, iRank)    
	for path in items:
	    sCost = path['cost']
	    sPath = ",".join(path['path'])
	print("busStops:")
	print(sPath)
	print("------")
	busStops = sPath.split(",")
	busStopsLength = len(busStops)
	busRoute = []
	pathMap = []
	stop1 = busStops[0]
	stop2 = busStops[1]
	for s1 in range(0,len(stopRouteData.SR)-1):
		if(stopRouteData.SR[s1][0]==stop1):
			for s2 in range(0,len(stopRouteData.SR)-1):
				if(s1==s2):
					continue
				if((stopRouteData.SR[s2][1]==stopRouteData.SR[s1][1]) and (stopRouteData.SR[s2][0]==stop2)):
					pathMap.append([stop1,stopRouteData.SR[s2][1]])
					break
				else:
					continue
			break

	for i in range(0,busStopsLength-1):
		stop1 = busStops[i]
		iN = i + 1
		stop2 = busStops[iN]
		routeFound = 0
		for j in range(0,len(stopRouteData.SR)-1):
			if(stopRouteData.SR[j][0]==stop1):			
				for k in range(0,len(stopRouteData.SR)-1):
					if(j==k):
						continue
					if( (stopRouteData.SR[k][1]==stopRouteData.SR[j][1]) 
						and (stopRouteData.SR[k][0]==stop2) ):
						pathMap.append([stop2,stopRouteData.SR[k][1]])		
						k=0
						routeFound=1
						break
					else:
						continue
			else:
				continue
			if(routeFound==1):
				break
	busChange = []
	busChange.append(pathMap[0])	
	for x in range(1,len(pathMap)-1):
		if(pathMap[x][1]!=pathMap[x-1][1]):
			busChange.append([pathMap[x-1][0],pathMap[x][1]])
	#print("PathMap:")
	#print(pathMap)
	#print(busChange)	
	return busChange