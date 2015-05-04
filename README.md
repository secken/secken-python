
## yangcong.py

##### RequestCallBack

&emsp;&emsp;&emsp;根据接口返回数据

##### api

&emsp;&emsp;&emsp;洋葱sdk

| Name        | Struct                | Description                     |
| :--------    | :----------------      | :-------------                   |
| [\_\_init\_\_](#__init__) | (appid,appkey,authid) | 传入洋葱提供的appid appkey authid |
| [getBindingCode](#user-content-getBindingCode) | () | 获取绑定的二维码地址 |
| [getLoginCode](#user-content-getLoginCode) | () | 获取登陆二维码 |
| [getResult](#user-content-getResult) | () | 获取结果 |
| [verifyOneClick](#user-content-verifyOneClick) | (userid,action,ip,username) | 验证一键认证 |
| [verifyOTP](#user-content-verifyOTP) | (userid,dnum) | 验证动态码 |
| [authPage](#user-content-authPage) | (callback) | 洋葱授权页 |

<h6 id="getBindingCode">getBindingCode</h6>
&emsp;&emsp;&emsp;获得绑定二维码地址 需要与getResult配合调用
<table>
    <thead>
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
                            <td>如果result.status为0则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>result</td>
                            <td>
                                <table>
                                    <thead>
                                        <tr>
                                            <th align="left">Name</th>
                                            <th align="left">Description</th>
                                        </tr>
                                    </thead>
                                    <tbody>
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
                                                            <td>200</td>
                                                            <td>请求成功</td>
                                                        </tr>
                                                        <tr>
                                                            <td>404</td>
                                                            <td>app不存在</td>
                                                        </tr>
                                                        <tr>
                                                            <td>403</td>
                                                            <td>签名错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>402</td>
                                                            <td>appid错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>400</td>
                                                            <td>参数格式错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>501</td>
                                                            <td>获取二维码失败</td>
                                                        </tr>
                                                        <tr>
                                                            <td>407</td>
                                                            <td>请求接口过于频繁</td>
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
                                            <td>*event_id</td>
                                            <td>请求成功时返回event_id</td>
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
<h6 id="getLoginCode">getLoginCode</h6>
&emsp;&emsp;&emsp;获得登陆二维码地址 需要与getResult配合调用
<table>
    <thead>
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
                            <td>如果result.status为0则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>result</td>
                            <td>
                                <table>
                                    <thead>
                                        <tr>
                                            <th align="left">Name</th>
                                            <th align="left">Description</th>
                                        </tr>
                                    </thead>
                                    <tbody>
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
                                                            <td>200</td>
                                                            <td>请求成功</td>
                                                        </tr>
                                                        <tr>
                                                            <td>404</td>
                                                            <td>app不存在</td>
                                                        </tr>
                                                        <tr>
                                                            <td>403</td>
                                                            <td>签名错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>402</td>
                                                            <td>appid错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>400</td>
                                                            <td>参数格式错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>501</td>
                                                            <td>获取二维码图片失败</td>
                                                        </tr>
                                                        <tr>
                                                            <td>407</td>
                                                            <td>请求接口过于频繁</td>
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
                                            <td>*event_id</td>
                                            <td>请求成功时返回event_id</td>
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

<h6 id="getResult">getResult</h6>
&emsp;&emsp;&emsp;查询UUID事件结果
<table>
    <thead>
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
                            <td>如果result.status为0则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>result</td>
                            <td>
                                <table>
                                    <thead>
                                        <tr>
                                            <th align="left">Name</th>
                                            <th align="left">Description</th>
                                        </tr>
                                    </thead>
                                    <tbody>
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
                                                            <td>200</td>
                                                            <td>请求成功</td>
                                                        </tr>
                                                        <tr>
                                                            <td>404</td>
                                                            <td>app不存在</td>
                                                        </tr>
                                                        <tr>
                                                            <td>403</td>
                                                            <td>签名错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>402</td>
                                                            <td>appid错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>400</td>
                                                            <td>参数格式错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>407</td>
                                                            <td>请求接口过于频繁</td>
                                                        </tr>
                                                        <tr>
                                                            <td>601</td>
                                                            <td>用户拒绝授权验证</td>
                                                        </tr>
                                                        <tr>
                                                            <td>602</td>
                                                            <td>等待用户响应超时，可重试</td>
                                                        </tr>
                                                        <tr>
                                                            <td>603</td>
                                                            <td>用户响应超时，不可重试</td>
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
                                        <tr>
                                            <td>*signature</td>
                                            <td>返回签名：[MD5(uid=$uidapp_key)]
例：uid=aaaa app_key=bbbb MD5(uid=aaaabbbb)</td>
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

<h6 id="verifyOneClick">verifyOneClick</h6>
&emsp;&emsp;&emsp;一键认证需要与getResult配合调用
<table>
    <thead>
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
                            <td>如果result.status为0则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>result</td>
                            <td>
                                <table>
                                    <thead>
                                        <tr>
                                            <th align="left">Name</th>
                                            <th align="left">Description</th>
                                        </tr>
                                    </thead>
                                    <tbody>
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
                                                            <td>200</td>
                                                            <td>请求成功</td>
                                                        </tr>
                                                        <tr>
                                                            <td>604</td>
                                                            <td>用户不存在</td>
                                                        </tr>
                                                        <tr>
                                                            <td>404</td>
                                                            <td>app不存在</td>
                                                        </tr>
                                                        <tr>
                                                            <td>403</td>
                                                            <td>签名错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>400</td>
                                                            <td>参数格式错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>407</td>
                                                            <td>请求接口过于频繁</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>*event_id</td>
                                            <td>返回事件id</td>
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

<h6 id="verifyOTP">verifyOTP</h6>
&emsp;&emsp;&emsp;动态码认证
<table>
    <thead>
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
                            <td>如果result.status为0则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>result</td>
                            <td>
                                <table>
                                    <thead>
                                        <tr>
                                            <th align="left">Name</th>
                                            <th align="left">Description</th>
                                        </tr>
                                    </thead>
                                    <tbody>
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
                                                            <td>200</td>
                                                            <td>请求成功</td>
                                                        </tr>
                                                        <tr>
                                                            <td>500</td>
                                                            <td>洋葱系统服务错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>604</td>
                                                            <td>用户不存在</td>
                                                        </tr>
                                                        <tr>
                                                            <td>404</td>
                                                            <td>app不存在</td>
                                                        </tr>
                                                        <tr>
                                                            <td>403</td>
                                                            <td>签名错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>402</td>
                                                            <td>appkey匹配失败appid匹配失败</td>
                                                        </tr>
                                                        <tr>
                                                            <td>400</td>
                                                            <td>参数格式错误</td>
                                                        </tr>
                                                        <tr>
                                                            <td>407</td>
                                                            <td>请求接口过于频繁</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
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
                            <td>如果result.status为0则为True否则为False</td>
                        </tr>
                        <tr>
                            <td>result</td>
                            <td>
                                <table>
                                    <thead>
                                        <tr>
                                            <th align="left">Name</th>
                                            <th align="left">Description</th>
                                        </tr>
                                    </thead>
                                    <tbody>
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
                                            <td>
                                                当code不为0时返回错误信息
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>*url</td>
                                            <td>当请求成功时返回授权页地址</td>
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

