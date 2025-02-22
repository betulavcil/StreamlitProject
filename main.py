
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from sklearn.exceptions import ConvergenceWarning
import warnings

warnings.simplefilter("ignore", category=ConvergenceWarning)
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 150)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


def prepare_data(df):

    df.info()

    # Exercise_Induced_Angina: Anjina pektoris, genellikle kalp kasındaki iskemi
    # veya koroner arter spazmı nedeniyle oluşan göğüste ağrı, sıkışma ve baskı hissi.
    #  0 : No,  1: Yes

    df = df.drop(['Physical_Activity_Level', 'BMI', 'Hypertension',
                            'Cholesterol_Level', 'Resting_BP', 'Heart_Rate', 'Stress_Level', 'Chest_Pain_Type', 'Thalassemia',
                            'ECG_Results', 'Max_Heart_Rate_Achieved'], axis=1)

    df["Gender"] = df["Gender"].map({'Male': 0, 'Female': 1})

    df.head(5)
    return df

def model(dataset):

    y = dataset["Heart_Attack_Risk"]
    X = dataset.drop(["Heart_Attack_Risk"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=17)




    classifier = RandomForestClassifier(n_estimators=10, criterion='gini', random_state=0)
    classifier.fit(X_train, y_train)

    random_forest_predictions = classifier.predict(X_test)
   # print("Random Forest Predictions:", random_forest_predictions)
    random_forest_accuracy = accuracy_score(y_test, random_forest_predictions)
    print("Random Forest Accuracy:", random_forest_accuracy)
    fmodel = classifier.fit(X_train, y_train)
    return fmodel

def main():

    dataset = pd.read_csv('heart_attack_risk_dataset.csv')
    dataset = prepare_data(dataset)
    final_model = model(dataset)
    joblib.dump(final_model, "final_model.pkl")
    return final_model


if __name__ == "__main__":
    print("İşlem başladı")
    main()









