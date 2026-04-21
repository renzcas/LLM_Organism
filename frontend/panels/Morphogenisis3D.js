// frontend/panels/Morphogenesis3D.js
import * as THREE from "three";

export default {
  name: "Morphogenesis3D",
  mounted() {
    const width = 400, height = 300;
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(width, height);
    this.$el.appendChild(renderer.domElement);

    const organs = [
      { name: "attention", x: -2, y: 1, z: 0 },
      { name: "symbolic", x: 0, y: 1, z: 0 },
      { name: "decision", x: 2, y: 1, z: 0 },
      { name: "memory", x: -1, y: -1, z: 0 },
      { name: "pipeline", x: 1, y: -1, z: 0 },
      { name: "hive", x: 0, y: -3, z: 0 }
    ];

    const material = new THREE.MeshBasicMaterial({ color: 0x00ffcc });
    organs.forEach(o => {
      const geo = new THREE.SphereGeometry(0.2, 16, 16);
      const mesh = new THREE.Mesh(geo, material.clone());
      mesh.position.set(o.x, o.y, o.z);
      scene.add(mesh);
    });

    camera.position.z = 6;

    const animate = () => {
      requestAnimationFrame(animate);
      scene.rotation.y += 0.005;
      renderer.render(scene, camera);
    };
    animate();
  },
  template: `<div><h2>Morphogenesis Map</h2></div>`
};
