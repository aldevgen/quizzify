"""Test main object."""

import pytest
from app.main import app
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def quizzify_test_app() -> FastAPI:
    """Create a FastAPI application for testing."""
    with TestClient(app) as client:
        yield client
