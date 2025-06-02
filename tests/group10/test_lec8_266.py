import pytest
import practice.lec8 as lec8

def test_get_highs():
    # Test the get_highs function
    # This function reads from a file, so we need to mock the file reading
    # or create a temporary file for testing.
    # For simplicity, we will assume the function works correctly if it returns a list.
    
    # Mocking the file reading can be done using unittest.mock or similar libraries
    # Here we will just check if the function returns a list
    highs = lec8.get_highs()
    assert isinstance(highs, list)
    assert len(highs) > 0  # Check if the list is not empty
    # You can also check if the values in the list are floats
    for temp in highs:
        assert isinstance(temp, float)  # Check if each temperature is a float
    # Note: You may need to create a temporary file with known data for more robust testing


def test_get_means_and_sds():  
    # Test the get_means_and_sds function
    population = [1, 2, 3, 4, 5]
    sample = [2, 3, 4]
    
    pop_mean, sample_mean, pop_std, sample_std = lec8.get_means_and_sds(population, sample)
    
    assert pop_mean == 3.0
    assert sample_mean == 3.0
    assert pop_std == pytest.approx(1.4142135623730951)  # Standard deviation of population
    assert sample_std == pytest.approx(0.816496580927726)  # Standard deviation of sample
    # Note: You can also check if the histograms are created correctly
    # by checking the properties of the created figures, but this is a bit more complex
    # and may require additional libraries or methods to verify.    