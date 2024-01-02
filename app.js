var http = require('http');
var fs = require('fs');
var path = require('path');

var server = http.createServer(function(req, res) {
    if (req.url === "/") {
        const path = path.join(__dirname, 'public', 'app.js');

        fs.readFile(path, 'utf-8', function(err, data) {
            if (err) {
                res.writeHead(500, {'Content-Type': 'text/plain'});
                res.end('Internal Server Error');
            } else {
                res.writeHead(200, {'Content-Type': 'text/html'});
                res.end(data);
            }
        })
    }
    else {
        res.writeHead(200, {'Content-Type': 'text/plain'});
        var message = 'It works!\n',
            version = 'NodeJS ' + process.versions.node + '\n',
            response = [message, version].join('\n');
        res.end(response);
    }
});
server.listen();