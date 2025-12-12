"""
main.py
This file creates the FastAPI backend for the Gravity Playground Simulator.
"""

from fastapi import FastAPI, HTTPException
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from physics import (
    PLANETS,
    weight_on_planet,
    escape_velocity,
    jump_height,
    fall_time,
    custom_planet_stats
)

app = FastAPI(
    title="Gravity Playground API",
    description="A simple physics simulator backend for kids to explore gravity.",
    version="1.0.0"
)

# --------------------------------------------
# CORS
# --------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------
# Root Endpoint
# --------------------------------------------
@app.get("/")
def home():
    return {"message": "Gravity Playground API is running!"}

# --------------------------------------------
# Get list of planets
# --------------------------------------------
@app.get("/planets")
def get_planets():
    return {"planets": list(PLANETS.keys())}

# --------------------------------------------
# Weight Endpoint
# --------------------------------------------
@app.get("/weight")
def api_weight(earth_weight: float, planet: str):
    return {"planet": planet, "weight": weight_on_planet(earth_weight, planet)}

# --------------------------------------------
# Escape Velocity Endpoint
# --------------------------------------------
@app.get("/escape_velocity")
def api_escape_velocity(planet: str):
    p = PLANETS[planet]
    return {
        "planet": planet,
        "escape_velocity": escape_velocity(p["mass"], p["radius"])
    }

# --------------------------------------------
# Jump Height Endpoint
# --------------------------------------------
@app.get("/jump_height")
def api_jump(earth_jump: float, planet: str):
    return {"planet": planet, "jump_height": jump_height(earth_jump, planet)}

# --------------------------------------------
# Fall Time Endpoint
# --------------------------------------------
@app.get("/fall_time")
def api_fall(distance: float, planet: str):
    return {"planet": planet, "fall_time": fall_time(distance, planet)}

# --------------------------------------------
# Custom Planet Endpoint (FIXED)
# --------------------------------------------
@app.get("/custom_planet")
def api_custom(
    radius: float,
    mass: Union[str, float],   # <-- ORDER FIXED (str FIRST)
    earth_weight: float,
    earth_jump: float,
    fall_distance: float
):
    # Convert mass safely no matter what format it's in
    try:
        mass = float(mass)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail="Invalid mass value. Must be numeric (supports scientific notation)."
        )

    return custom_planet_stats(radius, mass, earth_weight, earth_jump, fall_distance)
