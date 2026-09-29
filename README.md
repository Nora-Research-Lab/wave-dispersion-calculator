![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Wave Dispersion Calculator
 
*For oceanographers and coastal scientists: enter wave period and water depth to instantly compute wavelength, phase speed, group velocity, and wave classification.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Oceanography / Marine Geoscience
 
The tool computes the full linear wave dispersion solution. Inputs: (1) wave period T in seconds (float, range 1–30, default 10), (2) water depth d in meters (float, range 0.1–5000, default 10). Using the dispersion relation ω² = g k tanh(k d) where ω = 2π/T and g = 9.80665 m/s², the wavenumber k is found via a Newton-Raphson solver starting from an initial guess using the Eckart approximation: k₀ = ω²/g * coth( (ω² d / g)^0.75 ). The solver iterates until |f(k)| < 1e-8. Outputs: wavenumber k (rad/m, 4 decimals), wavelength L = 2π/k (m, 2 decimals), phase speed c = ω/k (m/s, 2 decimals), group velocity cg = 0.5 * c * (1 + 2kd / sinh(2kd)) (m/s, 2 decimals). A classification dropdown: if d/L < 0.05 → 'Shallow Water', if d/L > 0.5 → 'Deep Water', else 'Intermediate Water'. A secondary classification for Ursell number is optionally shown: if wave height H is also provided (optional input, default 1 m), compute Ursell number Ur = (H/L) / (d/L)³ and classify: Ur < 0.01 → linear waves, 0.01–0.1 → weakly nonlinear, >0.1 → strongly nonlinear (Stokes). The Gradio UI has a numerical input box for T (with slider), a numerical input box for d (with slider), and optional H input. Outputs are displayed as a set of labeled numbers and a classification badge. Also a matplotlib figure showing the dispersion curve (c vs T) for the given depth, with the current T marked. The figure is generated on the fly and displayed below the outputs. No AI/ML component.
 
## Run it
 
```bash
docker build -t wave-dispersion-calculator .
docker run -p 7860:7860 wave-dispersion-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-29.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
