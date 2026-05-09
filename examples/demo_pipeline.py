"""Demo: run the full three-agent pipeline on a synthetic sample."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import yaml
from agents.orchestrator import Orchestrator


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, "config", "config.yaml")
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    orch = Orchestrator(cfg)
    result = orch.run(sers_raw=None, seira_raw=None)
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()