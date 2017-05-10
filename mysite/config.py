#是否是本地调试版本，如果不是，则是发布版本
LOCAL_DEBUG = True


if LOCAL_DEBUG == True:
	SERVER_IP = '0.0.0.0'
	SERVER_PORT = '8080'
	HTTP_URL = "http://localhost:8080/"
else:
	SERVER_IP = '139.199.82.129'
	SERVER_PORT = '80'
	HTTP_URL = "http://139.199.82.129:80/"