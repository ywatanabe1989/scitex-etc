#!/usr/bin/env python3
"""Quickstart for scitex-etc: explore the media submodule API."""

import scitex_etc
import scitex_etc.media as media_mod
from scitex_etc.media.render import classify, detect


def main() -> int:
    print(f"scitex_etc.__all__: {scitex_etc.__all__}")
    print(f"media submodule: {media_mod.__name__}")
    print(
        f"media.render public API: "
        f"{[n for n in dir(media_mod.render) if not n.startswith('_')]}"
    )

    # Show that the API is importable.
    print(f"\nclassify function: {classify.__name__}(path)")
    print(f"detect function: {detect.__name__}(text)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
