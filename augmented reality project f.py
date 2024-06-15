import cv2
import numpy as np

# Setting up OpenCV and numpy
# Defining minimum matches threshold
# Initializing ORB detector with specific parameters

MIN_MATCHES = 20
detector = cv2.ORB_create(nfeatures=5000)


# Setting FLANN parameters for descriptor matching

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=100)
flann = cv2.FlannBasedMatcher(index_params, search_params)


# Loading input and augmenting images from file
# Resizing input and augmenting images
# Converting input image to grayscale
# Detecting keypoints and computing descriptors for input image

def load_input():
    input_image = cv2.imread("E:\Downloads\meluha.jpg")
    augment_image = cv2.imread("E:\Downloads\mask.jpg")

    input_image = cv2.resize(input_image, (300, 400), interpolation=cv2.INTER_AREA)
    augment_image = cv2.resize(augment_image, (300, 400))
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # find the keypoints with ORB
    keypoints, descriptors = detector.detectAndCompute(gray_image, None)

    return gray_image, augment_image, keypoints, descriptors


# Capturing frames from webcam
# Resizing captured frame
# Converting captured frame to grayscale
# Detecting keypoints and computing descriptors for captured frame
# Matching descriptors between input and captured frames
# Filtering matches based on distance ratio


def compute_matches(descriptors_input, descriptors_output):
    # Match descriptors
    if len(descriptors_output) != 0 and len(descriptors_input) != 0:
        matches = flann.knnMatch(np.asarray(descriptors_input, np.float32), np.asarray(descriptors_output, np.float32),
                                 k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.69 * n.distance:
                good.append(m)
        return good
    else:
        return None


if __name__ == '__main__':
    # Getting Information from the Input image
    input_image, augment_image, input_keypoints, input_descriptors = load_input()

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if len(input_keypoints) < MIN_MATCHES:
            continue

        frame = cv2.resize(frame, (600, 450))
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        output_keypoints, output_descriptors = detector.detectAndCompute(frame_bw, None)
        matches = compute_matches(input_descriptors, output_descriptors)

        if matches is not None:
            if len(matches) > 10:
                src_pts = np.float32([input_keypoints[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
                dst_pts = np.float32([output_keypoints[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

                # Find the homography matrix
                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                pts = np.float32([[0, 0], [0, 399], [299, 399], [299, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)
                M_aug = cv2.warpPerspective(augment_image, M, (600, 450))

                # Prepare the frame for addition operation with Mask Image
                frame_b = cv2.fillConvexPoly(frame, dst.astype(int), 0)
                final_output = frame_b + M_aug

                # Displaying final augmented output frame
                # Handling user key press events (e.g., exit on 'Esc' key)


                cv2.imshow('Final Output', final_output)
            else:
                cv2.imshow('Final Output', frame)
        else:
            cv2.imshow('Final Output', frame)

        key = cv2.waitKey(15)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    
            

