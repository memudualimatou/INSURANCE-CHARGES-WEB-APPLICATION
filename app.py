import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open("model.pkl", 'rb'))


@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'gender': 'Gender'}, {'gender': 'female'}, {'gender': 'male'}],
        data1=[{'noc': 'Number of Children'}, {'noc': 0}, {'noc': 1}, {'noc': 2}, {'noc': 3}, {'noc': 4}, {'noc': 5}],
        data2=[{'smoke': 'Smoking Status'}, {'smoke': 'yes'}, {'smoke': 'no'}],
        data3=[{'region': "Region"}, {'region': "northeast"}, {'region': "northwest"},
               {'region': 'southeast'}, {'region': "southwest"}])


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    input_data = list(request.form.values())
    if int(input_data[0]) & int(input_data[3]) & input_data[2].isdigit() == True:
        pass
    else:
        print(ValueError)

    if input_data[1] == 'female':
        input_data[1] = 0
    elif input_data[1] == 'male':
        input_data[1] = 1
    else:
        print(ValueError)

    if input_data[4] == 'no':
        input_data[4] = 0
    elif input_data[4] == 'yes':
        input_data[4] = 1
    else:
        print(ValueError)

    if input_data[5] == 'northeast':
        input_data[5] = 0
    elif input_data[5] == 'northwest':
        input_data[5] = 1
    elif input_data[5] == 'southeast':
        input_data[5] = 2
    elif input_data[5] == 'southwest':
        input_data[5] = 3
    else:
        print(ValueError)

    input_values = [x for x in input_data]
    arr_val = [np.array(input_values)]
    prediction = model.predict(arr_val)
    output = round(prediction[0], 3)
    return render_template('index.html', prediction_text=" The predicted insurance charges is {}".format(output),
                           data=[{'gender': 'Gender'}, {'gender': 'female'}, {'gender': 'male'}],
                           data1=[{'noc': 'Number of Children'}, {'noc': 0}, {'noc': 1}, {'noc': 2}, {'noc': 3},
                                  {'noc': 4}, {'noc': 5}],
                           data2=[{'smoke': 'Smoking Status'}, {'smoke': 'yes'}, {'smoke': 'no'}],
                           data3=[{'region': "Region"}, {'region': "northeast"}, {'region': "northwest"},
                                  {'region': 'southeast'}, {'region': "southwest"}])


if __name__ == '__main__':
    app.run(debug=True)
