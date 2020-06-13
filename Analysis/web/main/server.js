const http = require("http");
const fs = require("fs");
const url = require("url");
const exec = require('child_process').exec
const path = require('path')
const querystring = require('querystring')
// 创建服务器
http
    .createServer(function (req, res) {
        let body = ''
        // 解析请求，包括文件名
        let pathname = url.parse(req.url).pathname;
        // 输出请求的文件名
        console.log("Request for " + pathname + " received.");
        // 从文件系统中读取请求的文件内容
        fs.readFile(pathname.substr(1), function (err, data) {
            if (err) {
                console.log(err);
                // HTTP 状态码: 404 : NOT FOUND
                // Content Type: text/html
                res.writeHead(404, {
                    "Content-Type": "text/html"
                });
            } else {
                if(pathname.split(".")[1] == 'css'){
                    res.writeHead(200, {
                        "Content-Type": "text/css"
                    });
                }else{
                    // HTTP 状态码: 200 : OK
                    // Content Type: text/html
                    res.writeHead(200, {
                        "Content-Type": "text/html"
                    });
                }
                // 响应文件内容
                res.write(data.toString());
                res.end();
            }
            //  发送响应数据s
        });
        req.on("data", function(chunk){
            body += chunk;
        })
        req.on("end", function(){
            if(body==='')return
            body = querystring.parse(body);
            console.log(body);
            res.writeHead(200, {'Content-Type': 'text/html; charset=utf8'});
            if(body.city&&body.option&&body.mode)
                if(body.option === 'month_tem'&&body.year&&body.month){
                    console.log('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.year[0] + ' ' + body.month[0] + ' ' + body.mode[0])
                    exec('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.year[0] + ' ' + body.month[0] + ' ' + body.mode[0])
                }else if(body.option === 'year_tem'&&body.year){
                    console.log('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.year[1] + ' ' + body.mode[1])
                    exec('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.year[1] + ' ' + body.mode[1])
                }else if(body.option === 'month_tem_ch'&&body.month){
                    console.log('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.month[1] + ' ' + body.mode[2])
                    exec('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.month[1] + ' ' + body.mode[2])
                }
        })
    })
    .listen(3000);

// 控制台会输出以下信息
console.log("Server running at http://127.0.0.1:3000/");