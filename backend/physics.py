"""
physics.py  
This module contains all physics formulas used in the Gravity Playground Simulator.
Everything is written clearly so students and beginners can understand the logic.

Physics Reference:
- All values use SI units (meters, kilograms, seconds)
- Gravitational constant G = 6.67430e-11 m³/(kg·s²)
- Surface gravity: g = (G × M) / R²
- Weight: W = m × g
- Escape velocity: v = √(2GM/R)
"""

import math

# --------------------------------------------
# UNIVERSAL CONSTANTS
# --------------------------------------------

# Universal gravitational constant (m^3 / kg / s^2)
G = 6.67430e-11

# Valid ranges for input validation
VALID_RANGES = {
    "weight": (0.1, 500),  # kg
    "jump": (0.01, 10),    # m
    "distance": (0.1, 1000),  # m
    "radius": (100000, 1e9),  # m (100 km to 1 billion m)
    "mass": (1e20, 2e27),  # kg
}

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
# Validation Functions
# --------------------------------------------

def validate_value(value: float, min_val: float, max_val: float, name: str) -> None:
    """
    Validates that a value is within acceptable range.
    
    Args:
        value: The value to check
        min_val: Minimum allowed value
        max_val: Maximum allowed value
        name: Name of the parameter (for error messages)
    
    Raises:
        ValueError: If value is outside the valid range or is NaN/Inf
    """
    # Check for NaN or Inf
    if not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number, got {value}")
    
    if value < min_val or value > max_val:
        raise ValueError(
            f"{name} must be between {min_val} and {max_val}, got {value}"
        )

def validate_planet(planet: str) -> None:
    """
    Validates that the planet name exists.
    
    Args:
        planet: Planet name to validate
    
    Raises:
        ValueError: If planet doesn't exist
    """
    if planet not in PLANETS:
        raise ValueError(
            f"Unknown planet '{planet}'. Valid planets: {', '.join(PLANETS.keys())}"
        )

# --------------------------------------------
# 1. Surface Gravity
# --------------------------------------------

def surface_gravity(mass: float, radius: float) -> float:
    """
    Computes the gravitational acceleration (g)
    using: g = (G * mass) / radius^2
    
    Args:
        mass: Planet mass in kg
        radius: Planet radius in meters
    
    Returns:
        Surface gravity in m/s²
    """
    if radius == 0:
        raise ValueError("Radius cannot be zero")
    return G * mass / (radius ** 2)

# --------------------------------------------
# 2. Weight on Another Planet
# --------------------------------------------

def weight_on_planet(earth_weight: float, planet: str) -> float:
    """
    Computes a user's weight on a different planet by scaling with gravity ratio.
    
    Args:
        earth_weight: User's weight in kg on Earth
        planet: Name of the target planet
    
    Returns:
        Weight in Newtons on the target planet
    
    Raises:
        ValueError: If inputs are invalid
    """
    validate_value(earth_weight, *VALID_RANGES["weight"], "Weight")
    validate_planet(planet)
    
    g_earth = surface_gravity(PLANETS["Earth"]["mass"], PLANETS["Earth"]["radius"])
    g_planet = surface_gravity(PLANETS[planet]["mass"], PLANETS[planet]["radius"])

    return earth_weight * (g_planet / g_earth)

# --------------------------------------------
# 3. Escape Velocity
# --------------------------------------------

def escape_velocity(mass: float, radius: float) -> float:
    """
    Computes escape velocity: v = sqrt(2GM / R)
    
    Args:
        mass: Planet mass in kg
        radius: Planet radius in meters
    
    Returns:
        Escape velocity in m/s
    
    Raises:
        ValueError: If inputs are invalid
    """
    if radius == 0:
        raise ValueError("Radius cannot be zero")
    return math.sqrt((2 * G * mass) / radius)

# --------------------------------------------
# 4. Jump Height Scaling
# --------------------------------------------

def jump_height(earth_jump: float, planet: str) -> float:
    """
    Computes new jump height by scaling with gravity ratio.
    
    Args:
        earth_jump: Jump height on Earth in meters
        planet: Name of the target planet
    
    Returns:
        Jump height on the target planet in meters
    
    Raises:
        ValueError: If inputs are invalid
    """
    validate_value(earth_jump, *VALID_RANGES["jump"], "Jump height")
    validate_planet(planet)
    
    g_earth = surface_gravity(PLANETS["Earth"]["mass"], PLANETS["Earth"]["radius"])
    g_planet = surface_gravity(PLANETS[planet]["mass"], PLANETS[planet]["radius"])

    if g_planet == 0:
        raise ValueError("Planet gravity cannot be zero")
    
    return earth_jump * (g_earth / g_planet)

# --------------------------------------------
# 5. Free-Fall Time
# --------------------------------------------

def fall_time(distance: float, planet: str) -> float:
    """
    Computes fall time: distance = (1/2) g t^2 => t = sqrt(2d/g)
    
    Args:
        distance: Fall distance in meters
        planet: Name of the planet
    
    Returns:
        Fall time in seconds
    
    Raises:
        ValueError: If inputs are invalid
    """
    validate_value(distance, *VALID_RANGES["distance"], "Distance")
    validate_planet(planet)
    
    g = surface_gravity(PLANETS[planet]["mass"], PLANETS[planet]["radius"])
    if g == 0:
        raise ValueError("Planet gravity cannot be zero")
    
    return math.sqrt((2 * distance) / g)

# --------------------------------------------
# 6. Custom Planet Stats
# --------------------------------------------

def custom_planet_stats(
    radius: float,
    mass: float,
    earth_weight: float,
    earth_jump: float,
    fall_distance: float
) -> dict:
    """
    Computes all values for a user-defined planet:
    - gravity
    - weight
    - jump height
    - fall time
    - escape velocity
    
    Args:
        radius: Custom planet radius in meters
        mass: Custom planet mass in kg
        earth_weight: User weight on Earth in kg
        earth_jump: User jump height on Earth in meters
        fall_distance: Fall distance in meters
    
    Returns:
        Dictionary with all calculated values
    
    Raises:
        ValueError: If any input is invalid
    """
    validate_value(radius, *VALID_RANGES["radius"], "Radius")
    validate_value(mass, *VALID_RANGES["mass"], "Mass")
    validate_value(earth_weight, *VALID_RANGES["weight"], "Weight")
    validate_value(earth_jump, *VALID_RANGES["jump"], "Jump height")
    validate_value(fall_distance, *VALID_RANGES["distance"], "Distance")
    
    g_custom = surface_gravity(mass, radius)
    g_earth = surface_gravity(PLANETS["Earth"]["mass"], PLANETS["Earth"]["radius"])

    if g_custom == 0:
        raise ValueError("Custom planet gravity cannot be zero")

    return {
        "gravity": g_custom,
        "weight": earth_weight * (g_custom / g_earth),
        "jump_height": earth_jump * (g_earth / g_custom),
        "fall_time": math.sqrt((2 * fall_distance) / g_custom),
        "escape_velocity": escape_velocity(mass, radius),
    }
