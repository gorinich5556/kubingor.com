from re import T
import time


b=0
bb=0
bbb=0
while True:

    try:
        b=b+1
        time.sleep(0.01)
        if b>=100:
            bb=bb+1
            b=b-100
        if bb>=60:
            bbb=bbb+1
            bb=bb-60
        sekund = f'{bbb}.{bb}.{b}'
        print(sekund)

    except RecursionError:
        b=b+1
        if b>=100:
            bb=bb+1
            b=b-100
        if bb>=60:
            bbb=bbb+1
            bb=bb-60
        time.sleep(0.01)
        sekund = f'{bbb}.{bb}.{b}'
        print(sekund)

tick() 
#print(v)
