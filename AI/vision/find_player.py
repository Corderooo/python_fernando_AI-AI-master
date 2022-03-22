import cv2
from rotation_invariavant_match import get_matched_coordinates

needle_image = "AI/player.png"
map_image = "AI/vision/map.PNG"

needle = cv2.imread(needle_image,cv2.IMREAD_GRAYSCALE)
map = cv2.imread(map_image,cv2.IMREAD_GRAYSCALE)

needle = cv2.equalizeHist(needle)
map = cv2.equalizeHist(map)

print(get_matched_coordinates(needle, map))