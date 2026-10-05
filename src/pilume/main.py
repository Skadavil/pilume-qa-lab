from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="PiLume QA Lab",
    version="0.1.0",
)

light_state = {
    "power": False,
    "brightness": 0,
    "red": 255,
    "green": 255,
    "blue": 255,
    "mode": "simulation",
}


class LightCommand(BaseModel):
    brightness: int = Field(ge=0, le=100)
    red: int = Field(ge=0, le=255)
    green: int = Field(ge=0, le=255)
    blue: int = Field(ge=0, le=255)


@app.get("/")
def home():
    return {
        "project": "PiLume QA Lab",
        "status": "running",
        "mode": "simulation",
    }


@app.get("/api/status")
def get_status():
    return light_state


@app.post("/api/light")
def set_light(command: LightCommand):
    light_state.update(command.model_dump())
    light_state["power"] = command.brightness > 0
    return light_state


@app.post("/api/light/off")
def switch_off():
    light_state["power"] = False
    light_state["brightness"] = 0
    return light_state
