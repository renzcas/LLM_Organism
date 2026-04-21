// frontend/main.js
import { createApp } from "vue";
import AttentionPanel from "./panels/AttentionPanel";
import SymbolicPanel from "./panels/SymbolicPanel";
import DecisionPanel from "./panels/DecisionPanel";
import MemoryPanel from "./panels/MemoryPanel";
import PipelinePanel from "./panels/PipelinePanel";
import HivePanel from "./panels/HivePanel";

const App = {
  components: {
    AttentionPanel,
    SymbolicPanel,
    DecisionPanel,
    MemoryPanel,
    PipelinePanel,
    HivePanel
  },
  template: `
    <div>
      <h1>LLM Organism Cockpit</h1>
      <AttentionPanel />
      <SymbolicPanel />
      <DecisionPanel />
      <MemoryPanel />
      <PipelinePanel />
      <HivePanel />
    </div>
  `
};

createApp(App).mount("#app");
