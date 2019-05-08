#DayDayup4.py
'''根据df参数计算工作日力量的函数参数不同，这段代码可共用'''
#def保留字用于定义函数
#参数df，是一个占位符
def dayup(df):
    dayup=1
    for i in range(365):
        if i % 7 in[6,0]:
            dayup=dayup * (1-0.01)
        else:
            dayup=dayup * (1+df)
    return dayup
dayfactor=0.01
#while保留字判断条件是否成立，条件成立时循环执行
while dayup(dayfactor) < 37.78:
    dayfactor +=0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))
    
