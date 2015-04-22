$(function () {
  //var domain[];
    //var sin = [[1,1], [2,2], [3, 3], [4,3.5], [5,2.3]], cos = [[1, 2], [2,3], [3,1], [4,2.4], [5,3]];
    /*for (var i = 0; i < 10; i += 0.5) {
        sin.push([i, Math.sin(i)]);
        cos.push([i, Math.cos(i)]);
    }*/
    var showdata = [];
    var max = 0;
    $.get("/charts/linechart",
    {
      "domainname":"www.baidu.com"
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
        else
        {
          alert("data is error");
        }
      }
      else
      {
        alert("error");
      }
      //alert(max);
      var plot = $.plot($("#line-chart"),
           [ { data: showdata, label: "www.baidu.com"} ], {
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
    //alert(window.showdata);
});