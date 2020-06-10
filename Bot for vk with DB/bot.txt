# -'- coding: utf-8 -'-
import vk_api
import datetime
import vk
from vk_api import VkUpload 
import numpy as np
import numpy
#from random import randint
import wikipedia
import schedule
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import sqlite3
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token=')))))')




def uvedomlenia():
    con=sqlite3.connect('./sql/podpisota.db')
    cur=con.cursor()
    ki=event.user_id
    user=event.user_id
    vk.messages.send(
        user_id=user,
        random_id=get_random_id(),
        message='Отлично ! Раз вы здесь, то вы решили подключить уведомления о зарядке !\nДавайте Теперь решим с временем. Зарядки идут каждый понедельник и четверг с 8:00-8:25\nСейчас мы попробуем включить уведомление о зарядке !\n1 - чтобы получать обновления за день до начала зарядки\n2 - чтобы получать уведомления за час до зарядки\n3 - чтобы получать уведомления за 30 минут до начала до зарядке\n4 - чтобы получать уведомления за 10 минут до начала зарядки')
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text=="1":
            if event.from_user:
                vk.messages.send(
                    user_id=user,
                    random_id=get_random_id(),
                    message='Отлично, сейчас мы включим уведомление о зарядке в за 24 часа до ее начала\n')
                ti=['-8:30']
                sql_update_query = """Update core_fes set tim1 = ? where id = ?"""
                data = (ti, ki)
                cur.execute(sql_update_query, data)
                ti=['-8:30']
                sql_update_query = """Update core_fes set tim2 = ? where id = ?"""
                data = (ti, ki)
                cur.execute(sql_update_query, data)

        elif event.text=="2":
            if event.from_user:
                vk.messages.send(
                    user_id=user,
                    random_id=get_random_id(),
                    message='Отлично, сейчас мы включим уведомление о зарядке в за 1 час до ее начала\n')
                ti=['7:00']
                sql_update_query = """Update core_fes set tim1 = ? where id = ?"""
                data = (ti, ki)
                cur.execute(sql_update_query, data)
                ti=['7:00']
                sql_update_query = """Update core_fes set tim2 = ? where id = ?"""
                data = (ti, ki)
                cur.execute(sql_update_query, data)

        elif event.text=="3":
            if event.from_user:
                vk.messages.send(
                    user_id=user,
                    random_id=get_random_id(),
                    message='Отлично, сейчас мы включим уведомление о зарядке в за 30 мин до ее начала\n')
                #ti=['7:30']

            ki=event.user_id
            sql_update_query = """Update core_fes set tim1 = ? where id = ?"""
            data = ('7:30', ki)
            print (data)
            cur.execute(sql_update_query, data)
            sql_update_query = """Update core_fes set tim2 = ? where id = ?"""
            data = ('7:30', ki)
            print (data)
            cur.execute(sql_update_query, data)
            cur.close()


        elif event.text=="4":
            if event.from_user:
                vk.messages.send(
                    user_id=user,
                    random_id=get_random_id(),
                    message='Отлично, сейчас мы включим уведомление о зарядке в за 10 мин до ее начала\n')
                ti=['7:50']
                sql_update_query = """Update core_fes set tim1 = ? where id = ?"""
                data = (ti, ki)
                cur.execute(sql_update_query, data)
                ti=['7:50']
                sql_update_query = """Update core_fes set tim2 = ? where id = ?"""
                data = (ti, ki)
                cur.execute(sql_update_query, data)
    
    con.commit()
    con.close()








def sqlite3_example(user):
    print (1)
    con=sqlite3.connect('./sql/podpisota.db')
    cur=con.cursor()


    print (user)
    user_id=[]
    user_id.append(user)
    print (user_id)
    sql = """INSERT INTO core_fes (id) VALUES (?);"""
    cur.execute(sql,user_id)
    con.commit()
    cur.close()
    con.close()


def sqlite3_read(data_base,table,column_name):
    con=sqlite3.connect(data_base)  
    cur=con.cursor()
    query_columns='pragma table_info('+table+')'
    cur.execute(query_columns) 
    columns_description=cur.fetchall()
    columns_names=[]
    for column in columns_description:
        columns_names.append(column[1])
    print (columns_names)

    if column_name is None:
        query='SELECT * FROM '+table
        cur.execute(query)
        data=cur.fetchall()
    else:
        query='SELECT '+column_name+' FROM '+table 
        cur.execute(query)
        data=cur.fetchall()
        new_data=[]
        for element in data:
            new_data.append(element[0])
        data=new_data
        del(new_data)

    #print ("data")
    #print (data)
    #print_data(columns_names, data)
    cur.close()
    con.close()
    return (data)






def sqlite3_delete(user,data_base):
    con=sqlite3.connect(data_base)
    cur=con.cursor()
    sql_update_query = """DELETE from core_fes where id = ?"""
    bi=user
    cur.execute(sql_update_query, (bi, ))
    cur.close()
    con.close()


def sqlite3_del(data_base,table):
    con=sqlite3.connect(data_base)
    cur=con.cursor()
    query="DROP TABLE IF EXISTS "+table
    cur.execute(query)

    cur.close()
    con.close()





data_base='./sql/podpisota.db'
table='core_fes'


vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

#longpoll = VkBotLongPoll(vk_session, "195023553")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW: # последняя строчка
        if event.text == 'Начать':
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Еще раз, добро пожаловать в наш сервис !\n1 - отписаться\подписаться на рассылку\n2 - Информация о нашем сервисе\n3 - Управлять уведомлениями о зарядке')
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text!='':
            	if event.text=="3" or event.text==3:
            		uvedomlenia() 

