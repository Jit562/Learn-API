from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class jackthrottling(AnonRateThrottle):

    scope = 'jack'


class sackthrottling(UserRateThrottle):

    scope = 'sack'    
