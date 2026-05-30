# 🚢 Titanic Survival Prediction

## 📌 Project Overview
Built a Machine Learning model to predict whether a Titanic passenger 
survived or not, based on features like age, gender, and passenger class.

## 🎯 Results
- **Model:** Random Forest Classifier
- **Accuracy:** 83.24%
- **Key Finding:** Gender and passenger class were the strongest 
  predictors of survival

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Flask (API deployment)

## 📊 What I did
1. Cleaned missing data (Age, Cabin, Embarked)
2. Feature Engineering (FamilySize, IsAlone)
3. Trained Decision Tree → Random Forest
4. Evaluated with Confusion Matrix, Precision, Recall, F1
5. Deployed as Flask REST API

## 🚀 How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask API
python app.py

# Test prediction
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"PassengerId":1,"Pclass":1,"Sex":0,"Age":25,
     "SibSp":0,"Parch":0,"Fare":72,"Embarked_C":0,
     "Embarked_Q":0,"Embarked_S":1,"FamilySize":1,"IsAlone":1}'
```

## 📈 Model Performance
| Metric | Score |
|--------|-------|
| Accuracy | 83.24% |
| Precision | 0.83 |
| Recall | 0.70 |
| F1 Score | 0.76 |

## 👤 Author
Your Name — [LinkedIn][(your-linkedin-url)](https://www.linkedin.com/in/chebattina-indra-sekhar-b3213030b/)] | [GitHub][(your-github-url)(https://github.com/Indra-sekhar)
