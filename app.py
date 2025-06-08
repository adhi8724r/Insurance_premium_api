from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.user_input import UserInput
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()

@app.post('/predict')
def predict(data: UserInput):
    input = {
        'age' : data.age,
        'sex' : data.sex,
        'bmi'  : data.bmi,
        'smoker' : data.smoker,
        'region' : data.region,
        'children' : data.children
    }

    try:
        pred = predict_output(input)
        return JSONResponse(status_code=200, content={'predicted_premium':pred})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))


@app.get('/')
def welcome():
    return {'message':'welcome to insurance premium prediction API'}

@app.get('/health')
def health_check():
    return {
        'status':'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

