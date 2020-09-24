class PycustException(Exception):
    """Generic exception
    """

    def __init__(self, message, *args, **kwargs):
        """
        """

        self.message = "".join(
            (f"PyCUST error: {message}\n")
        super().__init__(self.message)