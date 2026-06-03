const API = "http://127.0.0.1:8000";

// Input validation ranges matching backend
const VALID_RANGES = {
    weight: [0.1, 500],
    jump: [0.01, 10],
    distance: [0.1, 1000],
    radius: [100000, 1e9],
    mass: [1e20, 2e27]
};

// Create twinkling stars
function createStars() {
    const starsContainer = document.getElementById('stars');
    for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.width = Math.random() * 3 + 'px';
        star.style.height = star.style.width;
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 3 + 's';
        starsContainer.appendChild(star);
    }
}

createStars();

// Validate input is within expected range
function validateInput(element) {
    const value = parseFloat(element.value);
    const min = parseFloat(element.min);
    const max = parseFloat(element.max);
    
    if (value < min || value > max) {
        console.warn(`Input ${element.id} out of range: ${value}`);
        element.style.borderColor = '#ff6b6b';
        return false;
    }
    element.style.borderColor = '';
    return true;
}

// Update slider display value
function updateSlider(elementId, value, unit) {
    const element = document.getElementById(elementId);
    if (value >= 1e24) {
        element.textContent = parseFloat(value).toExponential(2) + unit;
    } else {
        element.textContent = parseFloat(value).toLocaleString() + unit;
    }
}

// Load planets on page load
async function loadPlanets() {
    try {
        const res = await fetch(`${API}/planets`);
        const data = await res.json();

        const select = document.getElementById("planetSelect");
        select.innerHTML = "";

        data.planets.forEach(p => {
            const option = document.createElement("option");
            option.value = p;
            option.textContent = p;
            select.appendChild(option);
        });
    } catch (error) {
        console.error("Error loading planets:", error);
        document.getElementById("planetResults").innerHTML =
            "⚠️ Unable to connect to the API. Make sure the server is running!";
    }
}

window.onload = loadPlanets;

async function loadPlanetData() {
    const planet = document.getElementById("planetSelect").value;
    document.getElementById("planetResults").innerHTML =
        `<div class="single-result">
                    <span class="single-result-icon">✨</span>
                    Selected planet: <b>${planet}</b>
                </div>`;
}

async function calculateWeight() {
    const w = parseFloat(document.getElementById("earthWeight").value);
    const planet = document.getElementById("planetSelect").value;

    if (!planet) {
        document.getElementById("weightResult").innerHTML =
            `<div class="error-message">⚠️ Please select a planet first</div>`;
        return;
    }

    try {
        const res = await fetch(`${API}/weight?earth_weight=${w}&planet=${planet}`);
        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.detail || "Invalid input");
        }

        document.getElementById("weightResult").innerHTML =
            `<div class="result-cards">
                        <div class="result-card">
                            <span class="result-card-icon">🌍</span>
                            <div class="result-card-label">Planet</div>
                            <div class="result-card-value">${planet}</div>
                        </div>
                        <div class="result-card">
                            <span class="result-card-icon">⚖️</span>
                            <div class="result-card-label">Your Weight</div>
                            <div class="result-card-value">${data.weight.toFixed(2)} N</div>
                        </div>
                    </div>`;
    } catch (error) {
        document.getElementById("weightResult").innerHTML =
            `<div class="error-message">⚠️ ${error.message || 'Error calculating weight'}</div>`;
    }
}

async function calculateJump() {
    const j = parseFloat(document.getElementById("earthJump").value);
    const planet = document.getElementById("planetSelect").value;

    if (!planet) {
        document.getElementById("jumpResult").innerHTML =
            `<div class="error-message">⚠️ Please select a planet first</div>`;
        return;
    }

    try {
        const res = await fetch(`${API}/jump_height?earth_jump=${j}&planet=${planet}`);
        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.detail || "Invalid input");
        }

        document.getElementById("jumpResult").innerHTML =
            `<div class="result-cards">
                        <div class="result-card">
                            <span class="result-card-icon">🌍</span>
                            <div class="result-card-label">Planet</div>
                            <div class="result-card-value">${planet}</div>
                        </div>
                        <div class="result-card">
                            <span class="result-card-icon">🦘</span>
                            <div class="result-card-label">Jump Height</div>
                            <div class="result-card-value">${data.jump_height.toFixed(2)} m</div>
                        </div>
                    </div>`;
    } catch (error) {
        document.getElementById("jumpResult").innerHTML =
            `<div class="error-message">⚠️ ${error.message || 'Error calculating jump height'}</div>`;
    }
}

async function calculateFall() {
    const d = parseFloat(document.getElementById("fallDistance").value);
    const planet = document.getElementById("planetSelect").value;

    if (!planet) {
        document.getElementById("fallResult").innerHTML =
            `<div class="error-message">⚠️ Please select a planet first</div>`;
        return;
    }

    try {
        const res = await fetch(`${API}/fall_time?distance=${d}&planet=${planet}`);
        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.detail || "Invalid input");
        }

        document.getElementById("fallResult").innerHTML =
            `<div class="result-cards">
                        <div class="result-card">
                            <span class="result-card-icon">🌍</span>
                            <div class="result-card-label">Planet</div>
                            <div class="result-card-value">${planet}</div>
                        </div>
                        <div class="result-card">
                            <span class="result-card-icon">⏱️</span>
                            <div class="result-card-label">Fall Time</div>
                            <div class="result-card-value">${data.fall_time.toFixed(2)} s</div>
                        </div>
                    </div>`;
    } catch (error) {
        document.getElementById("fallResult").innerHTML =
            `<div class="error-message">⚠️ ${error.message || 'Error calculating fall time'}</div>`;
    }
}

async function calculateEscape() {
    const planet = document.getElementById("planetSelect").value;

    if (!planet) {
        document.getElementById("escapeResult").innerHTML =
            `<div class="error-message">⚠️ Please select a planet first</div>`;
        return;
    }

    try {
        const res = await fetch(`${API}/escape_velocity?planet=${planet}`);
        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.detail || "Invalid input");
        }

        document.getElementById("escapeResult").innerHTML =
            `<div class="result-cards">
                        <div class="result-card">
                            <span class="result-card-icon">🌍</span>
                            <div class="result-card-label">Planet</div>
                            <div class="result-card-value">${planet}</div>
                        </div>
                        <div class="result-card">
                            <span class="result-card-icon">🚀</span>
                            <div class="result-card-label">Escape Velocity</div>
                            <div class="result-card-value">${(data.escape_velocity / 1000).toFixed(2)} km/s</div>
                        </div>
                    </div>`;
    } catch (error) {
        document.getElementById("escapeResult").innerHTML =
            `<div class="error-message">⚠️ ${error.message || 'Error calculating escape velocity'}</div>`;
    }
}

async function generateCustomPlanet() {
    const radius = parseFloat(document.getElementById("customRadius").value);
    const massRaw = document.getElementById("customMass").value;
    const mass = encodeURIComponent(massRaw);
    const ew = parseFloat(document.getElementById("customEarthWeight").value);
    const ej = parseFloat(document.getElementById("customEarthJump").value);
    const fd = parseFloat(document.getElementById("customFallDistance").value);

    try {
        const res = await fetch(
            `${API}/custom_planet?radius=${radius}&mass=${mass}&earth_weight=${ew}&earth_jump=${ej}&fall_distance=${fd}`
        );

        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.detail || "Invalid parameters");
        }

        document.getElementById("customResult").innerHTML =
            `<div class="result-cards">
                <div class="result-card">
                    <span class="result-card-icon">🌍</span>
                    <div class="result-card-label">Gravity</div>
                    <div class="result-card-value">${data.gravity.toFixed(2)} m/s²</div>
                </div>
                <div class="result-card">
                    <span class="result-card-icon">⚖️</span>
                    <div class="result-card-label">Your Weight</div>
                    <div class="result-card-value">${data.weight.toFixed(2)} N</div>
                </div>
                <div class="result-card">
                    <span class="result-card-icon">🦘</span>
                    <div class="result-card-label">Jump Height</div>
                    <div class="result-card-value">${data.jump_height.toFixed(2)} m</div>
                </div>
                <div class="result-card">
                    <span class="result-card-icon">⏱️</span>
                    <div class="result-card-label">Fall Time</div>
                    <div class="result-card-value">${data.fall_time.toFixed(2)} s</div>
                </div>
                <div class="result-card">
                    <span class="result-card-icon">🚀</span>
                    <div class="result-card-label">Escape Velocity</div>
                    <div class="result-card-value">${(data.escape_velocity / 1000).toFixed(2)} km/s</div>
                </div>
            </div>`;
    } catch (error) {
        document.getElementById("customResult").innerHTML =
            `<div class="error-message">⚠️ ${error.message || 'Error simulating custom planet'}</div>`;
    }
}
