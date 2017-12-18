import task2

def test_1():
    assert task2.user_vk(1).get('response[0]') == 'Павел'