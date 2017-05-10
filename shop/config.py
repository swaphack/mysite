# -*- coding: utf-8 -*-

from mysite.config import HTTP_URL

# 商店地址
SHOP_URL = HTTP_URL + 'shop/'

# 商店操作处理
SHOP_OPERATOR_MARK = 'action'

# 微信操作处理
WEBCHAT_OPERATOR = [
	'item_list',
	'item_info',
]