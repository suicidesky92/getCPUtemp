import time

def get_tmp(core):
    file = open(f'/sys/class/hwmon/hwmon1/temp{core}_input', 'r')
    data = file.read()
    file.close()
    data = int(data) / 1000
    return data


while True:
    core = []
    s = 0
    time.sleep(300)
    for i in range(2,6):
        core.append(get_tmp(i))
    for i in core:
        s = s + i
    temp = s / len(core)
    file = open('temp.log','a')
    x = time.localtime()
    tologdata = f'{temp} C--- {x.tm_year}.{x.tm_mon}.{x.tm_mday} {x.tm_hour}:{x.tm_min}'
    file.write(f'{tologdata}\n')
    file.close()
    print(tologdata)

