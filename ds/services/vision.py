import cv2

WEARING_MASK = 'wearing mask'
NO_WEARING_MASK = 'not wearing mask'


def display_with(frame, face_locations, face_names):
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)


def display_mask_with_and_has_mask(frame, locs, preds):
    has_mask = True
    for (box, pred) in zip(locs, preds):
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred

        label = WEARING_MASK if mask > withoutMask else NO_WEARING_MASK
        color = (0, 255, 0) if label == WEARING_MASK else (0, 0, 255)
        has_mask = True if label == WEARING_MASK else False
        label = f'Person is {label}: {max(mask, withoutMask) * 100}'

        cv2.putText(
            frame,
            label,
            (startX, startY - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            color,
            2,
        )
        cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

    cv2.imshow('Video', frame)
    return has_mask
