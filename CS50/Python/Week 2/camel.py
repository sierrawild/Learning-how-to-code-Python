x = []
y = input("camelCase:").strip()

for i in y:
    if i.isupper():
        x.append("_"+ i.lower())
    else:
        x.append(i)
        
answer = "".join(x)

print(answer)