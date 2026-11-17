import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription

async def run():
    # 1. Initialize the peer connection
    pc = RTCPeerConnection()
    
    # 2. Open a Data Channel for arbitrary text/binary data
    channel = pc.createDataChannel("chat")
    
    @channel.on("open")
    def on_open():
        print("Data channel is open!")
        channel.send("Hello from Python side!")

    @channel.on("message")
    def on_message(message):
        print(f"Received message: {message}")

    # 3. Create an SDP Offer to initiate the handshake
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)
    
    # The 'offer' SDP string must now be sent to the remote peer 
    # via a signaling channel (like WebSockets or an HTTP API)
    print("Local SDP Offer generated. Ready for signaling.")
    
    # Keep the connection alive for demonstration
    await asyncio.sleep(60)
    await pc.close()

if __name__ == "__main__":
    asyncio.run(run())
