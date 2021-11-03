from flask import render_template, request
from app import app
import json, requests

## import functions and get class instances
import functions
prettyprint = functions.prettyprint()

## app routes
@app.route('/')
def home():
    return render_template('home.html',
                            title='Home')

@app.route('/about')
def about():
    return render_template('about.html',
                            title='About')

@app.route('/prettyprint', methods=['GET', 'POST'])
def prettyjson():
    if request.method == 'GET':
        # set empty variables
        checklines    = ''
        checkvalidate = ''
        codeinput     = ''
        codeoutput    = ''
        language      = ''
        validation    = True

    if request.method == 'POST':
        # set default variables
        validation    = True

        # check if linenumbers should be used
        try:
          checklines = request.form.getlist('checklines')[0]
          checklines = True
        except:
          checklines = False

        # check if code input should be validated
        try:
          checkvalidate = request.form.getlist('checkvalidate')[0]
          checkvalidate = True
        except:
          checkvalidate = False

        # code input and language
        codeinput = request.form['codeinput']
        language  = request.form['selectlanguage']

        # set codeoutput
        codeoutput = prettyprint.parse(input=codeinput, language=language)
        if not codeoutput:
            validation = False
            codeoutput = codeinput

    return render_template('prettyprint.html',
                            title = 'Pretty Print',
                            checklines    = checklines,
                            checkvalidate = checkvalidate,
                            language      = language,
                            codeinput     = codeinput,
                            codeoutput    = codeoutput,
                            valid         = validation)

## custom error pages
@app.errorhandler(403)
def page_not_found(e):
    return render_template('error.html', message='Forbidden', code='403'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message='Page not found', code='404'), 404

@app.errorhandler(405)
def page_not_found(e):
    return render_template('error.html', message='Method not allowed', code='405'), 405
