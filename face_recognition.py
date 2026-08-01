import os
import pickle

import cv2
import face_recognition
import numpy as np

EMBEDDINGS_DIR = "embeddings"

os.makedirs(EMBEDDINGS_DIR, exist_ok=True)

MATCH_THRESHOLD = 0.50


def load_image(image_path: str):

    image = face_recognition.load_image_file(image_path)

    return image


def detect_face(image):

    locations = face_recognition.face_locations(image)

    return locations


def generate_embedding(image):

    locations = detect_face(image)

    if len(locations) == 0:
        return None

    encodings = face_recognition.face_encodings(
        image,
        locations
    )

    if len(encodings) == 0:
        return None

    return encodings[0]


def save_embedding(student_id: int, embedding):

    file_path = os.path.join(
        EMBEDDINGS_DIR,
        f"{student_id}.pkl"
    )

    with open(file_path, "wb") as file:
        pickle.dump(embedding, file)


def load_embedding(student_id: int):

    file_path = os.path.join(
        EMBEDDINGS_DIR,
        f"{student_id}.pkl"
    )

    if not os.path.exists(file_path):
        return None

    with open(file_path, "rb") as file:
        return pickle.load(file)


def register_face(student_id: int, image_path: str):

    image = load_image(image_path)

    embedding = generate_embedding(image)

    if embedding is None:
        return False

    save_embedding(student_id, embedding)

    return True


def compare_faces(known_embedding, unknown_embedding):

    distance = np.linalg.norm(
        known_embedding - unknown_embedding
    )

    return distance


def recognize_face(image_path: str):

    image = load_image(image_path)

    unknown_embedding = generate_embedding(image)

    if unknown_embedding is None:
        return None

    best_student = None

    best_distance = 100

    for filename in os.listdir(EMBEDDINGS_DIR):

        if not filename.endswith(".pkl"):
            continue

        student_id = int(filename.split(".")[0])

        known_embedding = load_embedding(student_id)

        distance = compare_faces(
            known_embedding,
            unknown_embedding
        )

        if distance < best_distance:
            best_distance = distance
            best_student = student_id

    if best_distance <= MATCH_THRESHOLD:

        confidence = round(
            (1 - best_distance) * 100,
            2
        )

        return {
            "student_id": best_student,
            "confidence": confidence
        }

    return None


def recognize_from_webcam():

    camera = cv2.VideoCapture(0)

    while True:

        success, frame = camera.read()

        if not success:
            break

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        locations = detect_face(rgb)

        encodings = face_recognition.face_encodings(
            rgb,
            locations
        )

        for (top, right, bottom, left), encoding in zip(
            locations,
            encodings
        ):

            result = None

            best_distance = 100

            for filename in os.listdir(EMBEDDINGS_DIR):

                if not filename.endswith(".pkl"):
                    continue

                student_id = int(
                    filename.split(".")[0]
                )

                known = load_embedding(student_id)

                distance = compare_faces(
                    known,
                    encoding
                )

                if distance < best_distance:
                    best_distance = distance
                    result = student_id

            if result is not None and best_distance <= MATCH_THRESHOLD:

                label = f"ID:{result}"

            else:

                label = "Unknown"

            cv2.rectangle(
                frame,
                (left, top),
                (right, bottom),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                label,
                (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 0, 0),
                2
            )

        cv2.imshow(
            "AI Facial Attendance",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()

    cv2.destroyAllWindows()