# JSON - Javascript object notation like as python dictionary. why json ? to deal with website or development phase 

# import json ---> which give some functions to convert json to python and python to json
# null -> None , true - True

import json

#json.loads() --> JSON string to python object
#json.dumps() --> Python obj to Json string ...... loads , dumps, s means string

json_str = '{ "name" : "Ankur","isTeacher" : true}'

# print(type(json_str))

py_obj = json.loads(json_str)

print(type(py_obj),py_obj)   # <class 'dict'> {'name': 'Ankur', 'isTeacher': True}
   
#Reverse dumps()

python_obj = {
    "name" : "kk",
    "isTeacher" : True
}

json_string = json.dumps(python_obj)

print(type(json_string),json_string) # <class 'str'> {"name": "kk", "isTeacher": true}


#json.load() , json.dump() for deal with json files

#json.load()  read from json file
#json.dump()  write in json file

data = {
    "name" : "Abc",
    "isTeacher" : True
}
 
print("#########")
# with open("data.json" ,"r") as f:
#     py_obj1 = json.load(f)
#     print(py_obj1 , type(py_obj1))

print("#########")
with open("data.json" ,"w") as f:
#    json.dump(data,f)
     json.dump(data,f,indent=4,sort_keys=True)


