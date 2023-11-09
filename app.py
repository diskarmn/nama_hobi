import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template,request,redirect,url_for,jsonify,Response
from pymongo import MongoClient

app=Flask(__name__)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db=client[DB_NAME]

# mongo_uri="mongodb+srv://diskarmn:Diska123@cluster0.3lnlkgx.mongodb.net/?retryWrites=true&w=majority"
# client=MongoClient(mongo_uri)
# db=client.latihan


@app.route('/',methods=['GET'])
def index():
    semua=list(db.latihan1.find({},{'_id': False}))
    return render_template('index.html',semua=semua)
@app.route('/berhasil')
def berhasil():
    return render_template('berhasil.html')
@app.route('/tambah_data',methods=['POST'])
def tambah_data():
    if request.method=='POST':
        nama=request.form['nama']
        hobi=request.form['hobi']
        data={'nama':nama,'hobi':hobi}
        db.latihan1.insert_one(data)
        return redirect(url_for('berhasil'))


if __name__=='__main__':
    app.run('0.0.0.0',port=5000,debug=True)