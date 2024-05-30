
### OSI Model (Open System Interconnect)


  
- Application Layer
  - Browsing, Emails, File Transfer, etc..
  - Protocols : HTTP, SMTP, FTP
- Presentation Layer
  - Translation (to Binary), Compression, Encryption and Decryption
  - Protocols : SSL (for Encrypt/Decrypt)
- Session Layer
   - Session Management, Authentication / Authorization
   - Data is Stored in Terms of <b> Packets </b>

```
Application , Presentation and Session Layer are Handled by our Broswer.
```
- Transport Layer
    - <b> Segmentation </b> (DataPackets are Split to Small Units) , Flow Control, Error Control (Checksum && Automatic request for getting data)
    - Protocols : TCP (Trasnmission Control Protocol), UDP (User Datagram Protocol)
- Network Layer
  - Logical Addressing (IP) , Path Determination (OSPF, BGP)
  - Here <b> Data Packets </b> ( Segements + IP ) are Transferred to Data Link Layer
 
- Data Link Layer
  - Framing (Allows Upper Layers to Access Media)  , Media Access Control (Controls how data is placed and received on Media ( i.e Physical Layer - Fiber, LAN Canle, Air)
    - <b> Frames </b> (Data Packets + MAC Addresses)
    
```
Data Link Layer is Embedded in NIC of a Computer.
```

- Physical Layer
  - Final Transfer Happens via signals (Optical Fiber : Light, Copper Wires - Electric, Wireless - Air)
