# Gravity Playground API Documentation

## Base URL
```
http://127.0.0.1:8000
```

## Overview
The Gravity Playground API provides physics calculations for simulating gravity on different planets and custom celestial bodies. All endpoints return JSON responses.

## Error Handling

All endpoints follow consistent error handling:

### Success Response (2xx)
```json
{
  "field1": value1,
  "field2": value2
}
```

### Error Response (4xx/5xx)
```json
{
  "detail": "Error description"
}
```

**Common Status Codes:**
- `200 OK` - Request successful
- `422 Unprocessable Entity` - Invalid input parameters (out of range, invalid planet, etc.)
- `500 Internal Server Error` - Unexpected server error

## Endpoints

### GET /

Get API status and confirmation that the server is running.

**Response:**
```json
{
  "message": "Gravity Playground API is running!"
}
```

---

### GET /planets

Get the list of all available planets.

**Response:**
```json
{
  "planets": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
}
```

---

### GET /weight

Calculate the weight of an object on another planet.

**Parameters:**
- `earth_weight` (float, required): Object's mass on Earth in kg
  - Valid range: 0.1 - 500 kg
- `planet` (string, required): Target planet name (from /planets endpoint)

**Response:**
```json
{
  "planet": "Mars",
  "weight": 26.58
}
```

**Example Request:**
```
GET /weight?earth_weight=70&planet=Mars
```

**Error Examples:**
- Out of range: `{"detail": "Weight must be between 0.1 and 500, got 600"}`
- Invalid planet: `{"detail": "Unknown planet 'Pluto'. Valid planets: Mercury, Venus, Earth, ..."}`

---

### GET /escape_velocity

Calculate the escape velocity for a planet.

**Parameters:**
- `planet` (string, required): Planet name (from /planets endpoint)

**Response:**
```json
{
  "planet": "Jupiter",
  "escape_velocity": 59500.0
}
```

**Example Request:**
```
GET /escape_velocity?planet=Jupiter
```

**Notes:**
- Escape velocity is in m/s
- Multiply by 3.6 to convert to km/h, or divide by 1000 for km/s

---

### GET /jump_height

Calculate how high an object would jump on another planet.

**Parameters:**
- `earth_jump` (float, required): Jump height on Earth in meters
  - Valid range: 0.01 - 10 m
- `planet` (string, required): Target planet name (from /planets endpoint)

**Response:**
```json
{
  "planet": "Moon",
  "jump_height": 3.05
}
```

**Example Request:**
```
GET /jump_height?earth_jump=0.5&planet=Moon
```

---

### GET /fall_time

Calculate how long it takes for an object to fall a given distance on another planet.

**Parameters:**
- `distance` (float, required): Fall distance in meters
  - Valid range: 0.1 - 1000 m
- `planet` (string, required): Target planet name (from /planets endpoint)

**Response:**
```json
{
  "planet": "Mars",
  "fall_time": 2.45
}
```

**Example Request:**
```
GET /fall_time?distance=10&planet=Mars
```

---

### GET /custom_planet

Calculate all physics values for a custom planet.

**Parameters:**
- `radius` (float, required): Planet radius in meters
  - Valid range: 100,000 - 1,000,000,000 m
- `mass` (float or string, required): Planet mass in kg (supports scientific notation)
  - Valid range: 1e20 - 2e27 kg
  - Examples: `1.5e24`, `5.97e24`
- `earth_weight` (float, required): Object's mass on Earth in kg
  - Valid range: 0.1 - 500 kg
- `earth_jump` (float, required): Jump height on Earth in meters
  - Valid range: 0.01 - 10 m
- `fall_distance` (float, required): Fall distance in meters
  - Valid range: 0.1 - 1000 m

**Response:**
```json
{
  "gravity": 9.81,
  "weight": 70.0,
  "jump_height": 0.5,
  "fall_time": 1.43,
  "escape_velocity": 11200.0
}
```

**Example Request:**
```
GET /custom_planet?radius=6371000&mass=5.97e24&earth_weight=70&earth_jump=0.5&fall_distance=10
```

**Notes:**
- All physics values are returned in SI units (m/s², N, m, s, m/s)
- The mass parameter can include the "+" character in scientific notation, which is properly URL-encoded by the client

---

## Validation Rules

All endpoints validate input parameters:

### Parameter Constraints
| Parameter | Min | Max | Unit |
|-----------|-----|-----|------|
| earth_weight | 0.1 | 500 | kg |
| earth_jump | 0.01 | 10 | m |
| distance | 0.1 | 1000 | m |
| radius | 100,000 | 1e9 | m |
| mass | 1e20 | 2e27 | kg |

### Error Messages
- **Out of range**: Returns 422 with message like `"Weight must be between 0.1 and 500, got 600"`
- **Invalid planet**: Returns 422 with message like `"Unknown planet 'Pluto'. Valid planets: Mercury, Venus, ..."`
- **Invalid mass format**: Returns 422 with message `"Invalid mass value. Must be numeric (supports scientific notation)."`

---

## Usage Examples

### JavaScript/Fetch
```javascript
// Get weight on Mars
const response = await fetch('http://127.0.0.1:8000/weight?earth_weight=70&planet=Mars');
const data = await response.json();
console.log(`Weight on Mars: ${data.weight.toFixed(2)} N`);

// Handle errors
if (!response.ok) {
  console.error(`Error: ${data.detail}`);
}
```

### Python/Requests
```python
import requests

response = requests.get('http://127.0.0.1:8000/weight', params={
    'earth_weight': 70,
    'planet': 'Mars'
})

if response.status_code == 200:
    print(f"Weight on Mars: {response.json()['weight']:.2f} N")
else:
    print(f"Error: {response.json()['detail']}")
```

### cURL
```bash
curl "http://127.0.0.1:8000/weight?earth_weight=70&planet=Mars"
```

---

## Constants Used

### Universal Gravitational Constant
- **G** = 6.67430 × 10⁻¹¹ m³/(kg·s²)

### Planet Data
| Planet | Mass (kg) | Radius (m) |
|--------|-----------|-----------|
| Mercury | 3.30e23 | 2.44e6 |
| Venus | 4.87e24 | 6.05e6 |
| Earth | 5.97e24 | 6.37e6 |
| Mars | 6.42e23 | 3.39e6 |
| Jupiter | 1.90e27 | 6.99e7 |
| Saturn | 5.68e26 | 5.82e7 |
| Uranus | 8.68e25 | 2.54e7 |
| Neptune | 1.02e26 | 2.47e7 |

---

## Physics Formulas

### Surface Gravity
```
g = (G × M) / R²
```

### Weight
```
Weight = mass × g_planet
```

### Jump Height
```
Jump_height = earth_jump × (g_earth / g_planet)
```

### Fall Time
```
fall_time = √(2 × distance / g)
```

### Escape Velocity
```
v_escape = √((2 × G × M) / R)
```
