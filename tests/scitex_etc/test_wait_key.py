#!/usr/bin/env python3
# File: tests/scitex_etc/test_wait_key.py
# ----------------------------------------
"""Tests for scitex_etc.wait_key — real collaborators only, no mocks.

PA-306: no ``unittest.mock``, no ``monkeypatch``. The SUT exposes injectable
seams (``read_key``/``printer`` for ``wait_key``, ``printer``/``sleeper`` for
``count``) that default to the real implementations. Tests pass hand-rolled
fakes: a list-driven key source, a recording printer, a bounded sleeper, and a
process fake that records ``terminate``/``kill`` calls.
"""

import inspect
import os

import pytest

# Required for scitex_etc.wait_key module
pytest.importorskip("readchar")

# ----------------------------------------


class RecordingProcess:
    """Process fake recording terminate()/kill() invocations."""

    def __init__(self):
        self.terminate_calls = 0
        self.kill_calls = 0

    def terminate(self):
        self.terminate_calls += 1

    def kill(self):
        self.kill_calls += 1


class RecordingPrinter:
    """Callable that records every printed value in order."""

    def __init__(self):
        self.values = []

    def __call__(self, value):
        self.values.append(value)


def keys_from(sequence):
    """Return a zero-arg callable yielding the given keys in order."""
    it = iter(sequence)

    def _read_key():
        return next(it)

    return _read_key


class BoundedSleeper:
    """Sleep fake that records call count and stops a loop after `limit`."""

    def __init__(self, limit):
        self.limit = limit
        self.calls = 0

    def __call__(self, _seconds):
        self.calls += 1
        if self.calls >= self.limit:
            raise KeyboardInterrupt("stop")


class TestWaitKey:
    """wait_key: terminate-on-q, echo behaviour, kill restraint."""

    def test_wait_key_with_q_press_terminates_process_once(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        process = RecordingProcess()
        # Act
        wait_key(process, read_key=keys_from(["q"]), printer=RecordingPrinter())
        # Assert
        assert process.terminate_calls == 1

    def test_wait_key_with_q_press_echoes_q_then_quit_message(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        printer = RecordingPrinter()
        # Act
        wait_key(RecordingProcess(), read_key=keys_from(["q"]), printer=printer)
        # Assert
        assert printer.values == ["q", "q was pressed."]

    def test_wait_key_with_multiple_keys_terminates_after_q(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        process = RecordingProcess()
        # Act
        wait_key(
            process,
            read_key=keys_from(["a", "b", "c", "q"]),
            printer=RecordingPrinter(),
        )
        # Assert
        assert process.terminate_calls == 1

    def test_wait_key_with_multiple_keys_echoes_each_key_then_message(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        printer = RecordingPrinter()
        # Act
        wait_key(
            RecordingProcess(),
            read_key=keys_from(["a", "b", "c", "q"]),
            printer=printer,
        )
        # Assert
        assert printer.values == ["a", "b", "c", "q", "q was pressed."]

    def test_wait_key_with_special_chars_terminates_after_q(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        process = RecordingProcess()
        # Act
        wait_key(
            process,
            read_key=keys_from(["\n", "\t", " ", "1", "!", "q"]),
            printer=RecordingPrinter(),
        )
        # Assert
        assert process.terminate_calls == 1

    def test_wait_key_with_special_chars_echoes_all_keys_then_message(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        printer = RecordingPrinter()
        # Act
        wait_key(
            RecordingProcess(),
            read_key=keys_from(["\n", "\t", " ", "1", "!", "q"]),
            printer=printer,
        )
        # Assert
        assert printer.values == ["\n", "\t", " ", "1", "!", "q", "q was pressed."]

    def test_wait_key_with_uppercase_q_does_not_terminate_until_lowercase(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        process = RecordingProcess()
        # Act
        wait_key(process, read_key=keys_from(["Q", "q"]), printer=RecordingPrinter())
        # Assert
        assert process.terminate_calls == 1

    def test_wait_key_with_uppercase_q_then_lowercase_echoes_both(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        printer = RecordingPrinter()
        # Act
        wait_key(RecordingProcess(), read_key=keys_from(["Q", "q"]), printer=printer)
        # Assert
        assert printer.values == ["Q", "q", "q was pressed."]

    def test_wait_key_with_q_press_never_calls_kill(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        process = RecordingProcess()
        # Act
        wait_key(process, read_key=keys_from(["q"]), printer=RecordingPrinter())
        # Assert
        assert process.kill_calls == 0


class TestCount:
    """count: incrementing values, sleep between prints."""

    def test_count_prints_incrementing_values_starting_at_zero(self):
        # Arrange
        from scitex_etc.wait_key import count

        printer = RecordingPrinter()
        # Act — BoundedSleeper raises KeyboardInterrupt to escape the loop
        try:
            count(printer=printer, sleeper=BoundedSleeper(limit=5))
        except KeyboardInterrupt:
            pass
        # Assert
        assert printer.values == [0, 1, 2, 3, 4]

    def test_count_sleeps_between_each_printed_value(self):
        # Arrange
        from scitex_etc.wait_key import count

        sleeper = BoundedSleeper(limit=3)
        # Act — BoundedSleeper raises KeyboardInterrupt to escape the loop
        try:
            count(printer=RecordingPrinter(), sleeper=sleeper)
        except KeyboardInterrupt:
            pass
        # Assert
        assert sleeper.calls == 3


class TestModuleStructure:
    """Module exposes the documented public API."""

    def test_module_defines_callable_wait_key_function(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_callable = callable(getattr(module_under_test, "wait_key", None))
        # Assert
        assert is_callable is True

    def test_module_defines_callable_count_function(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_callable = callable(getattr(module_under_test, "count", None))
        # Assert
        assert is_callable is True

    def test_module_wait_key_is_a_python_function(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_fn = inspect.isfunction(module_under_test.wait_key)
        # Assert
        assert is_fn is True

    def test_module_count_is_a_python_function(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_fn = inspect.isfunction(module_under_test.count)
        # Assert
        assert is_fn is True

    def test_wait_key_signature_accepts_a_process_named_p(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        # Act
        params = inspect.signature(wait_key).parameters
        # Assert
        assert "p" in params


if __name__ == "__main__":
    pytest.main([os.path.abspath(__file__)])
