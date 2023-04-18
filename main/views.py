from django.shortcuts import render, HttpResponse
import pandas as pd
import numpy as np
import pickle as pkl

# Load the model from the file
car_model = pkl.load(open('LinearRegressionModelCar_Pred.pkl', 'rb'))

# craete df
car = pd.read_csv("cleaned car.csv")

# for i in car['name']:
#     print(i)

# Create your views here.

def Predict(company,c_model,year_pur,driven_car,fuel_type):
    # Prepare input data for prediction
    input_data = pd.DataFrame([[c_model,company, year_pur, driven_car, fuel_type]], columns=[
                              'name','company', 'year', 'kms_driven', 'fuel_type'])

# Make predictions
    predictions = car_model.predict(input_data)
    return str(np.round(predictions[0],2))


def home(request):
    car_companies = sorted(car['company'].unique())
    car_model = sorted(car['name'].unique())
    car_pur_year = sorted(car['year'].unique(), reverse=True)
    car_driven = sorted(car['kms_driven'].unique())
    car_fuel_type = sorted(car['fuel_type'].unique())
    Prediction=""
    company=""
    c_model=""
    year_pur=""
    fuel_type=""
    driven_car=""
    if request.method == "POST":
        company = request.POST.get('company')
        c_model = request.POST.get('car_model')
        year_pur = request.POST.get('year_pur')
        fuel_type = request.POST.get('fuel')
        driven_car = request.POST.get('killo_driven')
    
        # print(company, c_model, year_pur, fuel_type, driven_car)

        Prediction=Predict(company,c_model,year_pur,driven_car,fuel_type)
        print(Prediction)

    context = {
        'companies': car_companies,
        'model': car_model,
        'year': car_pur_year,
        'driven': car_driven,
        'fuel_type': car_fuel_type,
        'prediction':Prediction,
        'company':company,
        'cm':c_model,
        'yp':year_pur,
        'ft':fuel_type,
        'dc':driven_car
    }
    

    return render(request, "index.html", context)


##some prediction cars
def predicted_car(request):
    p=[]
    model_name=car['name'].head(12)
    model_name_df=car[['name','company','year','Price','kms_driven','fuel_type']].head(12)
    
    # print(model_name_df)    
    # for i in model_name_df:
    #     Predicts=Predict(i[0])
    # print(Predicts)    
    context={
        'mn':model_name,
    }
    return render(request, "predicted.html", context)
