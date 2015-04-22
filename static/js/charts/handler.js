function searchdomain(fuzz){
	var domainname = $("#querydomain").val();
	var date = $("#choosedomaindate").val();
	if (domainname == "输入查询域名") {
		domainname = "www.baidu.com";
	};
	var showdata = [];
	var max = 0;
	var getpath;
	if (fuzz == "no") {
		getpath = "/charts/searchdomain";
	}
	else {
		getpath = "/charts/searchdomainfuzz";
	}
	$.get(getpath,
	{
		"domainname":domainname,
		"date":date
	},
	function(data, status){
		if (status=="success") {
			if (data!="error") {
			//alert(data);
			datas = eval('(' + data + ')');
			for (var i = 0; i < datas.length; i++, tempdata = []) {
				showdata.push([i, datas[i]]);
				if (datas[i] > max) {
					max = datas[i];
				};
			};
		}
		else{
			alert("data is error");
		}
	}
	else{
		alert("error");
	}
	//alert(max);
	var plot = $.plot($("#line-chart"),
		[ { data: showdata, label: domainname} ], {
			series: {
				lines: { show: true },
				points: { show: true }
			},
			grid: { hoverable: true, clickable: true },
			yaxis: { min: 0, max: max + 1 },
			xaxis: { min: 0, max: 24 },
			colors: ["#F90", "#222", "#666", "#BBB"]
			});
	});
}

/*function searchfuzz(){
	var domainname = $("#nethie").val();
	if (domainname == "输入查询域名") {
		domainname = "www.baidu.com";
	};
	var showdata = [];
	var max = 0;
	$.get("/charts/searchdomainfuzz",
	{
		"domainname":domainname
	},
	function(data, status){
		if (status=="success") {
			if (data!="error") {
			//alert(data);
			datas = eval('(' + data + ')');
			for (var i = 0; i < datas.length; i++, tempdata = []) {
				showdata.push([i, datas[i]]);
				if (datas[i] > max) {
					max = datas[i];
				};
			};
		}
		else{
			alert("data is error");
		}
	}
	else{
		alert("error");
	}
	//alert(max);
	var plot = $.plot($("#line-chart"),
		[ { data: showdata, label: domainname} ], {
			series: {
				lines: { show: true },
				points: { show: true }
			},
			grid: { hoverable: true, clickable: true },
			yaxis: { min: 0, max: max + 1 },
			xaxis: { min: 0, max: 24 },
			colors: ["#F90", "#222", "#666", "#BBB"]
			});
	});
}*/

function searchip(){
	var queryip = $("#queryip").val();
	var iptype = $("#iptype").val()
	//alert(iptype);
	var date = $("#chooseipdate").val();
	if (queryip == "输入查询IP") {
		alert("请输入查询IP");
		return;
	};
	
	var showdata = [];
	var max = 0;
	var getpath;
	getpath = "/charts/searchip"
	$.get(getpath,
	{
		"queryip":queryip,
		"iptype":iptype,
		"date":date
	},
	function(data, status){
		if (status=="success") {
			if (data!="error") {
			//alert(data);
			datas = eval('(' + data + ')');
			for (var i = 0; i < datas.length; i++, tempdata = []) {
				showdata.push([i, datas[i]]);
				if (datas[i] > max) {
					max = datas[i];
				};
			};
		}
		else{
			alert("data is error");
		}
	}
	else{
		alert("error");
	}
	//alert(max);
	var plot = $.plot($("#line-chart-ip"),
		[ { data: showdata, label: queryip} ], {
			series: {
				lines: { show: true },
				points: { show: true }
			},
			grid: { hoverable: true, clickable: true },
			yaxis: { min: 0, max: max + 1 },
			xaxis: { min: 0, max: 24 },
			colors: ["#F90", "#222", "#666", "#BBB"]
			});
	});
}

function queryresponse(){
	var date = $("#queryresponsedate").val();
	if (date == "") {
		alert("请选择查看日期!");
		return;
	};
	//date = "20150422";
	//alert(iptype);
	var queryshowdata = [], responseshowdata = [];
	var max = 0;
	var getpath;
	getpath = "/charts/queryresponse"
	$.get(getpath,
	{
		"date":date
	},
	function(data, status){
		if (status=="success") {
			if (data!="error") {
			//alert(data);
			datas = eval('(' + data + ')');
			//alert(data);
			querydata = datas[0]
			responsedata = datas[1]
			//alert(querydata);
			//alert(responsedata);
			for (var i = 0, max = 0; i < responsedata.length; i++) {
				responseshowdata.push([i, responsedata[i]]);
				if (responsedata[i] > max) {
					max = responsedata[i];
				};
			};

			for (var i = 0, max = 0; i < querydata.length; i++) {
				queryshowdata.push([i, querydata[i]]);
				if (querydata[i] > max) {
					max = querydata[i];
				};
			};
		}
		else{
			alert("data is error");
		}
	}
	else{
		alert("error");
	}
	//alert(max);
	var plot = $.plot($("#line-chart-query-response"),
		[ { data: queryshowdata, label: "查询包"},  { data: responseshowdata, label: "应答包"} ], {
			series: {
				lines: { show: true },
				points: { show: true }
			},
			grid: { hoverable: true, clickable: true },
			yaxis: { min: 0, max: max + 1 },
			xaxis: { min: 0, max: 24 },
			colors: ["#F90", "#222", "#666", "#BBB"]
			});
	});
}