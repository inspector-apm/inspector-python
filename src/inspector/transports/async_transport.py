from src.inspector.transports import Transport
from src.inspector import Configuration
import http.client
from multiprocessing import Process, Value, Array
import ssl


class AsyncTransport(Transport):
    PORT = 443
    TIMEOUT = 10

    def __init__(self, configuration: Configuration):
        Transport.__init__(self, configuration)

    def _send_chunk(self, message_bytes):

        try:
            p = Process(target=AsyncTransport.send_data, args=(message_bytes))
            p.start()

        except Exception as e:
            print('ERROR: ', str(e))

    @staticmethod
    def send_data(self, message_bytes):
        try:
            headers = self._get_api_headers()

            print("ASYNC MESSAGE: ", message_bytes, flush=True)
            # http.client.HTTPSConnection.debuglevel = 1
            connection = http.client.HTTPSConnection(self._config.get_url(), self.PORT, timeout=self.TIMEOUT,
                                                     context=ssl._create_unverified_context())
            connection.request("POST", "", message_bytes, headers)
            response = connection.getresponse()
            print(response.status, response.reason, flush=True)
            print(response.read().decode(), flush=True)
            connection.close()
        except Exception as e:
            print('ERROR: ', str(e))
