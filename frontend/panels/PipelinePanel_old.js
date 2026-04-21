// frontend/panels/PipelinePanel.js
export default {
  name: "PipelinePanel",
  data() {
    return {
      pipelineJson: `{
  "steps": [
    { "organ": "attention", "method": "compute", "payload": {"inputs": [1,2,3]} },
    { "organ": "symbolic", "method": "compute", "payload": {"tokens": ["a","b","c"], "mode": "pairs"} }
  ]
}`,
      result: null,
      error: null
    };
  },
  methods: {
    async run() {
      try {
        const payload = JSON.parse(this.pipelineJson);
        const res = await fetch("/organism/pipeline/run", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });
        this.result = await res.json();
        this.error = null;
      } catch (e) {
        this.error = e.toString();
      }
    }
  },
  template: `
    <div>
      <h2>Pipeline Organ</h2>
      <textarea v-model="pipelineJson" rows="10" cols="60"></textarea>
      <br />
      <button @click="run">Run Pipeline</button>
      <pre v-if="error">Error: {{ error }}</pre>
      <pre>{{ result }}</pre>
    </div>
  `
};
