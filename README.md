# Physics-Guided Dual-Modal Spectroscopic Diagnostic Multi-Agent System

> A multi-agent framework for Parkinson's Disease (PD) prodromal biomarker analysis, 
> leveraging SERS/SEIRA dual-modal spectroscopy with physics-guided long-chain reasoning.

## 🌟 Overview

This project provides a **three-agent automated pipeline** for high-precision quantification 
of catecholamine metabolites (Dopamine, Norepinephrine, DOPAC, HVA) from surface-enhanced 
Raman (SERS) and surface-enhanced infrared (SEIRA) spectroscopy data. 

The underlying **dual-modal biosensor** has been published in *ACS Nano*. This repository 
hosts the companion **AI-driven analysis framework**, which is being prepared for a follow-up 
publication on cross-disease biomarker generalization.

## 🧠 Core Features

- **Physics-Guided Reasoning**: Breaks the "black-box" problem of end-to-end DL by anchoring 
  every decision to molecular vibrational physics.
- **Multi-Agent Collaboration**: Three specialized agents (Preprocessing / Physics / Diagnostic) 
  orchestrated with structured JSON message passing and self-reflective retry loops.
- **Dual-Modal Fusion**: Leverages the complementary symmetry between SERS and SEIRA channels.
- **White-Box Auditability**: Every diagnostic conclusion is traceable to its physical evidence.

## 🚀 Quick Start

```bash
git clone https://github.com/<your-username>/physics-guided-spectro-agents.git
cd physics-guided-spectro-agents
pip install -r requirements.txt
python examples/demo_pipeline.py

📈 Results
Efficiency: ~90% reduction in analysis time (from ~40 min to ~3 min per sample).
Accuracy: R² > 0.98 for four catecholamines in artificial CSF, nM-level LOD.
Robustness: Significantly improved cross-batch generalization over end-to-end DL baselines.


