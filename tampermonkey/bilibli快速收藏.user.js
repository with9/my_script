// ==UserScript==
// @name         bilibli快速收藏
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  bilibili collects
// @author       With
// @match        https://www.bilibili.com/medialist/*
// @icon         https://www.google.com/s2/favicons?domain=bilibili.com
// @grant        none
// ==/UserScript==
//@require https://gist.github.com/raw/2625891/waitForKeyElements.js
/* globals jQuery, $, waitForKeyElements */
(function() {
    'use strict';

    console.log('我的脚本加载了');


    var div1 = document.createElement('div')
    div1.id = 'div001'
    div1.style="position:absolute;z-index:999"
    document.getElementsByTagName('body')[0].appendChild(div1)

    function buildButton(bid,buttonText){
        var button1 = document.createElement("button"); //创建一个input对象（提示框按钮）
        button1.id = bid;
        button1.textContent = buttonText;
        //button1.style.width = "20px";
        //button1.style.height = "26px";
        button1.style="line-height: 15px;";
        button1.style.align = "center";
        return button1;

    }
    let button1=buildButton('b001','music');
    let button2=buildButton('b002','study');
    let button3=buildButton('b003','best');


    function sleep (time) {
        return new Promise((resolve) => setTimeout(resolve, time));
    }

    function get_index(name){
        //获得对应收藏夹的索引
        let collects=document.getElementsByClassName("group-list")[0];
        let lists=collects.getElementsByTagName('li');
        let title;
        for(let i=0;i<lists.length;i++){
            title=lists[i].getElementsByClassName('fav-title')[0].innerText;
            if(name===title){
                console.log(i)
                return i;
            }
        }
    }



    //绑定按键点击功能
    button1.onclick = async function (){
        document.getElementsByClassName('collect on')[0].click()
        await sleep(800);
        var ind=get_index('music');
        console.log(ind)
        var check=document.getElementsByClassName('group-list')[0].getElementsByTagName('input')[ind]
        if(!check.checked){
            check.click()
            await sleep(100);
            document.getElementsByClassName('btn submit-move')[0].click();
        }
        else{
            document.getElementsByClassName('close')[0].click();
        }

    }


    button2.onclick = async function (){
        document.getElementsByClassName('collect on')[0].click()
        await sleep(800);
        var ind=get_index('study');
        console.log(ind)
        var check=document.getElementsByClassName('group-list')[0].getElementsByTagName('input')[ind]
        if(!check.checked){
            check.click()
            await sleep(100);
            document.getElementsByClassName('btn submit-move')[0].click();
        }
        else{
            document.getElementsByClassName('close')[0].click();
        }

    }
    button3.onclick = async function (){
        document.getElementsByClassName('collect on')[0].click()
        await sleep(800);
        var ind=get_index('best');
        console.log(ind)
        var check=document.getElementsByClassName('group-list')[0].getElementsByTagName('input')[ind]
        if(!check.checked){
            check.click()
            await sleep(100);
            document.getElementsByClassName('btn submit-move')[0].click();
        }
        else{
            document.getElementsByClassName('close')[0].click();
        }

    }

    let x = document.getElementsByClassName("video-data")[0]
    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    x.appendChild(button1);
    x.appendChild(button2);
    x.appendChild(button3);
})();