import cv2
import numpy as np

# Question 1
video = cv2.VideoCapture('Test_video.avi')
ret1, frame1 = video.read()
ret2, frame2 = video.read()
if ret1 and ret2:
    cv2.imshow('Frame 1', frame1)
    cv2.imshow('Frame 2', frame2)
    # frame1 = ((2 * frame1.astype(np.float32) + 70) / 3).astype(np.uint8)
    # edges = cv2.Canny(frame1, 50, 150, apertureSize=3, L2gradient=True)
    # kernel = np.ones((3,3), np.uint8)
    # edges = cv2.dilate(edges, kernel, iterations=1)
    # cv2.imshow('Edges', edges)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()

# # Question 3
# sift = cv2.SIFT_create()
# kp1, des1 = sift.detectAndCompute(frame1, None)
# kp2, des2 = sift.detectAndCompute(frame2, None)
# bf = cv2.BFMatcher()
# matches = bf.match(des1, des2)
# matches = sorted(matches, key=lambda x: x.distance)
# img_matches = cv2.drawMatches(frame1, kp1, frame2, kp2, matches[:10], None, flags=2)
# cv2.imshow('SIFT Matches', img_matches)
# diff = cv2.absdiff(frame1, frame2)
# cv2.imshow('Difference', diff)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # Question 2
# coins = cv2.imread('coins.jpg')
# gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=60)
# output = coins.copy()
# if circles is not None:
#     circles = np.uint16(np.around(circles))
#     for i in circles[0, :]:
#         cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)
#         cv2.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)
# cv2.imshow('Coins Detected', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # Question 4
# left = cv2.imread('left.jpg', 0)
# right = cv2.imread('right.jpg', 0)
# stereo = cv2.StereoBM_create(numDisparities=16*4, blockSize=15)
# disparity = stereo.compute(left, right)
# cv2.imshow('Disparity', (disparity/np.max(disparity)*255).astype(np.uint8))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#















































