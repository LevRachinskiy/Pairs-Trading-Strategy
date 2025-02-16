# Pairs Trading Research Notes

## Concept Overview
- **Pairs Trading:** A market-neutral strategy that identifies two correlated assets and exploits deviations from their historical relationship.
- **Market Neutrality:** The strategy aims to hedge out systematic market risk by taking offsetting positions.
- **Co-integration:** Statistical tests (e.g., Engle-Granger) are used to verify that a pair of assets share a long-term equilibrium relationship.
- **Z-Score Thresholds:** Calculated from the spread between asset prices to identify statistically significant deviations that signal potential trades.

## Candidate Pairs
- **Example:** JPMorgan Chase (JPM) and Bank of America (BAC) have been identified as potential candidates due to their similar industry dynamics.
- Further analysis is required to validate the correlation and co-integration of the selected pairs.

## Next Steps
- Download and preprocess historical price data.
- Conduct exploratory data analysis (EDA) to assess the viability of the candidate pairs.
