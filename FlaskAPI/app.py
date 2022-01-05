import flask
from flask import Flask, jsonify, request, render_template
import json
from data_input import data_in
import numpy as np
import pickle
import pandas as pd


def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/', methods=['GET'])
# def getvalue():
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        rat=request.form['rating']
        cs=request.form['Company Size']
        to=request.form['Type of ownersip']
        ind=request.form['Industry']
        sec=request.form['Sector']
        rev=request.form['Revenu']
        num=request.form['num_comp']
        hor=request.form['Hourly']
        emp=request.form['Employer provided']
        state=request.form['state']
        sst=request.form['Same State']
        age=request.form['age']
        py=request.form['Python']
        sp=request.form['Spark']
        aws=request.form['aws']
        ex=request.form['Excel']
        js=request.form['job_simp']
        sen=request.form['Seniority']
        desc=request.form['desc__len']
        print(rat,cs,to,ind,sec,rev,num,hor,emp,state,sst,age,py,sp,aws,ex,js,sen,desc)
        df = pd.read_csv(r"E:\A vrudit\Working\Python Projects\glassdoor_own_old\eda_data.csv")
        df_model = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','num_comp','hourly','employer_provided',
             'job_state','same_state','age','python_yn','spark','aws','excel','job_simp','seniority','desc_len']]
        df_model.loc[len(df_model.index)]=[84.5, 3.8, cs, to, ind, sec, rev, 0, 0, 0, state, 0, 47, 1, 0, 0, 1, 'data scientist', 'na', 2555]     
        df_model.loc[len(df_model.index)-1,'Revenue']= 'Unknown / Non-Applicable'
        dfd=df_model.drop('avg_salary', axis =1)
        dfm=pd.get_dummies(dfd)
        print(dfm.columns.values)
        newdata = list(dfm.iloc[len(df_model.index)-1,:])
        print(len(newdata))
        print(newdata)
        x_in = np.array(newdata).reshape(1,-1)
        model = load_models()
        prediction = str(model.predict(x_in)[0])
        return prediction
        
#     print('done')
#     # return prediction
#     # return render_template('index.html')





# app = Flask(__name__)
# @app.route('/predict', methods=['GET'])
# def predict():
#     # stub input features
#     request_json = request.get_json()
#     x = request_json['input']
#     #print(x)
#     x_in = np.array(x).reshape(1,-1)
#     # load model
#     model = load_models()
#     prediction = model.predict(x_in)[0]
#     response = json.dumps({'response': prediction})
#     return response, 200

if __name__ == '__main__':
    application.run(debug=True)
