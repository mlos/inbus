from publisher import Publisher


p = Publisher(("127.0.0.1", 7222), "my-key")

p.publish("Hallo")

