import asyncio
from aiortc import RTCPeerConnection, RTCConfiguration, RTCIceServer

async def run():
    # Configure connection to your Kali Linux TURN server
    config = RTCConfiguration(
        iceServers=[
            RTCIceServer(
                urls="turn:10.158.86.162:3478?transport=udp",
                username="yash",
                credential="123"
            )
        ]
    )
    
    # Initialize the peer connection
    pc = RTCPeerConnection(configuration=config)
    print("Initializing WebRTC connection to TURN server...")

    # Optional: Create a data channel to send text/binary data
    channel = pc.createDataChannel("chat")
    
    @channel.on("open")
    def on_open():
        print("Data channel is open! Streaming data through TURN server...")
        channel.send("Hello from Python through the TURN server!")

    # Generate the local connection offer (triggers ICE gathering)
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)
    
    print("Gathering ICE candidates... look at your Kali terminal for logs!")
    # Keep the script running to maintain the connection state
    await asyncio.sleep(5)
    
    # Clean up connection
    await pc.close()

# Run the asynchronous loop
if __name__ == "__main__":
    asyncio.run(run())
