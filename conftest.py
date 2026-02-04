import pytest
from utils.config_loader import get_config

@pytest.fixture(scope="session")
def base_url():
    return get_config('env', 'base_url')