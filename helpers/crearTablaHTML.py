def crearTabla(dataFrame,nombreTabla):
    archivoHTML=dataFrame.to_html()
    archivo=open(f"./tables/{nombreTabla}.html","w")
    archivo.write('''
            <html>
                <head>
                    <title>tabla aire</title>
                </head>
                <body>
                ''')
    archivo.write(archivoHTML)
    archivo.write(
                    '''
                </body>
            </html>
        ''')