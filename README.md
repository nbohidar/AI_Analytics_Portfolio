# Drug Repurposing Similarity Score (DSS)

A multi-agent computational biology pipeline for scoring drug-to-drug similarity across three biological modalities — structure, network topology, and transcriptomics — to identify repurposing candidates.

---

## Overview

Before computing a Drug Similarity Score (DSS), a virtual advisory panel of three domain specialists was convened to debate which biological signals matter most for drug repurposing. The agents reached consensus on a weighted Gold Layer formula balancing chemistry, mechanism, and functional effect.

The pipeline then uses that formula as its foundation, scraping and transforming data through a Bronze → Silver → Gold medallion architecture.

---

## Project Structure

```
.
├── agents.py               # CrewAI agent definitions
├── Discussion_Panel.ipynb  # Specialist roundtable — DSS formula consensus
└── Data_Scraping.ipynb     # Bronze/Silver/Gold schema design and data pipeline
```

---

## Agents

Defined in `agents.py` using [CrewAI](https://github.com/joaomdmoura/crewAI):

| Agent | Role | Similarity Signal | Key Metric |
|---|---|---|---|
| `network_specialist` | Network Topologist | Protein-Protein Interaction (PPI) networks | Jaccard Target Overlap |
| `structural_specialist` | Structural Bioinformatician | Chemical fingerprints & docking pockets | Tanimoto Coefficient |
| `systems_specialist` | Systems Biologist | Gene expression (Transcriptomics / RNA-seq) | Connectivity Score |
| `schema_builder` | Data Engineer | Bronze layer schema design | — |

---

## Notebooks

### `Discussion_Panel.ipynb` — Specialist Roundtable

Three specialist agents debate the pros and cons of each similarity signal and reach consensus on a weighted DSS formula. The output is a structured JSON object containing:

- `weights` — relative contribution of each modality (must sum to 1.0)
- `explanation` — rationale for each weight
- `final_formula` — a concise, reusable scoring expression

The consensus formula feeds directly into the Gold Layer scoring logic.

### `Data_Scraping.ipynb` — Data Pipeline (Bronze → Silver → Gold)

The `schema_builder` agent consults each domain specialist to design the full data schema across three layers:

**Bronze Layer (Raw Ingestion)**
The data engineer consults each specialist individually to define minimum required inputs from publicly accessible biomedical databases. Outputs a unified schema and primary integration table covering:
- Structural data: drug identifiers, SMILES/canonical structures, fingerprint-ready fields, source provenance
- Network data: PPI targets, pathway identifiers, interaction scores
- Transcriptomic data: gene expression signatures, connectivity scores

**Silver Layer (Cleaned & Transformed)**
Per-modality tables are normalized and prepared for scoring. A CSV artifact (`bronze_to_silver_workflow.csv`) and JSON artifact (`silver_schema.json`) document the transformation logic.

**Gold Layer (Scored & Integrated)**
Silver tables are combined into the final DSS output using the formula agreed upon in the Discussion Panel. Artifacts produced:
- `silver_to_gold_workflow.csv` — transformation summary per modality
- `gold_schema.json` — final schema with metric rationale and integration strategy

---

## Setup

**Requirements**

- Python 3.13+
- A `.env` file with your LLM API key (loaded via `python-dotenv`)

**Install dependencies**

```bash
pip install crewai openai python-dotenv
```

**Configure environment**

```bash
cp .env.example .env
# Add your OPENAI_API_KEY or other LLM provider key
```

---

## Running the Pipeline

Run notebooks in order:

1. `Discussion_Panel.ipynb` — establishes the DSS formula
2. `Data_Scraping.ipynb` — designs schema and builds Bronze → Silver → Gold pipeline

---

## Output Artifacts

| File | Description |
|---|---|
| `bronze_to_silver_workflow.csv` | Bronze-to-Silver transformation plan per modality |
| `silver_schema.json` | Silver layer schema in JSON format |
| `silver_to_gold_workflow.csv` | Silver-to-Gold scoring and integration plan |
| `gold_schema.json` | Final Gold layer schema with metric rationale |

---

## Data Sources

All Bronze layer data is sourced from publicly accessible biomedical databases. Specific sources are defined per modality by the respective specialist agent during schema design.
