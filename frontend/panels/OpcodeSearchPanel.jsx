import { useState } from "react";

export default function OpcodeSearchPanel() {
  const [mnemonic, setMnemonic] = useState("");
  const [result, setResult] = useState(null);

  async function searchOpcode() {
    const res = await fetch("http://localhost:8000/opcode/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mnemonic })
    });

    const data = await res.json();
    setResult(data);
  }

  return (
    <div style={{ padding: 20 }}>
      <h2>Opcode Search</h2>

      <input
        value={mnemonic}
        onChange={(e) => setMnemonic(e.target.value)}
        placeholder="Enter mnemonic (e.g., mov)"
      />

      <button onClick={searchOpcode}>Search</button>

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}
