class MovieAlreadyAvailableError(Exception):
    def __init__(self,message):
        self.message=message

class MovieNotAvailableError(Exception):
    def __init__(self,message):
        self.message=message

class TicketsNotAvailableError(Exception):
    def __init__(self,message):
        self.message=message



# run this program  cd bookmovietickets template 