// frontend/panels/SymbolicPanel.js
export default {
  name: "SymbolicPanel",

  data() {
    return { 
      tokens: "", 
      mode: "pairs", 
      result: null,

      // NEW: organ type for dynamic visuals
      organType: "organ-helix"
    };
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
    <div class="symbolic-panel">
      <h2>Symbolic Organ</h2>

      <!-- NEW: Organ visual with rotation + dynamic type -->
      <div class="organ-spin-wrapper">
        <div class="organ-spin">
          <div :class="['organ-core', organType]"></div>
        </div>
      </div>

      <!-- Optional dropdown to switch organ types -->
      <select v-model="organType">
        <option value="organ-helix">Helix</option>
        <option value="organ-sheet">Sheet</option>
        <option value="organ-chaos">Chaos</option>
      </select>

      <br/><br/>

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
