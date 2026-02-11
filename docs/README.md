# Seduction Documentation

## Overview

Seduction is a social engineering analysis and awareness framework written in Julia. It provides tools for analyzing and understanding social engineering attack vectors, phishing campaigns, and human-factor vulnerabilities.

## Architecture

```
seduction/
├── src/
│   ├── Seduction.jl       # Main module
│   ├── phishing.jl        # Phishing analysis
│   ├── pretexting.jl      # Pretext generation analysis
│   ├── awareness.jl       # Training module
│   └── reporting.jl       # Report generation
├── models/                # ML models for detection
├── templates/             # Analysis templates
└── test/                  # Test suite
```

## Quick Start

```julia
using Seduction

# Analyze a suspected phishing email
result = analyze_email("suspicious_email.eml")
println(result.risk_score)  # 0.0 to 1.0
println(result.indicators)  # List of suspicious indicators

# Generate awareness training report
report = generate_training_report(organization_data)
export_report(report, "awareness_report.pdf")
```

## Modules

| Module | Purpose |
|--------|---------|
| `phishing` | Email and URL phishing analysis |
| `pretexting` | Social engineering scenario analysis |
| `awareness` | Security awareness training tools |
| `reporting` | Comprehensive report generation |
| `nlp` | Natural language analysis of SE attempts |
