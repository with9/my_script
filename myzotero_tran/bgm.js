{
	"translatorID": "54bf451f-6e73-44f7-8d04-86989ff310b4",
	"label": "bgm",
	"creator": "with",
	"target": "https?://bgm.tv/",
	"minVersion": "3.0",
	"maxVersion": "",
	"priority": 100,
	"inRepository": true,
	"translatorType": 4,
	"browserSupport": "gcsibv",
	"lastUpdated": "2021-08-02 03:06:44"
}

/*
	***** BEGIN LICENSE BLOCK *****

	Copyright © 2020 with
	
	This file is part of Zotero.

	Zotero is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	Zotero is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	GNU Affero General Public License for more details.

	You should have received a copy of the GNU Affero General Public License
	along with Zotero. If not, see <http://www.gnu.org/licenses/>.

	***** END LICENSE BLOCK *****
*/


function detectWeb(doc, url) {
	// TODO: adjust the logic here
	var a=doc.evaluate('//a[@class="focus chl anime"]', doc).iterateNext();
	if (a != null) {
		return "film";
	}
	return false;
}

function getSearchResults(doc, checkOnly) {
	var items = {};
	var found = false;
	// TODO: adjust the CSS selector
	var rows = doc.querySelectorAll('h2>a.title[href*="/article/"]');
	for (let row of rows) {
		// TODO: check and maybe adjust
		let href = row.href;
		// TODO: check and maybe adjust
		let title = ZU.trimInternal(row.textContent);
		if (!href || !title) continue;
		if (checkOnly) return true;
		found = true;
		items[href] = title;
	}
	return found ? items : false;
}

function doWeb(doc, url) {
	if (detectWeb(doc, url) == "multiple") {
		Zotero.selectItems(getSearchResults(doc, false), function (items) {
			if (items) ZU.processDocuments(Object.keys(items), scrape);
		});
	}
	else {
		scrape(doc, url);
	}
}

function scrape(doc, url) {
	var newItem = new Zotero.Item("film");
	var b =doc.getElementById('infobox').getElementsByTagName('li');
	var summary=doc.getElementById('subject_summary');
	var tags=doc.getElementsByClassName('subject_tag_section')[0].getElementsByTagName('a');
	var notes='<h2>infobox</h2>';
	notes=notes.concat(doc.getElementById('infobox').innerHTML);
	for(var i=0;i<b.length;i++){
	//     console.log(b[i]);
		if(b[i].innerText.indexOf('原作') != -1){
			newItem.creators.push({
			lastName: b[i].innerText.split(':')[1],
			creatorType: "scriptwriter",
			fieldMode: 1
		});
		}
		else if(b[i].innerText.indexOf('导演') != -1){
			newItem.creators.push({
			lastName: b[i].innerText.split(':')[1],
			creatorType: "author",
			fieldMode: 2
		});
		}
		else if(b[i].innerText.indexOf('放送开始') != -1){
			newItem.date=ZU.strToISO(b[i].innerText.split(':')[1]);
			
		}
		else if(b[i].innerText.indexOf('发售日') != -1){
			newItem.date=ZU.strToISO(b[i].innerText.split(':')[1]);
			
		}
		else if(b[i].innerText.indexOf('上映年度') != -1){
			newItem.date=ZU.strToISO(b[i].innerText.split(':')[1]);
			
		}
		else if(b[i].innerText.indexOf('话数') != -1){
			newItem.numberOfVolumes=Number(b[i].innerText.split(':')[1]);
		}
		else if(b[i].innerText.indexOf('中文名') != -1){
			var title=b[i].innerText.split(':')[1];
		}
		else if(b[i].innerText.indexOf('Copyright') != -1){
			newItem.rights=b[i].innerText.split(':')[1];
		}
	}
	if(summary != null){
		newItem.abstractNote=summary.innerText;
	}
	if(tags != null){
		for(i of tags){
			t_name=i.innerText.split(' ')[0];
			newItem.tags.push({tag: t_name});
		}
	}
	if(title == null){
		title=doc.title.split('|')[0];
		
	}
	newItem.tags.push({tag: 'bgm'})
	newItem.title=title;
	newItem.notes=notes;
	newItem.libraryCatalog='动画';
	newItem.url=url;
	newItem.attachments = [{
	url: url,
	title: title,
	mimeType: "text/html",
	snapshot: true
	}];
	newItem.complete();
}



/** BEGIN TEST CASES **/
var testCases = [
	{
		"type": "web",
		"url": "https://bgm.tv/subject/297969",
		"items": [
			{
				"itemType": "tvBroadcast",
				"title": "寒蝉鸣泣之时 业",
				"creators": [
					{
						"lastName": " 竜騎士07／07th Expansion",
						"creatorType": "author",
						"fieldMode": 1
					}
				],
				"date": "2020-10-01",
				"abstractNote": "远离城市中心，被浓郁的自然环境所环绕的村落——雏见泽村。\n原本早在过去就要沉入大坝底部的这个村落，如今仍然以同从前别无二致的景色，迎来了转学生·前原圭一。\n对于以前一直住在都市里的圭一而言，和雏见泽的同伴共度的热闹而平和的生活，本该是永远持续下去的幸福时光。\n一年一度举行的村中祭典，绵流。直到这一天到来为止……\n昭和五十八年，六月。寒蝉鸣泣之时。\n日常突然宣告结束，无止境的惨剧连锁开始了——",
				"libraryCatalog": "动画",
				"attachments": [],
				"tags": [
					{
						"tag": "2020"
					},
					{
						"tag": "2020年"
					},
					{
						"tag": "2020年10月"
					},
					{
						"tag": "2020年7月"
					},
					{
						"tag": "GAL改"
					},
					{
						"tag": "Passione"
					},
					{
						"tag": "TV"
					},
					{
						"tag": "bgm"
					},
					{
						"tag": "パッショーネ"
					},
					{
						"tag": "中原麻衣"
					},
					{
						"tag": "久弥直樹"
					},
					{
						"tag": "半年番"
					},
					{
						"tag": "原创"
					},
					{
						"tag": "堀江由衣"
					},
					{
						"tag": "寒蝉鸣泣之时"
					},
					{
						"tag": "川口敬一郎"
					},
					{
						"tag": "悬疑"
					},
					{
						"tag": "惊悚"
					},
					{
						"tag": "推理"
					},
					{
						"tag": "日本动画"
					},
					{
						"tag": "未定档"
					},
					{
						"tag": "渡辺明夫"
					},
					{
						"tag": "游戏改"
					},
					{
						"tag": "猎奇"
					},
					{
						"tag": "田村ゆかり"
					},
					{
						"tag": "病娇"
					},
					{
						"tag": "百合"
					},
					{
						"tag": "续作"
					},
					{
						"tag": "血腥"
					},
					{
						"tag": "轮回"
					},
					{
						"tag": "龙骑士07"
					}
				],
				"notes": [
					"infobox\n中文名: 寒蝉鸣泣之时 业\n话数: 24\n放送开始: 2020年10月1日\n放送星期: 星期四\n原作: 竜騎士07／07th Expansion\n导演: 川口敬一郎\n脚本: 川口敬一郎、久弥直樹\n分镜: 川口敬一郎、佐野隆史、杉島邦久、石黒達也、高橋丈夫\n演出: 浅利藤彰、さんぺい聖、龍輪直征、池端隆史、中村近世\n音乐: 川井憲次\n人物设定: 渡辺明夫、副：岩崎たいすけ、水上ろんど、植田和幸、川村幸祐、中平凱、蟄居太、森川侑紀\n系列构成: ハヤシナオキ(久弥直樹)\n美术监督: 井上一宏\n色彩设计: 小松亜理沙\n总作画监督: 橋本英樹、古川英樹、近藤源一郎、岩崎たいすけ、植田和幸、渡辺明夫、水上ろんど\n作画监督: 柳沢まさひで、成松義人、佐々木洋也、服部憲知、清水麻美、田守優希、海堂ヒロユキ、伊集院いづろ、小林史緒里、島崎望、石原恵治、岩崎たいすけ\n摄影监督: 戸澤雄一郎\n道具设计: 中平凱、福島達也\n原画: 龍輪直征、岩崎たいすけ、鈴木勘太、菊池勉、森川侑紀、荒木裕\n剪辑: 丹彩子\n主题歌编曲: 悠木真一、Tak Miyazawa\n主题歌作曲: 志倉千代丸\n主题歌作词: 志倉千代丸\n主题歌演出: 彩音、亜咲花\n企画: 菊池剛、志倉千代丸、難波秀行、工藤大丈\n製作: KADOKAWA、MAGES.、創通\n音响监督: 森下広人\n音效: 八十正太\n制片人: 西藤和広\n制作: インフィニット、永谷敬之\n音乐制作: フロンティアワークス\n动画制作: パッショーネ\n副导演: 池端隆史\nOP・ED 分镜: 高橋丈夫、小川優樹\n别名: 秋蝉鸣泣之时 业\n暮蝉悲鸣时 业\nhigurashi no naku koro ni gou\nWhen They Cry gou\n官方网站: https://higurashianime.com\n播放电视台: TOKYO MX\n其他电视台: BS11 / サンテレビ / AT-X\nCopyright: ©2020竜騎士07／ひぐらしのなく頃に製作委員会\n"
				],
				"seeAlso": []
			}
		]
	},
	{
		"type": "web",
		"url": "https://bgm.tv/subject/90518",
		"items": [
			{
				"itemType": "tvBroadcast",
				"title": "寒蝉鸣泣之时",
				"creators": [],
				"libraryCatalog": "bgm",
				"attachments": [],
				"tags": [],
				"notes": [],
				"seeAlso": []
			}
		]
	}
]
/** END TEST CASES **/
