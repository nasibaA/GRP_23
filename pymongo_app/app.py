from flask import Flask,render_template
from flask_pymongo import PyMongo
import datetime
app = Flask(__name__)

#setup mongo connection
app.config['MONGO_URI']="mongodb://localhost:27017/shows_db"
mongo = PyMongo(app)

#connect to collection
tv_shows = mongo.db.tv_shows

#insert
@app.route("/insert")
def insert():
    post_data = {'name':'sugarrush',
                'seasons':3,
                'duration':'40 minutes',
                'year':2019,
                'data_added':datetime.datetime.utcnow()}
    #insert record
    tv_shows.insert_one(post_data)
    return 'data created'



 # update   
@app.route('/update')
def update():
    # item we want to update
    item ={'name':'House'}
    # the new value we want to set
    updated_val = {'$set':{'seasons':4}}
    # make the update
    tv_shows.update_one(item,updated_val)
    return 'data updated'

#DElete
@app.route('/delete')
def delete():
    #Delete the original record
    tv_shows.delete_one({'name':'House'})

    return 'data deleted'


#READ
@app.route("/read")
def read():
    #find all items in db and save to avariable
    all_shows = list(tv_shows.find())

    return render_template('index.html',data = all_shows)

if __name__ == '__main__':
    app.run(debug=True)