# -*- coding: utf-8 -*-
# bilibili.py
import sys

import urllib
import BiliClient
import xbmcplugin
import xbmcgui
import urlparse

base_url = sys.argv[0]
handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
api = BiliClient.BiliClient()
action = args.get('action', None)
