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
        fs.readFile(decodeURI(pathname.substr(1)), function (err, data) {
            if (err||!data) {
                console.log(err);
                // HTTP 状态码: 404 : NOT FOUND
                // Content Type: text/html
                res.writeHead(404, {
                    "Content-Type": "text/html"
                });
                    //res.write(data.toString());
                    res.end();
            } else if(pathname.split(".")[1] == 'css'){
                    res.writeHead(200, {
                        "Content-Type": "text/css"
                    });
                    res.write(data.toString());
                    res.end();
            }else if(pathname.split(".")[1] == 'png'){
                    res.writeHead(200, {
                        "Content-Type": "image/png"
                    });
                    let imageFilePath = decodeURI(pathname).substr(1);
                    let stream = fs.createReadStream( imageFilePath );
                    let responseData = [];//存储文件流
                    if (stream) {//判断状态
                        stream.on( 'data', function( chunk ) {
                        responseData.push( chunk );
                        });
                        stream.on( 'end', function() {
                        var finalData = Buffer.concat( responseData );
                        res.write( finalData );
                        res.end();
                    });
                    }
            }else{
                    // HTTP 状态码: 200 : OK
                    // Content Type: text/html
                    res.writeHead(200, {
                        "Content-Type": "text/html"
                    });
                    res.write(data.toString());
                    res.end();
                }
                // 响应文件内容
            //  发送响应数据s
        });
        req.on("data", function(chunk){
            body += chunk;
        })
        req.on("end", function(){
            if(body==='')return
            body = querystring.parse(decodeURI(body));
            console.log(body);
            if(body.city&&body.option&&body.mode)
                if(body.option === 'month_tem'&&body.year&&body.month){
                    console.log('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.year + ' ' + body.month + ' ' + body.mode)
                    exec('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.year + ' ' + body.month + ' ' + body.mode)
                }else if(body.option === 'year_tem'&&body.year){
                    console.log('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.year + ' ' + body.mode)
                    exec('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.year + ' ' + body.mode)
                }else if(body.option === 'month_tem_ch'&&body.month){
                    console.log('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.month + ' ' + body.mode)
                    exec('python3 "' + path.resolve('./index.js', './../../../src/' + body.option + '.py') + '" ' + body.city + ' ' + body.month + ' ' + body.mode)
                }
        })
    })
    .listen(3000);

// 控制台会输出以下信息
console.log("Server running at http://127.0.0.1:3000/");