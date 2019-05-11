#bianliquanwenben1.py
fname=input("请输入要打开的文件名称：")
fo=open(fname,"r")
txt=fo.read(2)
while txt !="":
    #对txt进行处理,按数量读入，逐步处理
    txt=fo.read(2)
fo.close()
