from graph import DiGraph
import algorithms    
from bottle import route, run, response, request, static_file, template
import result
import os

@route('/')
def server_homepage():
    return static_file('index.html', root='../Client/')

@route('/buschange')
def returnsingle():
    source = request.GET.get('source')
    sink = request.GET.get('sink')
    rank = request.GET.get('rank')
	
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
    for path in items:
        sCost = path['cost']
        sPath = ", ".join(path['path'])               
        response.content_type='application/json'
        response.headers['Access-Control-Allow-Origin']='*'
        bus_Stop, bus_No, stop_Name, route_Id =  result.busChanger(source,sink,iRank)
        if i==1:
            return { "BusStop": bus_Stop, "BusNo": bus_No, "StopName": stop_Name, "RouteNo ": route_Id}
        else:
            i=i-1
            continue

@route('/pathavail')
def returnsingle():
    source = request.GET.get('source')
    sink = request.GET.get('sink')
    rank = request.GET.get('rank')
    
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
    for path in items:
        sCost = path['cost']
        sPath = ", ".join(path['path'])               
        response.content_type='application/json'
        response.headers['Access-Control-Allow-Origin']='*'
        if i==1:
            return { "Cost": sCost, "Path": sPath }
        else:
            i=i-1
            continue

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host='0.0.0.0', port = int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)