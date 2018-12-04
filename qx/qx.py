# -*- coding:utf-8 -*-
import requests, json
import sys

sys.path.append('../')
from app import mongo


class qqLogin():
    def __init__(self, id, qq, qurl):
        self.id = str(id)
        self.qq = qq
        self.qurl = qurl
        self.data = {
            'qq':qq,
            'FriendList':'',
            'GroupList':''

        }
        self.isUser()
    def isUser(self):
        if mongo.db[self.id].find_one({'qq':self.qq}):
            pass
        else:
            mongo.db[self.id].insert(self.data)
    def getCookie(self):
        url = 'https://ptlogin2.qun.qq.com/check_sig?pttype=2&uin=' + self.qq + '&service=jump&nodirect=0&ptsigx=' + self.qurl + '&s_url=https%3A%2F%2Fqun.qq.com%2F%3F_%3D1539597746536&f_url=&ptlang=2052&ptredirect=100&aid=1000101&daid=73&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=2&pt_aid=715030901&pt_aaid=0&pt_light=0&pt_3rd_aid=0'
        print(url)
        r = requests.get(url, allow_redirects=False)
        Cookie = r.cookies.get_dict()
        Uin = Cookie['uin']
        Skey = Cookie['skey']
        e = 5381
        for i in range(len(Skey)):
            e = e + (e << 5) + ord(Skey[i])
        bkn = str(2147483647 & e)
        try:
            self.getFriendList(Uin, bkn, Cookie)
        except:
            pass
        try:
            self.getGroupList(Uin, bkn, Cookie)
        except:
            pass

    def getGTK(cookie):
        hashes = 5381
        for letter in cookie['p_skey']:
            hashes += (hashes << 5) + ord(letter)
        return hashes & 0x7fffffff

    def getFriendList(self, Uin, bkn, cookie):
        url = "http://qun.qq.com/cgi-bin/qun_mgr/get_friend_list"
        # url = 'https://qun.qq.com/?_=1539597746536'
        data = 'bkn=' + str(bkn)
        r = requests.post(url, data=data, cookies=cookie).json()

        self.isUser()
        mongo.db[self.id].update_one({'qq':self.qq},{"$set": {'FriendList':r}})
        return 'ok'

        # FriendList = ''
        # for x in r['result']:
        #     try:
        #         # print(r['result'][x])
        #         firendClass = r['result'][x]['gname']
        #         a = [i for i in r['result'][x]['mems']]
        #         for i in r['result'][x]['mems']:
        #             firendList = ''
        #             # print(i['name']+' '+str(i['uin'])+' '+firendClass)
        #             # print()
        #             # firendList = i['name']+'|'+i['uin']+'|'+firendClass
        #             # print(firendClass)
        #             # print('------------------------------')
        #             FriendList += i['name'] + '\n' + str(
        #                 i['uin']) + '\n' + firendClass + '\n' + '*****************************' + '\n'
        #
        #     except:
        #         firendClass = ''
        #         try:
        #             for i in r['result'][x]['mems']:
        #                 firendList = ''
        #                 # print()
        #                 # firendList = i['name']+'|'+i['uin']+'|'+firendClass
        #                 # print(firendClass)
        #                 # print('------------------------------')
        #                 FriendList += i['name'] + '\n' + str(
        #                     i['uin']) + '\n' + firendClass + '\n' + '*****************************' + '\n'
        #         except:
        #             pass
        # try:
        #     with open(Uin + '.txt', 'a', encoding='utf8') as f:
        #         f.write(FriendList)
        #     print(Uin + ":生成完毕�?)
        # except Exception as e:
        #     print(e)

    def getGroupList(self, Uin, bkn, cookie):
        url = 'http://qun.qq.com/cgi-bin/qun_mgr/get_group_list'
        data = 'bkn=' + str(bkn)
        qun = requests.post(url, data=data, cookies=cookie).json()
        self.isUser()
        qunLists = []
        print(qun)
        try:
            for x in qun['create']:
                numbers = []
                url = 'http://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
                data = 'gc=' + str(x['gc']) + '&st=0&end=1999&sort=0&bkn=' + bkn
                r = requests.post(url, data=data, cookies=cookie).json()['mems']
                for i in r:
                    numberList = {
                        'nick':str(i['nick']),
                        'uin':str(i['uin'])
                    }
                    numbers.append(numberList)
                qunList = {
                    'gc': x['gc'],
                    'gn': x['gn'],
                    'numbers': numbers
                }
                qunLists.append(qunList)
        except Exception as e:
            print(e)
        try:
            for x in qun['join']:
                numbers = []
                url = 'http://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
                data = 'gc=' + str(x['gc']) + '&st=0&end=1999&sort=0&bkn=' + bkn
                r = requests.post(url, data=data, cookies=cookie).json()['mems']
                for i in r:
                    numberList = {
                        'nick':str(i['nick']),
                        'uin':str(i['uin'])
                    }
                    numbers.append(numberList)
                qunList = {
                    'gc': x['gc'],
                    'gn': x['gn'],
                    'numbers': numbers
                }
                qunLists.append(qunList)
        except Exception as e:
            print(e)
        try:
            for x in qun['manage']:
                numbers = []
                url = 'http://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
                data = 'gc=' + str(x['gc']) + '&st=0&end=1999&sort=0&bkn=' + bkn
                r = requests.post(url, data=data, cookies=cookie).json()['mems']
                for i in r:
                    numberList = {
                        'nick':str(i['nick']),
                        'uin':str(i['uin'])
                    }
                    numbers.append(numberList)
                qunList = {
                    'gc': x['gc'],
                    'gn': x['gn'],
                    'numbers': numbers
                }
                qunLists.append(qunList)
        except Exception as e:
            print(e)




        mongo.db[self.id].update_one({'qq':self.qq},{"$set": {'GroupList':qunLists}})