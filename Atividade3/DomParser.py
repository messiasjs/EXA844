from xml.dom.minidom import parse
import time

inicio = time.time()
OSMDocument = parse('map.osm')
amenity = None
name = None
count =0
t=""
print("Starting DOM Parser...")
for node in OSMDocument.getElementsByTagName("node"):	
	for tag in  node.getElementsByTagName("tag"):
		if tag.getAttribute("k") == "amenity":
			amenity = tag.getAttribute("v")
			#t = tag.getAttribute("v")
		if tag.getAttribute("k") == "name":
			name = tag.getAttribute("v")
	if name and amenity:
		count +=1
		print("Nome:", name, end="\t")
		print("Tipo: ", amenity, end="\t")
		print("Latitude: ", node.getAttribute("lat"), end="\t")
		print("Longitude: ", node.getAttribute("lon")) 
	amenity=False
	nome = None
fim = time.time()
print("DOM time:", fim - inicio)