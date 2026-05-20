import copy
import dataclasses
import sys
import os
from datetime import datetime

# Set up the path so we can import modules from the main InVesalius directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from invesalius.data.markers.marker import Marker

def test_marker_creation():
    print("--- TEST 1: Creation of a new marker ---")
    
    # Simulate a user click (passing only coordinates)
    new_marker = Marker(x=10.5, y=20.0, z=-5.2)
    
    print(f"Coordinates: {new_marker.position}")
    print(f"Generated timestamp: {new_marker.timestamp}")
    
    # Verify that the timestamp is generated upon initialization
    assert new_marker.timestamp != "", "Error: Timestamp was not generated!"
    print("Test 1 passed successfully!\n")

def test_backward_compatibility():
    print("--- TEST 2: Loading an old file (Backward Compatibility) ---")
    
    # Simulate a real dictionary from a legacy .inv3 file (without the timestamp field)
    legacy_data = {
        "marker_id": 0, "x": 1.0, "y": 2.0, "z": 3.0,
        "alpha": None, "beta": None, "gamma": None,
        "r": 1.0, "g": 1.0, "b": 0.0, "size": 2, "label": "Point A",
        "x_seed": 0, "y_seed": 0, "z_seed": 0,
        "is_target": False, "is_point_of_interest": False, "session_id": 1,
        "x_cortex": None, "y_cortex": None, "z_cortex": None,
        "alpha_cortex": None, "beta_cortex": None, "gamma_cortex": None,
        "marker_type": 1, "z_rotation": 0.0, "z_offset": 0.0,
        "mep_value": None, "brain_target_list": [],
        "x_world": 0.0, "y_world": 0.0, "z_world": 0.0,
        "alpha_world": 0.0, "beta_world": 0.0, "gamma_world": 0.0
        # The "timestamp" field is intentionally omitted here!
    }
    
    empty_marker = Marker()
    
    # Attempt to parse and load the legacy data
    loaded_marker = empty_marker.from_dict(legacy_data)
    
    # Use getattr() for a safe check, since InVesalius might set the missing value to None or ""
    restored_time = getattr(loaded_marker, 'timestamp', "")
    
    print(f"Restored timestamp (should be empty or None): '{restored_time}'")
    
    # Verify that the system handles the missing field gracefully
    assert restored_time in ["", None], "Error: Backward compatibility is not working!"
    print("Test 2 passed successfully!\n")

if __name__ == "__main__":
    test_marker_creation()
    test_backward_compatibility()