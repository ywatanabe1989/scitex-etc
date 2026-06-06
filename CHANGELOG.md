# Changelog

All notable changes to `scitex-etc` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.3.0]

### Removed

- `wait_key` / `count` — moved to **scitex-parallel** v0.2.0, unified with
  `scitex_gen.wait_key` under the signature `wait_key(process, key='q')`.
  Removes `readchar` from runtime dependencies.

### Retained

- `scitex_etc.media` — chat-pane / terminal / markdown media-reference
  detection & display (ADR-0001 in scitex-python). Public surface:
  `scitex_etc.media.render.{classify, detect, show, MEDIA_EXTENSIONS}`,
  the `python -m scitex_etc.media.render` CLI, and the
  `scitex_etc.media.render.mcp_server` MCP tools. The umbrella
  (`scitex.media`) re-exports from here.
- `count_grids`, `yield_grids` — parameter-grid iteration helpers
  (migrated from the umbrella in PR #21, Phase A).
- `search` — small substring/pattern search helper
  (migrated from the umbrella in PR #21, Phase A).

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
