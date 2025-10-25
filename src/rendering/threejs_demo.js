/**
 * threejs_demo.js
 * ============================
 * Neural Holography Engine (NHE) — 3D Web Visualization
 * -----------------------------------------------------
 *
 * Purpose:
 *     A minimal but functional Three.js demo for visualizing holographic 3D meshes.
 *     It loads the output .glb file generated from TripoSR / CRM / Seed3D refinement pipelines,
 *     applies real-time lighting, and enables orbital controls for user interaction.
 *
 * Functionality:
 *     - Load GLTF/GLB 3D mesh
 *     - Interactive rotation, zoom, and pan
 *     - Scene lighting (ambient + directional)
 *     - Placeholder for gesture and AI control integration
 *
 * Integration:
 *     Input: output_mesh.glb (from backend inference)
 *     Output: Interactive holographic visualization (browser)
 */

import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

// ============================================================
// 1️⃣ Scene Initialization
// ============================================================
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000); // pure black for holographic effect

const camera = new THREE.PerspectiveCamera(
  65,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
camera.position.set(0, 1, 3);

const renderer = new THREE.WebGLRenderer({
  antialias: true,
  alpha: true
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
document.body.appendChild(renderer.domElement);

// ============================================================
// 2️⃣ Lighting Setup
// ============================================================
const ambientLight = new THREE.AmbientLight(0x404040, 3); // soft fill
scene.add(ambientLight);

const dirLight = new THREE.DirectionalLight(0xffffff, 2);
dirLight.position.set(3, 5, 10);
scene.add(dirLight);

// Optional holographic glow
const hemiLight = new THREE.HemisphereLight(0x00ffff, 0x000000, 1.0);
scene.add(hemiLight);

// ============================================================
// 3️⃣ Load 3D Mesh
// ============================================================
const loader = new GLTFLoader();
const MESH_PATH = 'datasets/output_meshes/output_mesh.glb'; // change dynamically if needed

loader.load(
  MESH_PATH,
  (gltf) => {
    const model = gltf.scene;
    model.scale.set(1.2, 1.2, 1.2);
    model.position.set(0, -0.5, 0);
    scene.add(model);

    console.log('[INFO] 3D Model successfully loaded and added to scene.');
  },
  (xhr) => {
    console.log(`[LOADING] ${Math.round((xhr.loaded / xhr.total) * 100)}% loaded`);
  },
  (error) => {
    console.error('[ERROR] Error loading 3D model:', error);
  }
);

// ============================================================
// 4️⃣ Orbit Controls (Mouse Interaction)
// ============================================================
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.1;
controls.enableZoom = true;
controls.enablePan = true;
controls.autoRotate = true;
controls.autoRotateSpeed = 1.5;

// ============================================================
// 5️⃣ Gesture Hooks (Future Integration)
// ============================================================
//
// Integration placeholder for gesture recognition.
// When connected, replace mouse input with MediaPipe / Leap Motion events.
// Example:
// window.addEventListener('gestureZoomIn', () => controls.dollyIn(1.1));
// window.addEventListener('gestureRotate', (event) => controls.rotateLeft(event.detail.angle));
//
// These events would be emitted by a WebSocket bridge from Python’s gesture controller.
//

// ============================================================
// 6️⃣ Responsive Window Resize
// ============================================================
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// ============================================================
// 7️⃣ Animation Loop
// ============================================================
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}

animate();

// ============================================================
// 8️⃣ Debug / Developer Overlay
// ============================================================
//
// Optional overlay for developers to visualize render stats or instructions.
// Could integrate with dat.GUI, stats.js, or WebXR APIs.
//
console.log(`
[Neural Holography Engine: Web Visualization Active]
 - Controls: Orbit to rotate | Scroll to zoom | Right-click to pan
 - Ready for gesture module integration (MediaPipe / Leap Motion / Kinect)
 - Input Source: ${MESH_PATH}
`);
