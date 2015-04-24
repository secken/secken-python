# coding=u8

import urllib2
import urllib
import md5
import json
import threading
import time


class RequestCallBack(object):

    def __init__(self, entries):
        self.__dict__.update(**entries)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def getDictStruct(self):
        return self.__dict__


def __Post__(url, data):
    try:
        post_data = urllib.urlencode(data)
        req = urllib2.Request(url, post_data)
        req.add_header('Content-Type', "application/x-www-form-urlencoded")
        response = urllib2.urlopen(req)
        json_dict = json.loads(response.read())
        return json_dict
    except Exception, e:
        return {
            "code": 300060,
            "message": "network error"
        }


class api(object):

    __domain = "api.yangcong.com"
    __protocol = "https"
    __version = "v1"

    def __init__(self, appid, appkey, authid):
        if appid:
            self.appid = appid
        else:
            raise "appid can't not be 'None'"
        if appkey:
            self.appkey = appkey
        else:
            raise "appkey can't not be 'None'"
        if authid:
            self.authid = authid
        else:
            raise "authid can't not be 'None'"

    def __getUrl(self, name):
        return "%s://%s/%s/%s" % (self.__protocol, self.__domain, self.__version, name)

    def getBindingCode(self):
        # 传递参数
        data = {
            "appid": self.appid,
            "signature": md5.new("appid=%s" % (self.appid + self.appkey)).hexdigest()
        }

        # 网络请求
        json_dict = None
        try:
            json_dict = __Post__(self.__getUrl("GetBindingCode"), data)
        except Exception, e:
            json_dict = {
                "code": -1,
                "message": "network has exception"
            }

        # 返回dict结构
        result = {
            "success": json_dict["code"] == 0 and True or False,
            "result": RequestCallBack(json_dict)
        }

        result = RequestCallBack(result)

        # debug
        # print result

        return result

    def getLoginCode(self):
        # 传递参数
        data = {
            "appid": self.appid,
            "signature": md5.new("appid=%s" % (self.appid + self.appkey)).hexdigest()
        }

        # 网络请求

        json_dict = None
        try:
            json_dict = __Post__(self.__getUrl("GetLoginCode"), data)
        except Exception, e:
            json_dict = {
                "code": -1,
                "message": "network has exception"
            }

        # 返回dict结构
        result = {
            "success": json_dict["code"] == 0 and True or False,
            "result": RequestCallBack(json_dict)
        }

        return RequestCallBack(result)

    def getResult(self, uuid):

        signature = "appid=%suuid=%s%s" % (
            self.appid, uuid, self.appkey)

        data = {
            "appid": self.appid,
            "uuid": uuid,
            "signature": md5.new(signature).hexdigest()
        }

        # 网络请求

        json_dict = None
        try:
            json_dict = __Post__(self.__getUrl("GetResult"), data)
        except Exception, e:
            json_dict = {
                "code": -1,
                "message": "network has exception"
            }

        # 返回dict结构
        result = {
            "success": json_dict["code"] == 0 and True or False,
            "result": RequestCallBack(json_dict)
        }

        return RequestCallBack(result)

    def verifyOneClick(self, userid, action, ip=None, username=None):

        if userid == None:
            raise "userid can't be 'None'"
        if action == None:
            raise "action can't be 'None'"

        signature = "action=%sappid=%suserid=%s%s" % (
            action, self.appid, userid, self.appkey)

        data = {
            "appid": self.appid,
            "userid": userid,
            "action": action,
            "signature": md5.new(signature).hexdigest()
        }

        if ip:
            data["ip"] = ip

        if username:
            data["username"] = username

        # 网络请求

        json_dict = None
        try:
            json_dict = __Post__(self.__getUrl("VerifyOneClick"), data)
        except Exception, e:
            json_dict = {
                "code": -1,
                "message": "network has exception"
            }

        # 返回dict结构
        result = {
            "success": json_dict["code"] == 0 and True or False,
            "result": RequestCallBack(json_dict)
        }

        return RequestCallBack(result)

    def verifyOTP(self, userid, dnum):
        signature = "appid=%sdnum=%suserid=%s%s" % (
            self.appid, dnum, userid, self.appkey)

        data = {
            "appid": self.appid,
            "userid": userid,
            "dnum": dnum,
            "signature": md5.new(signature).hexdigest()
        }

        # 网络请求
        json_dict = None
        try:
            json_dict = __Post__(self.__getUrl("VerifyOTP"), data)
        except Exception, e:
            json_dict = {
                "code": -1,
                "message": "network has exception"
            }

        # 返回dict结构
        result = {
            "success": json_dict["code"] == 0 and True or False,
            "result": RequestCallBack(json_dict)
        }

        return RequestCallBack(result)
