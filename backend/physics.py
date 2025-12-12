"""
physics.py  
This module contains all physics formulas used in the Gravity Playground Simulator.
Everything is written clearly so students and beginners can understand the logic.
"""

import math

# --------------------------------------------
# UNIVERSAL CONSTANTS
# --------------------------------------------

# Universal gravitational constant (m^3 / kg / s^2)
G = 6.67430e-11

# --------------------------------------------
# PLANET DATA (Mass in kg, Radius in meters)
# --------------------------------------------

PLANETS = {
    "Mercury": {"mass": 3.30e23, "radius": 2.44e6},
    "Venus": {"mass": 4.87e24, "radius": 6.05e6},
    "Earth": {"mass": 5.97e24, "radius": 6.37e6},
    "Mars": {"mass": 6.42e23, "radius": 3.39e6},
    "Jupiter": {"mass": 1.90e27, "radius": 6.99e7},
    "Saturn": {"mass": 5.68e26, "radius": 5.82e7},
    "Uranus": {"mass": 8.68e25, "radius": 2.54e7},
    "Neptune": {"mass": 1.02e26, "radius": 2.47e7},
}

# --------------------------------------------
# 1. Surface Gravity
# --------------------------------------------

def surface_gravity(mass, radius):
    """
    Computes the gravitational acceleration (g)
    using: g = (G * mass) / radius^2
    """
    return G * mass / (radius ** 2)

# --------------------------------------------
# 2. Weight on Another Planet
# --------------------------------------------

def weight_on_planet(earth_weight, planet):
    """
    Computes a user's weight on a different planet by scaling with gravity ratio.
    """
    g_earth = surface_gravity(PLANETS["Earth"]["mass"], PLANETS["Earth"]["radius"])
    g_planet = surface_gravity(PLANETS[planet]["mass"], PLANETS[planet]["radius"])

    return earth_weight * (g_planet / g_earth)

# --------------------------------------------
# 3. Escape Velocity
# --------------------------------------------

def escape_velocity(mass, radius):
    """
    Computes escape velocity: v = sqrt(2GM / R)
    """
    return math.sqrt((2 * G * mass) / radius)

# --------------------------------------------
# 4. Jump Height Scaling
# --------------------------------------------

def jump_height(earth_jump, planet):
    """
    Computes new jump height by scaling with gravity ratio.
    """
    g_earth = surface_gravity(PLANETS["Earth"]["mass"], PLANETS["Earth"]["radius"])
    g_planet = surface_gravity(PLANETS[planet]["mass"], PLANETS[planet]["radius"])

    return earth_jump * (g_earth / g_planet)

# --------------------------------------------
# 5. Free-Fall Time
# --------------------------------------------

def fall_time(distance, planet):
    """
    Computes fall time: distance = (1/2) g t^2 => t = sqrt(2d/g)
    """
    g = surface_gravity(PLANETS[planet]["mass"], PLANETS[planet]["radius"])
    return math.sqrt((2 * distance) / g)

# --------------------------------------------
# 6. Custom Planet Stats
# --------------------------------------------

def custom_planet_stats(radius, mass, earth_weight, earth_jump, fall_distance):
    """
    Computes all values for a user-defined planet:
    - gravity
    - weight
    - jump height
    - fall time
    - escape velocity
    """
    g_custom = surface_gravity(mass, radius)
    g_earth = surface_gravity(PLANETS["Earth"]["mass"], PLANETS["Earth"]["radius"])

    return {
        "gravity": g_custom,
        "weight": earth_weight * (g_custom / g_earth),
        "jump_height": earth_jump * (g_earth / g_custom),
        "fall_time": math.sqrt((2 * fall_distance) / g_custom),
        "escape_velocity": escape_velocity(mass, radius),
    }
