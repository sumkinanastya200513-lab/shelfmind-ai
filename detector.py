def detect_price_tags(frame):

    height, width = frame.shape[:2]

    return [
        (
            width // 4,
            height // 4,
            width // 2,
            height // 2
        )
    ]