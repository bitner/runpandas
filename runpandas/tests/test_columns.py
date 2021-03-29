"""
Test module for runpandas column types (i.e. MeasureSeries)
"""

import os
import pytest
from runpandas import reader

pytestmark = pytest.mark.stable


@pytest.fixture
def dirpath(datapath):
    return datapath("io", "data")

def test_altitude_ascent_descent(dirpath):
    tcx_file = os.path.join(dirpath, "tcx", "basic.tcx")
    activity_tcx = reader._read_file(tcx_file, to_df=False)
    # test ascent and descent altitudes
    assert (activity_tcx["alt"].ascent[-5]) == 0.4805908200000033
    assert (activity_tcx["alt"].ascent[-1]) == 0.0
    assert (activity_tcx["alt"].descent[-1]) == -1.4420166019999954
    assert (activity_tcx["alt"].descent[-5]) ==  0.0

def test_distance_miles(dirpath):
    gpx_file = os.path.join(dirpath, "gpx", "stopped_example.gpx")
    activity_gpx = reader._read_file(gpx_file, to_df=False)
    activity_gpx['distpos']  = activity_gpx.compute.distance()
    # test distpos conversion (meters to miles)
    assert (activity_gpx["distpos"].miles[-1]) == 0.0031649143236707027
    # test distance conversion (meters to miles)
    distance = activity_gpx["distpos"].distance
    assert (distance.miles[-1]) == 7.825950111157077

def test_distance_km(dirpath):
    gpx_file = os.path.join(dirpath, "gpx", "stopped_example.gpx")
    activity_gpx = reader._read_file(gpx_file, to_df=False)
    activity_gpx['distpos']  = activity_gpx.compute.distance()
    # test distpos conversion (meters to miles)
    assert (activity_gpx["distpos"].km[-1]) == 0.005093437453100809
    # test distance conversion (meters to miles)
    distance = activity_gpx["distpos"].distance
    assert (distance.km[-1]) == 12.594649752172337

def test_speed_kmh(dirpath):
    tcx_file = os.path.join(dirpath, "tcx", "stopped_example.tcx")
    activity_tcx = reader._read_file(tcx_file, to_df=False)
    # test conversion method m/s to km/h
    assert (activity_tcx["speed"].kph[-1]) == 8.498772

def test_distpos_distance(dirpath):
    gpx_file = os.path.join(dirpath, "gpx", "stopped_example.gpx")
    activity_gpx = reader._read_file(gpx_file, to_df=False)
    activity_gpx['distpos']  = activity_gpx.compute.distance()
    # test distpos to distance
    assert (activity_gpx["distpos"].distance[-1]) == 12594.649752172338

def test_gradient_pct(dirpath):
    tcx_file = os.path.join(dirpath, "tcx", "basic.tcx")
    activity_tcx = reader._read_file(tcx_file, to_df=False)
    activity_tcx['grad'] = activity_tcx.compute.gradient()
    assert(activity_tcx['grad'].pct[-1]) == -9.78415717232968

def test_gradient_radians(dirpath):
    tcx_file = os.path.join(dirpath, "tcx", "basic.tcx")
    activity_tcx = reader._read_file(tcx_file, to_df=False)
    activity_tcx['grad'] = activity_tcx.compute.gradient()
    assert(activity_tcx['grad'].radians[-1]) == -0.0975311412476771

def test_gradient_degrees(dirpath):
    tcx_file = os.path.join(dirpath, "tcx", "basic.tcx")
    activity_tcx = reader._read_file(tcx_file, to_df=False)
    activity_tcx['grad'] = activity_tcx.compute.gradient()
    assert(activity_tcx['grad'].degrees[-1]) == -5.588122764586196