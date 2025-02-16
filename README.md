# Basic Pairs Trading Strategy

## Overview
This repository implements a pairs trading strategy based on a market-neutral approach, utilizing statistical methods such as co-integration and z-score thresholds to identify trading opportunities.

## Data Sources
- **Yahoo Finance:** Historical price data is downloaded using the `yfinance` library.
- **Time Horizon:** Data covers the past 5 years with daily observations.

## Research
- **Concepts:** The strategy is built on pairs trading principles, focusing on market neutrality, co-integration, and mean reversion.
- **Candidate Pairs:** We begin by analyzing stocks from the same sector or ETFs that exhibit correlated behavior. Detailed research notes are provided in `research_notes.md`.

## Roadmap
- **1)** Research & Data Preparation
- **2)** Strategy Development (statistical tests, signal logic, and parameter tuning)
- **3)** Backtesting & Evaluation (trade simulation, performance metrics, and visualization)

## Repository Structure
- `README.md` – Project overview and documentation.
- `research_notes.md` – Detailed research and candidate pairs analysis.
- `scripts/`
  - `data_acquisition.py` – Script to download historical price data.
- `notebooks/`
  - `data_eda.ipynb` – Jupyter Notebook for data cleaning and exploratory data analysis.
