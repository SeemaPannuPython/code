
from django import __main__
#from readlogfile import readlogFile
#from untitled.mainfile.packagecall import packagetesting
import sys
from datetime import date
import time
import datetime

# Pass by Value
def passByValue(str):
    print (str)
    str = "hello string";
    print (str) ;
    return str ;
def passByValueDic(str):
    print (str)
    str.popitem();
    dic2 = str.copy();
    print (str) ;
    print (dic2) ;
    del (str);
    return dic2 ;
#pass by reference
def passByRef(str):
    str.append(['by','ref']);
    print(str);
#Main File starting

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
    # time, share prize, stock type
    print("today time",time.asctime(time.localtime(time.time())))
    #append in dictionary
    print (stock_dic)
    list = [dic_key]
    list1 = [sys.argv[2],time.asctime(time.localtime(time.time()))]
    list.insert(4,list1)
    stock_dic[sys.argv[1]].append(list)
    print (stock_dic)
    #return record


### start main
#trade record [date time,pervalue,]
stock_dic = {'TEA' : ['Common',0,0,100],'POP':['Common',8,0,100],'ALE':['Common',23,0,60],'GIN':['Preffered',8,2,100],'JOE':['Common',13,0,250] }
dic_val =0 ;
while (sys.argv)
    for key in stock_dic :
         #print ("key :", key, stock_dic)
         if key == sys.argv[1] :
            print (key)
            dic_val = cal_div(stock_dic[key])
            pe_val =  cal_pe_ratio(stock_dic[key])
            print ("Pe_val :", pe_val)
            record_trade(stock_dic[key],stock_dic)
            break
 






# testing the Package working
    #packagetesting.focus();

# Pass by Value string
"""stringl = "string as value"
str2 = passByValue(stringl)
print (stringl)
print (str2)

# Pass by Value number
stringl = 24
str2 = passByValue(stringl)
print (stringl)
print (str2)

#pass by Value dictionary
dicname = {'name':'Seema','age':36, 'passion' : 'adventure'}
dicname2 = passByValueDic(dicname)
print (dicname)
print (dicname2)


#pass by reference list
list1 = ['testing', 'on','list'];
passByRef(list1);
print (list1);

#Function overloading testing

func();
func()


#Main File End





def hello ():
    print ("welcome to django Project");
    fd = open('logFile', 'a+');
    fd.write("welcome to my django Project\n");
    print ("COmpleted the writing in file ");


def focus():

    pass


"""

