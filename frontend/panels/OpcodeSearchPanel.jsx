import React, { useState } from "react";
import axios from "axios";
import OpcodeCard from "./OpcodeCard";

export default function OpcodeSearchPanel() {
  const [mnemonic, setMnemonic] = useState("");
  const [result, setResult] = useState(null);

  const search = async () => {
    if (!mnemonic.trim()) return;
    const res = await axios.post("/opcodes/lookup", {
      mnemonic,
      mode: "x86_64"
    });
    const first = (res.data.results || [])[0] || null;
    setResult(first);
  };

  return (
    <div>
      <h2>Opcode Search</h2>
      <input
        value={mnemonic}
        onChange={e => setMnemonic(e.target.value)}
        placeholder="cmp, mov, je..."
        style={{marginRight:"8px"}}
      />
      <button onClick={search}>Search</button>

      <div style={{marginTop:"16px"}}>
        <OpcodeCard opcode={result} />
      </div>
    </div>
  );
}
