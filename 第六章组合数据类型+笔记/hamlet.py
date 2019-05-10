#hamlet.py
def getText():
    txt=open("hamlet").read()
    txt=txt.lower()
    for ch in '|"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt=txt.replace(ch," ")
        return txt

    hamleTxt=getText()
    words=hamleTxt.split()
    counts={}
    for word in words:
        counts[word]=counts.get(word,0)+1
        items=list(counts.item())
        items.sort(key=lambda x:x[i],reverse=True)
        print("{0:<10}{1:>5}".format(word,count))
