import simplejson as json
import urllib
import requests

url = 'http://museus.cultura.gov.br/api/space/find?@select=name,endereco'

response =requests.get(url)
content = response.content.decode("utf8")
js = json.loads(content)
x=1
for k in js:
    nome = k["name"]
    end = k["endereco"]
    if(nome!=None):
        print(str(x)+" - "+nome)
    if(end!=None):
        print("End: "+end)
    x+=1