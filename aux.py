def aux(
    LOGO, NAME, BIO, DESC, IMG0, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, SOCIAL1_NAME, SOCIAL1_LINK,
    SOCIAL2_NAME, SOCIAL2_LINK, SOCIAL3_NAME, SOCIAL3_LINK, SOCIAL4_NAME, SOCIAL4_LINK, LANG_INPUT, POLICE_INPUT,
    BACKGROUND_INPUT, LOGO_NAME_PLACEMENT_INPUT, IMG0_BIO_PLACEMENT_INPUT, SOCIALS_PLACEMENT_INPUT
    ):
    
    import os 




    #TECTENIUM FOLDER CREATION
    if not os.path.exists('C:\\Tecnetium'):
        os.mkdir('C:\\Tecnetium')
    if not os.path.exists(f'''C:\\Tecnetium\\{NAME}'''):
        os.mkdir(f'''C:\\Tecnetium\\{NAME}''') 



    #HTML CREATION
    if LANG_INPUT == "0" :
        LANG = "en"
    elif LANG_INPUT == "1" :
        LANG = "es"
    elif LANG_INPUT == "2" :
        LANG = "fr"
    else :
        LANG = "en"

    html = f'''<!DOCTYPE html> 
    <html lang="{LANG}">
        <head> 
            <meta charset="utf-8"> 
            <title>{NAME}</title> 
            <meta name="description" content="{BIO}"> 
            <link href="style.css" rel="stylesheet" type="text/css"> 
        </head> 
        <body> 
            <div id="LOGO_NAME"> 
                <img src="{LOGO}" width="100"> 
                <h2>{NAME}</h2> 
            </div> 
            <div id="BIO_IMG0"> 
                <p>{BIO}</p> 
                <img src="{IMG0}" width="800"> 
            </div> 
            <div id="PART"> 
                <p class="part">-</p> 
            </div> 
            <div id="DESC"> 
                <p>{DESC}</p> 
            </div>
            <div id="PART"> 
                <p class="part">-</p> 
            </div>
            <div id="IMGS"> 
                <img src="{IMG1}" width="400"> 
                <img src="{IMG2}" width="400"> 
                <img src="{IMG3}" width="400"> 
                <img src="{IMG4}" width="400"> 
                <img src="{IMG5}" width="400"> 
                <img src="{IMG6}" width="400"> 
                <img src="{IMG7}" width="400"> 
                <img src="{IMG8}" width="400"> 
            </div> 
            <div id="PART"> 
                <p class="part">-</p> 
            </div> 
            <div id="SOCIALS"> 
                <a href="{SOCIAL1_LINK}">{SOCIAL1_NAME}</a> 
                <a href="{SOCIAL2_LINK}">{SOCIAL2_NAME}</a> 
                <a href="{SOCIAL3_LINK}">{SOCIAL3_NAME}</a> 
                <a href="{SOCIAL4_LINK}">{SOCIAL4_NAME}</a> 
            </div>
            <div id="POWERED"> 
                <a href="TECNETIUM">Powered by TECNETIUM</a> 
            </div> 
        </body> 
    </html>'''




    #CSS CREATION
    if POLICE_INPUT == "0" :
        POLICE = '''"Arial", sans-serif'''
    elif POLICE_INPUT == "1" :
        POLICE = '''"Verdana", sans-serif'''
    elif POLICE_INPUT == "2" :
        POLICE = '''"Times New Roman", serif'''
    elif POLICE_INPUT == "3" :
        POLICE = '''"Monaco", monospace'''
    else : 
        POLICE = '''"Arial", sans-serif'''

    if BACKGROUND_INPUT == "0" :
        BACKGROUND = "#fff"
    elif BACKGROUND_INPUT == "1" :
        BACKGROUND = "#F0F8FF"
    elif BACKGROUND_INPUT == "2" :
        BACKGROUND = "#F0FFFF"
    elif BACKGROUND_INPUT == "3" :
        BACKGROUND = "#F5F5DC"
    elif BACKGROUND_INPUT == "4" :
        BACKGROUND = "#DEB887"
    elif BACKGROUND_INPUT == "5" :
        BACKGROUND = "#FFF8DC"
    elif BACKGROUND_INPUT == "6" :
        BACKGROUND = "#D3D3D3"
    else :
        BACKGROUND = "#fff"

    if LOGO_NAME_PLACEMENT_INPUT == "0" :
        LOGO_NAME_PLACEMENT = '''display: flex;
        flex-direction: column;
        align-items: center;'''
    elif LOGO_NAME_PLACEMENT_INPUT == "1" :
        LOGO_NAME_PLACEMENT = '''display: flex;
        justify-content: space-around;
        align-items: center;'''
    else : LOGO_NAME_PLACEMENT = '''display: flex;
        flex-direction: column;
        align-items: center;'''

    if IMG0_BIO_PLACEMENT_INPUT == "0" :
        IMG0_BIO_PLACEMENT = '''display: flex;
        flex-direction: column;
        align-items: center;'''
    elif IMG0_BIO_PLACEMENT_INPUT == "1" :
        IMG0_BIO_PLACEMENT = '''display: flex;
        justify-content: space-around;
        align-items: center;'''
    else : 
        IMG0_BIO_PLACEMENT = '''display: flex;
        flex-direction: column;
        align-items: center;'''

    if SOCIALS_PLACEMENT_INPUT == "0" :
        SOCIALS_PLACEMENT = '''display: flex;
        flex-wrap: wrap;
        justify-content: space-around;'''
    elif SOCIALS_PLACEMENT_INPUT == "1" :
        SOCIALS_PLACEMENT = '''display: flex;
        align-items: center;
        flex-direction: column;'''
    else :
        SOCIALS_PLACEMENT = '''display: flex;
        flex-wrap: wrap;
        justify-content: space-around;'''

    css = ('''body,a{font-family:''')+POLICE+(''';color:#04091e;background:''')+BACKGROUND+(''';font-size:1em;line-height:2em;text-decoration: none}
    img{display:block;max-width:95%}
    .part{color:''')+BACKGROUND+('''}

    #LOGO_NAME
    {
        ''')+LOGO_NAME_PLACEMENT+('''
    }

    #BIO_IMG0
    {
        ''')+IMG0_BIO_PLACEMENT+('''
    }

    #DESC
    {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    #IMGS
    {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: center;
    }

    #PART
    {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    #SOCIALS
    {
        ''')+SOCIALS_PLACEMENT+('''
    }

    #POWERED
    {
        font-size: 60%;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }
    ''')

    #FILES CREATION
    f_html = open(f'''C:\\Tecnetium\\{NAME}\\index.html''', "w")
    f_html.write(html)
    f_css = open(f'''C:\\Tecnetium\\{NAME}\\style.css''', "w")
    f_css.write(css)
    path = os.path.realpath(f'''C:\\Tecnetium\\{NAME}''')
    os.startfile(path)
    path2 = os.path.realpath(f'''C:\\Tecnetium/{NAME}\\index.html''')
    os.startfile(path2)