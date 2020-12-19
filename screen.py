from screeninfo import get_monitors


class Screen:

    @staticmethod
    def get_size():
        m = get_monitors()
        return m[0].width-150, m[0].height-150
