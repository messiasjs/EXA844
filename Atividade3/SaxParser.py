import xml.sax
import time

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.currentLat = ""
    self.currentLon = ""
    self.currentType =None
    self.currentName =None
    self.amenity = False

  def startElement(self, tag, attributes):    
    if tag =="node":  
      self.currentLat = attributes.get("lat") 
      self.currentLon = attributes.get("lon")  
            
    if tag =="tag":	
      if attributes.get("k")=="amenity":
        self.amenity = True
        self.currentType = attributes.get("v") 
        
      if self.amenity and attributes.get("k")=="name":
        self.currentName = attributes.get("v")

  def endElement(self, tag):    
    if tag =="node" and  self.currentType and self.currentName:
      print("Nome:", self.currentName, end="\t")
      print("Tipo: ", self.currentType, end="\t")
      print("Latitude: ", self.currentLat, end="\t")
      print("Longitude: ", self.currentLon) 
      self.currentData = ""
      self.currentLat = ""
      self.currentLon = ""
      self.currentType =None
      self.currentName =None
      self.currentId = ""
      self.amenity =False

  def characters(self, content):	
    self.currentData += content


inicio = time.time()
parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")
fim = time.time()
print("SAX time:", fim - inicio)