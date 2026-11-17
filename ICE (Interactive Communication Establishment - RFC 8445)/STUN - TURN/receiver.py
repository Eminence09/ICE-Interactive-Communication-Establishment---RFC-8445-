import asyncio
import json
import logging
from aiortc import RTCPeerConnection, RTCConfiguration, RTCIceServer, RTCSessionDescription

# Enable logging to see the network process
logging.basicConfig(level=logging.INFO)

TURN_CONFIG = RTCConfiguration(
    iceServers=[
        RTCIceServer(
            urls="turn:10.30.148.137:3478?transport=udp",
            username="myuser",
            credential="mypassword123"
        )
    ]
)

async def run_receiver():
    pc = RTCPeerConnection(configuration=TURN_CONFIG)

    @pc.on("datachannel")
    def on_datachannel(channel):
        print("\n🎉 CONNECTED TO SENDER! Type your message below and hit Enter.")
        asyncio.ensure_future(send_messages(channel))

        @channel.on("message")
        def on_message(message):
            print(f"\n[Sender]: {message}")

    # Read the offer token from the sender
    offer_input = input("STEP 2: Paste the OFFER token from the Sender here: \n").strip()
    offer_data = json.loads(offer_input)
    
    await pc.setRemoteDescription(RTCSessionDescription(sdp=offer_data["sdp"], type=offer_data["type"]))

    # Generate the response token
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)
    
    # Give the TURN server 2 seconds to gather relay routes
    await asyncio.sleep(2)

    print("\n========= STEP 3: COPY THIS ANSWER TOKEN =========")
    print(json.dumps({"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}))
    print("====================================================\n")

    # Keep script running to maintain the connection
    while True:
        await asyncio.sleep(1)

async def send_messages(channel):
    loop = asyncio.get_event_loop()
    while True:
        message = await loop.run_in_executor(None, input, "You: ")
        if message:
            channel.send(message)

if __name__ == "__main__":
    asyncio.run(run_receiver())
