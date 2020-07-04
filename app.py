import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model.
with open(f'model/4july_lr_model.pickle', 'rb') as f:
    model = pickle.load(f)
    
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET','POST'])
def main():
    if flask.request.method == 'GET':
       return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
       itetypeinter= flask.request.form['itetypeinter']
       year = flask.request.form['year']
       month = flask.request.form['month']
       day = flask.request.form['day']
       hour = flask.request.form['hour']
       minute = flask.request.form['minute']
       protypehot = flask.request.form['protypehot']
       protypeothpro = flask.request.form['protypeothpro']
       protypeaircanc = flask.request.form['protypeaircanc']
       protypehotcanc = flask.request.form['protypehotcanc']
       protypeairloss = flask.request.form['protypeairloss']
       protypehotloss = flask.request.form['protypehotloss']
              
       input_variables = pd.DataFrame([[itetypeinter,year,month,day,hour,minute,protypehot,protypeothpro,protypeaircanc,protypehotcanc,protypeairloss,protypehotloss]],columns=['itetypeinter','year','month','day','hour','minute','protypehot','protypeothpro','protypeaircanc','protypehotcanc','protypeairloss','protypehotloss'],dtype=float,index=['input'])
       prediction = model.predict(input_variables)[0]
       #model = pd.read_pickle(r"C:\Users\Raja\Desktop\project\final_proj_g4\webapp\model\30june_lr_model.pickle")
       #NetFarePredicted=model.predict([[year,month,day,hour,minute,protypeaircanc,protypeairdebtnote,protypeairloss,protypehot,protypehotcanc,protypehotdebnote,protypehotloss,protypeothpro,protypeothprocanc ,protypeothprodebnote,itetypeinter]])
       #NetFarePredicted=NetFarePredicted[0]
       #print(f'NetFarePredicted:{NetFarePredicted:.2f}')
       return flask.render_template('main.html',original_input={'Itenerary_Type':itetypeinter,'Year':year,'Month':month,'Day':day,'Hour': hour,'Minute':minute,'Product_Type_Hotel':protypehot,'Product_Type_Other_Product':protypeothpro,'Product_Type_Air_Cancellation':protypeaircanc,'Product_Type_Hotel_Cancellation':protypehotcanc,'Product_Type_Air_Loss':protypeairloss,'Product_Type_Hotel_Loss':protypehotloss},result=prediction,)
    
if __name__ == '__main__':
    app.run()