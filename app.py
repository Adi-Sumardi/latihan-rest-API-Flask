#import library

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#inisiasi objek flask
app = Flask(__name__)

#inisiasi objek flask_restful
api = Api(app)

#inisiasi objek flask_cors
CORS(app)

#inisiasi variabel kosong dictionary
identitas = {} #variable global, dictionary = json

#membuat class resource
class ContohResource(Resource):
    #method GET dan POST
    def get(self):
        # response={"msg":"Hallo World, ini app Restfull API"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data berhasil disimpan"}
        return response

#setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
