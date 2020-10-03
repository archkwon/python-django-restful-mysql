from pyfcm import FCMNotification
from tacar_api.settings import base


class FcmTacar:

    def __init__(self):
        self.FCM_KEY = base.FCM_KEY
        self.push_service = FCMNotification(api_key=self.FCM_KEY)

    def singleFCMPush(self, title, body, tokenId):
        result = self.push_service.notify_single_device(registration_id=tokenId, message_title=title, message_body=body)
        print(result)

    def multiFCMPush(self, title, body, tokenIds):
        result = self.push_service.notify_multiple_devices(registration_ids=tokenIds, message_title=title,
                                                           message_body=body)
        print(result)
