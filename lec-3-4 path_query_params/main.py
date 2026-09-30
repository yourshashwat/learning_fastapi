from fastapi import FastAPI, Path, HTTPException, Query
import json
app= FastAPI()

@app.get("/")
def hello():
    return {"msg": "Patient information dashboard"}

@app.get("/about")
def about():
    return {"msg": "All the details about a patient is available"}

def load_data():
    with open('patients.json', 'r') as f:
        data= json.load(f)
    return data

@app.get("/view")
def view():
    data= load_data()
    return data

@app.get("/patients/{patiend_id}")
def getPatientData(patient_id:str = Path(..., description="Get information about a unique patient using patiend id. eg:P001 ")):
    data= load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(sort_by:str= Query(default='height', description="Sort on the basis of height, weight or BMI"),
                  order:str= Query(default='asc', description="asc for ascending, desc for descending")):
    data= load_data()
    valid_field=['height', 'weight', 'bmi']
    valid_order=['asc','desc']
    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail=f"Option not in {valid_field}")
    if order not in valid_order:
        raise HTTPException(status_code=400, detail=f"Option not in {valid_order}")
    rev= True if order=='desc' else False
    sorted_= sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=rev)
    print(data.values())
    return sorted_