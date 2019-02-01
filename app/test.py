#
# import collections
#
# with open('D:/test/symbols.txt', 'r') as f:
#     txt = f.read()
#     print(list(dict(collections.Counter(txt).most_common()[:-8:-1]).keys()))
#     f.close()







with open('D:/test/symbols.txt', 'r') as f:
    txt = f.read()

d = {}
for t in txt:
    if t in list(d.keys()):
        d[t] += 1
    else:
        d[t] = 1

s = [k[0] for k in sorted(d.items(), key=lambda x: x[1])[0:8]]
print(s)
