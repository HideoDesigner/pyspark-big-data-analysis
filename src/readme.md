## Design: Notebooks vs. Source Code

This project intentionally separates exploratory analysis from production-style
implementation.

### Notebooks (`notebooks/`)
The Jupyter notebook is used for:
- Exploratory data analysis
- Interactive experimentation with Spark DataFrames
- Debugging and validation of intermediate results

This mirrors how data scientists and engineers prototype ideas before formalizing
them into reusable systems.

### Source Code (`src/`)
The `src/` directory contains the core data processing pipeline:
- Spark session initialization
- Data loading logic
- Data cleaning and transformation functions
- Aggregation and analysis workflows

The pipeline is implemented in modular Python scripts to emphasize:
- Reusability
- Maintainability
- Clear separation of concerns
- Production-oriented design

### Rationale
Separating exploratory notebooks from source code reflects real-world data
engineering and analytics workflows, where experimentation is followed by
refactoring into scalable, testable systems.

This design choice highlights the transition from ad hoc analysis to structured
software engineering.
