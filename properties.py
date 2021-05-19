sender = "<EMAIL HERE>"
password = "<PASSWORD HERE>" # is there a way to encript this?
port = 465  # For SSL

def getHTML(message, author):
    html = """\
    <html>
        <body>
            <h1>Você recebeu um sugar!</h1><br>
            <img align="center" alt="Image" border="0" class="center fixedwidth" src="https://media4.giphy.com/media/sN6rHuJQ9p61y/giphy.gif?cid=20eb4e9d4d7nw2xgrgicddc2t7s7p4ay7taxvgaop4b3mwkh&amp;rid=giphy.gif" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 350px; display: block;" title="Image" width="350"/>
            
            <h2>Mensagem:</h2>
            <div style="background-color: #151515; box-sizing: border-box; width: 550px; margin: 0 auto; padding: 20px; border-radius: 5px; word-wrap: break-word;">
                <span style="position: relative; color: #fff;left: 50%; margin-left: -15.5em; text-align: left; font-size: 1.25em; font-family: monospace; white-space: normal; word-wrap: break-word;">
                    {}<br>
                    - {}
                </span>
            </div>
            
      </body>
    </html>
    """.format(message, author)

    return html

def getText(message, author):
    text = """\
    Você recebeu um sugar!!

    {}
    - {}

    """.format(message, author)

    return text