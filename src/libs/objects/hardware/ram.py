import libs.objects.hardware


class RAM(libs.objects.hardware):
    available_space = 0

    def __init__(self, aailable_space, used_space = 0):
        self.available_space = available_space
        self.used_space = used_space

    def lock(self, space):
        '''
        Lock space in RAM so that it is not free for other programs.
        '''
        pass




# Errors
class RAMError(libs.objects.hardware.HardwareError):
    pass

class RAMSpaceError(RAMError):
    '''
    There is not enough space available in RAM to do that.
    '''
    pass
    
