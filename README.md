# AI Infrastructure Optimization Platform

## Overview

AI workloads consume massive amounts of electricity, while renewable energy availability varies throughout the day. Most training and inference workloads are executed without considering renewable energy availability, leading to increased costs and carbon emissions.

This project aims to forecast solar energy generation and intelligently schedule AI workloads during periods of high renewable energy availability.

---

## Problem Statement

Modern AI systems require substantial computational resources. Data centers often run energy-intensive jobs regardless of renewable energy conditions.

Key challenges:

* Renewable energy generation fluctuates hourly.
* AI workloads are often scheduled inefficiently.
* Organizations lack intelligent systems that align compute demand with renewable supply.

This project addresses these challenges through forecasting and optimization.

---

## Solution

The platform combines:

1. Solar Energy Forecasting
2. Renewable Energy Scoring
3. Workload Scheduling
4. Optimization Recommendations

Pipeline:

Weather Data

↓

Solar Forecasting Model

↓

Predicted GHI

↓

Renewable Energy Score

↓

Workload Scheduler

↓

Optimal Execution Window

---

## Features

### Solar Forecasting

Predict hourly Global Horizontal Irradiance (GHI) using:

* Temperature
* Humidity
* Pressure
* Cloud Type
* Wind Speed
* Solar Geometry Features

### Renewable Energy Scoring

Convert predicted GHI into a standardized renewable score between 0 and 100.

Example:

GHI = 850 W/m²

Renewable Score = 85

### Workload Scheduling

Identify the best continuous execution window for AI workloads.

Example:

Input:

* Job Duration = 4 Hours

Output:

* Best Start Time = 11:00
* Average Renewable Score = 92

---

## Project Structure

```text
src/

├── ingestion/
├── processing/
├── models/
├── forecasting/
├── optimization/
├── storage/
├── api/
├── memory/
├── rag/
├── config/

├── logger.py
├── exception.py
└── utils.py
```

---

## Current Progress

### Phase 1: Solar Forecasting

Status: Completed

* Data ingestion
* Data cleaning
* Feature engineering
* Model training
* Model evaluation

### Phase 2: Renewable Scoring

Status: In Progress

* GHI normalization
* Renewable availability scoring

### Phase 3: Workload Scheduling

Status: In Progress

* Window optimization
* Renewable-aware scheduling

### Phase 4: Optimization Engine

Status: Planned

### Phase 5: FastAPI Deployment

Status: Planned

### Phase 6: Dashboard & Monitoring

Status: Planned

### Phase 7: Memory & RAG Integration

Status: Planned

---

## Model Performance

Current Baseline Model

* R² ≈ 0.95+
* MAE ≈ 24
* RMSE ≈ 55

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* FastAPI
* Git
* GitHub

---

## Future Enhancements

* Multi-horizon forecasting
* Renewable-aware AI workload orchestration
* Carbon footprint estimation
* Energy cost optimization
* Memory-driven scheduling decisions
* RAG-powered energy policy recommendations

---

## Author

Priyanshi Maheshwari
