userid = null;
bind = false;

function getResult(uuid, element, msg) {
    $.getJSON("result", {
        uuid: uuid
    }, function(result) {
        console.log(result);
        if (result.status == 200) {
            $(element).html(msg);
            $(element).css({
                "color": "green"
            });

            if (!bind) {
                
                userid = result.uid;
                bindingSuccess();
                bind = true;
            }
            return;
        } else {
            setTimeout(getResult(uuid, element, msg), 2000);
        }
    });
}

function bindingSuccess() {
    $.getJSON("loginCode", function(result) {
        //拿到登陆qr码
        $("#qrCodeLogin").attr("src", result.qrcode_url);
        //显示页面逻辑
        $($(".middle")[1]).show();
        getResult(result.event_id, $($(".middle")[1]).find("h5")[0], "登陆成功！");
    });
}

function clickLogin() {
    $.getJSON("verifyOneClick", {
        userid: userid,
        action: "test"
    }, function(result) {
        console.log(result)
        getResult(result.event_id, $($(".middle")[1]).find("h5")[1], "登陆成功！");
    });
}

function dnumLogin() {
    $.getJSON("verifyOTP", {
        userid: userid,
        dnum: $("#dnum").val()
    }, function(result) {
        if (result.status == 200) {
            $($($(".middle")[1]).find("h5")[2]).html("登陆成功！");
            $($($(".middle")[1]).find("h5")[2]).css({
                "color": "green"
            });
        } else {
            $($($(".middle")[1]).find("h5")[2]).html("动态码错误！");
            $($($(".middle")[1]).find("h5")[2]).css({
                "color": "red"
            });
        }
    });
}

getResult(uuid, $($(".middle")[0]).find("h5"), "绑定成功！");