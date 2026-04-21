// frontend/panels/PipelinePanel.js (replace template + logic)
export default {
  name: "PipelinePanel",
  data() {
    return {
      pipelineJson: `{
  "steps": [
    { "organ": "attention", "method": "compute", "payload": {"inputs": [1,2,3]} },
    { "organ": "symbolic", "method": "compute", "payload": {"tokens": ["a","b","c"], "mode": "pairs"} },
    { "organ": "decision", "method": "compute", "payload": {"symbols": [1,2,3], "policy": "max"} }
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
  computed: {
    tracedSteps() {
      if (!this.result || !this.result.results) return [];
      try {
        const parsed = JSON.parse(this.pipelineJson);
        return parsed.steps.map((s, idx) => ({
          index: idx,
          organ: s.organ,
          method: s.method,
          input: s.payload,
          output: this.result.results[idx]
        }));
      } catch {
        return [];
      }
    }
  },
  template: `
    <div>
      <h2>Pipeline Organ (Signal Trace)</h2>
      <textarea v-model="pipelineJson" rows="10" cols="60"></textarea>
      <br />
      <button @click="run">Run Pipeline</button>
      <pre v-if="error">Error: {{ error }}</pre>

      <div v-if="tracedSteps.length">
        <h3>Trace</h3>
        <div v-for="step in tracedSteps" :key="step.index" style="border:1px solid #ccc; margin:4px; padding:4px;">
          <strong>Step {{ step.index + 1 }}: {{ step.organ }}.{{ step.method }}</strong>
          <div><em>Input:</em> <pre>{{ step.input }}</pre></div>
          <div><em>Output:</em> <pre>{{ step.output }}</pre></div>
        </div>
      </div>
    </div>
  `
};
