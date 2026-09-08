# v1.10 audit outputs

The JSON files committed in this directory are compact audit summaries of the executed v1.10 benchmarks.

The canonical simulation scripts write their detailed generated outputs to this same `analysis/results_v1.10/` directory using `mcift_v110_*` filenames. Those generated JSON/CSV traces may contain more detail than the compact committed summaries.

Large time-series traces are intentionally not committed; they are reproducible by rerunning the corresponding simulation scripts.

This distinction keeps the repository reviewable while preserving the reported benchmark values and claim boundaries.
