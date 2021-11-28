import json
print('Date            Buying Rate     Selling Rate')
print('============================================')
f=open('euro.json') 
p=f.read()
readed=json.loads(p)
k=readed['rates']
for i in k:
    print(i['effectiveDate'],'    ',i['bid'],'        ',i['ask'])

f.close()