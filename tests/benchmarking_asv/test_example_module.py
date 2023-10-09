"""An example module containing testing of mock functions."""

import benchmarking_asv


def test_greetings() -> None:
    """Verify the output of the `greetings` function"""
    output = benchmarking_asv.example_module.greetings()
    assert output == "Hello from LINCC-Frameworks!"


def test_meaning() -> None:
    """Verify the output of the `meaning` function"""
    output = benchmarking_asv.example_module.meaning()
    assert output == 42
