# -*- coding: utf8 -*-
import random
from vk_api import VkUpload
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import requests
import sqlite3 as sql

session = requests.Session()

vk = vk_api.VkApi(token='30c34278ed19e41caf63623a32bea086a253d77d45a5e9508485ad4ae41e5ef4482f876fcbd0e2bd035d1')

attachments = []
photo_inf = []
kubik_ph = []
ruletka_ph = []
user_names = []



upload = VkUpload(vk)
image_url = 'https://images-na.ssl-images-amazon.com/images/I/61%2Bh1sZqpTL._SY355_.png'
image_url2 = 'https://cs.pikabu.ru/post_img/2013/06/25/6/1372148148_386219844.jpg'
image_url3 = 'https://pp.userapi.com/c831109/v831109497/115051/gdWtlHMsRDg.jpg'
image_url4 = 'https://pp.userapi.com/c852024/v852024334/153925/odjDzEvVB58.jpg'
image_url5 = 'https://pp.userapi.com/c852024/v852024879/157244/QP5Xi1msKe4.jpg'
image_url6 = 'https://pp.userapi.com/c852024/v852024879/15724c/hCRHTZuN-_U.jpg'
image_url7 = 'https://pp.userapi.com/c849136/v849136837/1ccc2f/rSyD5tX0hOI.jpg'
image_url8 = 'https://pp.userapi.com/c855724/v855724837/7b75b/DLFQWeEdouQ.jpg'
image_url9 = 'https://pp.userapi.com/c854528/v854528837/7e647/Me2D5mMJ_EQ.jpg'
image_url10 = 'https://pp.userapi.com/c854028/v854028837/7bc8d/PGggQNf8onY.jpg'
image_url11 = 'https://pp.userapi.com/c855436/v855436837/7e562/tbwXm7Sa_uc.jpg'
image_url12 = 'https://pp.userapi.com/c849124/v849124837/1c98f6/QAYJiAulJXg.jpg'
image_url13 = 'https://pp.userapi.com/c849236/v849236727/1c055f/i2rCmzg1CC8.jpg'
image_url14 = 'https://pp.userapi.com/c849236/v849236727/1c0568/6ItEnXVH4b8.jpg'
image_url15 = 'https://pp.userapi.com/c849236/v849236727/1c0571/lY0qoormnSQ.jpg'
image = session.get(image_url, stream=True)
image2 = session.get(image_url2, stream=True)
image3 = session.get(image_url3, stream=True)
image4 = session.get(image_url4, stream=True)
image5 = session.get(image_url5, stream=True)
image6 = session.get(image_url6, stream=True)
image7 = session.get(image_url7, stream=True)
image8 = session.get(image_url8, stream=True)
image9 = session.get(image_url9, stream=True)
image10 = session.get(image_url10, stream=True)
image11 = session.get(image_url11, stream=True)
image12 = session.get(image_url12, stream=True)
image13 = session.get(image_url13, stream=True)
image14 = session.get(image_url14, stream=True)
image15 = session.get(image_url15, stream=True)
photo = upload.photo_messages(photos=image.raw)[0]
photo2 = upload.photo_messages(photos=image2.raw)[0]
photo3 = upload.photo_messages(photos=image3.raw)[0]
photo4 = upload.photo_messages(photos=image4.raw)[0]
photo5 = upload.photo_messages(photos=image5.raw)[0]
photo6 = upload.photo_messages(photos=image6.raw)[0]
photo7 = upload.photo_messages(photos=image7.raw)[0]
photo8 = upload.photo_messages(photos=image8.raw)[0]
photo9 = upload.photo_messages(photos=image9.raw)[0]
photo10 = upload.photo_messages(photos=image10.raw)[0]
photo11 = upload.photo_messages(photos=image11.raw)[0]
photo12 = upload.photo_messages(photos=image12.raw)[0]
photo13 = upload.photo_messages(photos=image13.raw)[0]
photo14 = upload.photo_messages(photos=image14.raw)[0]
photo15 = upload.photo_messages(photos=image15.raw)[0]
attachments.append(
    'photo{}_{}'.format(photo['owner_id'], photo['id'])
)
attachments.append(
    'photo{}_{}'.format(photo2['owner_id'], photo2['id'])
)
attachments.append(
    'photo{}_{}'.format(photo3['owner_id'], photo3['id'])
)
photo_inf.append(
    'photo{}_{}'.format(photo4['owner_id'], photo4['id'])
)
photo_inf.append(
    'photo{}_{}'.format(photo5['owner_id'], photo5['id'])
)
photo_inf.append(
    'photo{}_{}'.format(photo6['owner_id'], photo6['id'])
)
kubik_ph.append(
    'photo{}_{}'.format(photo7['owner_id'], photo7['id'])
)
kubik_ph.append(
    'photo{}_{}'.format(photo8['owner_id'], photo8['id'])
)
kubik_ph.append(
    'photo{}_{}'.format(photo9['owner_id'], photo9['id'])
)
kubik_ph.append(
    'photo{}_{}'.format(photo10['owner_id'], photo10['id'])
)
kubik_ph.append(
    'photo{}_{}'.format(photo11['owner_id'], photo11['id'])
)
kubik_ph.append(
    'photo{}_{}'.format(photo12['owner_id'], photo12['id'])
)
ruletka_ph.append(
    'photo{}_{}'.format(photo13['owner_id'], photo13['id'])
)
ruletka_ph.append(
    'photo{}_{}'.format(photo14['owner_id'], photo14['id'])
)
ruletka_ph.append(
    'photo{}_{}'.format(photo15['owner_id'], photo15['id'])
)



demki = ['audio186841206_456240001', 'audio186841206_456240005', 'audio186841206_456240003', 'audio186841206_456240002',
         'audio186841206_456240000']

songs = ['audio186841206_456239904', 'audio186841206_456240004', 'audio186841206_456239981', 'audio186841206_456239980',
         'audio186841206_456239966', 'audio186841206_456239947', 'audio186841206_456239924', 'audio186841206_456240006',
         'audio186841206_456239995', 'audio186841206_456239927', 'audio186841206_456239895', 'audio186841206_456239849',
         'audio186841206_456239818']

print('Server started')

longpoll = VkBotLongPoll(vk, 183732788)

vk2 = vk.get_api()
zk = False
dl = False

def top_bl():
    top = []
    top2 = []
    top_igr1 = 0
    top_igr2 = 0
    top_igr3 = 0

    connection = sql.connect('user.sqlite', check_same_thread=False)
    q = connection.cursor()
    q.execute("SELECT * FROM user_inform1")
    result = q.fetchall()
    for rs in result:
        top.append((rs[3]))
    for i in top:
        if i >= top_igr1:
            top_igr1 = i
    top2.append(top_igr1)
    for i in top:
        if i >= top_igr2 and i not in top2:
            top_igr2 = i
    top2.append(top_igr2)
    for i in top:
        if i >= top_igr3 and i not in top2:
            top_igr3 = i
    top2.append(top_igr3)
    q.execute("SELECT * FROM user_inform1 WHERE Balance = %s" % (top2[0]))
    result = q.fetchall()
    id1 = result[0][0]
    name1 = result[0][1]
    q.execute("SELECT * FROM user_inform1 WHERE Balance = %s" % (top2[1]))
    result = q.fetchall()
    id2 = result[0][0]
    name2 = result[0][1]
    q.execute("SELECT * FROM user_inform1 WHERE Balance = %s" % (top2[2]))
    result = q.fetchall()
    id3 = result[0][0]
    name3 = result[0][1]
    top3 = 'ТОП ИГРОКОВ:\n\n1 Место:\nID:' + str(id1) + '\nНик: ' + name1 + '\nБаланс:' + str(top2[0]) + '$' + '\n\n2 Место:\nID:' + str(id2) + '\nНик: ' + name2 + '\nБаланс:' + str(top2[1]) + '$' + '\n\n3 Место:\nID:' + str(id3) + '\nНик: ' + name3 + '\nБаланс:' + str(top2[2])  + '$'
    print(top3)
    return top3

def zvanie_2(peer_id, from_id):
    connection = sql.connect('user.sqlite', check_same_thread=False)
    q = connection.cursor()
    q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (from_id))
    result = q.fetchall()
    if len(result) == 0:
        vk2.messages.send(
            random_id=0,
            peer_id=peer_id,
            message='Сначала создайте аккаунт!'
        )
    else:
        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (from_id))
        result = q.fetchall()
        balance = result[0][3]
        zvanie = result[0][5]
        koin = result[0][6]
        zv1 = 'Бомж'
        zv2 = 'Бизнесмен'
        zv3 = 'Миллионер'
        zv4 = 'Миллиардер'
        zv5 = 'Путин'
        if zvanie != 10 and zvanie != 6 and zvanie != 5:
            if balance < 100000:
                if zvanie == 0:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        0,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv1
                    )
            if 100000 <= balance < 1000000:
                if zvanie == 1:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        1,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv2
                    )
            if 1000000 <= balance < 1000000000:
                if zvanie == 2:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        2,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv3
                    )
            if 1000000000 <= balance < 1000000000000:
                if zvanie == 3:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        3,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv4
                    )
            if balance >= 1000000000000:
                if zvanie == 4:
                    pass
                else:
                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                        4,
                        from_id))
                    connection.commit()
                    connection.close()
                    vk2.messages.send(
                        random_id=0,
                        peer_id=peer_id,
                        message='Звание обновлено до ' + zv5
                    )



try:
    for event in longpoll.listen():
        try:
            if event.type == VkBotEventType.MESSAGE_NEW:
                if True:
                    if 'прив' in event.object.text.lower() or event.object.text.lower() == 'здарова' or 'салам' in event.object.text.lower() or event.object.text.lower() == 'начать':
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='Салам')
                        time.sleep(1)
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='''Напиши "Функции", чтобы я скинул список моих функций''')
                    elif event.object.text.lower() == 'функции':
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='''Cписок функций ниже:\n\n'"песня" - скинуть случайную песню\n\n"демка" - скинуть случайную демку🤤\n\n"создать аккаунт [придуманный ник]" - создать игровой аккаунт\n\n"игры" - посмотреть игрововые функции\n\n"баг [описание проблемы]" - сообщить о проблеме\n\n\n\n\n\ncreated by @dmseul'''
                        )
                    elif 'баг' in event.object.text.lower():
                        bag = event.object.text.lower().split("баг")[-1]
                        vk2.messages.send(
                            random_id=0,
                            peer_id=186841206,
                            message='Найдена проблема!\n' + '"' + bag + '"\n' + '\nОт: ' + str(event.object.from_id)
                        )
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='Создателю сообщено о баге, спасибо за внимательность.'
                        )
                    elif event.object.text.lower() == 'игры':
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            connection = sql.connect("user.sqlite", check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                            result = q.fetchall()
                            print(result)
                            user_name = result[0][1]
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message=user_name + """, мои игровые функции:\n\n"Профиль"\n\n"Звания" - посмотреть информацию о существующих званиях\n\n"Получить админку" - получить звание "Помощник Админа"\n\n"Купить коины [сумма коинов]" - купить GachCoin(стоимость одного - триллион долларов)
\n\n"Топ игроков" - посмотреть топ игроков\n\n"Баланс" - зачисление на баланс 10$, если у вас меньше 10$\n\n"Кубик [грань(от 1 до 6)]"\n\n"Казино [ставка]"\n\n"Рулетка [цвет] [ставка]"\n\n"Информация [название игры]" - информация о игре\n\n"Перевести сто [ник]" - перевести игроку с написанным ником 100$
\n\n"Перевести тысячу [ник]" - перевести игроку с написанным ником 1000$\n\n"Перевести сто тысяч [ник]" - перевести игроку с написанным ником 100000$\n\n"Перевести миллион [ник]" - перевести игроку с написанным ником 1000000$
\n\n"Перевести миллиард [ник]" - перевести игроку с написанным ником 1000000000$\n\n"Собственность [id]" - купить собственность с написанным ID:\n
1 - Дом(1000000$)
2 - Машина(100000$)
3 - Бар(1000000000$)"""
                        )
                    elif event.object.text.lower() == 'получить админку':
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        balance = result[0][3]
                        name = result[0][1]
                        koin = result[0][6]
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if koin >= 1000000:
                                if zvanie != 10 and zvanie != 6:
                                    connection = sql.connect("user.sqlite", check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                                        6,
                                        event.object.from_id))
                                    connection.commit()
                                    connection.close()
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Звание обновлено до Помщника Админа.\nНапишите "админка функции", чтобы посмотреть функции Помощника Админа '
                                    )
                                else:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Ваше звание повысить невозможно.'
                                    )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Нужно иметь минимум миллион GachCoin на счету!'
                                )
                    elif 'купить коины' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        balance = result[0][3]
                        name = result[0][1]
                        koin = result[0][6]
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            try:
                                kn = int(event.object.text.lower().split("купить коины")[-1])
                                kn2 = kn * 1000000000000
                                if balance >= kn2:
                                    connection = sql.connect("user.sqlite", check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                        balance - kn2,
                                        event.object.from_id))
                                    connection.commit()
                                    connection.close()
                                    connection = sql.connect("user.sqlite", check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("UPDATE user_inform1 SET GachCoin = '%s' WHERE User_ID = '%s'" % (
                                        koin + kn,
                                        event.object.from_id))
                                    connection.commit()
                                    connection.close()
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Вы купили ' + str(kn) + ' GachCoin!'
                                    )
                                    if koin + kn >= 100 and zvanie != 5 and zvanie != 6 and zvanie != 10:
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Zvanie = '%s' WHERE User_ID = '%s'" % (
                                            5,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Звание обновлено до Кибермиллиардер!'
                                        )
                                else:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Недостаточно средств'
                                    )
                            except:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Введите корректную сумму коинов!'
                                )

                    elif event.object.text.lower() == 'топ игроков':
                        print(1)
                        top3 = top_bl()
                        print(top3)
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message=top3
                        )
                    elif event.object.text.lower() == 'информация рулетка':
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        balance = result[0][3]
                        name = result[0][1]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                attachment=photo_inf[0],
                                message='ИНФОРМАЦИЯ О РУЛЕТКЕ:\n\nФормат:\nрулетка [цвет в Среднем роде] [ставка]\n\nЦвета:\n"Зеленое" - вероятность 1 к 12, коэффиецент х15\n"Черное" - вероятность 1 к 4, коэффициент х4\n"Красное" - вероятность 1 к 2, коэффициент х2\n\nПримечание:\nИменно "черное" и "зеленое", НЕ "чёрное" и "зелёное"\n\nПример: '
                            )
                    elif event.object.text.lower() == 'информация кубик':
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        balance = result[0][3]
                        name = result[0][1]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                attachment=photo_inf[1],
                                message='ИНФОРМАЦИЯ О КУБИКЕ:\n\nФормат:\nкубик [сторона кубика]\n\nСтороны: 6 сторон игрального кубика\n\nВыигрыш:\nВыигрыш составляет случайную сумму от 1000 до 10000\n\nCтоимость: 100$\n\nПример: '
                            )
                    elif event.object.text.lower() == 'информация казино':
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        balance = result[0][3]
                        name = result[0][1]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                attachment=photo_inf[2],
                                message='ИНФОРМАЦИЯ О КАЗИНО:\n\nФормат:\nказино [ставка]\n\nКоффициенты:\nх2\nx3\nx7\n\nПример: '
                            )


                    elif 'рулетка' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        balance = result[0][3]
                        name = result[0][1]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if 'рулетка зеленое' in event.object.text.lower():
                                try:
                                    st_2 = int(event.object.text.lower().split("рулетка зеленое ")[-1])
                                    black = random.randint(0, 12)
                                    if st_2 > 0:
                                        if balance >= st_2:
                                            connection = sql.connect("user.sqlite", check_same_thread=False)
                                            q = connection.cursor()
                                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (
                                                event.object.from_id))
                                            result = q.fetchall()
                                            balance = result[0][3]
                                            q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                balance - st_2,
                                                event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            if black == 12:
                                                connection = sql.connect("user.sqlite", check_same_thread=False)
                                                q = connection.cursor()
                                                q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (
                                                    event.object.from_id))
                                                result = q.fetchall()
                                                balance = result[0][3]
                                                name = result[0][1]
                                                win_2 = st_2 * 15
                                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    balance + win_2,
                                                    event.object.from_id))
                                                connection.commit()
                                                connection.close()
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    attachment=ruletka_ph[2],
                                                    message=name + ', поздравляю, вы выиграли ' + str(win_2) + '\nВыпало:'
                                                )
                                            else:
                                                ruletka_rnd = random.randint(0,1)
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    attachment=ruletka_ph[ruletka_rnd],
                                                    message=name + ', вы проиграли ' + str(st_2) + ':(' + '\nВыпало:'
                                                )
                                        else:
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Недостаточно средств'
                                            )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Cтавка должна быть больше нуля'
                                        )
                                except:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Введите корректную сумму ставки'
                                    )
                            elif 'рулетка черное' in event.object.text.lower():
                                try:
                                    st_2 = int(event.object.text.lower().split("рулетка черное ")[-1])
                                    black = random.randint(0, 3)
                                    if st_2 > 0:
                                        if balance >= st_2:
                                            connection = sql.connect("user.sqlite", check_same_thread=False)
                                            q = connection.cursor()
                                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (
                                                event.object.from_id))
                                            result = q.fetchall()
                                            balance = result[0][3]
                                            q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                balance - st_2,
                                                event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            if black == 3:
                                                connection = sql.connect("user.sqlite", check_same_thread=False)
                                                q = connection.cursor()
                                                q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (
                                                    event.object.from_id))
                                                result = q.fetchall()
                                                balance = result[0][3]
                                                name = result[0][1]
                                                win_2 = st_2 * 4
                                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    balance + win_2,
                                                    event.object.from_id))
                                                connection.commit()
                                                connection.close()
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    attachment=ruletka_ph[1],
                                                    message=name + ', поздравляю, вы выиграли ' + str(win_2) + '\nВыпало:'
                                                )
                                            else:
                                                ruletka_rnd = random.randint(0, 1)
                                                if ruletka_rnd == 0:
                                                    ruletka_list = 0
                                                if ruletka_rnd == 1:
                                                    ruletka_list = 2
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    attachment=ruletka_ph[ruletka_list],
                                                    message=name + ', вы проиграли ' + str(st_2) + ':(' + '\nВыпало:'
                                                )
                                        else:
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Недостаточно средств'
                                            )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Cтавка должна быть больше нуля'
                                        )
                                except:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Введите корректную сумму ставки'
                                    )
                            elif 'рулетка красное' in event.object.text.lower():
                                try:
                                    st_2 = int(event.object.text.lower().split("рулетка красное ")[-1])
                                    black = random.randint(0, 2)
                                    if st_2 > 0:
                                        if balance >= st_2:
                                            connection = sql.connect("user.sqlite", check_same_thread=False)
                                            q = connection.cursor()
                                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (
                                                event.object.from_id))
                                            result = q.fetchall()
                                            balance = result[0][3]
                                            q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                balance - st_2,
                                                event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            if black == 2:
                                                connection = sql.connect("user.sqlite", check_same_thread=False)
                                                q = connection.cursor()
                                                q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (
                                                    event.object.from_id))
                                                result = q.fetchall()
                                                balance = result[0][3]
                                                name = result[0][1]
                                                win_2 = st_2 * 2
                                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    balance + win_2,
                                                    event.object.from_id))
                                                connection.commit()
                                                connection.close()
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    attachment=ruletka_ph[0],
                                                    message=name + ', поздравляю, вы выиграли ' + str(win_2) + '\nВыпало:'
                                                )
                                            else:
                                                ruletka_rnd = random.randint(1,2)
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    attachment=ruletka_ph[ruletka_rnd],
                                                    message=name + ', вы проиграли ' + str(st_2) + ':(' + '\nВыпало:'
                                                )
                                        else:
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Недостаточно средств'
                                            )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Cтавка должна быть больше нуля'
                                        )
                                except:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Введите корректную сумму ставки'
                                    )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Введите один из трёх цветов:\nЧерное, зеленое, красное'
                                )

                    elif 'дай миллион' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("дай миллион ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance + 1000000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Миллион зачислен игроку ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'забери миллион' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("забери миллион ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance - 1000000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Миллион вычтен у игрока ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'дай тысячу' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("дай тысячу ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance + 1000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Тысяча зачислена игроку ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'забери тысячу' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("забери тысячу ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance - 1000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Тысяча вычтена у игрока ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'дай миллиард' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("дай миллиард ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance + 1000000000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Миллиард зачислен игроку ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'забери миллиард' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("забери миллиард ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance - 1000000000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Миллиард вычтен у игрока ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'дай триллион' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("дай триллион ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance + 1000000000000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Триллион зачислен игроку ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'забери триллион' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("забери триллион ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance - 1000000000000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Триллион вычтен у игрока ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'дай сто тысяч' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("дай сто тысяч ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance + 100000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Сто тысяч зачислено игроку ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )
                    elif 'забери сто тысяч' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if zvanie == 10:
                                add = int(event.object.text.lower().split("забери сто тысяч ")[-1])
                                q.execute("SELECT * FROM user_inform1 WHERE id = '%s'" % (add))
                                result = q.fetchall()
                                balance = result[0][3]
                                name = result[0][1]
                                q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE id = '%s'" % (
                                    balance - 100000,
                                    add))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Сто тысяч вычтено у игрока ' + name
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно прав'
                                )

                    elif 'перевести миллион' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        balance1 = result[0][3]
                        perevod = result[0][7]
                        poluch = result[0][8]
                        id1 = result[0][1]
                        name_per = result[0][1]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if balance1 >= 1000000:
                                try:
                                    add = event.object.text.lower().split("перевести миллион ")[-1]
                                    if id1 != add:
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Perewod = '%s' WHERE User_ID = '%s'" % (
                                            perevod + 1000000,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("SELECT * FROM user_inform1 WHERE Name = '%s'" % (add))
                                        result = q.fetchall()
                                        balance = result[0][3]
                                        name = result[0][1]
                                        user_id = result[0][2]
                                        poluch = result[0][8]
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE Name = '%s'" % (
                                            balance + 1000000,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Poluch = '%s' WHERE Name = '%s'" % (
                                            poluch + 1000000,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Миллион переведен игроку ' + name
                                        )
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=user_id,
                                            message='Вам перечислен миллион от игрока ' + name_per
                                        )
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                            balance1 - 1000000,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Нельзя переводить деньги самому себе!'
                                        )
                                except:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Введите корректный ID пользователя'
                                    )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно средств!'
                                )
                    elif 'перевести тысячу' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        balance1 = result[0][3]
                        perevod = result[0][7]
                        id1 = result[0][1]
                        name_per = result[0][1]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if balance1 >= 1000:
                                try:
                                    add = event.object.text.lower().split("перевести тысячу")[-1]
                                    if id1 != add:
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Perewod = '%s' WHERE User_ID = '%s'" % (
                                            perevod + 1000,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("SELECT * FROM user_inform1 WHERE iName = '%s'" % (add))
                                        result = q.fetchall()
                                        balance = result[0][3]
                                        name = result[0][1]
                                        user_id = result[0][2]
                                        poluch = result[0][8]
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE Name = '%s'" % (
                                            balance + 1000,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Poluch = '%s' WHERE Name = '%s'" % (
                                            poluch + 1000,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Тысяча переведена игроку ' + name
                                        )
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=user_id,
                                            message='Вам перечислена тысяча от игрока ' + name_per)
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                            balance1 - 1000,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Нельзя переводить деньги самому себе!'
                                        )
                                except:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Введите корректный ID пользователя'
                                    )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно средств!'
                                )
                    elif 'перевести миллиард' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        balance1 = result[0][3]
                        perevod = result[0][7]
                        id1 = result[0][1]
                        name_per = [0][1]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if balance1 >= 1000000000:
                                try:
                                    add = event.object.text.lower().split("перевести миллиард")[-1]
                                    if id1 != add:
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Perewod = '%s' WHERE User_ID = '%s'" % (
                                            perevod + 1000000000,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("SELECT * FROM user_inform1 WHERE Name = '%s'" % (add))
                                        result = q.fetchall()
                                        balance = result[0][3]
                                        name = result[0][1]
                                        user_id = result[0][2]
                                        poluch = result[0][8]
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE Name = '%s'" % (
                                            balance + 1000000000,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Poluch = '%s' WHERE Name = '%s'" % (
                                            poluch + 1000000000,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Миллиард переведен игроку ' + name
                                        )
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=user_id,
                                            message='Вам перечислен миллиард от игрока ' + name_per)
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                            balance1 - 1000000000,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Нельзя переводить деньги самому себе!'
                                        )
                                except:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Введите корректный ID пользователя'
                                    )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно средств!'
                                )
                    elif 'перевести сто тысяч' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        balance1 = result[0][3]
                        perevod = result[0][7]
                        id1 = result[0][1]
                        name_per = result[0][1]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if balance1 >= 100000:
                                try:
                                    add = event.object.text.lower().split("перевести сто тысяч")[-1]
                                    if id1 != add:
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Perewod = '%s' WHERE User_ID = '%s'" % (
                                            perevod + 100000,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("SELECT * FROM user_inform1 WHERE Name = '%s'" % (add))
                                        result = q.fetchall()
                                        balance = result[0][3]
                                        name = result[0][1]
                                        user_id = result[0][2]
                                        poluch = result[0][8]
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE Name = '%s'" % (
                                            balance + 100000,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Poluch = '%s' WHERE Name = '%s'" % (
                                            poluch + 100000,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Сто тысяч переведено игроку ' + name
                                        )
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=user_id,
                                            message='Вам перечислено сто тысяч от игрока ' + name_per)
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                            balance1 - 100000,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Нельзя переводить деньги самому себе!'
                                        )
                                except:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Введите корректный ID пользователя'
                                    )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно средств!'
                                )
                    elif 'перевести сто' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = '%s'" % (event.object.from_id))
                        result = q.fetchall()
                        zvanie = result[0][5]
                        balance1 = result[0][3]
                        perevod = result[0][7]
                        id1 = result[0][1]
                        name_per  = result[0][1]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            if balance1 >= 100:
                                try:
                                    add = event.object.text.lower().split("перевести сто ")[-1]
                                    if id1 != add:
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Perewod = '%s' WHERE User_ID = '%s'" % (
                                            perevod + 100,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("SELECT * FROM user_inform1 WHERE Name = '%s'" % (add))
                                        result = q.fetchall()
                                        balance = result[0][3]
                                        name = result[0][1]
                                        user_id = result[0][2]
                                        poluch = result[0][8]
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE Name = '%s'" % (
                                            balance + 100,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Poluch = '%s' WHERE Name = '%s'" % (
                                            poluch + 100,
                                            add))
                                        connection.commit()
                                        connection.close()
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Сто переведено игроку ' + name
                                        )
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=user_id,
                                            message='Вам перечислено сто от игрока ' + name_per)
                                        connection = sql.connect("user.sqlite", check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                            balance1 - 100,
                                            event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Нельзя переводить деньги самому себе!'
                                        )
                                except:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Введите корректный ID пользователя'
                                    )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Недостаточно средств!'
                                )
                    elif 'создать аккаунт' in event.object.text.lower():
                        if event.object.text.lower() != 'создать аккаунт' and event.object.text.lower() != 'создать аккаунт ':
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                            result = q.fetchall()
                            if len(result) == 0:
                                user_name = (event.object.text.lower().split("создать аккаунт ")[-1])
                                if 'создать аккаунт' in user_name:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message='Нужно обязательно ввести ник'
                                    )
                                else:
                                    if user_name not in user_names:
                                        user_names.append(user_name)
                                        user_info = vk.method("users.get",
                                                              {"user_ids": event.object.from_id,
                                                               "fields": "first_name"})
                                        print("Добавлен участник")
                                        q.execute(
                                            "INSERT INTO user_inform1 (Name, User_ID, Balance, Zvanie, GachCoin, Perewod, Poluch) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                                                user_name,
                                                event.object.from_id,
                                                0, 0, 0, 0, 0))
                                        connection.commit()
                                        connection.close()
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Аккаунт успешно создан'
                                        )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Ник занят!'
                                        )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Аккаунт уже создан.\nНапишите "Профиль", чтобы его просмотреть'
                                )
                        else:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Нужно обязательно ввести ник'
                            )
                    elif event.object.text.lower() == 'звания':
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='Звания:\n\n"Бомж" - начальное звание\n\n"Бизнесмен" - нужно иметь больше ста тысячь на счету'
'\n\n"Миллионер" - нужно иметь больше миллиона на счету\n\n"Миллиардер" - нужно иметь больше миллиарда на счету\n\n"Путин" - нужно иметь больше триллиона на счету\n\n"Кибермиллиардер" - нужно иметь минимум 100 GachCoin на счету\n\n"Помощник Админа" - нужно иметь миллион GachCoin на счету'
                        )
                    elif event.object.text.lower() == 'профиль':
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            print(result)
                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                            result = q.fetchall()
                            user_id = result[0][0]
                            name = result[0][1]
                            balance = result[0][3]
                            ownment = result[0][4]
                            zvanie = result[0][5]
                            perevod = result[0][7]
                            koin = result[0][6]
                            poluch = result[0][8]

                            ownment_message = ""
                            if zvanie == 0:
                                zvanie = 'Бомж'
                            elif zvanie == 1:
                                zvanie = 'Бизнесмен'
                            elif zvanie == 2:
                                zvanie = 'Миллионер'
                            elif zvanie == 3:
                                zvanie = 'Миллиардер'
                            elif zvanie == 4:
                                zvanie = 'Путин'
                            elif zvanie == 5:
                                zvanie == 'Кибермиллиардер'
                            elif zvanie == 6:
                                zvanie = 'Помощник Админа'
                            elif zvanie == 10:
                                zvanie = 'Админ'

                            if ownment != None:
                                dom = 0
                                car = 0
                                bar = 0
                                ownment = ownment.split(",")
                                ownment = ownment[:-1]
                                for own in ownment:
                                    if int(own) == 1:
                                        dom += 1
                                    elif int(own) == 2:
                                        car += 1
                                    elif int(own) == 3:
                                        bar += 1
                                ownment_message = "Машины: " + str(car) + "\nДома: " + str(dom) + "\nБары: " + str(bar)
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message="ID: " + str(user_id) + "\nНик: " + str(
                                    name) + "\n💰Баланс: " + str(
                                    balance) + "$" + '\nGachCoin: ' + str(koin) + '\nЗвание: ' + zvanie + '\nПолучено: ' + str(poluch) + '\nПереведено: ' + str(perevod) + "\nВаши владения:\n" + ownment_message

                            )
                    elif 'собственность' in event.object.text.lower():
                        try:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                            result = q.fetchall()
                            if len(result) == 0:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message='Сначала создайте аккаунт!'
                                )
                            else:
                                realty = int(event.object.text.lower().split("собственность")[1])
                                if realty == 1:
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    ownment = result[0][4]
                                    if money >= 1000000:
                                        if ownment != None:
                                            q.execute("UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                str(ownment) + "1,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 1000000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили дом!'
                                            )
                                        else:
                                            q.execute(
                                                "UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                    "1,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 1000000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили дом!'
                                            )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Недостаточно средств для покупки!'
                                        )
                                elif realty == 2:
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    ownment = result[0][4]
                                    if money >= 100000:
                                        if ownment != None:
                                            q.execute("UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                str(ownment) + "2,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 100000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили машину!'
                                            )
                                        else:
                                            q.execute(
                                                "UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                    "2,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 100000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили машину!!'
                                            )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Недостаточно средств для покупки!'
                                        )
                                elif realty == 3:
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    ownment = result[0][4]
                                    if money >= 1000000000:
                                        if ownment != None:
                                            q.execute("UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                str(ownment) + "3,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 1000000000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили бар!'
                                            )
                                        else:
                                            q.execute(
                                                "UPDATE user_inform1 SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                                    "3,", event.object.from_id))
                                            q.execute(
                                                "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                    money - 1000000000,
                                                    event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message='Вы купили бар!'
                                            )
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message='Недостаточно средств для покупки!'
                                        )
                        except:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message="Введите корректный id покупки!"
                            )
                    elif "баланс" in event.object.text.lower():
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            balance2 = result[0][3]
                            if balance2 < 10:
                                connection = sql.connect('user.sqlite', check_same_thread=False)
                                q = connection.cursor()
                                q.execute(
                                    "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (int(balance2) + 10,
                                                                                                     event.object.from_id))
                                connection.commit()
                                connection.close()
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message="Вам зачислено 10$!\nБаланс: " + str(balance2 + 10)
                                )
                            else:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message="Нужно иметь меньше 10$ на балансе!"
                                )
                    elif "казино" in event.object.text.lower():
                        connection = sql.connect('user.sqlite', check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )

                        else:
                            try:
                                money = result[0][3]
                                kazino = random.randint(1, 2)
                                rate = int(event.object.text.lower().split("казино ")[-1])
                                if rate > 0:
                                    if result[0][3] >= rate:
                                        connection = sql.connect('user.sqlite', check_same_thread=False)
                                        q = connection.cursor()
                                        q.execute(
                                            "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                int(money) -
                                                rate,
                                                event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        if kazino == 1:
                                            coefficient = random.randint(1, 3)
                                            if coefficient == 1:
                                                connection = sql.connect('user.sqlite', check_same_thread=False)
                                                q = connection.cursor()
                                                q.execute(
                                                    "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                        int(money) +
                                                        rate * 2,
                                                        event.object.from_id))
                                                connection.commit()
                                                connection.close()
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    message="Вы выиграли " + str(rate * 2) + "(х2)!"
                                                )
                                                zvanie_2(event.object.peer_id, event.object.from_id)
                                            elif coefficient == 2:
                                                connection = sql.connect('user.sqlite', check_same_thread=False)
                                                q = connection.cursor()
                                                q.execute(
                                                    "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                        int(money) +
                                                        rate * 3,
                                                        event.object.from_id))
                                                connection.commit()
                                                connection.close()
                                                vk2.messages.send(
                                                    random_id=0,
                                                    peer_id=event.object.peer_id,
                                                    message="Вы выиграли " + str(rate * 3) + "(х3)!"
                                                )
                                                zvanie_2(event.object.peer_id, event.object.from_id)
                                            else:
                                                x7 = random.randint(1, 2)
                                                if x7 == 1:
                                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                                    q = connection.cursor()
                                                    q.execute(
                                                        "UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                            int(money) +
                                                            rate * 7,
                                                            event.object.from_id))
                                                    connection.commit()
                                                    connection.close()
                                                    vk2.messages.send(
                                                        random_id=0,
                                                        peer_id=event.object.peer_id,
                                                        message="Вы выиграли " + str(rate * 7) + "(х7)!"
                                                    )
                                                    zvanie_2(event.object.peer_id, event.object.from_id)
                                                else:
                                                    vk2.messages.send(
                                                        random_id=0,
                                                        peer_id=event.object.peer_id,
                                                        message="Вы проиграли " + str(rate) + ":("
                                                    )
                                                    zvanie_2(event.object.peer_id, event.object.from_id)
                                        elif kazino == 2:
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                message="Вы проиграли " + str(rate) + ":("
                                            )
                                            zvanie_2(event.object.peer_id, event.object.from_id)
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message="Недостаточно средств!"
                                        )
                                else:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message="Cтавка должна быть больше нуля!"
                                    )
                            except:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message="Введите корректную сумму ставки!"
                                )
                    elif 'кубик' in event.object.text.lower():
                        connection = sql.connect("user.sqlite", check_same_thread=False)
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_inform1 WHERE User_ID = %s" % (event.object.from_id))
                        result = q.fetchall()
                        balance = result[0][3]
                        if len(result) == 0:
                            vk2.messages.send(
                                random_id=0,
                                peer_id=event.object.peer_id,
                                message='Сначала создайте аккаунт!'
                            )
                        else:
                            try:
                                if balance >= 100:
                                    cube = random.randint(1, 6)
                                    user_cube = int(event.object.text.lower().split('кубик')[-1])
                                    if 1 <= user_cube <= 6:
                                        user_win = random.randint(1000, 10000)
                                        balance = result[0][3]
                                        q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                            balance - 100, event.object.from_id))
                                        connection.commit()
                                        connection.close()
                                        user_name = result[0][1]
                                        if user_cube == cube:
                                            connection = sql.connect("user.sqlite", check_same_thread=False)
                                            q = connection.cursor()
                                            q.execute(
                                                "SELECT * FROM user_inform1 WHERE User_ID = %s" % (
                                                    event.object.from_id))
                                            result = q.fetchall()
                                            balance = result[0][3]
                                            user_name = result[0][1]

                                            q.execute("UPDATE user_inform1 SET Balance = '%s' WHERE User_ID = '%s'" % (
                                                balance + user_win, event.object.from_id))
                                            connection.commit()
                                            connection.close()
                                            if cube == 1:
                                                attachment = kubik_ph[0]
                                            if cube == 2:
                                                attachment = kubik_ph[1]
                                            if cube == 3:
                                                attachment = kubik_ph[2]
                                            if cube == 4:
                                                attachment = kubik_ph[3]
                                            if cube == 5:
                                                attachment = kubik_ph[4]
                                            if cube == 6:
                                                attachment = kubik_ph[5]
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                attachment=attachment,
                                                message=user_name + ", вы угадали! 😯 Выйгрыш " + str(user_win) + "$"
                                            )
                                            zvanie_2(event.object.peer_id, event.object.from_id)
                                        else:
                                            if cube == 1:
                                                attachment = kubik_ph[0]
                                            if cube == 2:
                                                attachment = kubik_ph[1]
                                            if cube == 3:
                                                attachment = kubik_ph[2]
                                            if cube == 4:
                                                attachment = kubik_ph[3]
                                            if cube == 5:
                                                attachment = kubik_ph[4]
                                            if cube == 6:
                                                attachment = kubik_ph[5]
                                            vk2.messages.send(
                                                random_id=0,
                                                peer_id=event.object.peer_id,
                                                attachment=attachment,
                                                message=user_name + ", вы проиграли! Выпало число " + str(cube) + " 😔"
                                            )
                                            zvanie_2(event.object.peer_id, event.object.from_id)
                                    else:
                                        vk2.messages.send(
                                            random_id=0,
                                            peer_id=event.object.peer_id,
                                            message="Введи число от 1 до 6!"
                                        )
                                else:
                                    vk2.messages.send(
                                        random_id=0,
                                        peer_id=event.object.peer_id,
                                        message="Недостаточно средств"
                                    )
                            except:
                                vk2.messages.send(
                                    random_id=0,
                                    peer_id=event.object.peer_id,
                                    message="Введите корректную сторону кубика"
                                )
                    elif event.object.text.lower() == 'демка':
                        message2 = random.randint(0, 4)
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=demki[message2],
                            message='👌🏻👈🏻'
                        )
                    elif 'бит' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=attachments[0],
                            message='блинб биты'
                        )
                    elif 'аниме' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=attachments[1],
                            message=' '
                        )
                    elif event.object.text.lower() == 'песня':
                        number = random.randint(0, 12)
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=songs[number]
                        )
                    elif 'прон' in event.object.text.lower() or 'порн' in event.object.text.lower() or 'дота' in event.object.text.lower() or 'dota' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            attachment=attachments[2],
                            message='Любишь гей порно я смотрю?'
                        )
                    elif 'как дела' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='Норм, нога только чешется')
                    elif 'ты пидор' in event.object.text.lower() or 'ты педик' in event.object.text.lower() or 'ты гандон' in event.object.text.lower() or 'ты мудак' in event.object.text.lower():
                        vk2.messages.send(
                            random_id=0,
                            peer_id=event.object.peer_id,
                            message='За базар вывезешь?')
        except:
            time.sleep(1)
except:
    time.sleep(60)
