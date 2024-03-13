from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
  <head>
    <title>SOFTWARE COMPANIES</title>
  </head>
  <body bgcolor="seablue" align="center">
    <table border="3" cellspacing="4" cellpadding="6" height="30" width="70" align="center" bgcolor="white">
      <caption><font color="white"><b>TOP 5 REVENUE GENERATING COMPANIES<b></font></caption>
      <tr>
        <th>Sno</th>
        <th>Company Name</th>
        <th>Revenue</th>
        <th>Price</th>
        <th>Today</th>
        <th>Country</th>
      </tr>
      <tr>
        <td>1</td>
        <td>APPLE</td>
        <td>$385.70B</td>
        <td>172.75</td>
        <td>+1.18%</td>
        <td>USA</td>
      </tr>
      <tr>        
        <td>2</td>
        <td>ALPHABET</td>
        <td>$307.39B</td>
        <td>138.94</td>
        <td>+0.42%</td>
        <td>USA</td>
      </tr>
      <tr>
        <td>3</td>
        <td>MICROSOFT</td>
        <td>$227.58B</td>
        <td>404.52</td>
        <td>-0.42%</td>
        <td>USA</td>
      </tr>
      <tr>
        <td>4</td>
        <td>IBM</td>
        <td>$61.85B</td>
        <td>191.73</td>
        <td>-2.15%</td>
        <td>USA</td>
      </tr>
      <tr>
        <td>5</td>
        <td>ORACLE</td>
        <td>$51.62B</td>
        <td>114.13</td>
        <td>+1.52%</td>
        <td>USA</td>
      </tr>
    </table>
  </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()