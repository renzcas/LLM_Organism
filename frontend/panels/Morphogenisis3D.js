// frontend/panels/Morphogenesis3D.js
import * as THREE from "three";

export default {
  name: "Morphogenesis3D",
  data() {
    return { intervalId: null, meshes: {}, scene: null, renderer: null, camera: null };
  },
  mounted() {
    const width = 400, height = 300;
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(width, height);
    this.$el.appendChild(renderer.domElement);

    const organs = [
      { key: "attention", x: -2, y: 1, z: 0 },
      { key: "symbolic", x: 0, y: 1, z: 0 },
      { key: "decision", x: 2, y: 1, z: 0 },
      { key: "memory", x: -1, y: -1, z: 0 },
      { key: "pipeline", x: 1, y: -1, z: 0 },
      { key: "hive", x: 0, y: -3, z: 0 }
    ];

    const meshes = {};
    organs.forEach(o => {
      const geo = new THREE.SphereGeometry(0.25, 16, 16);
      const mat = new THREE.MeshBasicMaterial({ color: 0x00ffcc });
      const mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(o.x, o.y, o.z);
      scene.add(mesh);
      meshes[o.key] = mesh;
    });

    camera.position.z = 6;

    const animate = () => {
      requestAnimationFrame(animate);
      scene.rotation.y += 0.003;
      renderer.render(scene, camera);
    };
    animate();

    this.scene = scene;
    this.renderer = renderer;
    this.camera = camera;
    this.meshes = meshes;

    this.intervalId = setInterval(this.refreshHealth, 2000);
  },
  beforeUnmount() {
    if (this.intervalId) clearInterval(this.intervalId);
  },
  methods: {
    async refreshHealth() {
      try {
        const res = await fetch("/organism/health");
        const data = await res.json();
        // Expecting something like { organs: { attention: {...}, ... } }
        const organs = data.organs || {};
        Object.keys(this.meshes).forEach(key => {
          const mesh = this.meshes[key];
          const status = organs[key]?.status || "unknown";
          if (status === "ok") {
            mesh.material.color.set(0x00ff00);
            mesh.scale.set(1.1, 1.1, 1.1);
          } else {
            mesh.material.color.set(0xff0000);
            mesh.scale.set(0.9, 0.9, 0.9);
          }
        });
      } catch (e) {
        // On error, dim everything
        Object.values(this.meshes).forEach(mesh => {
          mesh.material.color.set(0x555555);
        });
      }
    }
  },
  template: `<div><h2>Morphogenesis Map (Live Health)</h2></div>`
};
