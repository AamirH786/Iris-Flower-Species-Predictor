# views.py
from django.shortcuts import render
from joblib import load

#Loading Model
model = load('savedModel/model.joblib')

def Predictor(request):
    return render(request, 'index.html')

def FormInfo(request):
    try:
        sepal_length = float(request.GET['Slength'])
        sepal_width = float(request.GET['Swidth'])
        petal_length = float(request.GET['Plength'])
        petal_width = float(request.GET['Pwidth'])
        
        predicts = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        
        if predicts[0] == 'setosa':
            result = 'SETOSA'
        elif predicts[0] == 'versicolor':
            result = 'VERSICOLOR'
        else:
            result = 'VIRGINICA'
            
        return render(request, 'result.html', {'result': result})
    except (KeyError, ValueError) as e:
        error_message = "Invalid input: {}".format(str(e))
        return render(request, 'error.html', {'error_message': error_message})
    except Exception as e:
        error_message = "An error occurred: {}".format(str(e))
        return render(request, 'error.html', {'error_message': error_message})

