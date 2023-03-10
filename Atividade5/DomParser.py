import urllib.request
from bs4 import BeautifulSoup

tags ="<html>\n<head>\n</head>\n\n<body bgcolor=\"black\" text=\"white\">\n<div align=\"center\"><h1>Atividade 5</h1>\n\n\n"
htmlFile = open("index.html", "w", encoding="utf-8")
file = open("seeds.txt", "r", encoding="utf-8")
imageSrc = None
for line in file.readlines():
    line = line.rstrip('\n')
    page = urllib.request.urlopen(line)

    html = str(page.read().decode('utf-8'))

    soup = BeautifulSoup(html, 'lxml')

    title = soup.title.string
    print("Título:", title)
    for img in soup.find_all('img'):
        imageSrc = img.attrs.get("src")
        print("src: ", imageSrc)
        break

    if imageSrc and "http" not in imageSrc:
        src = imageSrc.split("/")
        if len(src)==1:
            imageSrc = line+"/"+imageSrc
        elif  "Atividade1" in imageSrc or  "Atividade 1" in imageSrc or  "atividade1" in imageSrc or  "atividade 1" in imageSrc:
            if len(src)>1:
                imageSrc = line+"/"+src[1]
        else :
            imageSrc = line+imageSrc
    elif not imageSrc:
        imageSrc = ""
    
    
    tags += "\n<h2>"+title+"</h2>\n<img src = \""+imageSrc+"\"width=350>\n\n"
    imageSrc = None
tags+="</div>\n</body>\n</html>"

htmlFile.write(tags)
htmlFile.close()