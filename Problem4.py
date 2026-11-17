import json 

with open ("students.json", "r", encoding= "utf-8") as f:
    data = json.load(f)

best = max(data, key=lambda x: x["grade"])

worst = min(data, key=lambda x: x["grade"])

total = 0
for i in data:
    total += i["grade"]
    
average = round(total / len(data), 1)

print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average}")
    

