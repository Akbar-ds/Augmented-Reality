import streamlit as st
import cv2
import numpy as np

MIN_MATCHES = 20
detector = cv2.ORB_create(nfeatures=5000)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=100)
flann = cv2.FlannBasedMatcher(index_params, search_params)

def load_input():
    input_image = cv2.imread("E:\\Downloads\\meluha.jpg")
    augment_image = cv2.imread("E:\\Downloads\\mask.jpg")

    input_image = cv2.resize(input_image, (300, 400), interpolation=cv2.INTER_AREA)
    augment_image = cv2.resize(augment_image, (300, 400))
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # find the keypoints with ORB
    keypoints, descriptors = detector.detectAndCompute(gray_image, None)

    return gray_image, augment_image, keypoints, descriptors

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

def main():
    st.title("Augmented Reality with OpenCV and Streamlit")

    # Custom CSS to increase the button size
    st.markdown("""
        <style>
        .stButton button {
            height: 3em;
            width: 10em;
            font-size: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    if 'run' not in st.session_state:
        st.session_state.run = False

    def start():
        st.session_state.run = True

    def stop():
        st.session_state.run = False

    col1, col2 = st.columns(2)
    with col1:
        st.button('Start', on_click=start)
    with col2:
        st.button('Stop', on_click=stop)

    if st.session_state.run:
        # Getting Information from the Input image
        input_image, augment_image, input_keypoints, input_descriptors = load_input()

        cap = cv2.VideoCapture(0)

        stframe = st.empty()

        while st.session_state.run:
            ret, frame = cap.read()
            if not ret:
                st.write("Failed to capture image")
                break

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

                    stframe.image(final_output, channels="BGR")
                else:
                    stframe.image(frame, channels="BGR")
            else:
                stframe.image(frame, channels="BGR")
            
            key = cv2.waitKey(1)
            if key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()





    
            

