import pytest

@pytest.fixture
def data():
    """Get the data"""
    return ['green onion == scallion', 'coriander != cilantro']

# ---- tests ---- #

# list comparison
def test_example(data):
    """Test equality"""
    expected_data = ['coriander != cilantro', 'green onion == scallion']
    assert all([element in data for element in expected_data])

# element exclusion
def test_example2(data):
    """Test exclusion"""
    undesired_data = ['garbanzo > chickpea', 'filbert > hazlenut']
    assert all([element not in data for element in undesired_data])
  
