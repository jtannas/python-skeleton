#!/usr/bin/python3.6
"""Test module for testing the app.example module"""
from app import example


def test_example_main(capsys):
    """Test the main method of the app.example module"""
    example.main()
    out, err = capsys.readouterr()
    assert out == 'Hello, world\n'
    assert err == ''
