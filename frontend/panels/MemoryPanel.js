// frontend/panels/MemoryPanel.js
export default {
  name: "MemoryPanel",
  data() {
    return {
      storeType: "episodic",
      storeKey: "",
      storeData: "",
      retrieveType: "episodic",
      retrieveKey: "",
      storeResult: null,
      retrieveResult: null
    };
  },
  methods: {
    async store() {
      const payload = {
        type: this.storeType,
        data: this.storeData
      };
      if (this.storeType === "semantic" && this.storeKey) {
        payload.key = this.storeKey;
      }
      const res = await fetch("/organism/memory/store", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      this.storeResult = await res.json();
    },
    async retrieve() {
      const payload = { type: this.retrieveType };
      if (this.retrieveType === "semantic" && this.retrieveKey) {
        payload.key = this.retrieveKey;
      }
      const res = await fetch("/organism/memory/retrieve", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      this.retrieveResult = await res.json();
    }
  },
  template: `
    <div>
      <h2>Memory Organ</h2>
      <h3>Store</h3>
      <select v-model="storeType">
        <option value="episodic">episodic</option>
        <option value="semantic">semantic</option>
      </select>
      <input v-if="storeType==='semantic'" v-model="storeKey" placeholder="key" />
      <input v-model="storeData" placeholder="data" />
      <button @click="store">Store</button>
      <pre>{{ storeResult }}</pre>

      <h3>Retrieve</h3>
      <select v-model="retrieveType">
        <option value="episodic">episodic</option>
        <option value="semantic">semantic</option>
      </select>
      <input v-if="retrieveType==='semantic'" v-model="retrieveKey" placeholder="key" />
      <button @click="retrieve">Retrieve</button>
      <pre>{{ retrieveResult }}</pre>
    </div>
  `
};
