import ds
import requests


def face_app():
    known_face_names, known_face_encodings = ds.services.face_encoder.generate_image_encodings('faces')
    have_sent = set()

    with ds.services.camera.Camera() as camera:
        for frame in camera.read_frames(no_limit=True):
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
                        json=({'id': face_name}),
                    )
                    have_sent.add(face_name)


def mask_app():

    model_path = 'models/mask_detector.model'
    prototxt_path = 'models/deploy.prototxt'
    weights_path = 'models/res10_300x300_ssd_iter_140000.caffemodel'

    ds.services.detector.setup_mask_models(model_path, prototxt_path, weights_path)

    with ds.services.camera.Camera() as camera:
        for frame in camera.read_frames(no_limit=True):
            locs, preds = ds.services.detector.detect_and_predict_mask(frame)
            ds.services.vision.display_mask_with(frame, locs, preds)


if __name__ == '__main__':
    face_app()
