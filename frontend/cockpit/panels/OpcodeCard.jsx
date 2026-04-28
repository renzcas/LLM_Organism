import React from "react";

export default function OpcodeCard({ opcode }) {
  if (!opcode) return null;

  return (
    <div style={{border:"1px solid #444", padding:"10px", borderRadius:"6px", marginBottom:"10px"}}>
      <h3>{opcode.mnemonic}</h3>

      {opcode.description && <p>{opcode.description}</p>}

      <strong>Category:</strong> {opcode.category || "unknown"}<br/>
      <strong>Flags:</strong> {(opcode.flags || []).join(", ")}<br/>

      <h4>Encodings</h4>
      <ul>
        {(opcode.encodings || []).map((e, i) => (
          <li key={i}>
            <strong>{e.opcode}</strong> — hex: {e.hex_example}
          </li>
        ))}
      </ul>

      <h4>Operands</h4>
      <ul>
        {(opcode.operands || []).map((o, i) => (
          <li key={i}>{o.type}</li>
        ))}
      </ul>
    </div>
  );
}
