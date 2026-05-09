"""
Orchestrator: central router managing multi-agent task scheduling,
self-reflection retry loops, and end-to-end lineage tracking.
"""

import json
import logging
import os
from typing import Dict, Any

from agents.preprocessing_agent import PreprocessingAgent
from agents.physics_agent import PhysicsAgent
from agents.diagnostic_agent import DiagnosticAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Orchestrator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.prep_agent = PreprocessingAgent(config["preprocessing"])
        self.physics_agent = PhysicsAgent(config["physics"])
        self.diag_agent = DiagnosticAgent(config["diagnostic"])
        self.max_retry = config["physics"].get("max_retry", 3)

    def run(self, sers_raw: Any, seira_raw: Any) -> Dict[str, Any]:
        """Run the full three-agent pipeline with self-reflection loop."""
        trace = {"steps": []}

        for attempt in range(self.max_retry):
            logger.info(f"=== Pipeline attempt {attempt + 1} ===")

            # Step 1: Preprocessing
            prep_out = self.prep_agent.process(sers_raw, seira_raw, attempt=attempt)
            trace["steps"].append({"agent": "preprocessing", "output": prep_out["quality"]})

            # Step 2: Physics reasoning
            phys_out = self.physics_agent.reason(
                prep_out["sers"], prep_out["seira"]
            )
            trace["steps"].append({"agent": "physics", "confidence": phys_out["capsim"]})

            # Self-reflection: if confidence too low, retry preprocessing
            if phys_out["capsim"] >= self.config["physics"]["similarity_threshold"]:
                break
            logger.warning("CaPSim below threshold, triggering self-reflection retry...")

        # Step 3: Diagnostic reasoning
        diag_out = self.diag_agent.diagnose(phys_out["features"])
        trace["steps"].append({"agent": "diagnostic", "report": diag_out})

        return {
            "report": diag_out,
            "trace": trace,
        }


if __name__ == "__main__":
    import yaml
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, "config", "config.yaml")
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    orchestrator = Orchestrator(cfg)
    print(json.dumps(orchestrator.run(None, None), indent=2, default=str))