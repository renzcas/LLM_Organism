// frontend/main.js
import { createApp } from "vue";
import AttentionPanel from "./panels/AttentionPanel";
import SymbolicPanel from "./panels/SymbolicPanel";
import DecisionPanel from "./panels/DecisionPanel";
import MemoryPanel from "./panels/MemoryPanel";
import PipelinePanel from "./panels/PipelinePanel";
import HivePanel from "./panels/HivePanel";
import Morphogenesis3D from "./panels/Morphogenesis3D";

const App = {
  components: {
    AttentionPanel,
    SymbolicPanel,
    DecisionPanel,
    MemoryPanel,
    PipelinePanel,
    HivePanel,
    Morphogenesis3D
  },
  data() {
    return {
      activeTab: "cognitive"
    };
  },
  template: `
    <div class="cockpit">
      <h1>LLM Organism Cockpit</h1>
      <nav class="tabs">
        <button @click="activeTab='cognitive'" :class="{active: activeTab==='cognitive'}">Cognitive Stack</button>
        <button @click="activeTab='pipeline'" :class="{active: activeTab==='pipeline'}">Pipelines</button>
        <button @click="activeTab='hive'" :class="{active: activeTab==='hive'}">Hive / Swarm</button>
        <button @click="activeTab='morpho'" :class="{active: activeTab==='morpho'}">3D Morphogenesis</button>
      </nav>

      <section v-if="activeTab==='cognitive'" class="grid">
        <AttentionPanel />
        <SymbolicPanel />
        <DecisionPanel />
        <MemoryPanel />
      </section>

      <section v-if="activeTab==='pipeline'">
        <PipelinePanel />
      </section>

      <section v-if="activeTab==='hive'">
        <HivePanel />
      </section>

      <section v-if="activeTab==='morpho'">
        <Morphogenesis3D />
      </section>
    </div>
  `
};

createApp(App).mount("#app");
