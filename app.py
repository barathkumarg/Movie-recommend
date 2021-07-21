from flask import Flask,render_template,url_for,request,redirect, jsonify
from config import *
import random
#print(get_movies("Dev"))
app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def home():

    return render_template("sample.html")

@app.route('/movies', methods=['GET'])
def movies():
    # if url is http://127.0.0.1:8000/movies?q=Petta
    query = request.args.get('q')

    return render_template('sample.html', query=query if query else '')

# api
@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":
        query = request.get_json()
        print(query)
        try:
            movies = get_movies(query['name'])
            print(movies)

            return jsonify({
                'result': movies,
                'error':False
            })
        except:
            return jsonify({
                'error': True
            })






if __name__=='__main__':
     app.run(debug=True)