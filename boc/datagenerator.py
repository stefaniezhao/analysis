# -*- coding: utf-8 -*-
from __future__ import division
import sys,datetime
from random import randint


def generate_log():
 
    
    action_cat = ['储蓄业务','理财业务']
    action_basic = ['账户概览','资产汇总','转账汇款','公共服务缴费','信用卡']
    action_wealthMgt = ['中银理财','外汇','基金','贵金属','证券期货','国债']
    day = 20
    
    oneday = datetime.timedelta(days=15)
    #log for days
    for i in range(1,2):
        for task in action_basic:
                precent = 1
        	firstday = datetime.date(2013,1,1)
        	for i in range(day):
                    print firstday,","," ",",", action_cat[0],",", task,",", int(randint(9000,10700)*precent),",",int(randint(1000,3400)*precent),",",int(randint(800000,1000000)*precent)
                    firstday = firstday + oneday
                    if(i>4):
                        precent = precent * (1-randint(1,3)/100)
                    else:
                        precent = precent * (1+randint(1,3)/100)
        for task in action_wealthMgt:
                precent = 1
                o_precent = 1
                d_precent = 1
        	firstday = datetime.date(2013,1,1)
        	for i in range(day):
                    print firstday,","," ", ",", action_cat[1],",",task,",",int(randint(8000,9000)*precent),",",int(randint(1000,1400)*precent),",",int(randint(800000,1000000)*o_precent),",",int(randint(200,300)*d_precent)
                    firstday = firstday + oneday
                    if task == '贵金属':
                        if(i<7):
                            precent = precent * (1-randint(1,5)/100)
                            o_precent = o_precent * (1+randint(1,5)/100)
                            d_precent = d_precent * (1-randint(1,5)/100)
                        elif i>7 and i <14:
                            precent = precent * (1+randint(10,20)/100)
                            o_precent = o_precent * (1-randint(10,30)/100)
                            d_precent = d_precent * (1+randint(30,50)/100)
                        else:
                            precent = 1
                            o_precent = o_precent * (1+randint(1,5)/100)
                            d_precent = d_precent * (1-randint(1,10)/100)
                    if task == '基金':
                        if i>12:
                            precent = precent * (1+randint(5,20)/100)
                            o_precent = o_precent * (1+randint(5,20)/100)
                            d_precent = 1
                        else:
                            precent = 1
                            o_precent = 1
                            d_precent = 1
                    if task == '证券期货':
                        if i>9:
                            precent = precent * (1-randint(2,10)/100)
                            o_precent = o_precent * (1-randint(5,20)/100)
                            d_precent = d_precent * (1-randint(2,10)/100)
                        else:
                            precent = 1
                            o_precent = 1
                            d_precent = 1
    
        #print firstday
        #user_set = set()
        

def generate_seq():
    seq_num = 100
    product_begin=45001
    product_end=75001
    actions = ['首页','查询','产品介绍','购买']
    action_basic = ['账户概览','资产汇总','转账汇款','公共服务缴费','信用卡']
    action_wealthMgt = ['中银理财','外汇','基金','贵金属','证券期货','国债']

    seq_long = 7

    for i in range(seq_num):
        seq = []
        seq_len = randint(2,seq_long)
        for i in range(seq_len):
            flag = randint(1,2)
            if flag == 1:
                seq.append(action_basic[randint(0,3)])
            else:
                seq.append(actions[randint(0,3)])
        print randint(500,10000),",",action_wealthMgt[randint(0,5)]+'-'+str(randint(product_begin,product_end)),",",seq
    
    
if __name__ == '__main__':
    generate_log()
