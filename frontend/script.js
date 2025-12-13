const API = "http://127.0.0.1:8000";

// Update slider label
function updateSlider(id, value, unit) {
    document.getElementById(id).textContent = value + unit;
}

// Load planets
async function loadPlanets() {
    try {
        const res = await fetch(`${API}/planets`);
        const data = await res.json();

        const select = document.getElementById("planetSelect");
        select.innerHTML = "";

        data.planets.forEach(p => {
            const opt = document.createElement("option");
            opt.value = p;
            opt.textContent = p;
            select.appendChild(opt);
        });
    } catch (e) {
        document.getElementById("planetResults").innerHTML =
            "Error loading planets.";
    }
}
window.onload = loadPlanets;

// Show selected planet
function loadPlanetData() {
    const p = document.getElementById("planetSelect").value;
    document.getElementById("planetResults").textContent =
        "Selected Planet: " + p;
}

// Weight
async function calculateWeight() {
    const mass = document.getElementById("earthWeight").value;
    const planet = document.getElementById("planetSelect").value;

    try {
        const res = await fetch(`${API}/weight?earth_weight=${mass}&planet=${planet}`);
        const data = await res.json();

        document.getElementById("weightResult").textContent =
            `Weight on ${planet}: ${data.weight.toFixed(2)} N`;
    } catch {
        document.getElementById("weightResult").textContent = "Error.";
    }
}

// Jump
async function calculateJump() {
    const j = document.getElementById("earthJump").value;
    const p = document.getElementById("planetSelect").value;

    try {
        const res = await fetch(`${API}/jump_height?earth_jump=${j}&planet=${p}`);
        const data = await res.json();

        document.getElementById("jumpResult").textContent =
            `Jump Height on ${p}: ${data.jump_height.toFixed(2)} m`;
    } catch {
        document.getElementById("jumpResult").textContent = "Error.";
    }
}

// Fall Time
async function calculateFall() {
    const d = document.getElementById("fallDistance").value;
    const p = document.getElementById("planetSelect").value;

    try {
        const res = await fetch(`${API}/fall_time?distance=${d}&planet=${p}`);
        const data = await res.json();

        document.getElementById("fallResult").textContent =
            `Fall Time on ${p}: ${data.fall_time.toFixed(2)} s`;
    } catch {
        document.getElementById("fallResult").textContent = "Error.";
    }
}

// Escape Velocity
async function calculateEscape() {
    const p = document.getElementById("planetSelect").value;

    try {
        const res = await fetch(`${API}/escape_velocity?planet=${p}`);
        const data = await res.json();

        document.getElementById("escapeResult").textContent =
            `Escape Velocity: ${(data.escape_velocity / 1000).toFixed(2)} km/s`;
    } catch {
        document.getElementById("escapeResult").textContent = "Error.";
    }
}

// Custom Planet
async function generateCustomPlanet() {
    const r = document.getElementById("customRadius").value;
    const m = encodeURIComponent(document.getElementById("customMass").value);
    const w = document.getElementById("customEarthWeight").value;
    const j = document.getElementById("customEarthJump").value;
    const fd = document.getElementById("customFallDistance").value;

    try {
        const res = await fetch(
            `${API}/custom_planet?radius=${r}&mass=${m}&earth_weight=${w}&earth_jump=${j}&fall_distance=${fd}`
        );
        const data = await res.json();

        document.getElementById("customResult").innerHTML =
            `Gravity: ${data.gravity.toFixed(2)} m/s²<br>
             Weight: ${data.weight.toFixed(2)} N<br>
             Jump Height: ${data.jump_height.toFixed(2)} m<br>
             Fall Time: ${data.fall_time.toFixed(2)} s<br>
             Escape Velocity: ${(data.escape_velocity/1000).toFixed(2)} km/s`;
    } catch {
        document.getElementById("customResult").textContent = "Error.";
    }
}
