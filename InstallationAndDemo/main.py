from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def hello():
    return {'message':"bigyajeet kumar patra"}

@app.get('/about')
def about():
    return {'message':"third year"}