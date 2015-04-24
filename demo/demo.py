# coding=u8
import sys
sys.path.append("..")

# import sdk.yangcong.api as yc
from sdk.yangcong import api as yangcong

# 官方测试AppId
__appid = "sBhl0JlvYRgl5pavOMredpVqY8XZruZR"

# 官方测试AppKey
__appkey = "0bZKeXF1VYDrP8GI99lj"

# 官方测试AuthId
__authid = "8JFOz3jUoSeiBYq6Lp8g"

yangcongApi = yangcong(__appid, __appkey, __authid)

import web
import json

urls = (
    "/bind", "Bind",
    "/result", "Result",
    "/loginCode", "LoginCode",
    "/verifyOneClick", "VerifyOneClick",
    "/verifyOTP","VerifyOTP"
)

app = web.application(urls, globals())
render = web.template.render('templates')

class VerifyOTP(object):

    def GET(self):
        userid = web.input().userid
        dnum = web.input().dnum

        result = yangcongApi.verifyOTP(userid, dnum)
        return json.dumps(result.result.getDictStruct())

class VerifyOneClick(object):

    def GET(self):
        userid = web.input().userid
        action = web.input().action

        result = yangcongApi.verifyOneClick(userid, action)
        return json.dumps(result.result.getDictStruct())


class LoginCode(object):

    def GET(self):
        result = yangcongApi.getLoginCode()
        return json.dumps(result.result.getDictStruct())


class Result:

    def GET(self):
        uuid = web.input().uuid
        result = {
            "code": 300060,
            "message": "params error"
        }
        if uuid:
            result = yangcongApi.getResult(uuid)
            return json.dumps(result.result.getDictStruct())
        else:
            return json.dumps(result)


class Bind:

    def GET(self):

        code = yangcongApi.getBindingCode()

        # 当返回状态正确时
        if code.success:
            return render.bind(code.result.url, code.result.uuid)
        else:
            return render.error(code.result.code, code.result.message)


def main():
    app.run()

if __name__ == '__main__':
    main()
