import asyncio
import json
import logging
from aiortc import RTCPeerConnection, RTCConfiguration, RTCIceServer

# Enable logging to see the network process
logging.basicConfig(level=logging.INFO)

TURN_CONFIG = RTCConfiguration(
    iceServers=[
        RTCIceServer(
            urls="turn:10.30.148.137:3478?transport=udp",
            username="yash",
            credential="123"
        )
    ]
)

async def run_sender():
    pc = RTCPeerConnection(configuration=TURN_CONFIG)
    
    # Create the data channel for communication
    channel = pc.createDataChannel("turn-chat-room")
    print("\n[System] Chat channel created.")

    @channel.on("open")
    def on_open():
        print("\n🎉 CONNECTED TO RECEIVER! Type your message below and hit Enter.")
        asyncio.ensure_future(send_messages(channel))

    @channel.on("message")
    def on_message(message):
        print(f"\n[Receiver]: {message}")

    # Create the network offer
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)
    
    # Give the TURN server 2 seconds to gather all relay routes
    await asyncio.sleep(2) 
    
    print("\n========= STEP 1: COPY THIS OFFER TOKEN =========")
    print(json.dumps({"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}))
    print("==================================================\n")

    # Wait for the user to input the response token from the receiver
    answer_input = input("STEP 4: Paste the ANSWER token from the Receiver here: \n").strip()
    answer_data = json.loads(answer_input)
    
    await pc.setRemoteDescription(
        from_json(answer_data) if hasattr(pc, 'from_json') else 
        from_dict(answer_data) if 'from_dict' in dir() else 
        RTCSessionDescription(sdp=answer_data["sdp"], type=answer_data["type"])
    )

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
    from aiortc import RTCSessionDescription
    asyncio.run(run_sender())
