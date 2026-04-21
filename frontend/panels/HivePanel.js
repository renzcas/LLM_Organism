// frontend/panels/HivePanel.js
export default {
  name: "HivePanel",
  data() {
    return {
      id: "",
      role: "",
      status: "active",
      members: null
    };
  },
  methods: {
    async register() {
      await fetch("/organism/hive/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          id: this.id,
          metadata: { role: this.role }
        })
      });
      await this.refresh();
    },
    async update() {
      await fetch("/organism/hive/update", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          id: this.id,
          status: this.status,
          metadata: { role: this.role }
        })
      });
      await this.refresh();
    },
    async refresh() {
      const res = await fetch("/organism/hive/list");
      this.members = await res.json();
    }
  },
  mounted() {
    this.refresh();
  },
  template: `
    <div>
      <h2>Hive Registry</h2>
      <input v-model="id" placeholder="organism id" />
      <input v-model="role" placeholder="role" />
      <select v-model="status">
        <option value="active">active</option>
        <option value="idle">idle</option>
        <option value="offline">offline</option>
      </select>
      <button @click="register">Register</button>
      <button @click="update">Update</button>
      <button @click="refresh">Refresh</button>
      <pre>{{ members }}</pre>
    </div>
  `
};
