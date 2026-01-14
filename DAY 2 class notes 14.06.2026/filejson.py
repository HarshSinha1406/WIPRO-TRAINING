import json
data={
    "name":"harsh",
    "age":23,
    "location":"patna , Bihar",
    "skills":["python","java"],
}
with open("data.json","w") as file:
    json.dump(data,file,indent=5)