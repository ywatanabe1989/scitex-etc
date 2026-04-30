#!/usr/bin/env python3
"""Quickstart for scitex-etc: explore the wait_key submodule API."""

import scitex_etc
import scitex_etc.wait_key as wait_key_mod
from scitex_etc.wait_key import count, wait_key


def main() -> int:
    print(f"scitex_etc.__all__: {scitex_etc.__all__}")
    print(f"wait_key submodule: {wait_key_mod.__name__}")
    print(
        f"wait_key submodule public API: "
        f"{[n for n in dir(wait_key_mod) if not n.startswith('_')]}"
    )

    # Show that the API is importable; we don't invoke wait_key (would block).
    print(f"\nwait_key function: {wait_key.__name__}(p)")
    print(f"count function: {count.__name__}()")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
