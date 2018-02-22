import quotes

def generate_html(image_html_list, title_list, author_list, top_com_list):
    print('Generating HTML')
    quote_source = "<a href=" +"\"" + quotes.url + "\"" + ">BrainyQuote - Quote of the Day</a>"

    # Email Header HTML
    code = """
    <html>
      <head></head>
      <body>
        <p align="center"><b><font size="7">The Feline Fanatic</b></font><br>
        <p align="center"><i><font size="4">"Your Daily Dose of All Things Fluffball"</i></font><br><br>
        <hr>
        <p align="center"><i><font size="5">""" + quotes.get_quote() + """</i></font><br>
        <p align="center"><font size="1">""" + quote_source + """</p></font>
        <hr><br>
    """
    # Image HTML Generator 
    counter = 0
    for img_code, title, author, comments in zip(image_html_list, title_list, author_list, top_com_list):
        block = """
        <table class="image" align="center">
            <caption align="top"><b><font size="5">""" + str(title) + """<br>
                - /u/""" + str(author) + """
            </font></b></caption><br>
        """
        
        block = make_img_html(block, counter, img_code, comments) + "</table><br><hr><br>"
        code += str(block)
        counter += 1

    # Email Footer HTML
    code += """
        <p align="center"><font size="1"> This message was procedurally generated by 'Cat Bot',
                                          a Reddit-scraping, Python-powered program developed by Garrett Blinkhorn</font></p>
        </p>
      </body>
    </html>
    """ 

    return code

# This function causes images to display on alternating sides of the email message
def make_img_html(block, counter, img_code, comments):
    if counter % 2 == 0:
        block += """<tr><td style="padding:0 50px 0 50px;">""" + str(img_code) + """</td>
                    <td align="center">""" + comments + """</td>
                </tr>"""
    else:
        block += """<tr><td align="center">""" + comments + """</td>
                        <td style="padding:0 50px 0 50px;">""" + str(img_code) + """</td>
                </tr>"""
    return block