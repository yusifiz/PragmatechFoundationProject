
# FAIL :(

import json

while True:
    order= input('Istifadeci elave etmek isteyirsinizmmi>? (Y/N) : ')
    if order=='Y':
        name=input('Ad daxil edin : ')
        surname=input('Soyad daxil edin : ')
        #user=[name,surname]
        # user=f'Istifadecinin adi : {name}, Istifadecinin Soyadi : {surname}\n'
         
        user={
            'name' :name,
            'surname':surname
        }
        data=json.dumps(user)
    
        conn=open('users.json','r')
        getDataFromJson=conn.read();

        print(getDataFromJson)
        print(type(getDataFromJson))
        convertToDict=json.loads(getDataFromJson)
        print(convertToDict)
        print(type(convertToDict))
        
        convertToList=[convertToDict]
        print(convertToList)
        print(type(convertToList))
        conn=open('users.json','w')
        a=conn.write(data)
        # print(a)
        # b=convertToList.append(a)

        conn=open('users.json','r')
        text=conn.read();
        b=convertToList.append(str(text))
        conn=open('users.json','w')
        conn.write(b)
        # print(type(text))
        # conToDict=json.loads(text)
        # print(conToDict)
        # print(type(conToDict))
        # conn=open('users.json','a')
        # conn.write(data) 
        # sd=convertToList.append(text)
        # print(sd)
        # us=convertToList.append(user)
        # print(us)
        # print(type(istifadeci))
        # print(type(user))
        # print(type(user))
        # data=json.dumps(user)
        
        
        # conn=open('users.json','w')
        # conn.write(data)  
        
        # conn=open('users.json','r')
        # getDataFromJson=conn.read();
        # getDataFromJson.append(user)
        # print(type(getDataFromJson))
        # conn=open('users.json','w')
        # conn.write(data)
        # conn=open('users.json','r')
        # getDataFromJson=conn.read();
        # convertToDict=json.loads(getDataFromJson)
        # print(type(convertToDict))
        
        # conn=open('users.json','a')
        # conn.write(data)
        # conn=open('users.json','a')
        # conn.write(data) 
        # conn=open('users.json','r')
               
        # conn=open('users.json','r')
        # getDataFromJson=conn.read();
        # conn=open('users.json','a')
        # conn.write(data) 
        
        

        
        # print(getDataFromJson)
        # for user in convertToDict:
        #     print(f'Telebe adi : {user["name"]},Telebe soyadi : {user["surname"]} \n')
        
    else:
        break

