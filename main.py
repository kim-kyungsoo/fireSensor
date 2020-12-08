from matplotlib import pyplot as plt
from re import *


f=open('D:/sensor/repeater12051809.log')
num=0;
fireType=[];fireTemp=[]; fireHumi=[]; fireSmoke=[]; fireMit=[]
gasType=[];gasTemp=[]; gasHumi=[]; gasSmell=[]; gasCo2=[]
while True:
    line = f.readline()
    if not line: break
    #print(line)
    m=search('RF2 >>  2[24]', line)
    #data=str[5:]
    num=num+1

    if m:
        print(m.string[:20], ']:', end=' ')
        print(m.string[m.end()+5:-1])
        begin=m.end()+5

        if m.string[begin:begin+4] =='0408':
            fireType.append(int(m.string[begin + 4:begin + 6], 16))
            fireTemp.append(int(m.string[begin+6:begin+8], 16))
            #print(m.string[begin+6:begin+8])
            fireHumi.append(int(m.string[begin+8:begin+10],16))
            #print(m.string[begin+8:begin+10])
            little=m.string[begin+12:begin+14]+m.string[begin+10:begin+12]
            fireSmoke.append(int(m.string[begin+10:begin+14],16))
            #fireSmoke.append(int(little,16))
             #print(m.string[begin+10:begin+14])
            fireMit.append(int(m.string[begin+14:begin+16],16))
            #print(m.string[begin+14:begin+16])
        elif m.string[begin:begin+4]=='0509':
            gasType.append(int(m.string[begin + 4:begin + 6], 16))
            gasTemp.append(int(m.string[begin+6:begin+8],16))
            gasHumi.append(int(m.string[begin+8:begin+10],16))
            little = m.string[begin + 12:begin + 14] + m.string[begin + 10:begin + 12]
            gasCo2.append(int(m.string[begin+10:begin+14],16))
            #gasSmell.append(int(m.string[begin+8:begin+12],16))
            #gasCo2.append(int(little,16))
            little = m.string[begin + 16:begin + 18] + m.string[begin + 14:begin + 16]
            gasSmell.append(int(m.string[begin+14:begin+18],16))
            #gasSmell.append(int(little, 16))
f.close()
print('화재타입:', fireType)
print('화재온도:', fireTemp)
print('화재습도:', fireHumi)
print('화재연기:', fireSmoke)
print('화재MIT:', fireMit)

print('가스타입:', gasType)
print('가스온도:', gasTemp)
print('가스습도:', gasHumi)
print('가스Co2:', gasCo2)
print('가스연기:', gasSmell)


plt.title("Fire Senseor")
plt.xlabel("Time(sec)")
plt.ylabel("C(%)")
plt.plot(fireType)
plt.plot(fireTemp)
plt.plot(fireHumi)

plt.legend(['Fire Type', 'Humi(%)', 'Temp(C)'])
plt.show()
plt.title("Fire Senseor")
plt.xlabel("Time(sec)")
plt.ylabel("%")
plt.plot(fireSmoke)
plt.legend(['Smoke'])
plt.show()

plt.title("Gas Senseor")
plt.xlabel("Time(sec)")
plt.ylabel("C(%)")
plt.plot(gasType)
plt.plot(gasHumi)
plt.plot(gasTemp)
plt.legend(['Gas Type','Humi(%)', 'Temp(C)'])
plt.show()

plt.title("Gas Senseor")
plt.xlabel("Time(sec)")
plt.ylabel("%")
plt.plot(gasCo2)
plt.plot(gasSmell)
plt.legend(['Co2', 'Smell)'])
plt.show()