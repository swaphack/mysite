# -*- coding: utf-8 -*-

#app配置

#应用id
APPID = "wx1a31b3c5bfb1b744"

AppSecret = "c2a622ee92d93ff152a1cef063996c19"

TOKEN = "jifueiw1121ljdfiae1"

EncodingAESKey = "0lmsuNSNRUORCb388vPDPZpuV94TByPrXtaEzfsgh28"

# 微信操作标识
WEBCHAT_OPERATOR_MARK = 'action'
# 微信操作处理
WEBCHAT_OPERATOR = [
	'access_token',
	'access_server_list',
]

# 微信请求地址
WEBCHAT_URL = {
	WEBCHAT_OPERATOR[0] : "https://api.weixin.qq.com/cgi-bin/token",
	WEBCHAT_OPERATOR[1] : "https://api.weixin.qq.com/cgi-bin/getcallbackip",
}


SHOW_PRINT = True