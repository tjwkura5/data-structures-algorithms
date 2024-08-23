def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + s + ":;"
    return res

def decode(str):
    pass 



print(encode(["Hello","World"]))