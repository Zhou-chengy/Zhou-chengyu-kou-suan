# coding: gbk
from random import randint
print('������ӷ�1,����2,�˷�3,����4')
fang = int(input())

if fang==1:
    bingo = False
    fenshu = 0
    while bingo == False:
        num = randint(1,1000)
        wen = randint(1,1000)
        print(str(num) + '+' + str(wen))
        fenshu +=1
        wee = int(input())
        daan1 = num + wen
        w = randint(1,200)
        e = randint(1,200)
        
        if wee==daan1:
            print('�ش���ȷ,��һ��')
            fenshu = fenshu+1
            wen = wen+w
            num = num+e

        if wee!=daan1:
            print('�ش����,��һ��')
            fenshu = fenshu-1
            wen = wen-1
            num = num-e

        if fenshu==10:
            print('��������')
            bingo = True

        if fenshu==-10:
            print('���ź�,��ʧ����')
            bingo = True

                    
if fang==2:
    bingo1 = False
    fenshu1 = 0
    while bingo1 == False:
        num1 = randint(1,1000)
        wen1 = randint(1,1000)
        print(str(num1) + '-' + str(wen1))
        fenshu1 +=1
        wee1 = int(input())
        daan2 = num1 - wen1
        w1 = randint(1,200)
        e1 = randint(1,200)
        
        if wee1==daan2:
            print('�ش���ȷ,��һ��')
            fenshu1 = fenshu1+1
            wen1 = wen1+w1
            num1 = num1+e1

        if wee1!=daan2:
            print('�ش����,��һ��')
            fenshu1 = fenshu1-1
            wen1 = wen1-w1
            num1 = num1-e1

        if fenshu1==10:
            print('��������')
            bingo1 = True

        if fenshu1==-10:
            print('���ź�,��ʧ����')
            bingo1 = True

if fang==3:
    bingo2 = False
    fenshu2 = 0
    while bingo2 == False:
        num2 = randint(1,1000)
        wen2 = randint(1,1000)
        print(str(num2) + '*' + str(wen2))
        fenshu2 +=1
        wee2 = int(input())
        daan3 = num2 * wen2
        w2 = randint(1,200)
        e2 = randint(1,200)
        
        if wee2==daan3:
            print('�ش���ȷ,��һ��')
            fenshu2 = fenshu2+1
            wen2 = wen2+w2
            num2 = num2+e2

        if wee2!=daan3:
            print('�ش����,��һ��')
            fenshu2 = fenshu2-1
            wen2 = wen2-w2
            num2 = num2-e2

        if fenshu2==10:
            print('��������')
            bingo2 = True

        if fenshu2==-10:
            print('���ź�,��ʧ����')
            bingo2 = True

if fang==4:
    bingo3 = False
    fenshu3 = 0
    while bingo3 == False:
        num3 = randint(1,1000)
        wen3 = randint(1,100)
        print(str(num3) + '/' + str(wen3))
        fenshu3 +=1
        wee3 = int(input())
        daan4 = num3 / wen3
        w3 = randint(1,200)
        e3 = randint(1,200)
        
        if wee3==daan4:
            print('�ش���ȷ,��һ��')
            fenshu3 = fenshu3+1
            wen3 = wen3+w3
            num3 = num3+e3

        if wee2!=daan4:
            print('�ش����,��һ��')
            fenshu = fenshu-1
            wen3 = wen3-w3
            num3 = num3-e3

        if fenshu3==10:
            print('��������')
            bingo3 = True

        if fenshu3==-10:
            print('���ź�,��ʧ����')
            bingo3 = True

                    
                      
                   
                   
               
            
               
               
           

           
