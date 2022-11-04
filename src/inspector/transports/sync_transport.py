from src.inspector.transports import Transport
from src.inspector import Configuration
import http.client
import ssl


class SyncTransport(Transport):
    PORT = 443
    TIMEOUT = 10

    def __init__(self, configuration: Configuration):
        Transport.__init__(self, configuration)

    def _send_chunk(self, message_bytes):
        headers = self._get_api_headers()
        try:
            print('\n\nmessage_bytes: ', message_bytes)
            connection = http.client.HTTPSConnection(self._config.get_url(), self.PORT, timeout=self.TIMEOUT,
                                                     context=ssl._create_unverified_context())
            connection.request("POST", "/", message_bytes, headers)
            response = connection.getresponse()
            print(response.status, response.reason)
            print(response.read().decode())
            connection.close()
        except Exception as e:
            print('ERROR: ', str(e))
