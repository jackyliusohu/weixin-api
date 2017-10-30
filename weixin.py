# encoding: utf-8
import os,sys,urllib,urllib2,json
from flask import Flask,request
app = Flask(__name__)

def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read().decode("utf8")
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token


def senddata(access_token,user,partyid,content):
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        "touser":user,    #企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
        "toparty":partyid,    #企业号中的部门id
        "msgtype":"text",  #企业号中的应用id，消息类型。
        "agentid":"2",
        "text":{
            "content":content
           },
        "safe":"0"
        }
    send_data = json.dumps(send_values, ensure_ascii=False)
    send_request = urllib2.Request(send_url, send_data)
    response = json.loads(urllib2.urlopen(send_request).read())
    return response


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        content = request.form['content']
        user = request.form['mobile']
        partyid = '2'
        corpid = 'XXX'   #CorpID是企业号的标识
        corpsecret = 'XXX'  #corpsecretSecret是管理>>组凭证密钥
        accesstoken = gettoken(corpid,corpsecret)
        send_request = senddata(accesstoken,user,partyid,content)
        return content 
    else:
        return "no post request 
