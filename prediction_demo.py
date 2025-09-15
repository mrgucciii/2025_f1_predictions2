# prediction_demo.py — مجرد توقعات ثابتة للتجربة
def predict():
    return {
        "race": "Monaco GP (Demo)",
        "mae": 2.9,
        "predictions": [
            {"driver": "Max Verstappen", "position": 1, "pred_time_s": 72.12},
            {"driver": "Charles Leclerc", "position": 2, "pred_time_s": 72.40},
            {"driver": "Lando Norris", "position": 3, "pred_time_s": 72.85}
        ]
    }

if __name__ == "__main__":
    print(predict())
