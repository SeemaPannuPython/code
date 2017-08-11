
from django import __main__
import sys
from datetime import date
import time


def cal_div(dic_key):
    print ("in fundtion cal_div", dic_key)
    div_val = 0 ;
    if 'Common' == dic_key[0] :
         print ("If Common Divident", dic_key[1],sys.argv[2])
         div_val = (float(dic_key[1]) // float(sys.argv[2]))
         print("value : ",div_val)
    else :
         print ("It is Preferred divident")
         div_val = float(dic_key[2]) * float(dic_key[3])//float(sys.argv[2])

    return div_val

def cal_pe_ratio(dic_key) :
    print ("in PE Ratio")
    return (float(sys.argv[2])/float(dic_key[1]))


def record_trade(dic_key,stock_dic) :
    print ("In record trade")
    list = [dic_key]
    list1 = [sys.argv[2],time.asctime(time.localtime(time.time()))]
    list.insert(4,list1)
    stock_dic[sys.argv[1]].append(list)
    print (stock_dic)
    #return record


### start main
stock_dic = {'TEA' : ['Common',0,0,100],'POP':['Common',8,0,100],'ALE':['Common',23,0,60],'GIN':['Preffered',8,2,100],'JOE':['Common',13,0,250] }
dic_val =0 ;
for key in stock_dic :
   if key == sys.argv[1] :
        print (key)
        #calculate Divident
        dic_val = cal_div(stock_dic[key])
        #calculate PE Ratio
        pe_val =  cal_pe_ratio(stock_dic[key])
        print ("Pe_val :", pe_val)
        #record Trade
        record_trade(stock_dic[key],stock_dic)




