from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.account_sid = "AC75fc0d5b46bb4bb8617edd30c3fa13a3"
        self.auth_token = "739c97ac35be7794cb4a9294c0db6c14"


    def send_notification(self,deals:str):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
                    .create(
                            body= deals,
                            from_='+16123143096',
                            to='+13605107170'
                        )

        print(message.status)
