# coding=u8
# Copyright 2014-2015 Secken, Inc.  All Rights Reserved.
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# NOTICE:  All information contained herein is, and remains
# the property of Secken, Inc. and its suppliers, if any.
# The intellectual and technical concepts contained
# herein are proprietary to Secken, Inc. and its suppliers
# and may be covered by China and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Secken, Inc..
#
# 注意：此处包含的所有信息，均属于Secken, Inc.及其供应商的私有财产。
# 此处包含的所有知识、专利均属于Secken, Inc.及其供应商，属于商业秘密，
# 并受到中国和其他国家的法律保护。这些信息及本声明，除非事先得到
# Secken, Inc.的书面授权，否则严禁复制或传播。
#
# @author     xupengjie (pengjiexu@secken.com)
# @version    1.25.0
#


# coding=utf8

import urllib2
import urllib
import md5
import json
import time


class StringException(Exception):

    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg = msg

    def __str__(self):
        return self.msg


class ParamsException(StringException):

    def __init__(self, msg, status=0, status_msg=None):
        StringException.__init__(self, msg)
        self.status = status
        self.description = status_msg


class InterfaceTimeoutException(StringException):
    pass


class SignatureException(StringException):
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

class ActionType:
    LoginAction = 1
    PayAction = 2
    DealAction = 3
    OtherAction = 4

class AuthType:
    ClickAuth = 1
    GestureAuth = 2
    FaceAuth = 3
    VoiceAuth = 4


def init(appid, appkey, authid):
    return api(appid, appkey, authid)


class api(object):

    __www = "api"
    __domain = ".yangcong.com"
    __protocol = "https"
    __version = "v2"
    __timeout = False
    __sdkVersion = "3.0"

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

    def __ResponseSignature__(self, json):
        str = ""
        for x in sorted(json.keys()):
            if x != "signature":
                str += "%s=%s" % (x, json[x])
        str += self.appkey
        return md5.new(str).hexdigest()

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

    def getBinding(self, callback=None):
        # 传递参数
        if callback is None or callback == "":
            data = {
                "app_id": self.appid,
                "signature": md5.new("app_id=%s" % (self.appid + self.appkey)).hexdigest()
            }
        else:
            en_callback = urllib.quote_plus(urllib.quote_plus(callback))
            data = {
                "app_id": self.appid,
                "callback": en_callback,
                "signature": md5.new("app_id=%scallback=%s%s" % (self.appid, urllib.quote_plus(callback), self.appkey)).hexdigest()
            }

        # 网络请求
        json_dict = None
        try:
            json_dict = \
                self.__ResponseToJson__(
                    self.__Get__(
                        self.__getUrl("qrcode_for_binding"), data))
        except Exception as e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }

        event_id = json_dict.get("event_id", None)

        if event_id is None:

            if json_dict["status"] == 200:
                raise ParamsException(
                    "server has fail can't not get event_id param")
            else:
                raise ParamsException("api system fail!", json_dict["status"], json_dict["description"])

        en_signature = self.__ResponseSignature__(json_dict)
        is_success = json_dict["status"] == 200 and True or False
        json_dict["success"] = is_success
        if is_success:
            if en_signature != json_dict["signature"]:
                raise SignatureException("signature fail!")

        json_dict["event_id"] = event_id.decode("utf-8")

        # 返回dict结构
        result = RequestCallBack(json_dict)
        self.__timeout = False
        return result

    def getAuth(self, callback=None):
        # 传递参数
        if callback is None or callback == "":
            data = {
                "app_id": self.appid,
                "signature": md5.new("app_id=%s" % (self.appid + self.appkey)).hexdigest()
            }
        else:
            en_callback = urllib.quote_plus(urllib.quote_plus(callback))
            data = {
                "app_id": self.appid,
                "callback": en_callback,
                "signature": md5.new("app_id=%scallback=%s%s" % (self.appid, urllib.quote_plus(callback), self.appkey)).hexdigest()
            }

        # 网络请求
        json_dict = None

        try:
            json_dict = \
                self.__ResponseToJson__(
                    self.__Get__(
                        self.__getUrl("qrcode_for_auth"), data))
        except Exception as e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }

        event_id = json_dict.get("event_id", None)

        if event_id is None:
            if json_dict["status"] == 200:
                raise ParamsException(
                    "server has fail can't not get event_id param")
            else:
                raise ParamsException("api system fail!", json_dict["status"], json_dict["description"])

        en_signature = self.__ResponseSignature__(json_dict)
        is_success = json_dict["status"] == 200 and True or False
        json_dict["success"] = is_success
        if is_success:
            if en_signature != json_dict["signature"]:
                raise SignatureException("signature fail!")

        json_dict["event_id"] = event_id.decode("utf-8")
        # 返回dict结构
        result = RequestCallBack(json_dict)
        self.__timeout = False
        return result

    def getResult(self, uuid):
        if self.__timeout:
            self.__timeout = False
            raise InterfaceTimeoutException(
                "interface timeout. plesae recheck")
        if uuid:
            uuid = uuid.decode("utf-8")
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
            except Exception as e:
                json_dict = {
                    "status": -1,
                    "description": "network has exception"
                }

            en_signature = self.__ResponseSignature__(json_dict)
            is_success = json_dict["status"] == 200 and True or False
            json_dict["success"] = is_success
            if is_success:
                if en_signature != json_dict["signature"]:
                    raise SignatureException("signature fail!")

            # 返回dict结构
            result = RequestCallBack(json_dict)
            code = json_dict["status"]
            if code == 603:
                self.__timeout = True
            return result
        else:
            raise ParamsException(
                "before getResult please call getLoginCode or getBindingCode or verifyOneClick")

    def realtimeAuth(self, action, auth, userid, callback=None, ip=None, username=None):

        if userid == None:
            raise ParamsException("userid can't be 'None'")
        if action == None:
            raise ParamsException("action can't be 'None'")
        if auth == None:
            raise ParamsException("action can't be 'None'")

        if callback == None or callback == "":
            signature = "action_type=%sapp_id=%sauth_type=%suid=%s%s" % (
                action, self.appid, auth, userid, self.appkey)
        elif ip == None or ip == "":
            signature = "action_type=%sapp_id=%sauth_type=%scallback=%suid=%s%s" % (
                action, self.appid, auth, callback,userid, self.appkey)
        else:
            signature = "action_type=%sapp_id=%sauth_type=%scallback=%suser_ip=%suid=%s%s" % (
                action, self.appid, auth, callback, ip, userid, self.appkey)

        data = {
            "action_type" : action,
            "app_id": self.appid,
            "auth_type": auth,
            "uid": userid,
            "signature": md5.new(signature).hexdigest()
        }

        if ip:
            data["user_ip"] = ip

        if username:
            data["username"] = username

        if callback:
            data["callback"] = callback

        # 网络请求

        json_dict = None
        try:
            json_dict = \
                self.__ResponseToJson__(
                    self.__Post__(
                        self.__getUrl("realtime_authorization"), data))
        except Exception as e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }

        event_id = json_dict.get("event_id", None)
        if event_id is None:
            if json_dict["status"] == 200:
                raise ParamsException(
                    "server has fail can't not get event_id param")
            else:
                raise ParamsException("api system fail!", json_dict["status"], json_dict["description"])

        en_signature = self.__ResponseSignature__(json_dict)
        is_success = json_dict["status"] == 200 and True or False
        json_dict["success"] = is_success
        if is_success:
            if en_signature != json_dict["signature"]:
                raise SignatureException("signature fail!")


        json_dict["event_id"] = json_dict["event_id"].decode("utf-8")

        json_dict["success"] = is_success

        # 返回dict结构
        result = RequestCallBack(json_dict)

        self.__timeout = False

        return result

    def offlineAuth(self, userid, dnum):
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
        except Exception as e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }

        en_signature = self.__ResponseSignature__(json_dict)
        is_success = json_dict["status"] == 200 and True or False
        json_dict["success"] = is_success
        if is_success:
            if en_signature != json_dict["signature"]:
                raise SignatureException("signature fail!")

        json_dict["success"] = is_success

        # 返回dict结构
        result = RequestCallBack(json_dict)

        return result

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
                    "status": 200
                }
        except Exception as e:
            json_dict = {
                "status": -1,
                "description": "network has exception"
            }

        json_dict["success"] = (
            json_dict["status"] == 200 and True or False)

        # 返回dict结构
        result = RequestCallBack(json_dict)

        return result
