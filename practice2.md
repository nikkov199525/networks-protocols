# Практическая работа № 2

Ковалев Никита  
Группа: p4150  
Дата выполнения задания: 12.05.2025  
Именование дисциплины: "Сети и протоколы"  

## Задание
1. Провести анализ пакетов в целом, какие есть в Вашей сетке и вывести статистику. 
2. Выбрать один протокол, собрать о нем данные, вывести его «внутренности» и разобрать с точки зрения содержимого пакета (что там есть, что за данные пакет хранит и передает). 
3. Написать отчет о проделанной работе. 
## Ход работы
Для общего анализа трафика в сети можно использовать команду
                                                                                                                 
"C:\Program Files\Wireshark\tshark.exe" -i 5 -a duration:30 -q -z io,phs                                  
Это означает, что захватываться пакеты будут 30 секунд, в моем случае на интерфейсе 5 и собирать я буду статистику по протоколам, при этом весь вывод отобразится только после того, как команда отработает.
Результат выполнения команды:
Capturing on 'Беспроводная сеть'                                                                                        
222 packets captured                                                                                                    
                                                                                                                        
===================================================================                                                     
Protocol Hierarchy Statistics                                                                                           
Filter:                                                                                                                 
                                                                                                                        
eth                                      frames:222 bytes:51543                                                         
  ip                                     frames:212 bytes:51123                                                         
    tcp                                  frames:208 bytes:50451                                                         
      tls                                frames:72 bytes:36429                                                          
        tcp.segments                     frames:3 bytes:3086                                                            
          tls                            frames:2 bytes:1944                                                            
      msdo                               frames:1 bytes:129                                                             
    udp                                  frames:4 bytes:672                                                             
      data                               frames:2 bytes:452                                                             
      dns                                frames:2 bytes:220                                                             
  arp                                    frames:10 bytes:420                                                            
===================================================================                                                     
                                                                                                                        

"C:\Program Files\Wireshark\tshark.exe" -i 5 -f "tcp" -a duration:1 -V                                    
Capturing on 'Беспроводная сеть'                                                                                        
Frame 1: 446 bytes on wire (3568 bits), 446 bytes captured (3568 bits) on interface \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}, id 0                                                                                                    
    Section number: 1                                                                                                   
    Interface id: 0 (\Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA})                                                
        Interface name: \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}                                              
        Interface description: Беспроводная сеть                                                                        
    Encapsulation type: Ethernet (1)                                                                                    
    Arrival Time: May 13, 2025 00:23:10.675907000 RTZ 2 (зима)                                                          
    UTC Arrival Time: May 12, 2025 21:23:10.675907000 UTC                                                               
    Epoch Arrival Time: 1747084990.675907000                                                                            
    [Time shift for this packet: 0.000000000 seconds]                                                                   
    [Time delta from previous captured frame: 0.000000000 seconds]                                                      
    [Time delta from previous displayed frame: 0.000000000 seconds]                                                     
    [Time since reference or first frame: 0.000000000 seconds]                                                          
    Frame Number: 1                                                                                                     
    Frame Length: 446 bytes (3568 bits)                                                                                 
    Capture Length: 446 bytes (3568 bits)                                                                               
    [Frame is marked: False]                                                                                            
    [Frame is ignored: False]                                                                                           
    [Protocols in frame: eth:ethertype:ip:tcp:tls]                                                                      
Ethernet II, Src: Intel_d1:26:fd (78:2b:46:d1:26:fd), Dst: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                          
    Destination: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                                                                    
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Source: Intel_d1:26:fd (78:2b:46:d1:26:fd)                                                                          
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Type: IPv4 (0x0800)                                                                                                 
    [Stream index: 0]                                                                                                   
Internet Protocol Version 4, Src: 192.168.0.111, Dst: 176.112.173.62                                                    
    0100 .... = Version: 4                                                                                              
    .... 0101 = Header Length: 20 bytes (5)                                                                             
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)                                                       
        0000 00.. = Differentiated Services Codepoint: Default (0)                                                      
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)                                     
    Total Length: 432                                                                                                   
    Identification: 0xff38 (65336)                                                                                      
    010. .... = Flags: 0x2, Don't fragment                                                                              
        0... .... = Reserved bit: Not set                                                                               
        .1.. .... = Don't fragment: Set                                                                                 
        ..0. .... = More fragments: Not set                                                                             
    ...0 0000 0000 0000 = Fragment Offset: 0                                                                            
    Time to Live: 128                                                                                                   
    Protocol: TCP (6)                                                                                                   
    Header Checksum: 0x0000 [validation disabled]                                                                       
    [Header checksum status: Unverified]                                                                                
    Source Address: 192.168.0.111                                                                                       
    Destination Address: 176.112.173.62                                                                                 
    [Stream index: 0]                                                                                                   
Transmission Control Protocol, Src Port: 2775, Dst Port: 443, Seq: 1, Ack: 1, Len: 392                                  
    Source Port: 2775                                                                                                   
    Destination Port: 443                                                                                               
    [Stream index: 0]                                                                                                   
    [Stream Packet Number: 1]                                                                                           
    [Conversation completeness: Incomplete (0)]                                                                         
        ..0. .... = RST: Absent                                                                                         
        ...0 .... = FIN: Absent                                                                                         
        .... 0... = Data: Absent                                                                                        
        .... .0.. = ACK: Absent                                                                                         
        .... ..0. = SYN-ACK: Absent                                                                                     
        .... ...0 = SYN: Absent                                                                                         
        [Completeness Flags: [ Null ]]                                                                                  
    [TCP Segment Len: 392]                                                                                              
    Sequence Number: 1    (relative sequence number)                                                                    
    Sequence Number (raw): 4288999899                                                                                   
    [Next Sequence Number: 393    (relative sequence number)]                                                           
    Acknowledgment Number: 1    (relative ack number)                                                                   
    Acknowledgment number (raw): 3093018745                                                                             
    0101 .... = Header Length: 20 bytes (5)                                                                             
    Flags: 0x018 (PSH, ACK)                                                                                             
        000. .... .... = Reserved: Not set                                                                              
        ...0 .... .... = Accurate ECN: Not set                                                                          
        .... 0... .... = Congestion Window Reduced: Not set                                                             
        .... .0.. .... = ECN-Echo: Not set                                                                              
        .... ..0. .... = Urgent: Not set                                                                                
        .... ...1 .... = Acknowledgment: Set                                                                            
        .... .... 1... = Push: Set                                                                                      
        .... .... .0.. = Reset: Not set                                                                                 
        .... .... ..0. = Syn: Not set                                                                                   
        .... .... ...0 = Fin: Not set                                                                                   
        [TCP Flags: ·······AP···]                                                                                       
    Window: 511                                                                                                         
    [Calculated window size: 511]                                                                                       
    [Window size scaling factor: -1 (unknown)]                                                                          
    Checksum: 0x2069 [unverified]                                                                                       
    [Checksum Status: Unverified]                                                                                       
    Urgent Pointer: 0                                                                                                   
    [Timestamps]                                                                                                        
        [Time since first frame in this TCP stream: 0.000000000 seconds]                                                
        [Time since previous frame in this TCP stream: 0.000000000 seconds]                                             
    [SEQ/ACK analysis]                                                                                                  
        [Bytes in flight: 392]                                                                                          
        [Bytes sent since last PSH flag: 392]                                                                           
    TCP payload (392 bytes)                                                                                             
Transport Layer Security                                                                                                
    TLSv1.2 Record Layer: Application Data Protocol: Hypertext Transfer Protocol                                        
        Content Type: Application Data (23)                                                                             
        Version: TLS 1.2 (0x0303)                                                                                       
        Length: 387                                                                                                     
        Encrypted Application Data […]: 06da1c396aa2b1386d1d663729d2d09af528daa3b206e338e9083b21357de3780db92cb58c981aa8917c910c29b2c4cf4239dd788a72593f7e28d95ae8aac4d5e11bb5fd3e5f773ef2a25079b0578d214600de2ebca43b7c00990e47272685533ee0119e50245                                                                                                                   
        [Application Data Protocol: Hypertext Transfer Protocol]                                                        
                                                                                                                        
Frame 2: 274 bytes on wire (2192 bits), 274 bytes captured (2192 bits) on interface \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}, id 0                                                                                                    
    Section number: 1                                                                                                   
    Interface id: 0 (\Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA})                                                
        Interface name: \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}                                              
        Interface description: Беспроводная сеть                                                                        
    Encapsulation type: Ethernet (1)                                                                                    
    Arrival Time: May 13, 2025 00:23:10.697609000 RTZ 2 (зима)                                                          
    UTC Arrival Time: May 12, 2025 21:23:10.697609000 UTC                                                               
    Epoch Arrival Time: 1747084990.697609000                                                                            
    [Time shift for this packet: 0.000000000 seconds]                                                                   
    [Time delta from previous captured frame: 0.021702000 seconds]                                                      
    [Time delta from previous displayed frame: 0.021702000 seconds]                                                     
    [Time since reference or first frame: 0.021702000 seconds]                                                          
    Frame Number: 2                                                                                                     
    Frame Length: 274 bytes (2192 bits)                                                                                 
    Capture Length: 274 bytes (2192 bits)                                                                               
    [Frame is marked: False]                                                                                            
    [Frame is ignored: False]                                                                                           
    [Protocols in frame: eth:ethertype:ip:tcp:tls]                                                                      
Ethernet II, Src: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3), Dst: Intel_d1:26:fd (78:2b:46:d1:26:fd)                          
    Destination: Intel_d1:26:fd (78:2b:46:d1:26:fd)                                                                     
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Source: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                                                                         
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Type: IPv4 (0x0800)                                                                                                 
    [Stream index: 0]                                                                                                   
Internet Protocol Version 4, Src: 176.112.173.62, Dst: 192.168.0.111                                                    
    0100 .... = Version: 4                                                                                              
    .... 0101 = Header Length: 20 bytes (5)                                                                             
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)                                                       
        0000 00.. = Differentiated Services Codepoint: Default (0)                                                      
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)                                     
    Total Length: 260                                                                                                   
    Identification: 0xc3b0 (50096)                                                                                      
    010. .... = Flags: 0x2, Don't fragment                                                                              
        0... .... = Reserved bit: Not set                                                                               
        .1.. .... = Don't fragment: Set                                                                                 
        ..0. .... = More fragments: Not set                                                                             
    ...0 0000 0000 0000 = Fragment Offset: 0                                                                            
    Time to Live: 54                                                                                                    
    Protocol: TCP (6)                                                                                                   
    Header Checksum: 0x617d [validation disabled]                                                                       
    [Header checksum status: Unverified]                                                                                
    Source Address: 176.112.173.62                                                                                      
    Destination Address: 192.168.0.111                                                                                  
    [Stream index: 0]                                                                                                   
Transmission Control Protocol, Src Port: 443, Dst Port: 2775, Seq: 1, Ack: 393, Len: 220                                
    Source Port: 443                                                                                                    
    Destination Port: 2775                                                                                              
    [Stream index: 0]                                                                                                   
    [Stream Packet Number: 2]                                                                                           
    [Conversation completeness: Incomplete (8)]                                                                         
        ..0. .... = RST: Absent                                                                                         
        ...0 .... = FIN: Absent                                                                                         
        .... 1... = Data: Present                                                                                       
        .... .0.. = ACK: Absent                                                                                         
        .... ..0. = SYN-ACK: Absent                                                                                     
        .... ...0 = SYN: Absent                                                                                         
        [Completeness Flags: ··D···]                                                                                    
    [TCP Segment Len: 220]                                                                                              
    Sequence Number: 1    (relative sequence number)                                                                    
    Sequence Number (raw): 3093018745                                                                                   
    [Next Sequence Number: 221    (relative sequence number)]                                                           
    Acknowledgment Number: 393    (relative ack number)                                                                 
    Acknowledgment number (raw): 4289000291                                                                             
    0101 .... = Header Length: 20 bytes (5)                                                                             
    Flags: 0x018 (PSH, ACK)                                                                                             
        000. .... .... = Reserved: Not set                                                                              
        ...0 .... .... = Accurate ECN: Not set                                                                          
        .... 0... .... = Congestion Window Reduced: Not set                                                             
        .... .0.. .... = ECN-Echo: Not set                                                                              
        .... ..0. .... = Urgent: Not set                                                                                
        .... ...1 .... = Acknowledgment: Set                                                                            
        .... .... 1... = Push: Set                                                                                      
        .... .... .0.. = Reset: Not set                                                                                 
        .... .... ..0. = Syn: Not set                                                                                   
        .... .... ...0 = Fin: Not set                                                                                   
        [TCP Flags: ·······AP···]                                                                                       
    Window: 716                                                                                                         
    [Calculated window size: 716]                                                                                       
    [Window size scaling factor: -1 (unknown)]                                                                          
    Checksum: 0xf4c5 [unverified]                                                                                       
    [Checksum Status: Unverified]                                                                                       
    Urgent Pointer: 0                                                                                                   
    [Timestamps]                                                                                                        
        [Time since first frame in this TCP stream: 0.021702000 seconds]                                                
        [Time since previous frame in this TCP stream: 0.021702000 seconds]                                             
    [SEQ/ACK analysis]                                                                                                  
        [This is an ACK to the segment in frame: 1]                                                                     
        [The RTT to ACK the segment was: 0.021702000 seconds]                                                           
        [Bytes in flight: 220]                                                                                          
        [Bytes sent since last PSH flag: 220]                                                                           
    TCP payload (220 bytes)                                                                                             
Transport Layer Security                                                                                                
    TLSv1.2 Record Layer: Application Data Protocol: Hypertext Transfer Protocol                                        
        Content Type: Application Data (23)                                                                             
        Version: TLS 1.2 (0x0303)                                                                                       
        Length: 215                                                                                                     
        Encrypted Application Data […]: f1ffaf534bd1655e8e1e3e00ec57f3ec420f65b107ee751ff3aa78af92312909d5bc600d84a0471b01743965b7915f3b3d6a9a65b63a66581c15e28a647e926353ad726f89c467f42abfbf2dea859fd489dc4f10769c57a921f8abe066caf5a10fc9c407e6213                                                                                                                   
        [Application Data Protocol: Hypertext Transfer Protocol]                                                        
                                                                                                                        
Frame 3: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}, id 0                                                                                                        
    Section number: 1                                                                                                   
    Interface id: 0 (\Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA})                                                
        Interface name: \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}                                              
        Interface description: Беспроводная сеть                                                                        
    Encapsulation type: Ethernet (1)                                                                                    
    Arrival Time: May 13, 2025 00:23:10.723158000 RTZ 2 (зима)                                                          
    UTC Arrival Time: May 12, 2025 21:23:10.723158000 UTC                                                               
    Epoch Arrival Time: 1747084990.723158000                                                                            
    [Time shift for this packet: 0.000000000 seconds]                                                                   
    [Time delta from previous captured frame: 0.025549000 seconds]                                                      
    [Time delta from previous displayed frame: 0.025549000 seconds]                                                     
    [Time since reference or first frame: 0.047251000 seconds]                                                          
    Frame Number: 3                                                                                                     
    Frame Length: 66 bytes (528 bits)                                                                                   
    Capture Length: 66 bytes (528 bits)                                                                                 
    [Frame is marked: False]                                                                                            
    [Frame is ignored: False]                                                                                           
    [Protocols in frame: eth:ethertype:ip:tcp]                                                                          
Ethernet II, Src: Intel_d1:26:fd (78:2b:46:d1:26:fd), Dst: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                          
    Destination: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                                                                    
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Source: Intel_d1:26:fd (78:2b:46:d1:26:fd)                                                                          
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Type: IPv4 (0x0800)                                                                                                 
    [Stream index: 0]                                                                                                   
Internet Protocol Version 4, Src: 192.168.0.111, Dst: 212.192.20.195                                                    
    0100 .... = Version: 4                                                                                              
    .... 0101 = Header Length: 20 bytes (5)                                                                             
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)                                                       
        0000 00.. = Differentiated Services Codepoint: Default (0)                                                      
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)                                     
    Total Length: 52                                                                                                    
    Identification: 0xfee0 (65248)                                                                                      
    010. .... = Flags: 0x2, Don't fragment                                                                              
        0... .... = Reserved bit: Not set                                                                               
        .1.. .... = Don't fragment: Set                                                                                 
        ..0. .... = More fragments: Not set                                                                             
    ...0 0000 0000 0000 = Fragment Offset: 0                                                                            
    Time to Live: 128                                                                                                   
    Protocol: TCP (6)                                                                                                   
    Header Checksum: 0x0000 [validation disabled]                                                                       
    [Header checksum status: Unverified]                                                                                
    Source Address: 192.168.0.111                                                                                       
    Destination Address: 212.192.20.195                                                                                 
    [Stream index: 1]                                                                                                   
Transmission Control Protocol, Src Port: 3422, Dst Port: 48933, Seq: 0, Len: 0                                          
    Source Port: 3422                                                                                                   
    Destination Port: 48933                                                                                             
    [Stream index: 1]                                                                                                   
    [Stream Packet Number: 1]                                                                                           
    [Conversation completeness: Incomplete (0)]                                                                         
        ..0. .... = RST: Absent                                                                                         
        ...0 .... = FIN: Absent                                                                                         
        .... 0... = Data: Absent                                                                                        
        .... .0.. = ACK: Absent                                                                                         
        .... ..0. = SYN-ACK: Absent                                                                                     
        .... ...0 = SYN: Absent                                                                                         
        [Completeness Flags: [ Null ]]                                                                                  
    [TCP Segment Len: 0]                                                                                                
    Sequence Number: 0    (relative sequence number)                                                                    
    Sequence Number (raw): 1402797154                                                                                   
    [Next Sequence Number: 1    (relative sequence number)]                                                             
    Acknowledgment Number: 0                                                                                            
    Acknowledgment number (raw): 0                                                                                      
    1000 .... = Header Length: 32 bytes (8)                                                                             
    Flags: 0x002 (SYN)                                                                                                  
        000. .... .... = Reserved: Not set                                                                              
        ...0 .... .... = Accurate ECN: Not set                                                                          
        .... 0... .... = Congestion Window Reduced: Not set                                                             
        .... .0.. .... = ECN-Echo: Not set                                                                              
        .... ..0. .... = Urgent: Not set                                                                                
        .... ...0 .... = Acknowledgment: Not set                                                                        
        .... .... 0... = Push: Not set                                                                                  
        .... .... .0.. = Reset: Not set                                                                                 
        .... .... ..1. = Syn: Set                                                                                       
            [Expert Info (Chat/Sequence): Connection establish request (SYN): server port 48933]                        
                [Connection establish request (SYN): server port 48933]                                                 
                [Severity level: Chat]                                                                                  
                [Group: Sequence]                                                                                       
        .... .... ...0 = Fin: Not set                                                                                   
        [TCP Flags: ··········S·]                                                                                       
    Window: 64240                                                                                                       
    [Calculated window size: 64240]                                                                                     
    Checksum: 0xaac1 [unverified]                                                                                       
    [Checksum Status: Unverified]                                                                                       
    Urgent Pointer: 0                                                                                                   
    Options: (12 bytes), Maximum segment size, No-Operation (NOP), Window scale, No-Operation (NOP), No-Operation (NOP), SACK permitted                                                                                                         
        TCP Option - Maximum segment size: 1460 bytes                                                                   
            Kind: Maximum Segment Size (2)                                                                              
            Length: 4                                                                                                   
            MSS Value: 1460                                                                                             
        TCP Option - No-Operation (NOP)                                                                                 
            Kind: No-Operation (1)                                                                                      
        TCP Option - Window scale: 8 (multiply by 256)                                                                  
            Kind: Window Scale (3)                                                                                      
            Length: 3                                                                                                   
            Shift count: 8                                                                                              
            [Multiplier: 256]                                                                                           
        TCP Option - No-Operation (NOP)                                                                                 
            Kind: No-Operation (1)                                                                                      
        TCP Option - No-Operation (NOP)                                                                                 
            Kind: No-Operation (1)                                                                                      
        TCP Option - SACK permitted                                                                                     
            Kind: SACK Permitted (4)                                                                                    
            Length: 2                                                                                                   
    [Timestamps]                                                                                                        
        [Time since first frame in this TCP stream: 0.000000000 seconds]                                                
        [Time since previous frame in this TCP stream: 0.000000000 seconds]                                             
                                                                                                                        
Frame 4: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}, id 0                                                                                                        
    Section number: 1                                                                                                   
    Interface id: 0 (\Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA})                                                
        Interface name: \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}                                              
        Interface description: Беспроводная сеть                                                                        
    Encapsulation type: Ethernet (1)                                                                                    
    Arrival Time: May 13, 2025 00:23:10.737635000 RTZ 2 (зима)                                                          
    UTC Arrival Time: May 12, 2025 21:23:10.737635000 UTC                                                               
    Epoch Arrival Time: 1747084990.737635000                                                                            
    [Time shift for this packet: 0.000000000 seconds]                                                                   
    [Time delta from previous captured frame: 0.014477000 seconds]                                                      
    [Time delta from previous displayed frame: 0.014477000 seconds]                                                     
    [Time since reference or first frame: 0.061728000 seconds]                                                          
    Frame Number: 4                                                                                                     
    Frame Length: 54 bytes (432 bits)                                                                                   
    Capture Length: 54 bytes (432 bits)                                                                                 
    [Frame is marked: False]                                                                                            
    [Frame is ignored: False]                                                                                           
    [Protocols in frame: eth:ethertype:ip:tcp]                                                                          
Ethernet II, Src: Intel_d1:26:fd (78:2b:46:d1:26:fd), Dst: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                          
    Destination: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                                                                    
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Source: Intel_d1:26:fd (78:2b:46:d1:26:fd)                                                                          
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Type: IPv4 (0x0800)                                                                                                 
    [Stream index: 0]                                                                                                   
Internet Protocol Version 4, Src: 192.168.0.111, Dst: 176.112.173.62                                                    
    0100 .... = Version: 4                                                                                              
    .... 0101 = Header Length: 20 bytes (5)                                                                             
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)                                                       
        0000 00.. = Differentiated Services Codepoint: Default (0)                                                      
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)                                     
    Total Length: 40                                                                                                    
    Identification: 0xff39 (65337)                                                                                      
    010. .... = Flags: 0x2, Don't fragment                                                                              
        0... .... = Reserved bit: Not set                                                                               
        .1.. .... = Don't fragment: Set                                                                                 
        ..0. .... = More fragments: Not set                                                                             
    ...0 0000 0000 0000 = Fragment Offset: 0                                                                            
    Time to Live: 128                                                                                                   
    Protocol: TCP (6)                                                                                                   
    Header Checksum: 0x0000 [validation disabled]                                                                       
    [Header checksum status: Unverified]                                                                                
    Source Address: 192.168.0.111                                                                                       
    Destination Address: 176.112.173.62                                                                                 
    [Stream index: 0]                                                                                                   
Transmission Control Protocol, Src Port: 2775, Dst Port: 443, Seq: 393, Ack: 221, Len: 0                                
    Source Port: 2775                                                                                                   
    Destination Port: 443                                                                                               
    [Stream index: 0]                                                                                                   
    [Stream Packet Number: 3]                                                                                           
    [Conversation completeness: Incomplete (8)]                                                                         
        ..0. .... = RST: Absent                                                                                         
        ...0 .... = FIN: Absent                                                                                         
        .... 1... = Data: Present                                                                                       
        .... .0.. = ACK: Absent                                                                                         
        .... ..0. = SYN-ACK: Absent                                                                                     
        .... ...0 = SYN: Absent                                                                                         
        [Completeness Flags: ··D···]                                                                                    
    [TCP Segment Len: 0]                                                                                                
    Sequence Number: 393    (relative sequence number)                                                                  
    Sequence Number (raw): 4289000291                                                                                   
    [Next Sequence Number: 393    (relative sequence number)]                                                           
    Acknowledgment Number: 221    (relative ack number)                                                                 
    Acknowledgment number (raw): 3093018965                                                                             
    0101 .... = Header Length: 20 bytes (5)                                                                             
    Flags: 0x010 (ACK)                                                                                                  
        000. .... .... = Reserved: Not set                                                                              
        ...0 .... .... = Accurate ECN: Not set                                                                          
        .... 0... .... = Congestion Window Reduced: Not set                                                             
        .... .0.. .... = ECN-Echo: Not set                                                                              
        .... ..0. .... = Urgent: Not set                                                                                
        .... ...1 .... = Acknowledgment: Set                                                                            
        .... .... 0... = Push: Not set                                                                                  
        .... .... .0.. = Reset: Not set                                                                                 
        .... .... ..0. = Syn: Not set                                                                                   
        .... .... ...0 = Fin: Not set                                                                                   
        [TCP Flags: ·······A····]                                                                                       
    Window: 510                                                                                                         
    [Calculated window size: 510]                                                                                       
    [Window size scaling factor: -1 (unknown)]                                                                          
    Checksum: 0x1ee1 [unverified]                                                                                       
    [Checksum Status: Unverified]                                                                                       
    Urgent Pointer: 0                                                                                                   
    [Timestamps]                                                                                                        
        [Time since first frame in this TCP stream: 0.061728000 seconds]                                                
        [Time since previous frame in this TCP stream: 0.040026000 seconds]                                             
    [SEQ/ACK analysis]                                                                                                  
        [This is an ACK to the segment in frame: 2]                                                                     
        [The RTT to ACK the segment was: 0.040026000 seconds]                                                           
                                                                                                                        
Frame 5: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}, id 0                                                                                                        
    Section number: 1                                                                                                   
    Interface id: 0 (\Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA})                                                
        Interface name: \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}                                              
        Interface description: Беспроводная сеть                                                                        
    Encapsulation type: Ethernet (1)                                                                                    
    Arrival Time: May 13, 2025 00:23:10.799916000 RTZ 2 (зима)                                                          
    UTC Arrival Time: May 12, 2025 21:23:10.799916000 UTC                                                               
    Epoch Arrival Time: 1747084990.799916000                                                                            
    [Time shift for this packet: 0.000000000 seconds]                                                                   
    [Time delta from previous captured frame: 0.062281000 seconds]                                                      
    [Time delta from previous displayed frame: 0.062281000 seconds]                                                     
    [Time since reference or first frame: 0.124009000 seconds]                                                          
    Frame Number: 5                                                                                                     
    Frame Length: 66 bytes (528 bits)                                                                                   
    Capture Length: 66 bytes (528 bits)                                                                                 
    [Frame is marked: False]                                                                                            
    [Frame is ignored: False]                                                                                           
    [Protocols in frame: eth:ethertype:ip:tcp]                                                                          
Ethernet II, Src: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3), Dst: Intel_d1:26:fd (78:2b:46:d1:26:fd)                          
    Destination: Intel_d1:26:fd (78:2b:46:d1:26:fd)                                                                     
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Source: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                                                                         
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Type: IPv4 (0x0800)                                                                                                 
    [Stream index: 0]                                                                                                   
Internet Protocol Version 4, Src: 212.192.20.195, Dst: 192.168.0.111                                                    
    0100 .... = Version: 4                                                                                              
    .... 0101 = Header Length: 20 bytes (5)                                                                             
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)                                                       
        0000 00.. = Differentiated Services Codepoint: Default (0)                                                      
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)                                     
    Total Length: 52                                                                                                    
    Identification: 0x0000 (0)                                                                                          
    010. .... = Flags: 0x2, Don't fragment                                                                              
        0... .... = Reserved bit: Not set                                                                               
        .1.. .... = Don't fragment: Set                                                                                 
        ..0. .... = More fragments: Not set                                                                             
    ...0 0000 0000 0000 = Fragment Offset: 0                                                                            
    Time to Live: 55                                                                                                    
    Protocol: TCP (6)                                                                                                   
    Header Checksum: 0x9929 [validation disabled]                                                                       
    [Header checksum status: Unverified]                                                                                
    Source Address: 212.192.20.195                                                                                      
    Destination Address: 192.168.0.111                                                                                  
    [Stream index: 1]                                                                                                   
Transmission Control Protocol, Src Port: 48933, Dst Port: 3422, Seq: 0, Ack: 1, Len: 0                                  
    Source Port: 48933                                                                                                  
    Destination Port: 3422                                                                                              
    [Stream index: 1]                                                                                                   
    [Stream Packet Number: 2]                                                                                           
    [Conversation completeness: Incomplete, SYN_SENT (1)]                                                               
        ..0. .... = RST: Absent                                                                                         
        ...0 .... = FIN: Absent                                                                                         
        .... 0... = Data: Absent                                                                                        
        .... .0.. = ACK: Absent                                                                                         
        .... ..0. = SYN-ACK: Absent                                                                                     
        .... ...1 = SYN: Present                                                                                        
        [Completeness Flags: ·····S]                                                                                    
    [TCP Segment Len: 0]                                                                                                
    Sequence Number: 0    (relative sequence number)                                                                    
    Sequence Number (raw): 3020247393                                                                                   
    [Next Sequence Number: 1    (relative sequence number)]                                                             
    Acknowledgment Number: 1    (relative ack number)                                                                   
    Acknowledgment number (raw): 1402797155                                                                             
    1000 .... = Header Length: 32 bytes (8)                                                                             
    Flags: 0x012 (SYN, ACK)                                                                                             
        000. .... .... = Reserved: Not set                                                                              
        ...0 .... .... = Accurate ECN: Not set                                                                          
        .... 0... .... = Congestion Window Reduced: Not set                                                             
        .... .0.. .... = ECN-Echo: Not set                                                                              
        .... ..0. .... = Urgent: Not set                                                                                
        .... ...1 .... = Acknowledgment: Set                                                                            
        .... .... 0... = Push: Not set                                                                                  
        .... .... .0.. = Reset: Not set                                                                                 
        .... .... ..1. = Syn: Set                                                                                       
            [Expert Info (Chat/Sequence): Connection establish acknowledge (SYN+ACK): server port 48933]                
                [Connection establish acknowledge (SYN+ACK): server port 48933]                                         
                [Severity level: Chat]                                                                                  
                [Group: Sequence]                                                                                       
        .... .... ...0 = Fin: Not set                                                                                   
        [TCP Flags: ·······A··S·]                                                                                       
    Window: 64240                                                                                                       
    [Calculated window size: 64240]                                                                                     
    Checksum: 0xa78a [unverified]                                                                                       
    [Checksum Status: Unverified]                                                                                       
    Urgent Pointer: 0                                                                                                   
    Options: (12 bytes), Maximum segment size, No-Operation (NOP), No-Operation (NOP), SACK permitted, No-Operation (NOP), Window scale                                                                                                         
        TCP Option - Maximum segment size: 1460 bytes                                                                   
            Kind: Maximum Segment Size (2)                                                                              
            Length: 4                                                                                                   
            MSS Value: 1460                                                                                             
        TCP Option - No-Operation (NOP)                                                                                 
            Kind: No-Operation (1)                                                                                      
        TCP Option - No-Operation (NOP)                                                                                 
            Kind: No-Operation (1)                                                                                      
        TCP Option - SACK permitted                                                                                     
            Kind: SACK Permitted (4)                                                                                    
            Length: 2                                                                                                   
        TCP Option - No-Operation (NOP)                                                                                 
            Kind: No-Operation (1)                                                                                      
        TCP Option - Window scale: 7 (multiply by 128)                                                                  
            Kind: Window Scale (3)                                                                                      
            Length: 3                                                                                                   
            Shift count: 7                                                                                              
            [Multiplier: 128]                                                                                           
    [Timestamps]                                                                                                        
        [Time since first frame in this TCP stream: 0.076758000 seconds]                                                
        [Time since previous frame in this TCP stream: 0.076758000 seconds]                                             
    [SEQ/ACK analysis]                                                                                                  
        [This is an ACK to the segment in frame: 3]                                                                     
        [The RTT to ACK the segment was: 0.076758000 seconds]                                                           
                                                                                                                        
Frame 6: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}, id 0                                                                                                        
    Section number: 1                                                                                                   
    Interface id: 0 (\Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA})                                                
        Interface name: \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}                                              
        Interface description: Беспроводная сеть                                                                        
    Encapsulation type: Ethernet (1)                                                                                    
    Arrival Time: May 13, 2025 00:23:10.800008000 RTZ 2 (зима)                                                          
    UTC Arrival Time: May 12, 2025 21:23:10.800008000 UTC                                                               
    Epoch Arrival Time: 1747084990.800008000                                                                            
    [Time shift for this packet: 0.000000000 seconds]                                                                   
    [Time delta from previous captured frame: 0.000092000 seconds]                                                      
    [Time delta from previous displayed frame: 0.000092000 seconds]                                                     
    [Time since reference or first frame: 0.124101000 seconds]                                                          
    Frame Number: 6                                                                                                     
    Frame Length: 54 bytes (432 bits)                                                                                   
    Capture Length: 54 bytes (432 bits)                                                                                 
    [Frame is marked: False]                                                                                            
    [Frame is ignored: False]                                                                                           
    [Protocols in frame: eth:ethertype:ip:tcp]                                                                          
Ethernet II, Src: Intel_d1:26:fd (78:2b:46:d1:26:fd), Dst: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                          
    Destination: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                                                                    
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Source: Intel_d1:26:fd (78:2b:46:d1:26:fd)                                                                          
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Type: IPv4 (0x0800)                                                                                                 
    [Stream index: 0]                                                                                                   
Internet Protocol Version 4, Src: 192.168.0.111, Dst: 212.192.20.195                                                    
    0100 .... = Version: 4                                                                                              
    .... 0101 = Header Length: 20 bytes (5)                                                                             
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)                                                       
        0000 00.. = Differentiated Services Codepoint: Default (0)                                                      
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)                                     
    Total Length: 40                                                                                                    
    Identification: 0xfee1 (65249)                                                                                      
    010. .... = Flags: 0x2, Don't fragment                                                                              
        0... .... = Reserved bit: Not set                                                                               
        .1.. .... = Don't fragment: Set                                                                                 
        ..0. .... = More fragments: Not set                                                                             
    ...0 0000 0000 0000 = Fragment Offset: 0                                                                            
    Time to Live: 128                                                                                                   
    Protocol: TCP (6)                                                                                                   
    Header Checksum: 0x0000 [validation disabled]                                                                       
    [Header checksum status: Unverified]                                                                                
    Source Address: 192.168.0.111                                                                                       
    Destination Address: 212.192.20.195                                                                                 
    [Stream index: 1]                                                                                                   
Transmission Control Protocol, Src Port: 3422, Dst Port: 48933, Seq: 1, Ack: 1, Len: 0                                  
    Source Port: 3422                                                                                                   
    Destination Port: 48933                                                                                             
    [Stream index: 1]                                                                                                   
    [Stream Packet Number: 3]                                                                                           
    [Conversation completeness: Incomplete, CLIENT_ESTABLISHED (3)]                                                     
        ..0. .... = RST: Absent                                                                                         
        ...0 .... = FIN: Absent                                                                                         
        .... 0... = Data: Absent                                                                                        
        .... .0.. = ACK: Absent                                                                                         
        .... ..1. = SYN-ACK: Present                                                                                    
        .... ...1 = SYN: Present                                                                                        
        [Completeness Flags: ····SS]                                                                                    
    [TCP Segment Len: 0]                                                                                                
    Sequence Number: 1    (relative sequence number)                                                                    
    Sequence Number (raw): 1402797155                                                                                   
    [Next Sequence Number: 1    (relative sequence number)]                                                             
    Acknowledgment Number: 1    (relative ack number)                                                                   
    Acknowledgment number (raw): 3020247394                                                                             
    0101 .... = Header Length: 20 bytes (5)                                                                             
    Flags: 0x010 (ACK)                                                                                                  
        000. .... .... = Reserved: Not set                                                                              
        ...0 .... .... = Accurate ECN: Not set                                                                          
        .... 0... .... = Congestion Window Reduced: Not set                                                             
        .... .0.. .... = ECN-Echo: Not set                                                                              
        .... ..0. .... = Urgent: Not set                                                                                
        .... ...1 .... = Acknowledgment: Set                                                                            
        .... .... 0... = Push: Not set                                                                                  
        .... .... .0.. = Reset: Not set                                                                                 
        .... .... ..0. = Syn: Not set                                                                                   
        .... .... ...0 = Fin: Not set                                                                                   
        [TCP Flags: ·······A····]                                                                                       
    Window: 513                                                                                                         
    [Calculated window size: 131328]                                                                                    
    [Window size scaling factor: 256]                                                                                   
    Checksum: 0xaab5 [unverified]                                                                                       
    [Checksum Status: Unverified]                                                                                       
    Urgent Pointer: 0                                                                                                   
    [Timestamps]                                                                                                        
        [Time since first frame in this TCP stream: 0.076850000 seconds]                                                
        [Time since previous frame in this TCP stream: 0.000092000 seconds]                                             
    [SEQ/ACK analysis]                                                                                                  
        [This is an ACK to the segment in frame: 5]                                                                     
        [The RTT to ACK the segment was: 0.000092000 seconds]                                                           
        [iRTT: 0.076850000 seconds]                                                                                     
                                                                                                                        
Frame 7: 571 bytes on wire (4568 bits), 571 bytes captured (4568 bits) on interface \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}, id 0                                                                                                    
    Section number: 1                                                                                                   
    Interface id: 0 (\Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA})                                                
        Interface name: \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}                                              
        Interface description: Беспроводная сеть                                                                        
    Encapsulation type: Ethernet (1)                                                                                    
    Arrival Time: May 13, 2025 00:23:10.800356000 RTZ 2 (зима)                                                          
    UTC Arrival Time: May 12, 2025 21:23:10.800356000 UTC                                                               
    Epoch Arrival Time: 1747084990.800356000                                                                            
    [Time shift for this packet: 0.000000000 seconds]                                                                   
    [Time delta from previous captured frame: 0.000348000 seconds]                                                      
    [Time delta from previous displayed frame: 0.000348000 seconds]                                                     
    [Time since reference or first frame: 0.124449000 seconds]                                                          
    Frame Number: 7                                                                                                     
    Frame Length: 571 bytes (4568 bits)                                                                                 
    Capture Length: 571 bytes (4568 bits)                                                                               
    [Frame is marked: False]                                                                                            
    [Frame is ignored: False]                                                                                           
    [Protocols in frame: eth:ethertype:ip:tcp:tls]                                                                      
Ethernet II, Src: Intel_d1:26:fd (78:2b:46:d1:26:fd), Dst: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                          
    Destination: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                                                                    
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Source: Intel_d1:26:fd (78:2b:46:d1:26:fd)                                                                          
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Type: IPv4 (0x0800)                                                                                                 
    [Stream index: 0]                                                                                                   
Internet Protocol Version 4, Src: 192.168.0.111, Dst: 212.192.20.195                                                    
    0100 .... = Version: 4                                                                                              
    .... 0101 = Header Length: 20 bytes (5)                                                                             
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)                                                       
        0000 00.. = Differentiated Services Codepoint: Default (0)                                                      
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)                                     
    Total Length: 557                                                                                                   
    Identification: 0xfee2 (65250)                                                                                      
    010. .... = Flags: 0x2, Don't fragment                                                                              
        0... .... = Reserved bit: Not set                                                                               
        .1.. .... = Don't fragment: Set                                                                                 
        ..0. .... = More fragments: Not set                                                                             
    ...0 0000 0000 0000 = Fragment Offset: 0                                                                            
    Time to Live: 128                                                                                                   
    Protocol: TCP (6)                                                                                                   
    Header Checksum: 0x0000 [validation disabled]                                                                       
    [Header checksum status: Unverified]                                                                                
    Source Address: 192.168.0.111                                                                                       
    Destination Address: 212.192.20.195                                                                                 
    [Stream index: 1]                                                                                                   
Transmission Control Protocol, Src Port: 3422, Dst Port: 48933, Seq: 1, Ack: 1, Len: 517                                
    Source Port: 3422                                                                                                   
    Destination Port: 48933                                                                                             
    [Stream index: 1]                                                                                                   
    [Stream Packet Number: 4]                                                                                           
    [Conversation completeness: Incomplete, ESTABLISHED (7)]                                                            
        ..0. .... = RST: Absent                                                                                         
        ...0 .... = FIN: Absent                                                                                         
        .... 0... = Data: Absent                                                                                        
        .... .1.. = ACK: Present                                                                                        
        .... ..1. = SYN-ACK: Present                                                                                    
        .... ...1 = SYN: Present                                                                                        
        [Completeness Flags: ···ASS]                                                                                    
    [TCP Segment Len: 517]                                                                                              
    Sequence Number: 1    (relative sequence number)                                                                    
    Sequence Number (raw): 1402797155                                                                                   
    [Next Sequence Number: 518    (relative sequence number)]                                                           
    Acknowledgment Number: 1    (relative ack number)                                                                   
    Acknowledgment number (raw): 3020247394                                                                             
    0101 .... = Header Length: 20 bytes (5)                                                                             
    Flags: 0x018 (PSH, ACK)                                                                                             
        000. .... .... = Reserved: Not set                                                                              
        ...0 .... .... = Accurate ECN: Not set                                                                          
        .... 0... .... = Congestion Window Reduced: Not set                                                             
        .... .0.. .... = ECN-Echo: Not set                                                                              
        .... ..0. .... = Urgent: Not set                                                                                
        .... ...1 .... = Acknowledgment: Set                                                                            
        .... .... 1... = Push: Set                                                                                      
        .... .... .0.. = Reset: Not set                                                                                 
        .... .... ..0. = Syn: Not set                                                                                   
        .... .... ...0 = Fin: Not set                                                                                   
        [TCP Flags: ·······AP···]                                                                                       
    Window: 513                                                                                                         
    [Calculated window size: 131328]                                                                                    
    [Window size scaling factor: 256]                                                                                   
    Checksum: 0xacba [unverified]                                                                                       
    [Checksum Status: Unverified]                                                                                       
    Urgent Pointer: 0                                                                                                   
    [Timestamps]                                                                                                        
        [Time since first frame in this TCP stream: 0.077198000 seconds]                                                
        [Time since previous frame in this TCP stream: 0.000348000 seconds]                                             
    [SEQ/ACK analysis]                                                                                                  
        [iRTT: 0.076850000 seconds]                                                                                     
        [Bytes in flight: 517]                                                                                          
        [Bytes sent since last PSH flag: 517]                                                                           
    TCP payload (517 bytes)                                                                                             
Transport Layer Security                                                                                                
    TLSv1 Record Layer: Handshake Protocol: Client Hello                                                                
        Content Type: Handshake (22)                                                                                    
        Version: TLS 1.0 (0x0301)                                                                                       
        Length: 512                                                                                                     
        Handshake Protocol: Client Hello                                                                                
            Handshake Type: Client Hello (1)                                                                            
            Length: 508                                                                                                 
            Version: TLS 1.2 (0x0303)                                                                                   
                [Expert Info (Chat/Deprecated): This legacy_version field MUST be ignored. The supported_versions extension is present and MUST be used instead.]                                                                               
                    [This legacy_version field MUST be ignored. The supported_versions extension is present and MUST be used instead.]                                                                                                          
                    [Severity level: Chat]                                                                              
                    [Group: Deprecated]                                                                                 
            Random: d9eed1d388e159ed4e2a296f3d7441b93e9b90d83490b5612359302cae11622b                                    
                GMT Unix Time: Nov 11, 2085 11:52:35.000000000 RTZ 2 (зима)                                             
                Random Bytes: 88e159ed4e2a296f3d7441b93e9b90d83490b5612359302cae11622b                                  
            Session ID Length: 32                                                                                       
            Session ID: 6de19da0e2b5c54575ceb223b9fb87689961f750e2a5fdcc65dbf6e539a7d96e                                
            Cipher Suites Length: 32                                                                                    
            Cipher Suites (16 suites)                                                                                   
                Cipher Suite: Reserved (GREASE) (0x9a9a)                                                                
                Cipher Suite: TLS_AES_128_GCM_SHA256 (0x1301)                                                           
                Cipher Suite: TLS_AES_256_GCM_SHA384 (0x1302)                                                           
                Cipher Suite: TLS_CHACHA20_POLY1305_SHA256 (0x1303)                                                     
                Cipher Suite: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (0xc02b)                                          
                Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)                                            
                Cipher Suite: TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 (0xc02c)                                          
                Cipher Suite: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)                                            
                Cipher Suite: TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 (0xcca9)                                    
                Cipher Suite: TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (0xcca8)                                      
                Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (0xc013)                                               
                Cipher Suite: TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (0xc014)                                               
                Cipher Suite: TLS_RSA_WITH_AES_128_GCM_SHA256 (0x009c)                                                  
                Cipher Suite: TLS_RSA_WITH_AES_256_GCM_SHA384 (0x009d)                                                  
                Cipher Suite: TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)                                                     
                Cipher Suite: TLS_RSA_WITH_AES_256_CBC_SHA (0x0035)                                                     
            Compression Methods Length: 1                                                                               
            Compression Methods (1 method)                                                                              
                Compression Method: null (0)                                                                            
            Extensions Length: 403                                                                                      
            Extension: Reserved (GREASE) (len=0)                                                                        
                Type: Reserved (GREASE) (51914)                                                                         
                Length: 0                                                                                               
                Data: <MISSING>                                                                                         
            Extension: supported_versions (len=7) TLS 1.3, TLS 1.2                                                      
                Type: supported_versions (43)                                                                           
                Length: 7                                                                                               
                Supported Versions length: 6                                                                            
                Supported Version: Reserved (GREASE) (0x0a0a)                                                           
                Supported Version: TLS 1.3 (0x0304)                                                                     
                Supported Version: TLS 1.2 (0x0303)                                                                     
            Extension: session_ticket (len=0)                                                                           
                Type: session_ticket (35)                                                                               
                Length: 0                                                                                               
                Session Ticket: <MISSING>                                                                               
            Extension: signature_algorithms (len=18)                                                                    
                Type: signature_algorithms (13)                                                                         
                Length: 18                                                                                              
                Signature Hash Algorithms Length: 16                                                                    
                Signature Hash Algorithms (8 algorithms)                                                                
                    Signature Algorithm: ecdsa_secp256r1_sha256 (0x0403)                                                
                        Signature Hash Algorithm Hash: SHA256 (4)                                                       
                        Signature Hash Algorithm Signature: ECDSA (3)                                                   
                    Signature Algorithm: rsa_pss_rsae_sha256 (0x0804)                                                   
                        Signature Hash Algorithm Hash: Unknown (8)                                                      
                        Signature Hash Algorithm Signature: Unknown (4)                                                 
                    Signature Algorithm: rsa_pkcs1_sha256 (0x0401)                                                      
                        Signature Hash Algorithm Hash: SHA256 (4)                                                       
                        Signature Hash Algorithm Signature: RSA (1)                                                     
                    Signature Algorithm: ecdsa_secp384r1_sha384 (0x0503)                                                
                        Signature Hash Algorithm Hash: SHA384 (5)                                                       
                        Signature Hash Algorithm Signature: ECDSA (3)                                                   
                    Signature Algorithm: rsa_pss_rsae_sha384 (0x0805)                                                   
                        Signature Hash Algorithm Hash: Unknown (8)                                                      
                        Signature Hash Algorithm Signature: Unknown (5)                                                 
                    Signature Algorithm: rsa_pkcs1_sha384 (0x0501)                                                      
                        Signature Hash Algorithm Hash: SHA384 (5)                                                       
                        Signature Hash Algorithm Signature: RSA (1)                                                     
                    Signature Algorithm: rsa_pss_rsae_sha512 (0x0806)                                                   
                        Signature Hash Algorithm Hash: Unknown (8)                                                      
                        Signature Hash Algorithm Signature: Unknown (6)                                                 
                    Signature Algorithm: rsa_pkcs1_sha512 (0x0601)                                                      
                        Signature Hash Algorithm Hash: SHA512 (6)                                                       
                        Signature Hash Algorithm Signature: RSA (1)                                                     
            Extension: ec_point_formats (len=2)                                                                         
                Type: ec_point_formats (11)                                                                             
                Length: 2                                                                                               
                EC point formats Length: 1                                                                              
                Elliptic curves point formats (1)                                                                       
                    EC point format: uncompressed (0)                                                                   
            Extension: server_name (len=14) name=yahoo.com                                                              
                Type: server_name (0)                                                                                   
                Length: 14                                                                                              
                Server Name Indication extension                                                                        
                    Server Name list length: 12                                                                         
                    Server Name Type: host_name (0)                                                                     
                    Server Name length: 9                                                                               
                    Server Name: yahoo.com                                                                              
            Extension: signed_certificate_timestamp (len=0)                                                             
                Type: signed_certificate_timestamp (18)                                                                 
                Length: 0                                                                                               
            Extension: extended_master_secret (len=0)                                                                   
                Type: extended_master_secret (23)                                                                       
                Length: 0                                                                                               
            Extension: renegotiation_info (len=1)                                                                       
                Type: renegotiation_info (65281)                                                                        
                Length: 1                                                                                               
                Renegotiation Info extension                                                                            
                    Renegotiation info extension length: 0                                                              
            Extension: application_settings (len=5)                                                                     
                Type: application_settings (17513)                                                                      
                Length: 5                                                                                               
                ALPS Extension Length: 3                                                                                
                Supported ALPN List                                                                                     
                    Supported ALPN Length: 2                                                                            
                    Supported ALPN: h2                                                                                  
            Extension: psk_key_exchange_modes (len=2)                                                                   
                Type: psk_key_exchange_modes (45)                                                                       
                Length: 2                                                                                               
                PSK Key Exchange Modes Length: 1                                                                        
                PSK Key Exchange Mode: PSK with (EC)DHE key establishment (psk_dhe_ke) (1)                              
            Extension: compress_certificate (len=3)                                                                     
                Type: compress_certificate (27)                                                                         
                Length: 3                                                                                               
                Algorithms Length: 2                                                                                    
                Algorithm: brotli (2)                                                                                   
            Extension: application_layer_protocol_negotiation (len=14)                                                  
                Type: application_layer_protocol_negotiation (16)                                                       
                Length: 14                                                                                              
                ALPN Extension Length: 12                                                                               
                ALPN Protocol                                                                                           
                    ALPN string length: 2                                                                               
                    ALPN Next Protocol: h2                                                                              
                    ALPN string length: 8                                                                               
                    ALPN Next Protocol: http/1.1                                                                        
            Extension: supported_groups (len=10)                                                                        
                Type: supported_groups (10)                                                                             
                Length: 10                                                                                              
                Supported Groups List Length: 8                                                                         
                Supported Groups (4 groups)                                                                             
                    Supported Group: Reserved (GREASE) (0x0a0a)                                                         
                    Supported Group: x25519 (0x001d)                                                                    
                    Supported Group: secp256r1 (0x0017)                                                                 
                    Supported Group: secp384r1 (0x0018)                                                                 
            Extension: status_request (len=5)                                                                           
                Type: status_request (5)                                                                                
                Length: 5                                                                                               
                Certificate Status Type: OCSP (1)                                                                       
                Responder ID list Length: 0                                                                             
                Request Extensions Length: 0                                                                            
            Extension: key_share (len=43) x25519                                                                        
                Type: key_share (51)                                                                                    
                Length: 43                                                                                              
                Key Share extension                                                                                     
                    Client Key Share Length: 41                                                                         
                    Key Share Entry: Group: Reserved (GREASE), Key Exchange length: 1                                   
                        Group: Reserved (GREASE) (2570)                                                                 
                        Key Exchange Length: 1                                                                          
                        Key Exchange: 00                                                                                
                    Key Share Entry: Group: x25519, Key Exchange length: 32                                             
                        Group: x25519 (29)                                                                              
                        Key Exchange Length: 32                                                                         
                        Key Exchange: 44261e6d0f3b91c4b386c033b67823e986e1349a886a2bcf83f7241fda866f49                  
            Extension: Reserved (GREASE) (len=1)                                                                        
                Type: Reserved (GREASE) (43690)                                                                         
                Length: 1                                                                                               
                Data: 00                                                                                                
            Extension: padding (len=206)                                                                                
                Type: padding (21)                                                                                      
                Length: 206                                                                                             
                Padding Data […]: 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                                                                                                           
            [JA4: t13d1516h2_8daaf6152771_e5627efa2ab1]                                                                 
            [JA4_r: t13d1516h2_002f,0035,009c,009d,1301,1302,1303,c013,c014,c02b,c02c,c02f,c030,cca8,cca9_0005,000a,000b,000d,0012,0015,0017,001b,0023,002b,002d,0033,4469,ff01_0403,0804,0401,0503,0805,0501,0806,0601]                        
            [JA3 Fullstring: 771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,43-35-13-11-0-18-23-65281-17513-45-27-16-10-5-51-21,29-23-24,0]                                                                   
            [JA3: 3fc764dc206c2e8d6e58c546d09dadf0]                                                                     
                                                                                                                        
Frame 8: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}, id 0                                                                                                        
    Section number: 1                                                                                                   
    Interface id: 0 (\Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA})                                                
        Interface name: \Device\NPF_{E453D0C9-B93A-4550-A890-DD57B9110EFA}                                              
        Interface description: Беспроводная сеть                                                                        
    Encapsulation type: Ethernet (1)                                                                                    
    Arrival Time: May 13, 2025 00:23:10.842666000 RTZ 2 (зима)                                                          
    UTC Arrival Time: May 12, 2025 21:23:10.842666000 UTC                                                               
    Epoch Arrival Time: 1747084990.842666000                                                                            
    [Time shift for this packet: 0.000000000 seconds]                                                                   
    [Time delta from previous captured frame: 0.042310000 seconds]                                                      
    [Time delta from previous displayed frame: 0.042310000 seconds]                                                     
    [Time since reference or first frame: 0.166759000 seconds]                                                          
    Frame Number: 8                                                                                                     
    Frame Length: 54 bytes (432 bits)                                                                                   
    Capture Length: 54 bytes (432 bits)                                                                                 
    [Frame is marked: False]                                                                                            
    [Frame is ignored: False]                                                                                           
    [Protocols in frame: eth:ethertype:ip:tcp]                                                                          
Ethernet II, Src: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3), Dst: Intel_d1:26:fd (78:2b:46:d1:26:fd)                          
    Destination: Intel_d1:26:fd (78:2b:46:d1:26:fd)                                                                     
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Source: TPLink_36:2b:c3 (5c:e9:31:36:2b:c3)                                                                         
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)                               
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)                                            
    Type: IPv4 (0x0800)                                                                                                 
    [Stream index: 0]                                                                                                   
Internet Protocol Version 4, Src: 212.192.20.195, Dst: 192.168.0.111                                                    
    0100 .... = Version: 4                                                                                              
    .... 0101 = Header Length: 20 bytes (5)                                                                             
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)                                                       
        0000 00.. = Differentiated Services Codepoint: Default (0)                                                      
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)                                     
    Total Length: 40                                                                                                    
    Identification: 0x8645 (34373)                                                                                      
    010. .... = Flags: 0x2, Don't fragment                                                                              
        0... .... = Reserved bit: Not set                                                                               
        .1.. .... = Don't fragment: Set                                                                                 
        ..0. .... = More fragments: Not set                                                                             
    ...0 0000 0000 0000 = Fragment Offset: 0                                                                            
    Time to Live: 55                                                                                                    
    Protocol: TCP (6)                                                                                                   
    Header Checksum: 0x12f0 [validation disabled]                                                                       
    [Header checksum status: Unverified]                                                                                
    Source Address: 212.192.20.195                                                                                      
    Destination Address: 192.168.0.111                                                                                  
    [Stream index: 1]                                                                                                   
Transmission Control Protocol, Src Port: 48933, Dst Port: 3422, Seq: 1, Ack: 518, Len: 0                                
    Source Port: 48933                                                                                                  
    Destination Port: 3422                                                                                              
    [Stream index: 1]                                                                                                   
    [Stream Packet Number: 5]                                                                                           
    [Conversation completeness: Incomplete, DATA (15)]                                                                  
        ..0. .... = RST: Absent                                                                                         
        ...0 .... = FIN: Absent                                                                                         
        .... 1... = Data: Present                                                                                       
        .... .1.. = ACK: Present                                                                                        
        .... ..1. = SYN-ACK: Present                                                                                    
        .... ...1 = SYN: Present                                                                                        
        [Completeness Flags: ··DASS]                                                                                    
    [TCP Segment Len: 0]                                                                                                
    Sequence Number: 1    (relative sequence number)                                                                    
    Sequence Number (raw): 3020247394                                                                                   
    [Next Sequence Number: 1    (relative sequence number)]                                                             
    Acknowledgment Number: 518    (relative ack number)                                                                 
    Acknowledgment number (raw): 1402797672                                                                             
    0101 .... = Header Length: 20 bytes (5)                                                                             
    Flags: 0x010 (ACK)                                                                                                  
        000. .... .... = Reserved: Not set                                                                              
        ...0 .... .... = Accurate ECN: Not set                                                                          
        .... 0... .... = Congestion Window Reduced: Not set                                                             
        .... .0.. .... = ECN-Echo: Not set                                                                              
        .... ..0. .... = Urgent: Not set                                                                                
        .... ...1 .... = Acknowledgment: Set                                                                            
        .... .... 0... = Push: Not set                                                                                  
        .... .... .0.. = Reset: Not set                                                                                 
        .... .... ..0. = Syn: Not set                                                                                   
        .... .... ...0 = Fin: Not set                                                                                   
        [TCP Flags: ·······A····]                                                                                       
    Window: 501                                                                                                         
    [Calculated window size: 64128]                                                                                     
    [Window size scaling factor: 128]                                                                                   
    Checksum: 0xdf53 [unverified]                                                                                       
    [Checksum Status: Unverified]                                                                                       
    Urgent Pointer: 0                                                                                                   
    [Timestamps]                                                                                                        
        [Time since first frame in this TCP stream: 0.119508000 seconds]                                                
        [Time since previous frame in this TCP stream: 0.042310000 seconds]                                             
    [SEQ/ACK analysis]                                                                                                  
        [This is an ACK to the segment in frame: 7]                                                                     
        [The RTT to ACK the segment was: 0.042310000 seconds]                                                           
        [iRTT: 0.076850000 seconds]                                                                                     
                                                                                                                        
8 packets captured                                                                                                      

Если взять последний захваченный пакет, то станет понятно, что это ответный tcp- пакет, не содержащий полезных данных. Скорее всего, он нужен для поддержания соединения.