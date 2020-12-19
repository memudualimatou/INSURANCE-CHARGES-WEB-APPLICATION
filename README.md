


<h2 align="center"> INSURANCE CHARGES  PREDICTION SYSTEM</h2>

<h4 align="center"><i>This is a charge prediction system. The aim is to predict individual insurance charges based on their status</i></h4><br>


## 😇 INSPIRATION
The purposes of this Project to look into different features to observe their relationship, and plot a regression algorithm based on several features of individual such as age, physical/family condition and location against their existing medical expense to be used for predicting future medical expenses of individuals that help medical insurance to make decision on charging the premium.The dataset has 7 coloumns which are age,sex,region,charges,numberOfChildren, smoke and BMI wwhich is Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women. BMI= m/h^2
where
m	=	mass (in kilograms)
h	=	height (in meters)


<br><br>


## ⚙️ HOW DOES THE INSURANCE CHARGES PREDICTION SYSTEM WORKS?

This sytem is a flask web application  hosted on heroku. The user has to input some data and get the predicted charges immediately.
The system's interface is built using using HTML & CSS  from scratch.Everything is all about preferences but I will personnaly prefer to  style my web app than using the plain streamlit interface.
So We use randomforestRegression algorithm to build the model, sterialize it and destrerialize it using Pickle to make prediction. Whenever a user enter the correspondant input through the interface, at the backend , a function in the flask app is called to fetch the inputted data, clean it and displayed the predicted outcome.<br><br>

The system depends on the following files.
1. `insurance.csv` [See here](https://github.com/memudualimatou/INSURANCE-CHARGES-WEB-APPLICATION/blob/master/insurance.csv) :The system database  [CLICK HERE TO DOWNLOAD](https://www.kaggle.com/noordeen/insurance-premium-prediction)
2. `insurances.ipynb` [See here](https://github.com/memudualimatou/INSURANCE-CHARGES-WEB-APPLICATION/blob/master/Insurances.ipynb) :The model notebook
3. `insurances.py` [See here](https://github.com/memudualimatou/INSURANCE-CHARGES-WEB-APPLICATION/blob/master/Insurances.py): The model python file
4. `app.py` [See here](https://github.com/memudualimatou/INSURANCE-CHARGES-WEB-APPLICATION/blob/master/app.py): The flask app
5. `index.html` [See here](https://github.com/memudualimatou/INSURANCE-CHARGES-WEB-APPLICATION/blob/master/templates/index.html): The html file is located insite the Templates folder
6. `AppStyle.css` [See here](https://github.com/memudualimatou/INSURANCE-CHARGES-WEB-APPLICATION/blob/master/static/AppStyle.css): The css file is located inside the static folder.<br><br><br>


## ⚠️ THE TECHNOLOGY
* [FLASK](https://en.wikipedia.org/wiki/Flask_(web_framework))

* [HEROKU](https://en.wikipedia.org/wiki/Heroku)

* [PICKLE](https://en.wikipedia.org/wiki/Pickle)

* [RANDOM FOREST REGRESSION](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)<br><br>


# ⌛ Project Demo
<br>

[DEPLOYED ON HEROKU | CLICK HERE TO TEST THE SYSTEM](https://insurance-web-application.herokuapp.com/)
<br>
<br>

![capture](https://github.com/memudualimatou/INSURANCE-CHARGES-WEB-APPLICATION/blob/main/images/ezgif.com-gif-maker%20(3).gif)<br>
<br><br>

# 🔑 Prerequisites
All the dependencies and required libraries are included in the file `requirements.txt` [See here](https://github.com/memudualimatou/INSURANCE-CHARGES-WEB-APPLICATION/blob/master/requirements.txt): The css file located inside the static foler.
<br><br>

## 🚀 INSTALLATION

Clone the repo\
```$ git clone https://git.heroku.com/my-insurance-web-app.git```


Now, run the following command in your Terminal/Command Prompt to install the libraries required

```$ pip3 install -r requirements.txt```


# 👏 And it's done!
Feel free to mail me for any doubts/query ✉️ anikesadia01@gmail.com
<br><br>



# ❤️ Owner
Made with ❤️  by MEMUDU Alimatou Sadia Anike.

