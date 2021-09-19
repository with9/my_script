{
	"translatorID": "a4c501ed-3936-4f68-854c-346ce877ebf8",
	"label": "dlsite",
	"creator": "with",
	"target": "^https?://www.dlsite.com",
	"minVersion": "3.0",
	"maxVersion": "",
	"priority": 100,
	"inRepository": true,
	"translatorType": 4,
	"browserSupport": "gcsibv",
	"lastUpdated": "2021-08-09 11:43:17"
}

/*
	***** BEGIN LICENSE BLOCK *****

	Copyright © 2021 Philipp Zumstein
	
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
	var a=doc.getElementsByClassName('icon_SOU')[0].innerText;
	if (a == 'ボイス・ASMR') {
		return "audioRecording";
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
	var newItem = new Zotero.Item("audioRecording");
	var title=doc.getElementById('work_name').getElementsByTagName('a')[0].innerText;
	var infos=doc.getElementById('work_right').getElementsByTagName('tr');
	var notes='<h1>'+title+'</h1>';
	notes=notes.concat(doc.getElementById('work_right').innerHTML);
	notes=notes.concat(doc.getElementsByClassName('work_parts_container')[0].innerHTML);
	// var imgs=doc.getElementsByClassName('thumb_box');
	// for(var i of imgs){
	// 	notes=notes.concat(i.innerHTML);
	// }
	
	var marker=doc.getElementsByClassName('maker_name')[0].innerText;
	newItem.creators.push({
		lastName: marker,
		creatorType: 'wordsBy',
		fieldMode: 2
	});
	rights=marker;
	
	for(var info of infos){
		if(info.innerText.indexOf('声優') != -1){
			voicers=info.getElementsByTagName('a');
			for(var voicer of voicers){
				newItem.creators.push({
					lastName: voicer.innerText,
					creatorType: "author",
					fieldMode: 1
				});
			}
		}
		else if(info.innerText.indexOf('ジャンル') != -1){
			var tags=info.getElementsByTagName('a');
			for(var tag_name of tags){
				newItem.tags.push({tag: tag_name.innerText});
			}
		}
		else if(info.innerText.indexOf('販売日') != -1){
			newItem.date=ZU.strToISO(info.innerText.split('	')[1]);
		}
	}
	newItem.title=title;
	newItem.url=url;
	// newItem.
	newItem.notes.push({note: notes});
	newItem.attachments = [{
	url: url,
	title: title,
	mimeType: "text/html",
	snapshot: true
	}];
	newItem.abstractNote=doc.getElementsByClassName('work_parts_container')[0].innerText;
	newItem.rights=rights;
	newItem.language='ja';
	newItem.complete();
}
