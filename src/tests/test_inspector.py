from src.inspector import Configuration, Inspector
from src.inspector.transports import CurlTransport
from src.inspector.models import Transaction
from src.inspector.models import HasContext
import resource
import time



def test_configuration_construction():

    #context_obj = HasContext()
    # print("MICROTIME: ", context_obj.get_microtime())

    """
    trans_obj = Transaction('nome')
    trans_obj = trans_obj.start()
    trans_obj = trans_obj.end()
    print('\n\n\nPEAK: ', trans_obj.get_memory_peak())
    print('\n\n\nstart: ', trans_obj.get_timestamp())
    print('\n\n\nduration: ', trans_obj.get_duration())
    """

    config = Configuration('fc2d6a4e0bea2467ea9f32c57d5880cf06a7a24d')
    config.set_transport('sync')

    inspector = Inspector(config)

    inspector.start_transaction('path/di/invio/test')
    inspector.current_transaction().set_result('success')
    obj_test = {
        'foo': 'bar'
    }
    # inspector.current_transaction().add_context('test', obj_test)
    # inspector.current_transaction().add_context('test2', obj_test)
    inspector.current_transaction().end()


    print('DEBUG: ', inspector.current_transaction().__dict__)

    # segment = inspector.start_segment('process', 'test segment')
    # segment.end()

    # inspector.start_transaction('path/di/test2')
    # inspector.current_transaction().set_result('success')
    # obj_test = {
    #     'foo2': 'bar2'
    # }
    # inspector.current_transaction().add_context('test2', obj_test)



    """
    config = Configuration('0d06b54a3de0bbf94686227e613a5f0f032f3e2f')
    config.set_transport('sync')

    test = CurlTransport(config)
    """

    assert True

