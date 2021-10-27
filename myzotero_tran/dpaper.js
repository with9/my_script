{
	"translatorID": "78ba8722-6748-47f4-9976-8985d75a220c",
	"label": "dpaper",
	"creator": "with",
	"target": "http://dpaper.las.ac.cn",
	"minVersion": "3.0",
	"maxVersion": "",
	"priority": 100,
	"inRepository": true,
	"translatorType": 4,
	"browserSupport": "gcsibv",
	"lastUpdated": "2021-10-28 09:30:08"
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
	var a=doc.evaluate('//span[@id="education"]',doc).iterateNext().textContent
	if (a!=null){
		return "thesis"
	}
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



function scrape(doc,url){
	if (detectWeb(doc,url)=="thesis"){
		var newItem=new Zotero.Item('thesis');
		var title=doc.evaluate('//h2[@id="title_cn"]',doc).iterateNext().textContent;
		var teacher=doc.evaluate('//span[@id="teacher_name"]/a',doc).iterateNext().text
		var author=doc.evaluate('//span[@id="author_name"]/a',doc).iterateNext().text
		doc.getElementById("more_abstract_cn").click()
		var abstract=doc.evaluate('//span[@id="abstract_cn"]',doc).iterateNext().textContent
		var regexp2 =  "\'(.*?)\'";
		var sid=doc.evaluate('//span[@id="fullText"]/a',doc).iterateNext().href.match(regexp2)[0]
		var pdfurl="http://dpaper.las.ac.cn/Dpaper/detail/getFile?student_no="+sid+"&type=all"
		pdfurl=pdfurl.replace(/\'/g,'')
		newItem.url=url;
		newItem.title=title;
		newItem.creators=[{
			lastName: author,
			creatorType: "author",
		},
		{
			lastName: teacher,
			creatorType: "contributor"
		}
		]
		newItem.abstractNote=abstract
		newItem.sid=sid
		var iso=doc.evaluate('//span[@id="education_grant_time"]',doc).iterateNext().innerText
		newItem.date=ZU.strToISO(iso)
		newItem.attachments = [
			{url:pdfurl, title:title, mimeType:"application/pdf"}
		]
		newItem.complete();
	}
}
