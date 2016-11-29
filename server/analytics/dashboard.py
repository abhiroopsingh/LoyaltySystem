from flask import Flask, render_template

import json
app = Flask(__name__)

@app.route('/<int:businessid>')
def hello_world(businessid):
    bsn = database.businesses().where(id=businessid).get()
    return render_template('dashboard.html', business=businessid, businessname=bsn.name)

@app.route('/all_balances/<int:businessid>')
def allbalances(businessid):
    acts = database.accounts().where(businessid=businessid).all()
    lst = []
    for act in acts:
        usr = database.users().where(id=act.customerid).get()
        user = {'id': act.customerid, 'name': usr.name}
        lst.append({'user':user, 'balance':act.points})
    lst = sorted(lst, key=lambda x:x['user']['id'])

    return json.dumps(lst)

@app.route('/time_balances/<int:businessid>')
def timebalances(businessid):
    balances = database.accounts().where(businessid=businessid).all()
    trans = database.transactions().where(businessid=businessid).all()
    now = util.time_sec()
    points = { b.customerid :[{'x':now, 'y':b.points}] for b in balances }
    newb = { b.customerid: b.points for b in balances}
    for t in trans:
        for id, pts in newb.items():
            if t.customerid == id:
                pts -= t.points
            points[id].append({'x':t.time, 'y':pts})
    return json.dumps(
        points.values()
    )
            

util = None
database = None
def start(db, port, utl):
    global util
    util = utl
    global database
    database = db 
    app.run(port=port, host='0.0.0.0', threaded=True, debug=True)
    
