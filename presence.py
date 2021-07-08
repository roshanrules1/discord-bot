import pypresence
import time

client_id = os.getenv("CLIENT_ID")
Client = pypresence.Client(client_id, pipe=0)
Client.start()

print(
    Client.set_activity(
        state="kinda working",
        details="just gotta figure this cloud part",
        large_image="gojo",
        small_image="NAME OF SMALL IMAGE HERE",
        large_text="fox-y",
        start=time.time(),
    )
)
