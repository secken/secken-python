# coding=utf8

import urllib2
import urllib
import md5
import json
import threading
import time
import base64


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
        self.__entries = entries
        self.__dict__.update(**entries)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def getDictStruct(self):
        
        result = dict()
        result.update(**self.__entries)

        for x in result:
            if type(result[x]) is RequestCallBack:
                result[x] = result[x].getDictStruct()

        return result

class api(object):
    __www = "api"
    __domain = ".yangcong.com"
    __protocol = "https"
    __version = "v2"
    __timeout = False
    __sdkVersion = "1.7 Stable"

    def __Get__(self, url, data):
        params = ""
        if data:
            params = "?"
            for x in data:
                params += x
                params += "=" + str(data[x])
                params += "&"
            params = params[:-1]

        req = urllib2.Request(url + params)
        req.add_header('Sdk', self.__sdkVersion)
        response = urllib2.urlopen(req)
        return response

    def __Post__(self, url, data):
        post_data = urllib.urlencode(data)
        req = urllib2.Request(url, post_data)
        req.add_header('Content-Type', "application/x-www-form-urlencoded")
        req.add_header('Sdk', self.__sdkVersion)
        response = urllib2.urlopen(req)
        return response
    
    def __ResponseToJson__(self, response):
        json_dict = json.loads(response.read())
        return json_dict
        
    def __ResponseToLocation__(self, response):
        url = response.geturl()
        return url

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
            "app_id": self.appid,
            "signature": md5.new("app_id=%s" % (self.appid + self.appkey)).hexdigest()
        }

        # 网络请求
        json_dict = None
        try:
            json_dict = \
                self.__ResponseToJson__(
                    self.__Get__(
                        self.__getUrl("qrcode_for_binding"), data))
        except Exception, e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }

        event_id = json_dict.get("event_id",None)

        if event_id is None:
            if json_dict["status"] == 200:
                raise ParamsException("server has fail can't not get event_id param")
            else:
                raise ParamsException("api system fail!")

        json_dict["event_id"] = base64.b64encode(event_id.decode("utf-8"))

        # 返回dict结构
        result = {
            "success": json_dict["status"] == 200 and True or False,
            "result": RequestCallBack(json_dict)
        }
        
        result = RequestCallBack(result)
        
        print result.getDictStruct()
        
        return result

    def getLoginCode(self):
        # 传递参数
        data = {
            "app_id": self.appid,
            "signature": md5.new("app_id=%s" % (self.appid + self.appkey)).hexdigest()
        }

        # 网络请求

        json_dict = None

        try:
            json_dict = \
                self.__ResponseToJson__(
                    self.__Get__(
                        self.__getUrl("qrcode_for_auth"), data))
        except Exception, e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }

        event_id = json_dict.get("event_id",None)

        if event_id is None:
            if json_dict["status"] == 200:
                raise ParamsException("server has fail can't not get event_id param")
            else:
                raise ParamsException("api system fail!")

        json_dict["event_id"] = base64.b64encode(event_id.decode("utf-8"))

        # 返回dict结构
        result = {
            "success": json_dict["status"] == 200 and True or False,
            "result": RequestCallBack(json_dict)
        }

        return RequestCallBack(result)

    def getResult(self, uuid):
        if self.__timeout:
            self.__timeout = False
            raise InterfaceTimeoutException(
                "interface timeout. plesae recheck")
        if uuid:
            uuid = base64.b64decode(uuid.decode("utf-8"))
            signature = "app_id=%sevent_id=%s%s" % (
                self.appid, uuid, self.appkey)

            data = {
                "app_id": self.appid,
                "event_id": uuid,
                "signature": md5.new(signature).hexdigest()
            }

            # 网络请求
            json_dict = None
            try:
                json_dict = \
                    self.__ResponseToJson__(
                        self.__Get__(
                            self.__getUrl("event_result"), data))
            except Exception, e:
                json_dict = {
                    "status": -1,
                    "description": "network has exception"
                }

            # 返回dict结构
            result = {
                "success": json_dict["status"] == 200 and True or False,
                "result": RequestCallBack(json_dict)
            }

            code = json_dict["status"]

            if code == 603:
                self.__timeout = True

            result = RequestCallBack(result)

            return result
        else:
            raise ParamsException(
                "before getResult please call getLoginCode or getBindingCode or verifyOneClick")

    def verifyOneClick(self, userid, action="", ip=None, username=None):

        if userid == None:
            raise ParamsException("userid can't be 'None'")
        if action == None:
            raise ParamsException("action can't be 'None'")

        signature = "action_type=%sapp_id=%suid=%s%s" % (
            action, self.appid, userid, self.appkey)

        data = {
            "app_id": self.appid,
            "uid": userid,
            "action_type": action,
            "signature": md5.new(signature).hexdigest()
        }

        if ip:
            data["user_ip"] = ip

        if username:
            data["Username"] = username

        # 网络请求

        json_dict = None
        try:
            json_dict = \
                self.__ResponseToJson__(
                    self.__Post__(
                        self.__getUrl("realtime_authorization"), data))
        except Exception, e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }
        if json_dict["event_id"] is None:
            if json_dict["status"] == 200 :
                raise ParamsException("server has fail can't not get event_id param")
            else: 
                raise ParamsException("api system fail!")

        json_dict["event_id"] = base64.b64encode(json_dict["event_id"].decode("utf-8"))

        # 返回dict结构
        result = {
            "success": json_dict["status"] == 200 and True or False,
            "result": RequestCallBack(json_dict)
        }

        return RequestCallBack(result)

    def verifyOTP(self, userid, dnum):
        signature = "app_id=%sdynamic_code=%suid=%s%s" % (
            self.appid, dnum, userid, self.appkey)

        data = {
            "app_id": self.appid,
            "uid": userid,
            "dynamic_code": dnum,
            "signature": md5.new(signature).hexdigest()
        }

        # 网络请求
        json_dict = None
        try:
            json_dict = \
                self.__ResponseToJson__(
                    self.__Post__(
                        self.__getUrl("offline_authorization"), data))
        except Exception, e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }

        # 返回dict结构
        result = {
            "success": json_dict["status"] == 200 and True or False,
            "result": RequestCallBack(json_dict)
        }

        return RequestCallBack(result)

    def authPage(self, callback):
        t = long(round(time.time()))
        signature = "auth_id=%scallback=%stimestamp=%s%s" % (
            self.authid, callback, t, self.appkey)

        data = {
            "timestamp": t,
            "auth_id": self.authid,
            "callback": callback,
            "signature": md5.new(signature).hexdigest()
        }

        # 网络请求
        json_dict = None
        try:
            json_dict = \
            {
                "url": self.__ResponseToLocation__(
                        self.__Get__(
                            self.__getUrl("auth_page", "auth"), data)),
                "status":200 
            }
        except Exception, e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }

        # 返回dict结构
        result = {
            "success": json_dict["status"] == 200 and True or False,
            "result": RequestCallBack(json_dict)
        }

        return RequestCallBack(result)
