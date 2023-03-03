from xml.dom.minidom import parse
import time

inicio = time.time()
OSMDocument = parse('map.osm')
amenity = False
count =0
t=""
print("Starting DOM Parser...")
for node in OSMDocument.getElementsByTagName("node"):	
	for tag in  node.getElementsByTagName("tag"):
		if tag.getAttribute("k") == "amenity":
			amenity =True
			t = tag.getAttribute("v")
		if tag.getAttribute("k") == "name" and amenity:
			count +=1
			print("Nome:", tag.getAttribute("v"), end="\t")
			print("Tipo: ", t, end="\t")
			print("Latitude: ", node.getAttribute("lat"), end="\t")
			print("Longitude: ", node.getAttribute("lon")) 
	amenity=False
fim = time.time()
print("DOM time:", fim - inicio)