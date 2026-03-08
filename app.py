from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("car_price_pipeline.pkl")

class CarInput(BaseModel):

    Manufacturer: str
    Category: str

    Leather_interior: str = Field(alias="Leather interior")
    Fuel_type: str = Field(alias="Fuel type")
    Engine_volume: float = Field(alias="Engine volume")
    Gear_box_type: str = Field(alias="Gear box type")
    Drive_wheels: str = Field(alias="Drive wheels")

    Mileage: int
    Cylinders: int
    Doors: int

    Wheel: str
    Color: str
    Airbags: int
    Levy: float
    Car_Age: int


@app.post("/predict")
def predict(car: CarInput):

    input_dict = car.dict(by_alias=True)

    input_df = pd.DataFrame([input_dict])
    print(input_df)

    prediction = model.predict(input_df)

    return {"Predicted Price": float(prediction[0])}