import ds


def app():
    known_face_names, known_face_encodings = ds.services.face_encoder.generate_image_encodings('faces')

    print(f'Known face names is {known_face_names}')

    with ds.services.camera.Camera() as camera:
        for frame in camera.read_frames(no_limit=True):
            print(f'Frame is {frame}')
            print(f'{known_face_encodings}')
            print(f'{known_face_names}')
            face_locations, face_names = ds.services.detector.face_detect(
                frame,
                known_face_encodings,
                known_face_names,
            )
            ds.services.vision.display_with(frame, face_locations, face_names)


if __name__ == '__main__':
    app()
