from rest_framework.throttling import UserRateThrottle

class VipulRateThrottle(UserRateThrottle):
    scope = 'vipul'
