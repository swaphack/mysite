# -*- coding: utf-8 -*-

class AccountActor(object):
	"""docstring for AccountActor"""
	def __init__(self):
		super(AccountActor, self).__init__()


########################################################################
global __account_actor
__account_actor = AccountActor()

def get_account_actor():
	global __account_actor
	return __account_actor
