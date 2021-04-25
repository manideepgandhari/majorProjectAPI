from flask import Flask,jsonify,request
from flask_restful import Api
import joblib
from flask_restful import Resource,reqparse

app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['PREFERRED_URL_SCHEME']='https'

@app.route('/',methods=['POST'])
def index():
    if request.method == 'POST':
        parser=reqparse.RequestParser()
        parser.add_argument('EC',type=str,required=True,help="EC cannot be left blank ")
        parser.add_argument('Temp',type=str,required=True,help="Temp cannot be left blank ")
        parser.add_argument('Moisture',type=str,required=True,help="Moisture cannot be left blank ")
        parser.add_argument('Growth',type=str,required=True,help="Growth cannot be left blank ")
        data=parser.parse_args()
        model = joblib.load(open('./resources/filename.joblib', 'rb'))
        predict = model.predict([[data['EC'],data['Temp'],data['Moisture'],data['Growth']]])
        print(predict)
        return predict[0]
    else:
        return "Request Not Acceptable"
if __name__ == "__main__":
    app.run()
