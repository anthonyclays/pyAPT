from controller import Controller


class TDC001(Controller):

    """
    A controller for a TDC001 Servo controller
    """

    def __init__(self, *args, **kwargs):
        super(TDC001, self).__init__(*args, **kwargs)

        # These values do not appear to modify the maximum velocity or
        # acceleration at all.
        self.max_velocity = 2.0
        self.max_acceleration = 2.0

        # Encoder count: precisely 1920 steps to move 1 degree
        enccnt = 1920
        # Untouched.
        T = 2048 / 6e6

        # these equations are taken from the APT protocol manual
        self.position_scale = enccnt
        self.velocity_scale = enccnt * T * 65536
        self.acceleration_scale = enccnt * T * T * 65536

        # One full rotation
        self.linear_range = (0, 360)
