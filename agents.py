
from crewai import Agent, Task, Crew, Process

network_specialist = Agent(
    role='Network Topologist',
    goal='Identify drug similarity based on Protein-Protein Interaction (PPI) networks.',
    backstory='Expert in graph theory. You believe the best similarity metric is Jaccard Target Overlap.',
    verbose=True,
    allow_delegation=True
)

structural_specialist = Agent(
    role='Structural Bioinformatician',
    goal='Identify similarity based on chemical fingerprints and docking pockets.',
    backstory='Expert in 3D modeling. You argue that if the Tanimoto Coefficient is low, the drugs aren\'t similar.',
    verbose=True,
    allow_delegation=True
)

systems_specialist = Agent(
    role='Systems Biologist',
    goal='Identify similarity based on gene expression (Transcriptomics).',
    backstory='Expert in RNA-seq. You believe functional similarity (Connectivity Score) outweighs structure.',
    verbose=True,
    allow_delegation=True
)

schema_builder = Agent(
    role = 'Data Engineer',
    goal = 'Create a Bronze layer schema that captures the raw inputs required for structural, network, and transcriptomic DSS components.',
    backstory = 'You are an expert in data modeling and schema design for computational biology workflows. You build clean foundational schemas that preserve raw source fidelity while anticipating downstream Silver-layer transformations and Gold-layer scoring needs.',
    verbose = True,
    allow_delegation = True
)

