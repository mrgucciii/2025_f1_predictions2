# app.py
from fastapi import FastAPI, HTTPException
import importlib

app = FastAPI(title="F1 Predictions API")

# حالياً عندنا سباق تجريبي فقط
RACE_MAP = {
    "monaco": "prediction_demo"
}

@app.get("/")
def root():
    return {"status": "ok", "message": "F1 Predictions API is running 🚀"}

@app.get("/predict")
def predict(race: str):
    mod_name = RACE_MAP.get(race.lower())
    if not mod_name:
        raise HTTPException(status_code=400, detail="Race not supported yet")
    try:
        mod = importlib.import_module(mod_name)
        if not hasattr(mod, "predict"):
            raise RuntimeError(f"{mod_name}.py missing predict()")
        return {"status": "ok", "data": mod.predict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
