// ==UserScript==
// @name         网易音乐收藏器
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  collect music with one button
// @author       with
// @match        https://music.163.com/
// @icon         https://www.google.com/s2/favicons?domain=163.com
// @grant        none
// ==/UserScript==
(function() {
    'use strict';

    // Your code here..
    console.log('我的脚本加载了');
    var button1 = document.createElement("button"); //创建一个input对象（提示框按钮）
    button1.id = "id001";
    button1.textContent = "日";
    button1.style.width = "20px";
    button1.style.height = "20px";
    button1.style.align = "center";

    var button2 = document.createElement("button"); //创建一个input对象（提示框按钮）
    button2.id = "id002";
    button2.textContent = "纯";
    button2.style.width = "20px";
    button2.style.height = "20px";
    button2.style.align = "center";

    var button3 = document.createElement("button"); //创建一个input对象（提示框按钮）
    button3.id = "id003";
    button3.textContent = "华";
    button3.style.width = "20px";
    button3.style.height = "20px";
    button3.style.align = "center";

    var button4 = document.createElement("button"); //创建一个input对象（提示框按钮）
    button4.id = "id003";
    button4.textContent = "欧";
    button4.style.width = "20px";
    button4.style.height = "20px";
    button4.style.align = "center";

    function simple(){
        console.log('collected')
    }

    //绑定按键点击功能
    button1.onclick = function (){
        console.log('日语收藏');
        document.getElementsByClassName('icn icn-add j-flag')[0].click()
        setTimeout(simple(),1000)
        var f=document.getElementById('g_iframe').contentDocument
        f.evaluate(".//li[@data-id=992803120]",f).iterateNext().click()
        document.getElementsByClassName('icn icn-list s-fc3')[0].click()
        return;
    };

    button2.onclick = function (){
        console.log('纯音乐收藏');
        document.getElementsByClassName('icn icn-add j-flag')[0].click()
        setTimeout(simple(),1000)
        var f=document.getElementById('g_iframe').contentDocument
        f.evaluate(".//li[@data-id=992929247]",f).iterateNext().click()
        document.getElementsByClassName('icn icn-list s-fc3')[0].click()
        return;
    };

    button3.onclick = function (){
        console.log('华语收藏');
        document.getElementsByClassName('icn icn-add j-flag')[0].click()
        setTimeout(simple(),1000)
        var f=document.getElementById('g_iframe').contentDocument
        f.evaluate(".//li[@data-id=992846395]",f).iterateNext().click()
        document.getElementsByClassName('icn icn-list s-fc3')[0].click()
        return;
    };

    button4.onclick = function (){
        console.log('欧洲语言');
        document.getElementsByClassName('icn icn-add j-flag')[0].click()
        setTimeout(simple(),1000)
        var f=document.getElementById('g_iframe').contentDocument
        f.evaluate(".//li[@data-id=992958658]",f).iterateNext().click()
        document.getElementsByClassName('icn icn-list s-fc3')[0].click()
        return;
    };
    var x = document.getElementsByClassName('bg')[0];
    x.appendChild(button1);
    x.appendChild(button2);
    x.appendChild(button3);
    x.appendChild(button4);
})();
