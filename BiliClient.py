# -*- coding: utf-8 -*-
__author__ = 'hexpang'
import APIHelper


class BiliClient(APIHelper.APIHelper):
    def __init__(self):
        APIHelper.APIHelper.__init__(self)
        self.baseUrl = "http://api.bilibili.cn/"

    def request(self, action):
        reqUrl = self.baseUrl + "/" + action
        return APIHelper.APIHelper.request(self, reqUrl, param)
