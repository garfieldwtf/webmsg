from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')  # Ensure UTF-8 encoding
        self.end_headers()

        message = os.getenv('MESSAGE', 'Hello, Docker World!')
        
        # HTML content with updated server identifier and refresh button
        html_content = f"""
        <html>
            <head>
                <title>Custom Message</title>
                <meta charset="UTF-8">  <!-- Ensure UTF-8 Encoding -->
                <style>
                    * {{
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }}
                    body {{
                        font-family: 'Arial', sans-serif;
                        background: linear-gradient(135deg, #FF7F50, #FFD700);
                        height: 100vh;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        color: #fff;
                        text-align: center;
                    }}
                    .container {{
                        background-color: rgba(255, 255, 255, 0.9);
                        border-radius: 15px;
                        padding: 40px;
                        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
                        width: 80%;
                        max-width: 600px;
                    }}
                    h1 {{
                        font-size: 48px;
                        font-weight: bold;
                        color: #FF6347;
                        margin-bottom: 20px;
                    }}
                    p {{
                        font-size: 20px;
                        font-weight: 300;
                        color: #333;
                        margin-bottom: 30px;
                    }}
                    .message {{
                        font-size: 36px;
                        color: #FF1493;
                        margin-top: 20px;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 10px 20px;
                        margin-top: 20px;
                        background-color: #32CD32;
                        color: white;
                        font-size: 18px;
                        text-decoration: none;
                        border-radius: 25px;
                        transition: background-color 0.3s ease;
                        cursor: pointer;
                    }}
                    .btn:hover {{
                        background-color: #228B22;
                    }}
                    @media (max-width: 600px) {{
                        h1 {{
                            font-size: 36px;
                        }}
                        p {{
                            font-size: 18px;
                        }}
                    }}
                </style>
                <script>
                    // Refresh the page when the button is clicked
                    function refreshPage() {{
                        window.location.reload();
                    }}
                </script>
            </head>
            <body>
                <div class="container">
                    <h1>Server Identifier</h1>
                    <p>We’re happy to see you here! Below is your custom message:</p>
                    <div class="message">{message}</div>
                    <button class="btn" onclick="refreshPage()">Refresh Page</button>
                </div>
            </body>
        </html>
        """
        
        self.wfile.write(bytes(html_content, 'utf-8'))

# Start the server
httpd = HTTPServer(('0.0.0.0', 8080), MyHandler)
httpd.serve_forever()

