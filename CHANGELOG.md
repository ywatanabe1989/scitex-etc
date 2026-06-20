# Changelog

All notable changes to `scitex-etc` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.1]

### Changed

- CI/CD workflows standardized to the canonical fleet set
  (`pytest-matrix`, `import-smoke`, `quality`, `docs`, `release`,
  `newb`, `auto-merge-to-develop`, `cla`) on `ubuntu-latest`. The
  pytest matrix now uploads coverage to Codecov with a per-job `HOME`
  and `disable_safe_directory: true`. The previous consolidated
  `ci.yml`/`release.yml` were removed.
- Back-merged `main` into `develop` to reconcile release metadata.

## [0.2.0]

### Added

- `scitex_etc.media` — media handling absorbed from the `scitex` umbrella
  (`scitex.media`, umbrella-thinning Phase A, ADR 0001). Public surface:
  `scitex_etc.media.render.{classify, detect, show, MEDIA_EXTENSIONS}`, the
  `python -m scitex_etc.media.render` CLI, and the
  `scitex_etc.media.render.mcp_server` MCP tools. The umbrella now re-exports
  `scitex.media` from `scitex_etc.media`.

## [0.1.5]

- Initial CHANGELOG entry — see git log for prior history.
