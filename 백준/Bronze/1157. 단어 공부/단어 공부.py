word = input().upper()

dict = {
    
}

for c in word:
    if c not in dict:
        dict[c] = 1
    dict[c] += 1

count = 0
max_key = None

for key, value in dict.items():
    if max_key is None:
        max_key = key
        count = 1
    else:
        if dict[max_key] < value:
            max_key = key
            count = 1
        elif dict[max_key] == value:
            count += 1
        else:
            continue

if count >= 2:
    print("?")
else:
    print(max_key)
