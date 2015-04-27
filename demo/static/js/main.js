userid = null
bind = false

function getResult(element, msg) {
    $.getJSON("result", function(result) {
        console.log(result);
        if (result.code == 0) {
            $(element).html(msg);
            $(element).css({
                "color": "green"
            });

            if (!bind) {
                userid = result.userid;
                bindingSuccess();
                bind = true;
            }
            return;
        } else {
            setTimeout(getResult(element, msg), 2000);
        }
    });
}

function bindingSuccess() {
    $.getJSON("loginCode", function(result) {
        //拿到登陆qr码
        $("#qrCodeLogin").attr("src", result.url);
        //显示页面逻辑
        $($(".middle")[1]).show();
        getResult($($(".middle")[1]).find("h5")[0], "登陆成功！");
    });
}

function clickLogin() {
    $.getJSON("verifyOneClick", {
        userid: userid,
        action: "test"
    }, function(result) {
        console.log(result)
        getResult($($(".middle")[1]).find("h5")[1], "登陆成功！");
    });
}

function dnumLogin() {
    $.getJSON("verifyOTP", {
        userid: userid,
        dnum: $("#dnum").val()
    }, function(result) {
        if (result.code == 0) {
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

getResult($($(".middle")[0]).find("h5"), "绑定成功！");