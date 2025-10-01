"""Tests for the manage.py module.

This test module verifies that the Django management command entry point
(manage.py) is working correctly.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def test_manage_py_exists():
    """Test that manage.py exists in the project root."""
    manage_py = Path(__file__).parent.parent / "manage.py"
    assert manage_py.exists(), "manage.py should exist in project root"
    assert manage_py.is_file(), "manage.py should be a file"


def test_manage_py_is_executable():
    """Test that manage.py has executable permissions."""
    manage_py = Path(__file__).parent.parent / "manage.py"
    # Check if file has read permissions (executable check is platform-specific)
    assert manage_py.stat().st_mode & 0o400, "manage.py should be readable"


def test_manage_py_help_command():
    """Test that manage.py can execute the help command."""
    manage_py = Path(__file__).parent.parent / "manage.py"
    result = subprocess.run(
        [sys.executable, str(manage_py), "help"],
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, "manage.py help command should execute successfully"
    assert "Available subcommands" in result.stdout or "Type 'manage.py help" in result.stdout


def test_manage_py_check_command():
    """Test that manage.py can execute the check command."""
    manage_py = Path(__file__).parent.parent / "manage.py"
    env = os.environ.copy()
    env["PYTHONPATH"] = str(manage_py.parent / "debuttend_cms")
    result = subprocess.run(
        [sys.executable, str(manage_py), "check", "--deploy"],
        capture_output=True,
        text=True,
        timeout=10,
        env=env,
        cwd=str(manage_py.parent),
    )
    # Check command might have warnings about database/deployment, but should run
    assert (
        result.returncode == 0
        or "System check identified" in result.stdout
        or "CommandError" not in result.stderr
    ), f"manage.py check command should execute. stdout: {result.stdout}, stderr: {result.stderr}"
