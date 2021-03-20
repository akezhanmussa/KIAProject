import face_recognition
import pathlib


def _take_image_name(image_path):
    return pathlib.Path(image_path).name.split('.')[0]


def _image_to_encoding(image_path):
    if not pathlib.Path(image_path).exists():
        raise FileNotFoundError(f'{image_path} does not exist')

    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    image_name = _take_image_name(image_path)
    return image_name, face_encoding


def generate_image_encodings(directory):
    if not pathlib.Path(directory).is_dir():
        raise IsADirectoryError(f'{directory} is not directory')

    face_encodings = []
    face_names = []

    for image_path in pathlib.Path(directory).iterdir():
        image_name, face_encoding = _image_to_encoding(image_path)
        face_names.append(image_name)
        face_encodings.append(face_encoding)

    return face_names, face_encodings
