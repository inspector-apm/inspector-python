from ..inspector import Configuration, Inspector
import time


class Test:

    def test_error(self, value_str):
        value = 'test'
        raise ValueError('errore di test')


def test_configuration_construction():
    config = Configuration('10ae3b6fdf91396a6a81be019c743dc8c0f4098d')
    config.set_transport('async')

    inspector = Inspector(config)

    inspector.start_transaction('python/test/async2')
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
    inspector.segment().add_context('test_segment', obj_test2)
    time.sleep(3)
    inspector.segment().end()

    """
    try:
        obj_test = Test()
        obj_test.test_error('test')
    except Exception as e:
        inspector.report_exception(e)
    """
    assert True
