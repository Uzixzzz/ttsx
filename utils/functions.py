import random

def get_session():
    session = ''
    s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    for i in range(100):
        session += random.choice(s)
    return session


def get_order_num():
    num = ''
    s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    for i in range(10):
        num += random.choice(s)
        order_time = datetime.now().strftime('%Y%m%d%H%R%S')
    return order_time