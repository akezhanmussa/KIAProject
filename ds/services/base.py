class Service:

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


global_x = 1000
