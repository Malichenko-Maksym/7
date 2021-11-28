import json
stud={'name':'Max',
      'surname':"Malichenko",
      'age': 17,
      'men':True,
      'university':'UEK',
      'grades':[5,4.5,5.5]}
f=open('student.json','w')
json.dump(stud,f,indent=4)
f.close()