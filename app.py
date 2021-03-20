import ds
import requests
import time

THRESHOLD = 60


def app():
    have_sent = {}
    model_path = 'models/mask_detector.model'
    prototxt_path = 'models/deploy.prototxt'
    weights_path = 'models/res10_300x300_ssd_iter_140000.caffemodel'
    known_face_names, known_face_encodings = ds.services.face_encoder.generate_image_encodings('faces')
    ds.services.detector.setup_mask_models(model_path, prototxt_path, weights_path)

    with ds.services.camera.Camera() as camera:
        for frame in camera.read_frames(no_limit=True):
            locs, preds = ds.services.detector.detect_and_predict_mask(frame)
            has_mask = ds.services.vision.display_mask_with_and_has_mask(frame, locs, preds)

            if not has_mask:
                face_locations, face_names = ds.services.detector.face_detect(
                    frame,
                    known_face_encodings,
                    known_face_names,
                )
                ds.services.vision.display_with(frame, face_locations, face_names)

                for face_name in face_names:
                    if face_name not in have_sent:
                        requests.post(
                            'http://127.0.0.1:5000/nomask',
                            json=(
                                {
                                    'id': face_name,
                                },
                                {
                                    'location': ds.services.location.current_location(),
                                },
                            ),
                        )
                        have_sent[face_name] = (time.time(), 1)
                    else:
                        curr_time = time.time()
                        old_time, count = have_sent[face_name]

                        if curr_time - old_time > THRESHOLD:
                            new_count = count + 1
                            have_sent[face_name] = (curr_time, new_count)

                            # sending to Admin
                            if new_count >= 3:
                                requests.post(
                                    'http://127.0.0.1:5000/admin',
                                    json=(
                                        {
                                            'id': face_name,
                                        },
                                        {
                                            'location': ds.services.location.current_location(),
                                        },
                                    ),
                                )


if __name__ == '__main__':
    app()
