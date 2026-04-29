from typing import List, Dict, Any

TRACK_REGS = {"rax", "rbx", "rcx", "rdx", "rsi", "rdi"}

class SymbolicState:
    def __init__(self):
        self.regs = {}
        self.constraints = []
        self.calls = []
        self.loop_iters = {}

    def copy(self):
        s = SymbolicState()
        s.regs = dict(self.regs)
        s.constraints = list(self.constraints)
        s.calls = list(self.calls)
        s.loop_iters = dict(self.loop_iters)
        return s

class SymbolicExecEngine:
    def __init__(self, semantics: List[Dict], graph: Dict):
        self.semantics = semantics
        self.graph = graph

    def extract_loop_invariants(self, state: SymbolicState, s: Dict):
        if s["behavior"] == "integer_add" and s["operands"][0] in TRACK_REGS:
            reg = s["operands"][0]
            if reg not in state.loop_iters:
                state.loop_iters[reg] = 0
            state.loop_iters[reg] += 1

    def extract_call(self, state: SymbolicState, s: Dict):
        if s["behavior"] == "call":
            state.calls.append(s["operands"][0] if s["operands"] else "unknown_call")

    def extract_constraint(self, state: SymbolicState, s: Dict):
        if s["behavior"] == "compare" and len(s["operands"]) == 2:
            state.constraints.append(f"{s['operands'][0]} ? {s['operands'][1]}")

    def update_register(self, state: SymbolicState, s: Dict):
        if s["behavior"] == "integer_add" and len(s["operands"]) == 2:
            reg = s["operands"][0]
            val = s["operands"][1]
            prev = state.regs.get(reg, reg)
            state.regs[reg] = f"({prev} + {val})"

    def run(self) -> List[Dict[str, Any]]:
        state = SymbolicState()
        paths = []

        for s in self.semantics:
            beh = s["behavior"]

            self.update_register(state, s)
            self.extract_constraint(state, s)
            self.extract_call(state, s)
            self.extract_loop_invariants(state, s)

            if beh.startswith("cond_branch"):
                paths.append({
                    "branch_at": s["index"],
                    "branch": s["mnemonic"],
                    "constraints": list(state.constraints),
                    "registers": dict(state.regs),
                    "calls": list(state.calls),
                    "loop_invariants": dict(state.loop_iters),
                })

        return paths

    def diff_paths(self, left_paths, right_paths):
        diff = []
        max_len = max(len(left_paths), len(right_paths))
        for i in range(max_len):
            lp = left_paths[i] if i < len(left_paths) else None
            rp = right_paths[i] if i < len(right_paths) else None
            diff.append({
                "index": i,
                "left": lp,
                "right": rp,
                "same_constraints": lp and rp and lp["constraints"] == rp["constraints"],
                "same_calls": lp and rp and lp["calls"] == rp["calls"],
                "same_invariants": lp and rp and lp["loop_invariants"] == rp["loop_invariants"],
            })
        return diff
