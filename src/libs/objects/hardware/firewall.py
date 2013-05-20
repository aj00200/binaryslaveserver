import libs.objects

class BaseFirewall(libs.object.Object):
    '''
    Base firewall class.
    '''
    def __init__(self, rules={}):
        self.rules = rules


class PortFilter(BaseFilter):
    '''
    Simple port filter, dropping packets based on port number.
    '''
    pass


class StateFilter(BaseFilter):
    '''
    Filter out packets not associated with an established connection.
    '''
    pass


class DPIFilter(BaseFirewall):
    '''
    Do protocol detection and filtering on all ports.
    '''
    pass


class StateDPIFilter(StateFilter, DPIFilter):
    '''
    Combine the state filter with the DPI filter.
    ''''
    pass
