// frontend/panels/DecisionPanel.js
export default {
  name: "DecisionPanel",
  data() {
    return { symbols: "", policy: "first", result: null };
  },
  methods: {
    async compute() {
      const res = await fetch("/organism/decision/compute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          symbols: this.symbols.split(",").map(v => v.trim()),
          policy: this.policy
        })
      });
      this.result = await res.json();
    }
  },
  template: `
    <div>
      <h2>Decision Organ</h2>
      <input v-model="symbols" placeholder="1,2,3" />
      <select v-model="policy">
        <option value="first">first</option>
        <option value="max">max</option>
        <option value="min">min</option>
        <option value="random">random</option>
      </select>
      <button @click="compute">Decide</button>
      <pre>{{ result }}</pre>
    </div>
  `
};
