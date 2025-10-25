/**
 * leapmotion_stub.js
 * ==========================================
 * Neural Holography Engine (NHE)
 * Leap Motion / Ultraleap Gesture Stub
 * ------------------------------------------
 *
 * Purpose:
 *   Simulate Leap Motion hand-tracking data for testing holographic controls.
 *   Generates mock hand positions, rotations, and pinch/zoom gestures.
 *
 * Integration:
 *   - Dispatches synthetic gesture events for hologram rotation, zoom, and close
 *   - Compatible with threejs_demo.js / alternative_rendering.js
 *   - Acts as placeholder for real Leap Motion WebSocket or WebXR API
 *
 * Author: Neural Systems Research Group (NHE)
 * Year: 2025
 */

// ============================================================
// 1️⃣ Stub Parameters
// ============================================================
const leapGestures = [
  { type: 'rotate', duration: 2500 },
  { type: 'zoom_in', duration: 1500 },
  { type: 'zoom_out', duration: 1500 },
  { type: 'close', duration: 1200 }
];

let currentIndex = 0;
let gestureActive = false;

// ============================================================
// 2️⃣ Event Dispatcher
// ============================================================
function dispatchLeapEvent(gestureType) {
  const event = new CustomEvent('leap-gesture', { detail: { type: gestureType } });
  window.dispatchEvent(event);
  console.log(`[LEAP STUB] Dispatched gesture: ${gestureType}`);
}

// ============================================================
// 3️⃣ Gesture Simulation Loop
// ============================================================
function simulateLeapGestures() {
  if (gestureActive) return;
  gestureActive = true;

  const gesture = leapGestures[currentIndex];
  dispatchLeapEvent(gesture.type);

  setTimeout(() => {
    gestureActive = false;
    currentIndex = (currentIndex + 1) % leapGestures.length;
    simulateLeapGestures();
  }, gesture.duration);
}

// ============================================================
// 4️⃣ Optional Visual Debugging
// ============================================================
//
// Display a small HUD or canvas showing hand gestures
const debugCanvas = document.createElement('canvas');
debugCanvas.width = 200;
debugCanvas.height = 200;
debugCanvas.style.position = 'absolute';
debugCanvas.style.top = '10px';
debugCanvas.style.right = '10px';
debugCanvas.style.border = '1px solid #0ff';
document.body.appendChild(debugCanvas);

const ctx = debugCanvas.getContext('2d');

function drawDebug(gestureType) {
  ctx.clearRect(0, 0, debugCanvas.width, debugCanvas.height);
  ctx.fillStyle = '#00ffff';
  ctx.font = '16px Arial';
  ctx.fillText(`Leap Gesture: ${gestureType}`, 10, 50);
}

// Extend dispatchLeapEvent to include debug drawing
function dispatchLeapEventWithDebug(gestureType) {
  drawDebug(gestureType);
  dispatchLeapEvent(gestureType);
}

// Replace old loop with debug-enabled loop
function simulateLeapGesturesDebug() {
  if (gestureActive) return;
  gestureActive = true;

  const gesture = leapGestures[currentIndex];
  dispatchLeapEventWithDebug(gesture.type);

  setTimeout(() => {
    gestureActive = false;
    currentIndex = (currentIndex + 1) % leapGestures.length;
    simulateLeapGesturesDebug();
  }, gesture.duration);
}

// ============================================================
// 5️⃣ Initialization
// ============================================================
window.addEventListener('load', () => {
  console.log('[INFO] Leap Motion Gesture Stub initialized.');
  simulateLeapGesturesDebug();
});

// ============================================================
// 6️⃣ Developer Info
// ============================================================
console.log(`
[Neural Holography Engine: Leap Motion Stub Active]
 - Mode: Simulated IR hand tracking
 - Supported Gestures: rotate, zoom_in, zoom_out, close
 - Integration: Dispatches "leap-gesture" events
 - Visual Debug: On-screen HUD
 - Replaceable with: Real Ultraleap WebSocket or WebXR API
`);
