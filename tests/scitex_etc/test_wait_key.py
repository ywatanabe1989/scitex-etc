#!/usr/bin/env python3
# Timestamp: "2025-06-02 15:05:32 (ywatanabe)"
# File: tests/scitex_etc/test_wait_key.py
# ----------------------------------------
import inspect
import os
from unittest.mock import Mock, call, patch

import pytest

# Required for scitex_etc.wait_key module
pytest.importorskip("readchar")

__FILE__ = "./tests/scitex/etc/test_wait_key.py"
__DIR__ = os.path.dirname(__FILE__)
# ----------------------------------------


class TestWaitKey:
    """Tests for scitex_etc.wait_key module — one assertion per test."""

    # ------------------------------------------------------------------
    # wait_key: basic q press
    # ------------------------------------------------------------------
    def test_wait_key_with_q_press_terminates_process(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        mock_process = Mock()
        # Act
        with patch("scitex_etc.wait_key.readchar.readchar", return_value="q"):
            with patch("builtins.print"):
                wait_key(mock_process)
        # Assert
        assert mock_process.terminate.call_count == 1

    def test_wait_key_with_q_press_prints_q_then_quit_message(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        mock_process = Mock()
        # Act
        with patch("scitex_etc.wait_key.readchar.readchar", return_value="q"):
            with patch("builtins.print") as mock_print:
                wait_key(mock_process)
        # Assert
        assert mock_print.call_args_list == [call("q"), call("q was pressed.")]

    # ------------------------------------------------------------------
    # wait_key: multiple keys before q
    # ------------------------------------------------------------------
    def test_wait_key_with_multiple_keys_terminates_after_q(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        mock_process = Mock()
        key_sequence = ["a", "b", "c", "q"]
        # Act
        with patch("scitex_etc.wait_key.readchar.readchar", side_effect=key_sequence):
            with patch("builtins.print"):
                wait_key(mock_process)
        # Assert
        assert mock_process.terminate.call_count == 1

    def test_wait_key_with_multiple_keys_prints_all_keys_and_message(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        mock_process = Mock()
        key_sequence = ["a", "b", "c", "q"]
        expected = [call("a"), call("b"), call("c"), call("q"), call("q was pressed.")]
        # Act
        with patch("scitex_etc.wait_key.readchar.readchar", side_effect=key_sequence):
            with patch("builtins.print") as mock_print:
                wait_key(mock_process)
        # Assert
        assert mock_print.call_args_list == expected

    # ------------------------------------------------------------------
    # wait_key: special characters before q
    # ------------------------------------------------------------------
    def test_wait_key_with_special_chars_terminates_after_q(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        mock_process = Mock()
        key_sequence = ["\n", "\t", " ", "1", "!", "q"]
        # Act
        with patch("scitex_etc.wait_key.readchar.readchar", side_effect=key_sequence):
            with patch("builtins.print"):
                wait_key(mock_process)
        # Assert
        assert mock_process.terminate.call_count == 1

    def test_wait_key_with_special_chars_prints_all_keys(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        mock_process = Mock()
        key_sequence = ["\n", "\t", " ", "1", "!", "q"]
        expected = [
            call("\n"),
            call("\t"),
            call(" "),
            call("1"),
            call("!"),
            call("q"),
            call("q was pressed."),
        ]
        # Act
        with patch("scitex_etc.wait_key.readchar.readchar", side_effect=key_sequence):
            with patch("builtins.print") as mock_print:
                wait_key(mock_process)
        # Assert
        assert mock_print.call_args_list == expected

    # ------------------------------------------------------------------
    # wait_key: case sensitivity — uppercase Q does not terminate
    # ------------------------------------------------------------------
    def test_wait_key_with_uppercase_q_then_lowercase_q_terminates_once(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        mock_process = Mock()
        key_sequence = ["Q", "q"]
        # Act
        with patch("scitex_etc.wait_key.readchar.readchar", side_effect=key_sequence):
            with patch("builtins.print"):
                wait_key(mock_process)
        # Assert
        assert mock_process.terminate.call_count == 1

    def test_wait_key_with_uppercase_q_then_lowercase_q_prints_both(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        mock_process = Mock()
        key_sequence = ["Q", "q"]
        expected = [call("Q"), call("q"), call("q was pressed.")]
        # Act
        with patch("scitex_etc.wait_key.readchar.readchar", side_effect=key_sequence):
            with patch("builtins.print") as mock_print:
                wait_key(mock_process)
        # Assert
        assert mock_print.call_args_list == expected

    # ------------------------------------------------------------------
    # wait_key: does not call kill() — only terminate()
    # ------------------------------------------------------------------
    def test_wait_key_with_q_press_does_not_call_kill(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        mock_process = Mock()
        # Act
        with patch("scitex_etc.wait_key.readchar.readchar", return_value="q"):
            with patch("builtins.print"):
                wait_key(mock_process)
        # Assert
        assert mock_process.kill.called is False

    # ------------------------------------------------------------------
    # count: increments counter (uses KeyboardInterrupt to escape loop)
    # ------------------------------------------------------------------
    def test_count_prints_incrementing_values_starting_at_zero(self):
        # Arrange
        from scitex_etc.wait_key import count

        printed_values = []

        def fake_print(value):
            printed_values.append(value)
            if len(printed_values) >= 5:
                raise KeyboardInterrupt("stop")

        # Act
        with patch("scitex_etc.wait_key.time.sleep"):
            with patch("builtins.print", side_effect=fake_print):
                try:
                    count()
                except KeyboardInterrupt:
                    pass
        # Assert
        assert printed_values == [0, 1, 2, 3, 4]

    def test_count_runs_until_keyboardinterrupt_is_raised(self):
        # Arrange
        from scitex_etc.wait_key import count

        call_counter = {"n": 0}

        def fake_print(value):
            call_counter["n"] += 1
            if call_counter["n"] >= 10:
                raise KeyboardInterrupt("stop")

        # Act
        with patch("scitex_etc.wait_key.time.sleep"):
            with patch("builtins.print", side_effect=fake_print):
                try:
                    count()
                except KeyboardInterrupt:
                    pass
        # Assert
        assert call_counter["n"] == 10

    def test_count_calls_sleep_between_prints(self):
        # Arrange
        from scitex_etc.wait_key import count

        printed = []

        def fake_print(value):
            printed.append(value)
            if len(printed) >= 3:
                raise KeyboardInterrupt("stop")

        # Act
        with patch("scitex_etc.wait_key.time.sleep") as mock_sleep:
            with patch("builtins.print", side_effect=fake_print):
                try:
                    count()
                except KeyboardInterrupt:
                    pass
        # Assert
        assert mock_sleep.call_count == 2

    # ------------------------------------------------------------------
    # module structure
    # ------------------------------------------------------------------
    def test_module_exposes_readchar_attribute_for_patching(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        has_readchar = hasattr(module_under_test, "readchar")
        # Assert
        assert has_readchar is True

    def test_module_exposes_callable_readchar_readchar(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_callable = callable(module_under_test.readchar.readchar)
        # Assert
        assert is_callable is True

    def test_module_exposes_multiprocessing_attribute(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        has_mp = hasattr(module_under_test, "multiprocessing")
        # Assert
        assert has_mp is True

    def test_module_exposes_multiprocessing_process_class(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        has_process = hasattr(module_under_test.multiprocessing, "Process")
        # Assert
        assert has_process is True

    def test_module_exposes_time_attribute_for_patching(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        has_time = hasattr(module_under_test, "time")
        # Assert
        assert has_time is True

    def test_module_exposes_callable_time_sleep(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_callable = callable(module_under_test.time.sleep)
        # Assert
        assert is_callable is True

    def test_module_defines_wait_key_function(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        has_wait_key = hasattr(module_under_test, "wait_key")
        # Assert
        assert has_wait_key is True

    def test_module_defines_count_function(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        has_count = hasattr(module_under_test, "count")
        # Assert
        assert has_count is True

    def test_module_wait_key_is_callable(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_callable = callable(module_under_test.wait_key)
        # Assert
        assert is_callable is True

    def test_module_count_is_callable(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_callable = callable(module_under_test.count)
        # Assert
        assert is_callable is True

    def test_module_wait_key_is_function(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_fn = inspect.isfunction(module_under_test.wait_key)
        # Assert
        assert is_fn is True

    def test_module_count_is_function(self):
        # Arrange
        import scitex_etc.wait_key as module_under_test

        # Act
        is_fn = inspect.isfunction(module_under_test.count)
        # Assert
        assert is_fn is True

    # ------------------------------------------------------------------
    # function signatures
    # ------------------------------------------------------------------
    def test_wait_key_signature_has_one_parameter(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        # Act
        params = inspect.signature(wait_key).parameters
        # Assert
        assert len(params) == 1

    def test_wait_key_signature_parameter_is_named_p(self):
        # Arrange
        from scitex_etc.wait_key import wait_key

        # Act
        params = inspect.signature(wait_key).parameters
        # Assert
        assert "p" in params

    def test_count_signature_has_no_parameters(self):
        # Arrange
        from scitex_etc.wait_key import count

        # Act
        params = inspect.signature(count).parameters
        # Assert
        assert len(params) == 0


if __name__ == "__main__":
    import pytest

    pytest.main([os.path.abspath(__file__)])

# --------------------------------------------------------------------------------
# Start of Source Code from: src/scitex_etc/wait_key.py
# --------------------------------------------------------------------------------
# import multiprocessing
# import time
# import readchar
#
# def wait_key(p):
#     key = "x"
#     while key != "q":
#         key = readchar.readchar()
#         print(key)
#     print("q was pressed.")
#     p.terminate()
#
# def count():
#     counter = 0
#     while True:
#         print(counter)
#         time.sleep(1)
#         counter += 1
# --------------------------------------------------------------------------------
# End of Source Code
# --------------------------------------------------------------------------------
