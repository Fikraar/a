from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='Templates')

model=pickle.load(open('model.pk','rb'))


@app.route('/')
def hello_world():
    return render_template("gaptester.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output=prediction

    if output == 0:
        return render_template('gaptester.html',pred='Partial Discharge Phenomeon not Occured raise kV AC and VMT1' )
    if output == 1 :
        return render_template('gaptester.html',pred='Partial Discharge Noise Occured')
    if output == 2 :
        return render_template('gaptester.html',pred='Corona Light Occured')
    if output == 3 :
        return render_template('gaptester.html',pred='Partial Discharge Noise and Corona Light Occured')
    else:
        return render_template('gaptester.html',pred='flashover occured')
    


if __name__ == '__main__':
    app.run(debug=True)
