from subscriber import Subscriber


s = Subscriber(("127.0.0.1", 7222), "my-key")

s.wait_for_published_message()
