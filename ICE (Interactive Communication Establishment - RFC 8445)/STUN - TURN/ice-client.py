import asyncio
from aiortc import RTCPeerConnection, RTCIceServer, RTCConfiguration
async def test_ice():
    # 1. Map to the coturn server running locally in WSL
    config = RTCConfiguration(
        iceServers=[
            RTCIceServer(urls="stun:127.0.0.1:3478"),
            RTCIceServer(urls="turn:127.0.0.1:3478", username="yash", credential="123")
        ]
    )
    
    pc = RTCPeerConnection(configuration=config)
    
    # 2. Monitor candidate gathering states via event handlers
    @pc.on("icegatheringstatechange")
    def on_gathering_change():
        print(f"Gathering State Changed: {pc.iceGatheringState}")
    # Create a local data channel to force ICE candidate gathering
    pc.createDataChannel("chat")
    
    print("Starting local offer generation to trigger ICE...")
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)
    
    # Give the async loop a moment to talk to the local coturn server
    await asyncio.sleep(5)
    
        # 3. Inspect the discovered candidates
    print("\n--- Gathered Local Candidates ---")
    if pc.sctp and pc.sctp.transport:
        ice_transport = pc.sctp.transport.transport
        # Access the underlying iceGatherer to fetch local candidates
        if hasattr(ice_transport, "_iceGatherer"):
            candidates = ice_transport._iceGatherer.getLocalCandidates()
            for candidate in candidates:
                print(f"Type: {candidate.type} | Addr: {candidate.ip}:{candidate.port} | Proto: {candidate.protocol}")
        else:
            print("IceGatherer not found on transport.")
    else:
        print("No ICE candidates gathered or transport not initialized.")

if __name__ == "__main__":
    asyncio.run(test_ice())