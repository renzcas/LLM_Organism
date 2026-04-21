// frontend/panels/SymbolicPanel.js
export default {
  name: "SymbolicPanel",
  data() {
    return { tokens: "", mode: "pairs", result: null };
  },
  methods: {
    async compute() {
      const res = await fetch("/organism/symbolic/compute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          tokens: this.tokens.split(",").map(t => t.trim()),
          mode: this.mode
        })
      });
      this.result = await res.json();
    }
  },
  template: `
    <div>
      <h2>Symbolic Organ</h2>
      <input v-model="tokens" placeholder="a,b,c" />
      <select v-model="mode">
        <option value="pairs">pairs</option>
        <option value="triples">triples</option>
        <option value="graph">graph</option>
      </select>
      <button @click="compute">Compute</button>
      <pre>{{ result }}</pre>
    </div>
  `
};
