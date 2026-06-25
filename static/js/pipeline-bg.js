import * as THREE from 'three';

const wrap = document.getElementById('hero-canvas-wrap');
if (!wrap) throw new Error('no canvas wrap');

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(60, wrap.clientWidth / wrap.clientHeight, 0.1, 100);
camera.position.set(0, 0, 18);

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(wrap.clientWidth, wrap.clientHeight);
wrap.appendChild(renderer.domElement);

const AMBER  = new THREE.Color(0xf0a020);
const PASS   = new THREE.Color(0x3fb950);
const FAIL   = new THREE.Color(0xf85149);
const DIM    = new THREE.Color(0x30363d);

// ── Stage nodes laid out left-to-right like a pipeline ──
const STAGES = ['plan','code','build','test','release','monitor'];
const stageNodes = [];

STAGES.forEach((s, i) => {
  const x = (i / (STAGES.length - 1)) * 20 - 10;
  const y = Math.sin(i * 0.9) * 2;
  const geo = new THREE.SphereGeometry(0.22, 16, 16);
  const mat = new THREE.MeshBasicMaterial({ color: AMBER, transparent: true, opacity: 0.9 });
  const mesh = new THREE.Mesh(geo, mat);
  mesh.position.set(x, y, 0);
  mesh.userData = { stage: s, baseX: x, baseY: y, phase: i * 0.8 };
  scene.add(mesh);
  stageNodes.push(mesh);
});

// Edges between consecutive stage nodes
for (let i = 0; i < stageNodes.length - 1; i++) {
  const pts = [stageNodes[i].position.clone(), stageNodes[i + 1].position.clone()];
  const geo = new THREE.BufferGeometry().setFromPoints(pts);
  const mat = new THREE.LineBasicMaterial({ color: 0x30363d, transparent: true, opacity: 0.5 });
  scene.add(new THREE.Line(geo, mat));
}

// ── Floating particles (test results flying through) ──
const PARTICLE_COUNT = 60;
const particles = [];

for (let i = 0; i < PARTICLE_COUNT; i++) {
  const geo = new THREE.SphereGeometry(0.04, 6, 6);
  const isPass = Math.random() > 0.25;
  const mat = new THREE.MeshBasicMaterial({
    color: isPass ? PASS : FAIL,
    transparent: true,
    opacity: 0.6 + Math.random() * 0.4,
  });
  const mesh = new THREE.Mesh(geo, mat);
  mesh.position.set(
    (Math.random() - 0.5) * 22,
    (Math.random() - 0.5) * 10,
    (Math.random() - 0.5) * 6
  );
  mesh.userData = {
    vx: 0.015 + Math.random() * 0.025,  // left→right drift
    vy: (Math.random() - 0.5) * 0.008,
    vz: (Math.random() - 0.5) * 0.005,
    isPass,
  };
  scene.add(mesh);
  particles.push(mesh);
}

// ── Mouse parallax ──
let targetRotY = 0, targetRotX = 0;
window.addEventListener('mousemove', (e) => {
  targetRotY = (e.clientX / window.innerWidth - 0.5) * 0.3;
  targetRotX = (e.clientY / window.innerHeight - 0.5) * 0.15;
});

window.addEventListener('resize', () => {
  camera.aspect = wrap.clientWidth / wrap.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(wrap.clientWidth, wrap.clientHeight);
});

const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
let t = 0;

function animate() {
  requestAnimationFrame(animate);
  t += 0.016;

  if (!prefersReducedMotion) {
    // Stage nodes breathe
    stageNodes.forEach((node, i) => {
      node.position.y = node.userData.baseY + Math.sin(t + node.userData.phase) * 0.25;
      // Pulse opacity
      node.material.opacity = 0.6 + Math.sin(t * 1.2 + i) * 0.3;
    });

    // Particles drift left→right through the pipeline
    particles.forEach(p => {
      p.position.x += p.userData.vx;
      p.position.y += p.userData.vy;
      p.position.z += p.userData.vz;
      if (p.position.x > 12) {
        p.position.x = -12;
        p.position.y = (Math.random() - 0.5) * 10;
      }
    });

    // Camera parallax
    camera.rotation.y = THREE.MathUtils.lerp(camera.rotation.y, targetRotY, 0.03);
    camera.rotation.x = THREE.MathUtils.lerp(camera.rotation.x, targetRotX, 0.03);
  }

  renderer.render(scene, camera);
}

animate();
