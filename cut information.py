import json
f=open('students.json')
g=open('limited.json','w')

p=f.read()
readed=json.loads(p)
limited=[]

for i in readed:
    limited.append( {'first_name':i['first_name'],
                     'last_name':i['last_name'],
                     'id':i['id']
                     } )
json.dump(limited,g, indent=4)

f.close()
g.close()
