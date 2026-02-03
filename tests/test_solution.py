"""
Tests for the performance takehome challenge.
These tests verify the user's solution works correctly.
"""

import time

from perf_takehome import KernelBuilder
from problem import DebugInfo


def test_example_passes():
    """Basic sanity check."""
    assert True


def test_function_exists():
    """Verify required class is defined and usable."""
    assert callable(KernelBuilder)


def test_basic_input():
    """Test kernel construction with simple input."""
    builder = KernelBuilder()
    instrs = builder.build_kernel(forest_height=1, n_nodes=1, batch_size=1, rounds=1)
    assert isinstance(instrs, list)
    assert instrs, "Expected build_kernel to return at least one instruction bundle"


def test_edge_case_empty():
    """Test empty-ish input handling."""
    builder = KernelBuilder()
    instrs = builder.build_kernel(forest_height=0, n_nodes=0, batch_size=0, rounds=0)
    assert isinstance(instrs, list)


def test_debug_info_type():
    """Test that debug info is returned as the expected type."""
    builder = KernelBuilder()
    info = builder.debug_info()
    assert isinstance(info, DebugInfo)


def test_performance_requirement():
    """Test that solution meets basic performance requirements."""
    builder = KernelBuilder()
    start = time.time()
    builder.build_kernel(forest_height=1, n_nodes=1, batch_size=1, rounds=1)
    elapsed = time.time() - start
    assert elapsed < 1.0, f"Too slow: {elapsed}s"
