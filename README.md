####Attention

Python Version : 3.0

#### Examples

###### getBinding
>```python
>import secken
>
>seckenApi = secken.init(appkey,appid,authid)
>
>result = seckenApi.getBinding()
>if result.success:
>    # 返回二维码地址
>    return result.qrcode_url
>
>```

###### getAuth
>```python
>import secken
>
>seckenApi = secken.init(appkey,appid,authid)
>
>result = seckenApi.getAuth()
>if result.success:
>    # 返回二维码地址
>    return result.qrcode_url
>
>```

###### realtimeAuth
>```python
>import secken
>
>seckenApi = secken.init(appkey,appid,authid)
>
>result = seckenApi.realtimeAuth(
>         ActionType.LoginAction, AuthType.GestureAuth, userid)
>if result.success:
>    # 返回事件ID
>    return result.event_id
>
>```

#### Api Document


#### Exception:

> - ParamsException 参数错误
> - InterfaceTimeoutException 接口超时
> - SignatureException 签名异常

#### Class:

##### RequestCallBack

> - 根据接口返回数据

##### ActionType

> - 在线验证动作
> - LoginAction 登陆动作
> - PayAction 支付动作
> - DealAction 交易动作
> - OtherAction 其他动作

##### AuthType

> - 验证类型
> - ClickAuth 单击验证
> - GestureAuth 手势验证
> - FaceAuth 人脸验证
> - VoiceAuth 声音验证

##### api

&emsp;&emsp;&emsp;洋葱sdk secken.init(appkey,appid,authid) 初始化验证并返回api类

| Name        | Struct                | Description                     |
| :--------    | :----------------      | :-------------                   |
| [\_\_init\_\_](#__init__) | (appid,appkey,authid) | 传入洋葱提供的appid appkey authid |
| [getBinding](#user-content-getBindingCode) | (\*callback) | 获取绑定的二维码地址 |
| [getAuth](#user-content-getLoginCode) | (\*callback) | 获取登陆二维码 |
| [getResult](#user-content-getResult) | (event_id) | 获取结果 |
| [realtimeAuth](#user-content-verifyOneClick) | (action,auth,userid,\*callback,\*ip,\*username) | 验证一键认证 |
| [offlineAuth](#user-content-verifyOTP) | (uid,dynamic_code) | 验证动态码 |
| [authPage](#user-content-authPage) | (callback) | 洋葱授权页 |
<h6 id="getBindingCode">getBindingCode</h6>
&emsp;&emsp;&emsp;获得绑定二维码地址 需要与getResult配合调用
<table>
    <thead>
        <tr>
            <th colspan="2" align="left">Request</th>
        </tr>
        <tr>
            <th align="left">*callback</th>
            <td>回调地址，调用成功后洋葱服务器会请求该地址，具体请查看<a href="http://www.yangcong.com/api">官方文档</a></td>
        </tr>
        <tr>
            <th colspan="2" align="left">Return</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th align="left">RequestCallBack</th>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th align="left">Name</th>
                            <th align="left">Description</th>
                        </tr>
                        <tr>
                            <td>success</td>
                            <td>如果result.status为200时则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>status</td>
                            <td>
                                返回状态码:
                                <table>
                                    <tbody>
                                        <tr>
                                            <td>-1</td>
                                            <td>网络异常</td>
                                        </tr>
                                        <tr>
                                            <td>501</td>
                                            <td>生成二维码图像失败</td>
                                        </tr>
                                        <tr>
                                        <td colspan="2"><a href="https://www.yangcong.com/api">查看公共错误码</a></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td>description</td>
                            <td>状态信息</td>
                        </tr>
                        <tr>
                            <td>*qrcode_url</td>
                            <td>请求成功时返回二维码地址</td>
                        </tr>
                        <tr>
                            <td>*qrcode_data</td>
                            <td>请求成功时返回二维码内容，可自己生成</td>
                        </tr>
                        <tr>
                            <td>*event_id</td>
                            <td>请求成功时返回event_id</td>
                        </tr>
                    </thead>
                </table>
            </td>
        </tr>
    </tbody>
</table>
<h6 id="getLoginCode">getAuth</h6>
&emsp;&emsp;&emsp;获得登陆二维码地址 需要与getResult配合调用
<table>
    <thead>
        <tr>
            <th colspan="2" align="left">Request</th>
        </tr>
        <tr>
            <th align="left">*callback</th>
            <td>回调地址，调用成功后洋葱服务器会请求该地址，具体请查看<a href="http://www.yangcong.com/api">官方文档</a></td>
        </tr>
        <tr>
            <th colspan="2" align="left">Return</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th align="left">RequestCallBack</th>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th align="left">Name</th>
                            <th align="left">Description</th>
                        </tr>
                        <tr>
                            <td>success</td>
                            <td>如果result.status为200时则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>status</td>
                            <td>
                                返回状态码:
                                <table>
                                    <tbody>
                                        <tr>
                                            <td>-1</td>
                                            <td>网络异常</td>
                                        </tr>
                                        <tr>
                                            <td>501</td>
                                            <td>生成二维码图像失败</td>
                                        </tr>
                                        <tr>
                                        <td colspan="2"><a href="https://www.yangcong.com/api">查看公共错误码</a></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td>description</td>
                            <td>状态信息</td>
                        </tr>
                        <tr>
                            <td>*qrcode_url</td>
                            <td>请求成功时返回二维码地址</td>
                        </tr>
                        <tr>
                            <td>*qrcode_data</td>
                            <td>请求成功时返回二维码内容，可自己生成</td>
                        </tr>
                        <tr>
                            <td>*event_id</td>
                            <td>请求成功时返回event_id</td>
                        </tr>
                    </thead>
                </table>
            </td>
        </tr>
    </tbody>
</table>

<h6 id="getResult">getResult</h6>
&emsp;&emsp;&emsp;查询UUID事件结果
<table>
    <thead>
        <tr>
            <th colspan="2" align="left">Request</th>
        </tr>
        <tr>
            <th align="left">event_id</th>
            <td>事件ID，具体请查看<a href="http://www.yangcong.com/api">官方文档</a></td>
        </tr>
        <tr>
            <th colspan="2" align="left">Return</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th align="left">RequestCallBack</th>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th align="left">Name</th>
                            <th align="left">Description</th>
                        </tr>
                        <tr>
                            <td>success</td>
                            <td>如果result.status为200时则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>status</td>
                            <td>
                                返回状态码:
                                <table>
                                    <tbody>
                                        <tr>
                                            <td>-1</td>
                                            <td>网络异常</td>
                                        </tr>
                                        <tr>
                                            <td>601</td>
                                            <td>用户拒绝授权</td>
                                        </tr>
                                        <tr>
                                            <td>602</td>
                                            <td>等待用户响应，可重试</td>
                                        </tr>
                                        <tr>
                                            <td>603</td>
                                            <td>用户响应超时，不可重试，事件超时</td>
                                        </tr>
                                        <tr>
                                            <td>604</td>
                                            <td>event_id 不存在</td>
                                        </tr>
                                        <tr>
                                        <td colspan="2"><a href="https://www.yangcong.com/api">查看公共错误码</a></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td>description</td>
                            <td>状态信息</td>
                        </tr>
                        <tr>
                            <td>*uid</td>
                            <td>返回用户ID</td>
                        </tr>
                    </thead>
                </table>
            </td>
        </tr>
    </tbody>
</table>

<h6 id="verifyOneClick">realtimeAuth</h6>
&emsp;&emsp;&emsp;一键认证需要与getResult配合调用
<table>
    <thead>
        <tr>
            <th colspan="2" align="left">Request</th>
        </tr>
        <tr>
            <th align="left">action</th>
            <td>动作，详见ActionType类</td>
        </tr>
        <tr>
            <th align="left">auth</th>
            <td>验证方法，详见AuthType类</td>
        </tr>
        <tr>
            <th align="left">userid</th>
            <td>洋葱返回的userid</td>
        </tr>
        <tr>
            <th align="left">*callback</th>
            <td>回调地址，调用成功后洋葱服务器会请求该地址，具体请查看<a href="http://www.yangcong.com/api">官方文档</a></td>
        </tr>
        <tr>
            <th align="left">*ip</th>
            <td>客户ip</td>
        </tr>
        <tr>
            <th align="left">*username</th>
            <td>用户名称</td>
        </tr>
        <tr>
            <th colspan="2" align="left">Return</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th align="left">RequestCallBack</th>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th align="left">Name</th>
                            <th align="left">Description</th>
                        </tr>
                        <tr>
                            <td>success</td>
                            <td>如果result.status为200时则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>status</td>
                            <td>
                                返回状态码:
                                <table>
                                    <tbody>
                                        <tr>
                                            <td>-1</td>
                                            <td>网络异常</td>
                                        </tr>
                                        <tr>
                                            <td>604</td>
                                            <td>用户不存在</td>
                                        </tr>
                                        <tr>
                                            <td>605</td>
                                            <td>用户未开启该类型验证</td>
                                        </tr>
                                        <tr>
                                        <td colspan="2"><a href="https://www.yangcong.com/api">查看公共错误码</a></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td>description</td>
                            <td>状态信息</td>
                        </tr>
                        <tr>
                            <td>*event_id</td>
                            <td>返回事件id</td>
                        </tr>
                    </thead>
                </table>
            </td>
        </tr>
    </tbody>
</table>

<h6 id="verifyOTP">offlineAuth</h6>
&emsp;&emsp;&emsp;动态码认证
<table>
    <thead>
        <tr>
            <th colspan="2" align="left">Request</th>
        </tr>
        <tr>
            <th align="left">uid</th>
            <td>uid洋葱返回的uid</td>
        </tr>
        <tr>
            <th align="left">dynamic_code</th>
            <td>洋葱的6位动态验证码</td>
        </tr>
        <tr>
            <th colspan="2" align="left">Return</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th align="left">RequestCallBack</th>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th align="left">Name</th>
                            <th align="left">Description</th>
                        </tr>
                        <tr>
                            <td>success</td>
                            <td>如果result.status为200时则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>status</td>
                            <td>
                                返回状态码:
                                <table>
                                    <tbody>
                                        <tr>
                                            <td>-1</td>
                                            <td>网络异常</td>
                                        </tr>
                                        <tr>
                                            <td>600</td>
                                            <td>动态吗验证失败</td>
                                        </tr>
                                        <tr>
                                            <td>604</td>
                                            <td>用户不存在</td>
                                        </tr>
                                        <tr>
                                        <td colspan="2"><a href="https://www.yangcong.com/api">查看公共错误码</a></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </thead>
                </table>
            </td>
        </tr>
    </tbody>
</table>

<h6 id="authPage">authPage</h6>
&emsp;&emsp;&emsp;洋葱授权页
<table>
    <thead>
        <tr>
            <th colspan="2" align="left">Request</th>
        </tr>
        <tr>
            <th align="left">callback</th>
            <td>授权的回调地址</td>
        </tr>
        <tr>
            <th colspan="2" align="left">Return</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th align="left">RequestCallBack</th>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th align="left">Name</th>
                            <th align="left">Description</th>
                        </tr>
                        <tr>
                            <td>success</td>
                            <td>如果result.status为200时则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>code</td>
                            <td>
                                返回状态码:
                                <table>
                                    <tbody>
                                        <tr>
                                            <td>-1</td>
                                            <td>网络异常</td>
                                        </tr>
                                        <tr>
                                            <td>200</td>
                                            <td>请求成功</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td>*message</td>
                            <td>当code不为200时返回错误信息</td>
                        </tr>
                        <tr>
                            <td>*url</td>
                            <td>当请求成功时返回授权页地址</td>
                        </tr>
                    </thead>
                </table>
            </td>
        </tr>
    </tbody>
</table>