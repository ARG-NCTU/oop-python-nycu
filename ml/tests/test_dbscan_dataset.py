import add_path
import numpy as np
import pytest
from dbscan.dataset import ConcentricCircle, GaussianMixture, TwoMoon


# Tests for GaussianMixture dataset
def test_gaussian_mixture_initialization():
    dataset = GaussianMixture()
    assert dataset is not None

def test_gaussian_mixture_generate_data():
    dataset = GaussianMixture()
    dataset.generate_data()
    assert dataset.data is not None
    assert dataset.label is not None
    assert dataset.centers is not None

def test_gaussian_mixture_visualize():
    dataset = GaussianMixture()
    dataset.generate_data()
    dataset.visualize(save=True, save_name="test_gaussian_mixture")

# Tests for TwoMoon dataset
def test_two_moon_initialization():
    dataset = TwoMoon()
    assert dataset is not None

def test_two_moon_generate_data():
    dataset = TwoMoon()
    dataset.generate_data()
    assert dataset.data is not None
    assert dataset.label is not None

def test_two_moon_visualize():
    dataset = TwoMoon()
    dataset.generate_data()
    dataset.visualize(save=True, save_name="test_two_moon")

# Tests for ConcentricCircle dataset
def test_concentric_circle_initialization():
    dataset = ConcentricCircle()
    assert dataset is not None

def test_concentric_circle_generate_data():
    dataset = ConcentricCircle()
    dataset.generate_data()
    assert dataset.data is not None
    assert dataset.label is not None

def test_concentric_circle_visualize():
    dataset = ConcentricCircle()
    dataset.generate_data()
    dataset.visualize(save=True, save_name="test_concentric_circle")
