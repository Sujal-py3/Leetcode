# FluxGen R&D Internship Assignment - Visual Guide

Here is a quick visual breakdown of the logic I used to solve the three problems in `FluxGen_Round1_Assignment.txt`.

## Problem 1: The Incomplete Geometry
**The Logic:**
Since the reservoir is natural, we can't assume simple shapes. I used Alpha Shapes to hug the actual data points and Kriging to intelligently guess the depths in the blind spots based on nearby trends.

```mermaid
graph TD
    A[Raw Depth Points 65%] --> B{Analyze Geometry}
    B -->|Define Boundary| C[Alpha Shapes]
    B -->|Analyze Spatial Trend| D[Variogram Modeling]
    C --> E[Constrained Interpolation Grid]
    D --> E
    E --> F[Ordinary Kriging]
    F --> G[Estimated Surface DEM]
    F --> H[Variance/Uncertainty Map]
    G --> I[Volumetric Integration]
```

## Problem 2: The Spectral Discrepancy
**The Logic:**
Satellites can be tricked by sun glint or mud. This flow checks for those "false positives" before we panic and send an alert.

```mermaid
graph TD
    A[Satellite Alert: High Greenness] --> B{Atmospheric Check}
    B -->|High Cloud Cover| C[Dismiss: Cloud Shadow]
    B -->|Clear Sky| D{Spectral Check: NIR Band}
    D -->|Low NIR| E[Dismiss: Glint / Sediment]
    D -->|High NIR| F{Context Check}
    F -->|High Wind speed| G[Dismiss: Mixing Artifact]
    F -->|Low Temp| G
    F -->|Warm & Calm| H[VALIDATE ALERT]
    H --> I[Spatial Weighting IDW]
```

## Problem 3: The Balancing Act
**The Logic:**
Water doesn't teleport, and it expands when hot. This model accounts for the delay (routing) and the thermal expansion so our "Digital Twin" doesn't see a ghost flood.

```mermaid
graph TD
    A[Rainfall Input t=0] --> B{Hydrologic Abstractions}
    B -->|Loss| C[Infiltration Saturation]
    B -->|Loss| D[Depression Storage]
    B --> E[Effective Runoff]
    E --> F[Routing Delay t=12]
    F --> G[Lake Inflow]
    G --> H[Level Sensor Reading]
    H --> I{Temperature Correction}
    I -->|Calc Mass| J[Mass = Volume * Density T]
    J --> K[True Mass Balance]
```

