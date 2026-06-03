# 🌍 Gravity Playground Simulator  
A U&I Science Fair Project

This project is a science-fair learning tool built for U&I.  
It allows students to explore how **gravity changes on different planets** by simulating:

- ⚖️ **Weight on different planets**  
- 🛠️ **Custom planet gravity** (user-defined mass & radius)  
- 🚀 **Escape velocity**  
- 🦘 **Jump height variation**  
- 🪂 **Fall time simulation**

The goal is to make space physics interactive, visual, and easy to understand for kids.

---

## 🚀 Tech Stack

### **Backend**
- **FastAPI** – REST API for physics calculations  
- **Python** – Gravity formulas & simulations  

### **Frontend**
- **HTML** – Semantic structure with accessibility labels  
- **CSS** – Custom UI with animations and responsive design  
- **JavaScript** – Fetch API calls + dynamic UI with validation  

---

## 📋 Features

✅ **Input Validation** - Client and server-side validation with clear error messages  
✅ **Accessibility** - ARIA labels, keyboard navigation, focus indicators, motion preferences  
✅ **Error Handling** - Descriptive error messages from API with proper HTTP status codes  
✅ **Physics Accuracy** - Uses real planetary data and proper SI units  
✅ **Interactive UI** - Real-time slider updates with visual feedback  
✅ **Custom Planets** - Create your own planets with custom mass and radius  

---

## 🛠️ Setup Instructions

### **Backend Setup**

#### Step 1: Navigate to backend directory
```bash
cd backend
```

#### Step 2: Create virtual environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Run backend server
```bash
uvicorn main:app --reload
```

The backend will be available at `http://127.0.0.1:8000`

**API Documentation:** http://127.0.0.1:8000/docs (auto-generated interactive docs)

---

### **Frontend Setup**

1. Navigate to the `frontend` folder
2. Open `index.html` with **Live Server** extension in VSCode
   - If not installed, search for "Live Server" in VSCode Extensions
   - Right-click `index.html` → "Open with Live Server"

The frontend will be available at `http://127.0.0.1:5500` (or the port Live Server assigns)

---

## 🎯 Project Structure

```
U-I-Gravity-Science-Fair/
├── backend/
│   ├── main.py           # FastAPI application with endpoints
│   ├── physics.py        # Physics calculations & validation
│   ├── requirements.txt   # Python dependencies
│   └── run.sh            # Script to start server
├── frontend/
│   ├── index.html        # HTML structure
│   ├── styles.css        # CSS styling & animations
│   └── script.js         # JavaScript with API calls
├── API_DOCUMENTATION.md  # Complete API reference
└── README.md             # This file
```

---

## 📚 Documentation

- **[API_DOCUMENTATION.md](./API_DOCUMENTATION.md)** - Complete API endpoint reference with examples
- **Backend Code** - Well-documented with docstrings and type hints
- **Frontend Code** - JSDoc comments for all functions
- **Code Comments** - Physics formulas and validation logic clearly explained

---

## 🧪 Testing the Application

### Test the Backend
```bash
# Get list of planets
curl "http://127.0.0.1:8000/planets"

# Calculate weight on Mars (70 kg person)
curl "http://127.0.0.1:8000/weight?earth_weight=70&planet=Mars"

# Calculate escape velocity for Jupiter
curl "http://127.0.0.1:8000/escape_velocity?planet=Jupiter"

# Create custom planet simulation
curl "http://127.0.0.1:8000/custom_planet?radius=6371000&mass=5.97e24&earth_weight=70&earth_jump=0.5&fall_distance=10"
```

### Test the Frontend
1. Start the backend (`uvicorn main:app --reload`)
2. Open frontend in Live Server
3. Try these interactions:
   - Select different planets and see how weight/jump height change
   - Use the sliders to adjust values (notice the validation)
   - Create a custom planet with extreme values (e.g., small radius, large mass)
   - Check console for validation warnings

---

## 🎓 Physics Reference

All calculations use **SI units** (meters, kilograms, seconds):

### Formulas Used

**Surface Gravity:**
```
g = (G × M) / R²
```

**Weight:**
```
Weight = mass × g
```

**Jump Height:**
```
Jump_height = earth_jump × (g_earth / g_planet)
```

**Fall Time:**
```
t = √(2 × distance / g)
```

**Escape Velocity:**
```
v = √((2 × G × M) / R)
```

### Constants

- **Universal Gravitational Constant (G):** 6.67430 × 10⁻¹¹ m³/(kg·s²)
- **Earth Gravity (g):** ~9.81 m/s²

### Planet Data

| Planet | Mass (kg) | Radius (m) |
|--------|-----------|-----------|
| Mercury | 3.30 × 10²³ | 2.44 × 10⁶ |
| Venus | 4.87 × 10²⁴ | 6.05 × 10⁶ |
| Earth | 5.97 × 10²⁴ | 6.37 × 10⁶ |
| Mars | 6.42 × 10²³ | 3.39 × 10⁶ |
| Jupiter | 1.90 × 10²⁷ | 6.99 × 10⁷ |
| Saturn | 5.68 × 10²⁶ | 5.82 × 10⁷ |
| Uranus | 8.68 × 10²⁵ | 2.54 × 10⁷ |
| Neptune | 1.02 × 10²⁶ | 2.47 × 10⁷ |

---

## 🚀 How It Works

### User Flow

1. **User opens the app** → Frontend loads planet list from API
2. **User selects a planet** → Frontend displays selected planet
3. **User adjusts sliders** → Real-time display updates, validation provides feedback
4. **User clicks "Calculate"** → Frontend calls API with parameters
5. **API validates input** → Returns error if out of range
6. **API calculates physics** → Returns results with precision
7. **Frontend displays results** → Shows cards with formatted values

### Error Handling

- **Backend:** Validates all inputs, returns HTTP 422 with detailed error messages
- **Frontend:** 
  - Validates input against min/max on change
  - Checks for planet selection before API calls
  - Displays backend error messages to users
  - Handles network errors gracefully

---

## 🎨 UI/UX Features

- **Animated Background** - Twinkling stars, floating planets, rocket animation
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Real-time Feedback** - Sliders show values as you move them
- **Visual Validation** - Red border appears when input is out of range
- **Clear Results** - Grid of cards with emoji icons for quick understanding
- **Accessible** - Full keyboard navigation, screen reader support, focus indicators

---

## 🔧 Development Tips

### Adding a New Planet
1. Add planet data to `PLANETS` dict in `backend/physics.py`
2. Format: `"Name": {"mass": value_in_kg, "radius": value_in_m}`
3. Restart the server - it auto-loads the new planet

### Modifying Validation Ranges
1. Edit `VALID_RANGES` in `backend/physics.py`
2. Update the frontend HTML `input` min/max/step attributes
3. Update hint text in `index.html`
4. Update `VALID_RANGES` in `frontend/script.js` for reference

### Running in Production
- Use a production ASGI server: `gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app`
- Deploy frontend to static hosting (Netlify, Vercel, GitHub Pages)
- Update API endpoint in frontend from `localhost:8000` to production URL

---

## 📝 License
This project is created for educational purposes as part of the U&I Science Fair.

---

## 🤝 Contributing
Contributions are welcome! Please ensure:
- New functions have docstrings/JSDoc comments
- Input validation is added for any new parameters
- Backend changes include error handling
- Frontend changes maintain accessibility standards

---

## 📞 Support
For questions or issues:
1. Check the [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)
2. Review the code comments and docstrings
3. Test with curl or browser DevTools to debug API issues
4. Check browser console for client-side errors


