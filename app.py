from flask import request,Flask,jsonify
import pickle
import pandas as pd

#initialize Flask app
app = Flask(__name__)

#load saved model
with open("titanic_model.pkl","rb") as f:
    model = pickle.load(f)

print("Model loaded successfully!")

#Create prediction request

@app.route("/predict",methods=["POST"])

def predict():
    #get data from request
    data = request.get_json()
    
    #convert to DataFrame
    passenger = pd.DataFrame([[
        data["PassengerId"],
        data["Pclass"],
        data["Sex"],
        data["Age"],
        data["SibSp"],
        data["Parch"],
        data["Fare"],
        data["Embarked_C"],
        data["Embarked_Q"],
        data["Embarked_S"],
        data["FamilySize"],
        data["IsAlone"]
    ]],columns=["PassengerId","Pclass","Sex","Age","SibSp",
                 "Parch","Fare","Embarked_C","Embarked_Q",
                 "Embarked_S","FamilySize","IsAlone"])
# Make prediction
    prediction = model.predict(passenger)
    result = "Survived! ✅" if prediction[0] == 1 else "Died ❌"
    
    return jsonify({"prediction": result})

# Run app
if __name__ == "__main__":
    app.run(debug=True)