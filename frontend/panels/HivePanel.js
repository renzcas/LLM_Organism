// frontend/panels/HivePanel.js
export default {
  name: "HivePanel",
  data() {
    return {
      id: "",
      role: "",
      status: "active",
      members: {},
      roleCounts: {}
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
      const data = await res.json();
      this.members = data.members || {};
      const counts = {};
      Object.values(this.members).forEach(m => {
        const role = m.metadata?.role || "unknown";
        counts[role] = (counts[role] || 0) + 1;
      });
      this.roleCounts = counts;
    }
  },
  mounted() {
    this.refresh();
  },
  template: `
    <div>
      <h2>Hive Registry / Swarm</h2>
      <div>
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
      </div>

      <h3>Members</h3>
      <table border="1" cellpadding="4">
        <tr><th>ID</th><th>Status</th><th>Role</th></tr>
        <tr v-for="(m, key) in members" :key="key">
          <td>{{ key }}</td>
          <td>{{ m.status }}</td>
          <td>{{ m.metadata?.role || 'unknown' }}</td>
        </tr>
      </table>

      <h3>Role Distribution</h3>
      <div style="display:flex; gap:8px;">
        <div v-for="(count, role) in roleCounts" :key="role" style="text-align:center;">
          <div :style="{background:'#4caf50', width:'40px', height:(10+count*10)+'px'}"></div>
          <small>{{ role }} ({{ count }})</small>
        </div>
      </div>
    </div>
  `
};
