import React, { useState } from "react";
import axios from "axios";

export default function SymbolicExecutionPanel() {
  const [semanticsJson, setSemanticsJson] = useState("");
  const [graphJson, setGraphJson] = useState("");
  const [result, setResult] = useState(null);

  const run = async () => {
    const payload = {
      semantics: JSON.parse(semanticsJson),
      graph: JSON.parse(graphJson)
    };
    const res = await axios.post("/symexec/analyze", payload);
    setResult(res.data);
  };

  return (
    <div className="panel">
      <h2>Symbolic Execution Organ</h2>

      <textarea
        placeholder="Semantics JSON"
        value={semanticsJson}
        onChange={e => setSemanticsJson(e.target.value)}
      />

      <textarea
        placeholder="CFG JSON"
        value={graphJson}
        onChange={e => setGraphJson(e.target.value)}
      />

      <button onClick={run}>Analyze</button>

      {result && (
        <pre>{JSON.stringify(result.paths, null, 2)}</pre>
      )}
    </div>
  );
}
