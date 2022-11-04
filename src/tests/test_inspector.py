from src.inspector import Configuration, Inspector
import time

def test_configuration_construction():
    config = Configuration('10ae3b6fdf91396a6a81be019c743dc8c0f4098d')
    config.set_transport('sync')

    inspector = Inspector(config)

    inspector.start_transaction('python/test/transaction4/sleep')
    inspector.transaction().set_result('success')
    obj_test = {
        'foo': 'bar'
    }
    inspector.transaction().add_context('test', obj_test)
    inspector.transaction().add_context('test2', obj_test)
    # inspector.current_transaction().end()

    # print('\nDEBUG: ', inspector.current_transaction().__dict__)

    segment = inspector.start_segment('process', 'test segment')
    obj_test2 = {
        'foo_segment': 'bar'
    }
    inspector.current_segment().add_context('test_segment', obj_test2)
    time.sleep(3)
    inspector.current_segment().end()

    # segment.add_context('test_segment', obj_test2)

    # inspector.start_transaction('python/new/test11')
    # inspector.current_transaction().set_result('success')
    # obj_test = {
    #     'foo2': 'bar2'
    # }
    # inspector.current_transaction().add_context('test2', obj_test)

    assert True
