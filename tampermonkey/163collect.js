// ==UserScript==
// @name         网易音乐收藏器
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  collect music with one button
// @author       with
// @match        https://music.163.com/
// @icon         https://s1.music.126.net/style/favicon.ico
// @grant        none
// ==/UserScript==
(function() {
    'use strict';

    // Your code here..
    console.log('我的脚本加载了');

    var div1 = document.createElement('div')
    div1.id = 'div001'
    div1.style="position:absolute;z-index:999"
    document.getElementsByTagName('body')[0].appendChild(div1)

    var button1 = document.createElement("button"); //创建一个input对象（提示框按钮）
    button1.id = "id001";
    button1.textContent = "日语";
    button1.style.width = "60px";
    button1.style.height = "40px";
    button1.style.align = "center";

    var button2 = document.createElement("button"); //创建一个input对象（提示框按钮）
    button2.id = "id002";
    button2.textContent = "纯音乐";
    button2.style.width = "60px";
    button2.style.height = "40px";
    button2.style.align = "center";

    var button3 = document.createElement("button"); //创建一个input对象（提示框按钮）
    button3.id = "id003";
    button3.textContent = "华语";
    button3.style.width = "60px";
    button3.style.height = "40px";
    button3.style.align = "center";

    var button4 = document.createElement("button"); //创建一个input对象（提示框按钮）
    button4.id = "id004";
    button4.textContent = "欧洲语言";
    button4.style.width = "60px";
    button4.style.height = "40px";
    button4.style.align = "center";

    var button5 = document.createElement("button"); //创建一个input对象（提示框按钮）
    button5.id = "id005";
    button5.textContent = "2listen";
    button5.style.width = "60px";
    button5.style.height = "40px";
    button5.style.align = "center";
    function simple(){
        console.log('collected')
    }

    //绑定按键点击功能
    button1.onclick = function (){
        console.log('日语收藏');
        //为所欲为 功能实现处
        document.getElementsByClassName('icn icn-add j-flag')[0].click()
        setTimeout(simple(),1000)
        var f=document.getElementById('g_iframe').contentDocument
        f.evaluate(".//li[@data-id=992803120]",f).iterateNext().click()
        setTimeout(simple(),1000)
        //document.getElementsByClassName('nxt')[0].click()
        return;
    };

    button2.onclick = function (){
        console.log('纯音乐收藏');
        //为所欲为 功能实现处
        document.getElementsByClassName('icn icn-add j-flag')[0].click()
        setTimeout(simple(),1000)
        var f=document.getElementById('g_iframe').contentDocument
        f.evaluate(".//li[@data-id=992929247]",f).iterateNext().click()
        setTimeout(simple(),1000)
        //document.getElementsByClassName('nxt')[0].click()
        return;
    };

    button3.onclick = function (){
        console.log('华语收藏');
        //为所欲为 功能实现处
        document.getElementsByClassName('icn icn-add j-flag')[0].click()
        setTimeout(simple(),1000)
        var f=document.getElementById('g_iframe').contentDocument
        f.evaluate(".//li[@data-id=992846395]",f).iterateNext().click()
        setTimeout(simple(),1000)
        //document.getElementsByClassName('nxt')[0].click()
        return;
    };

    button4.onclick = function (){
        console.log('欧洲语言');
        //为所欲为 功能实现处
        document.getElementsByClassName('icn icn-add j-flag')[0].click()
        setTimeout(simple(),1000)
        var f=document.getElementById('g_iframe').contentDocument
        f.evaluate(".//li[@data-id=992958658]",f).iterateNext().click()
        setTimeout(simple(),1000)
        //document.getElementsByClassName('nxt')[0].click()
        return;
    };

    button5.onclick = function (){
        console.log('2listen');
        //为所欲为 功能实现处
        document.getElementsByClassName('icn icn-add j-flag')[0].click()
        setTimeout(simple(),1000)
        var f=document.getElementById('g_iframe').contentDocument
        f.evaluate(".//li[@data-id=3062682750]",f).iterateNext().click()
        setTimeout(simple(),1000)
        //document.getElementsByClassName('nxt')[0].click()
        return;
    };
    var x = document.getElementById('div001')
    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    x.appendChild(button1);
    x.appendChild(button2);
    x.appendChild(button3);
    x.appendChild(button4);
    x.appendChild(button5);
    //var y = document.getElementById('s_btn_wr');
    //y.appendChild(button);
})();