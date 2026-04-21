export default {
  name: "AttentionPanel",
  data() {
    return { inputs: "", result: null };
  },
  methods: {
    async compute() {
      const res = await fetch("/organism/attention/compute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ inputs: this.inputs.split(",").map(Number) })
      });
      this.result = await res.json();
    }
  },
  template: `
    <div>
      <h2>Attention Organ</h2>
      <input v-model="inputs" placeholder="1,2,3" />
      <button @click="compute">Compute</button>
      <pre>{{ result }}</pre>
    </div>
  `
};
