import cv2
import pytest

from TC_Face_detection_in_video_stream import test_face_detection_video_stream 

faces,face_locations=test_face_detection_video_stream()
def test_atleast_one_face_detected():
    assert len(face_locations) > 0

def test_all_face_ids_are_integers():
    # Check that all face IDs are integers
    assert all(isinstance(fid, int) for fid in face_locations.keys())

def test_all_face_centers_are_tuples():
    # Check that all face centers are tuples with two elements
    assert all(isinstance(loc, tuple) and len(loc) == 2 for loc in face_locations.values())

def test_face_count():
    # Check that the face count is accurate
    assert len(face_locations) == sum(1 for _ in faces)
