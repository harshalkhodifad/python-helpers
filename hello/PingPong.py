class PingPong(object):
    def __init__(self, *args, **kwargs):
        print("Ping Pong")
        self.name = input("Enter Your Name: ")

    def say_hi(self):
        print("Hi {}".format(self.name))
