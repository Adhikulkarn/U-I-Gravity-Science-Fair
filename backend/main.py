"""
main.py
FastAPI backend for the Gravity Playground Simulator.

This server provides REST endpoints for physics calculations related to gravity,
weight, jump height, fall time, and escape velocity on different planets.

Architecture:
- FastAPI application with CORS enabled for frontend communication
- Input validation on all parameters with clear error messages
- Consistent error handling with HTTP status codes (422 for validation errors)
- Physics calculations delegated to physics.py module
- All values use SI units throughout

Endpoints:
- GET /                  - Server status
- GET /planets           - List available planets
- GET /weight            - Calculate weight on a planet
- GET /escape_velocity   - Calculate escape velocity
- GET /jump_height       - Calculate jump height on a planet
- GET /fall_time         - Calculate fall time for a distance
- GET /custom_planet     - Calculate all values for a custom planet

Running the server:
    uvicorn main:app --reload

The server will be available at http://127.0.0.1:8000
Interactive API docs available at http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
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

# Error handler for validation errors
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    """Handle validation errors with proper HTTP response."""
    return JSONResponse(
        status_code=422,
        content={"detail": str(exc)}
    )

# Error handler for all other errors
@app.exception_handler(Exception)
async def general_error_handler(request, exc):
    """Handle unexpected errors."""
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred"}
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
    """Calculate weight on another planet."""
    try:
        result = weight_on_planet(earth_weight, planet)
        return {"planet": planet, "weight": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except KeyError:
        raise HTTPException(
            status_code=422,
            detail=f"Unknown planet: {planet}"
        )

# --------------------------------------------
# Escape Velocity Endpoint
# --------------------------------------------
@app.get("/escape_velocity")
def api_escape_velocity(planet: str):
    """Calculate escape velocity for a planet."""
    try:
        p = PLANETS[planet]
        result = escape_velocity(p["mass"], p["radius"])
        return {
            "planet": planet,
            "escape_velocity": result
        }
    except KeyError:
        raise HTTPException(
            status_code=422,
            detail=f"Unknown planet: {planet}"
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

# --------------------------------------------
# Jump Height Endpoint
# --------------------------------------------
@app.get("/jump_height")
def api_jump(earth_jump: float, planet: str):
    """Calculate jump height on another planet."""
    try:
        result = jump_height(earth_jump, planet)
        return {"planet": planet, "jump_height": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except KeyError:
        raise HTTPException(
            status_code=422,
            detail=f"Unknown planet: {planet}"
        )

# --------------------------------------------
# Fall Time Endpoint
# --------------------------------------------
@app.get("/fall_time")
def api_fall(distance: float, planet: str):
    """Calculate fall time on a planet."""
    try:
        result = fall_time(distance, planet)
        return {"planet": planet, "fall_time": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except KeyError:
        raise HTTPException(
            status_code=422,
            detail=f"Unknown planet: {planet}"
        )

# --------------------------------------------
# Custom Planet Endpoint
# --------------------------------------------
@app.get("/custom_planet")
def api_custom(
    radius: float,
    mass: Union[str, float],
    earth_weight: float,
    earth_jump: float,
    fall_distance: float
):
    """Calculate all physics values for a custom planet."""
    try:
        # Convert mass safely
        try:
            mass = float(mass)
        except (ValueError, TypeError):
            raise HTTPException(
                status_code=422,
                detail="Invalid mass value. Must be numeric (supports scientific notation)."
            )
        
        result = custom_planet_stats(radius, mass, earth_weight, earth_jump, fall_distance)
        return result
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
