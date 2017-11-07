
from inbus.client.subscriber import Subscriber


subscriber must use the with paradigm!

sub = Subscriber("super-app")

while True:
    
    print sub.wait_for_published_message()

