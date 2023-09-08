"""An example module containing testing of mock functions."""

from benchmarking_asv import example_module


def test_greetings() -> None:
    """Verify the output of the `greetings` function"""
    output = example_module.greetings()
    assert output == "Hello from LINCC-Frameworks!"


def test_meaning() -> None:
    output = example_module.meaning()
    assert output ==    42
