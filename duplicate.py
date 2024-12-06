studentdata={
    "student1":{
        "name":"Joel",
        "grade":8
    },
    "student2":{
        "name":"Joel",
        "grade":8
    }
}
result={}
for key,value in studentdata.items():
    if value not in result.values():
        result[key]=value
print(result)