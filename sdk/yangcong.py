# coding=u8

import urllib2
import urllib
import md5
import json
import threading
import time


class StringException(Exception):

    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg = msg

    def __str__(self):
        return self.msg


class ParamsException(StringException):
    pass


class InterfaceTimeoutException(StringException):
    pass


class RequestCallBack(object):

    def __init__(self, entries):
        self.__dict__.update(**entries)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def getDictStruct(self):
        return self.__dict__


class api(object):
    __www = "api"
    __domain = ".yangcong.com"
    __protocol = "https"
    __version = "v1"
    __uuid = None
    __timeout = False
    __sdkVersion = "1.1 Beta"

    def __Get__(self, url, data):
        params = ""
        if data:
            params = "?"
            for x in data:
                params += x
                params += "=" + str(data[x])
                params += "&"
            params = params[0:len(params) - 1]

        req = urllib2.Request(url + params)
        req.add_header('SDK', self.__sdkVersion)
        response = urllib2.urlopen(req)
        url = response.geturl()
        json_dict = {
            "code": 0,
            "url": url
        }
        return json_dict

    def __Post__(self, url, data):
        post_data = urllib.urlencode(data)
        req = urllib2.Request(url, post_data)
        req.add_header('Content-Type', "application/x-www-form-urlencoded")
        req.add_header('SDK', self.__sdkVersion)
        response = urllib2.urlopen(req)
        json_dict = json.loads(response.read())
        return json_dict

    def __init__(self, appid, appkey, authid):
        if appid:
            self.appid = appid
        else:
            raise ParamsException("appid can't not be 'None'")
        if appkey:
            self.appkey = appkey
        else:
            raise ParamsException("appkey can't not be 'None'")
        if authid:
            self.authid = authid
        else:
            raise ParamsException("authid can't not be 'None'")

    def __getUrl(self, name, www=None):
        if www is None:
            www = self.__www
        return "%s://%s%s/%s/%s" % (self.__protocol, www, self.__domain, self.__version, name)

    def getBindingCode(self):
        # 传递参数
        data = {
            "appid": self.appid,
            "signature": md5.new("appid=%s" % (self.appid + self.appkey)).hexdigest()
        }

        # 网络请求
        json_dict = None
        try:
            json_dict = self.__Post__(self.__getUrl("GetBindingCode"), data)
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

        if json_dict["uuid"] is None:
            raise ParamsException("server has fail can't not get uuid param")
        else:
            self.__uuid = json_dict["uuid"]

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
            json_dict = self.__Post__(self.__getUrl("GetLoginCode"), data)
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

        if json_dict["uuid"] is None:
            raise ParamsException("server has fail can't not get uuid param")
        else:
            self.__uuid = json_dict["uuid"]

        return RequestCallBack(result)

    def getResult(self):
        if self.__timeout:
            self.__timeout = False
            raise InterfaceTimeoutException(
                "interface timeout. plesae recheck")
        if self.__uuid:
            signature = "appid=%suuid=%s%s" % (
                self.appid, self.__uuid, self.appkey)

            data = {
                "appid": self.appid,
                "uuid": self.__uuid,
                "signature": md5.new(signature).hexdigest()
            }

            # 网络请求

            json_dict = None
            try:
                json_dict = self.__Post__(self.__getUrl("GetResult"), data)
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

            code = json_dict["code"]

            if code == 0:
                self.__uuid = None

            if code == 300058:
                self.__uuid = None
                self.__timeout = True

            return RequestCallBack(result)
        else:
            raise ParamsException(
                "before getResult please call getLoginCode or getBindingCode or verifyOneClick")

    def verifyOneClick(self, userid, action, ip=None, username=None):

        if userid == None:
            raise ParamsException("userid can't be 'None'")
        if action == None:
            raise ParamsException("action can't be 'None'")

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
            json_dict = self.__Post__(self.__getUrl("VerifyOneClick"), data)
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

        if json_dict["uuid"] is None:
            raise ParamsException("server has fail can't not get uuid param")
        else:
            self.__uuid = json_dict["uuid"]

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
            json_dict = self.__Post__(self.__getUrl("VerifyOTP"), data)
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

    def authPage(self, callback):
        t = long(round(time.time()))
        signature = "authid=%scallback=%stime=%s%s" % (
            self.authid, callback, t, self.appkey)

        data = {
            "time": t,
            "authid": self.authid,
            "callback": callback,
            "signature": md5.new(signature).hexdigest()
        }

        # 网络请求
        json_dict = None
        try:
            json_dict = self.__Get__(self.__getUrl("AuthPage", "auth"), data)
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
