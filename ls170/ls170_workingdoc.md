# LS170 — Lesson 1: The Internet

## 1. Networks and the Internet

A **computer network** consists of independent devices connected so that they can exchange information. Each device maintains its own memory, execution state, and internal processes. Communication occurs by transmitting information across boundaries rather than sharing memory.

The **Internet** is a global network of interconnected networks that communicate using common protocols.

### Addressing, forwarding, and routing

Communication between two directly connected devices presents little ambiguity about the intended recipient. As networks grow, the system must identify recipients and determine how to reach them.

- **Addressing:** Identifies the intended destination.
- **Forwarding:** Moves data toward its next destination using existing forwarding information.
- **Routing:** Determines available paths through networks and supplies information used for forwarding.

A **switch** connects devices within a local network and forwards frames based on link-layer addresses.

A **router** connects different networks and forwards IP packets toward their destinations.

### Hop-by-hop forwarding

A router does not need the complete itinerary for every packet. It examines the destination IP address, consults its forwarding information, and selects the appropriate next hop.

Each router maintains its own forwarding state. A packet can therefore travel across multiple independently operated networks through a sequence of local decisions.

**Governing principle:** The sender need not know the entire route; forwarding decisions can be distributed among routers.

### Redundancy and fault tolerance

Networks may contain multiple paths between destinations. If a link or router fails, routing mechanisms may discover and use an alternative path.

Recovery requires that:

- Another usable path exists.
- The network can detect or otherwise learn about the failure.
- Routing information can adapt to the changed conditions.

Communication may be interrupted during recovery, and an alternative route is not guaranteed.

**Redundancy** provides alternative resources or paths. **Fault tolerance** is the ability of a system to continue operating despite certain failures.

---

## 2. Network Protocols

A **protocol** is a set of agreed rules governing communication between participants.

Protocols establish:

- **Syntax:** Message structure, formatting, and representation.
- **Semantics:** What messages and fields mean and what actions they require.
- **Timing and sequencing:** When messages may be exchanged and in what order.

Protocols may also define acknowledgment, error detection, retransmission, and recovery behavior.

### Protocols and state transitions

Participants coordinate by exchanging messages rather than sharing internal memory.

A protocol may define which actions are valid in particular states and what events trigger transitions.

Example:

1. Sender requests permission to transmit.
2. Receiver acknowledges readiness.
3. Sender begins transmitting data.

This is an illustrative handshake. Not every protocol requires an acceptance exchange.

**Governing principle:** Protocols allow independent participants to coordinate their behavior through agreed message formats and state transitions.

### Protocol interoperability

Different networks can use different hardware and underlying technologies while communicating through compatible protocols.

For example, Ethernet and Wi-Fi provide different link-layer mechanisms, but both can carry IP packets.

A single communication process normally involves multiple complementary protocols, not one protocol exclusively.

Encryption is another protocol-dependent concern. Encrypted communication requires compatible cryptographic mechanisms, but not every network protocol provides or requires encryption.

---

## 3. Layered Network Architecture

A **layered architecture** divides network communication into separate responsibilities.

Each layer provides services to the layer above and relies on services from the layer below.

**Governing distinction:** Layers have separate responsibilities but operational dependencies.

A correctly constructed HTTP request cannot reach a remote server if the necessary underlying network connectivity is unavailable.

### OSI and TCP/IP reference models

| OSI model | TCP/IP model |
|---|---|
| Application | Application |
| Presentation | Application |
| Session | Application |
| Transport | Transport |
| Network | Internet |
| Data Link | Link |
| Physical | Link |

These are conceptual models. Correspondence between the models is approximate, and implementations do not necessarily follow every distinction rigidly.

### TCP/IP layer responsibilities

**Application layer**

Defines application-level communication, such as HTTP requests and responses.

**Transport layer**

Provides communication services between application processes. TCP provides a reliable, ordered byte stream; UDP provides a datagram-oriented transport service.

**Internet layer**

Provides logical IP addressing and packet forwarding across interconnected networks.

**Link layer**

Supports communication over local network links, including framing and link-layer addressing. The four-layer TCP/IP model includes the underlying physical transmission mechanisms within its Link layer.

### Layer responsibility versus dependency

A layer does not generally need to interpret the application-level meaning of the data it carries.

For example:

- HTTP defines a web request.
- TCP carries application data.
- IP provides addressing and forwarding.
- Ethernet carries frames across a local link.
- Physical hardware transmits signals representing bits.

Each component performs the job appropriate to its layer.

---

## 4. Encapsulation and Decapsulation

A **Protocol Data Unit (PDU)** is the unit of data handled by a particular protocol layer.

### Encapsulation — Sender

As information moves **down** the protocol stack, each layer treats the data from the layer above as its payload and adds protocol-specific information, typically a header.

For an HTTP request carried over TCP/IP and Ethernet:

Application: HTTP message

↓ TCP adds transport information

Transport: TCP segment

↓ IP adds network information

Internet: IP packet

↓ Ethernet adds link information

Link: Ethernet frame

↓ Physical transmission

The completed frame is represented as physical signals for transmission.

**Encapsulation proceeds downward through the protocol stack.**

### Decapsulation — Receiver

The receiving system processes information at each layer and passes the enclosed payload upward.

Ethernet frame

↑ Link layer processes framing information

IP packet

↑ Internet layer processes IP information

TCP segment

↑ Transport layer processes TCP information

Application data

The receiving transport layer may need to reassemble data before delivering it to the application.

**Decapsulation proceeds upward through the protocol stack.**

### Two distinct boundaries

**Between layers:** Data passes between networking components inside a computer, with changes to its logical representation.

**Between devices:** Information crosses a physical network connection as transmitted signals.

Passing data between software layers is not itself physical network transmission.

### Encapsulation at intermediate routers

A router performing ordinary IP forwarding:

1. Receives a link-layer frame.
2. Processes the incoming link-layer information.
3. Examines the enclosed IP packet.
4. Consults forwarding information and selects the outgoing path.
5. Updates necessary IP fields and encapsulates the packet for the next link.

Link-layer framing can change at every hop while the packet continues toward its IP destination.

The router normally does not need to interpret the TCP segment or HTTP request.

**Governing principle:** Each network component interprets the protocol information necessary for its own responsibilities.

---

## 5. The Physical Network

Bits are abstract units of binary information. Physical networks transmit signals that **represent** those bits.

Network hardware converts digital information into physical signals and receiving hardware interprets those signals.

Different media use different physical representations:

- **Copper:** Electrical signals.
- **Fiber optics:** Light signals.
- **Wireless:** Electromagnetic radio waves.

The encoding method determines how physical variations represent binary information. A particular voltage does not universally correspond to a particular bit value.

**Core transformation:**

Abstract information → Physical representation → Transmission → Interpretation → Abstract information

### Bandwidth and latency

**Bandwidth** measures a communication link's capacity to transmit data per unit of time, usually in bits per second (bps).

**Latency** measures the delay involved in transferring information between points.

Road analogy:

- Bandwidth: How many cars a road can accommodate per unit of time.
- Latency: How long a car takes to complete its journey.

Increasing the number of lanes increases capacity without necessarily increasing the speed of an individual car.

**Governing distinction:** High bandwidth does not necessarily mean low latency.

### Four components of network latency

**1. Processing delay**

Time a network device spends examining and handling data, such as evaluating packet headers.

**2. Queuing delay**

Time a packet spends waiting for its turn to be processed or transmitted, often because multiple packets compete for limited resources.

**3. Transmission delay**

Time required to place all the bits of a packet onto a link.

Depends on:

- Data size
- Link transmission rate

Transmission delay = Packet size in bits / Transmission rate in bits per second

**4. Propagation delay**

Time required for a physical signal to travel through the transmission medium.

Depends on:

- Distance
- Propagation speed of the signal through that medium

Propagation delay = Distance / Propagation speed

Increasing bandwidth can reduce transmission delay and may reduce queuing delay, but does not itself increase the signal's propagation speed.

### Network hops

A **hop** is a forwarding step along a network path, typically from one router to the next.

Packets may pass through multiple intermediate devices before reaching their destinations.

Each hop can introduce additional processing, queuing, transmission, and propagation delays.

### Round-trip time (RTT)

**Round-trip time** is the elapsed time for data to reach a destination and for a response or acknowledgment to return.

The outgoing and return paths need not be identical.

### Bandwidth bottlenecks

A network path may contain links with different capacities.

A lower-capacity link can limit the throughput of the entire path.

Example:

100 Mbps → 10 Mbps → 100 Mbps

The middle link is the bottleneck. Assuming no other limiting factors, sustained end-to-end throughput cannot exceed its 10 Mbps capacity.

---

## 6. The Link/Data Link Layer

The Link layer provides mechanisms for communication across local network links.

It adds logical structure to binary data using **framing**.

### Ethernet

**Ethernet** is a widely used networking technology operating at the Data Link layer, with Ethernet standards also specifying physical-layer technologies.

An Ethernet frame contains structured information used in local-link communication.

A simplified Ethernet frame includes:

| Component | Purpose |
|---|---|
| Destination MAC address | Identifies the intended link-layer destination |
| Source MAC address | Identifies the sending network interface |
| Payload | Carries higher-layer data, often an IP packet |
| Frame Check Sequence (FCS) | Supports error detection |

Other framing fields exist; this is a simplified representation.

### MAC addresses

A **Media Access Control (MAC) address** is a link-layer address associated with a network interface.

A traditional Ethernet MAC address is 48 bits and is commonly represented as six pairs of hexadecimal digits.

Example:

`00:1A:2B:3C:4D:5E`

Each hexadecimal digit represents four binary bits.

6 pairs × 2 digits × 4 bits = 48 bits.

MAC addresses are not inherently hierarchical according to network location.

### Switches and forwarding tables

An Ethernet switch learns associations between source MAC addresses and its ports.

Its forwarding table allows it to determine which port should receive frames addressed to known destinations.

If a destination address is unknown, an Ethernet switch ordinarily floods the frame through eligible ports in the same VLAN, except the incoming port.

A switch does not need to interpret the HTTP request inside an Ethernet frame.

**Governing principle:** Link-layer communication concerns delivery across a local link, not determining an entire route through the Internet.

---

## 7. The Internet/Network Layer

The Internet layer provides IP addressing and packet forwarding between different networks.

### IP addressing

An **IP address** is a logical address assigned to a network interface.

Unlike a hardware MAC address, an IP address reflects an interface's logical position within an IP network and can change when its network attachment changes.

IP addressing supports hierarchical organization.

### Hierarchical addressing

IP addresses can be grouped using network prefixes.

Routers can maintain forwarding information about address ranges rather than individual entries for every device on the Internet.

Example:

`192.168.2.0/24`

The `/24` means that the first 24 bits identify the network prefix.

A router with an appropriate route for this prefix can forward traffic destined for addresses such as `192.168.2.75` without requiring a dedicated entry for that individual address.

Routers select the most specific matching prefix using **longest-prefix matching**.

**Governing principle:** Hierarchical IP addressing makes large-scale routing manageable.

Unlike postal ZIP codes, IP prefixes represent logical network organization rather than fixed geographic locations.

### Local versus remote delivery

When a host sends data:

1. It constructs an IP packet with source and destination addresses.
2. It determines whether the destination is reachable on its local network.
3. For a remote destination, it sends the packet toward an appropriate router.
4. Routers forward the packet toward the destination network.
5. On the final local link, link-layer addressing supports delivery to the destination interface.

The final router may use a protocol such as ARP (IPv4) or Neighbor Discovery (IPv6) to determine the appropriate local-link address.

### Routing versus forwarding

**Routing:** Determines network reachability and paths.

**Forwarding:** Uses forwarding information to send an individual packet toward its next hop.

Routing establishes the information used for forwarding; forwarding applies that information to packets.

### IP addressing versus subnetting

**IP addressing** provides logical addresses for interfaces on IP networks.

**Subnetting** divides an IP address space into smaller logical networks by using longer network prefixes.

Subnetting does not replace IP addressing. It organizes address space within it.

Example:

`192.168.1.0/24`

Can be divided into:

- `192.168.1.0/25`
- `192.168.1.128/25`

Each `/25` range contains 128 IPv4 addresses.

### IP addresses and uniqueness

An IP address identifies a network interface within a particular addressing scope.

Publicly routable IP addresses must be globally unique within ordinary Internet routing.

Private IP addresses can be reused independently across different private networks.

For example, many home networks can simultaneously contain a device using:

`192.168.1.42`

Private addresses are not directly routed across the public Internet. Network Address Translation (NAT) commonly allows private-network devices to communicate externally through public addressing.

A device may have multiple IP addresses, and addresses can change when the device moves between networks.

---

## 8. IPv4 and IPv6

### IPv4

IPv4 uses **32-bit addresses**, commonly represented as four decimal octets separated by periods.

Example:

`192.168.1.42`

Each octet contains eight bits.

4 × 8 = 32 bits.

IPv4 provides approximately 4.3 billion possible address values, although not all are available for ordinary public host addressing.

### IPv6

IPv6 uses **128-bit addresses**.

In fully expanded notation, an IPv6 address contains eight groups of four hexadecimal digits, separated by colons.

Example:

`2001:0db8:0000:0000:0000:0000:0000:0001`

Each group represents 16 bits.

8 × 16 = 128 bits.

IPv6 allows compressed notation:

`2001:db8::1`

In a common IPv6 `/64` subnet arrangement:

- First 64 bits: Network prefix
- Last 64 bits: Interface identifier

This 64/64 division is common, not a universal requirement for every IPv6 address or allocation.

IPv6 provides an enormously larger address space than IPv4 and introduces changes to packet header design.

### Address representation comparison

| Address type | Size | Representation |
|---|---|---|
| MAC (typical Ethernet) | 48 bits | 6 pairs of hexadecimal digits |
| IPv4 | 32 bits | 4 decimal octets |
| IPv6 | 128 bits | 8 groups of 16 bits in expanded hexadecimal notation |

---

## 9. Critical Distinctions — Quiz Review

**Encapsulation vs. Decapsulation**

Encapsulation moves downward through the protocol stack. The PDU from a higher layer becomes the payload of the layer below.

Decapsulation moves upward as receiving layers process protocol information and pass payloads toward the application.

**Ethernet vs. TCP**

Ethernet operates at the Link/Data Link layer (with associated physical-layer specifications).

TCP operates at the Transport layer.

**MAC vs. IP**

MAC addressing supports local-link communication.

IP addressing supports logical addressing and forwarding between networks.

**IP addressing vs. Subnetting**

Subnetting organizes IP address ranges. It is not an alternative to IP addressing.

**IPv6 vs. MAC notation**

IPv6: Eight groups of up to four hexadecimal digits in fully expanded form.

Traditional Ethernet MAC: Six groups of two hexadecimal digits.

**Protocol cooperation**

A single network communication can involve multiple protocols at different layers. Protocols are not necessarily mutually exclusive alternatives.

**IP uniqueness**

IP addresses are unique within their relevant addressing scope, but private IP address values can be reused on independent networks.

**Bandwidth vs. Latency**

Bandwidth measures capacity. Latency measures delay. Improving one does not automatically eliminate limitations imposed by the other.

---

## 10. Final Mental Model

The Internet connects independent networks using shared protocols and hierarchical addressing.

Communication involves several distinct responsibilities:

**Sender → Protocols → Representation → Transmission → Forwarding → Receiver**

At the sending host, application data is encapsulated through successive protocol layers. Network hardware encodes that information as physical signals.

Intermediate networking devices interpret the information needed for their own forwarding responsibilities.

At the destination, the receiving system processes the appropriate protocol layers and delivers the recovered application data.

The entire process depends on agreed rules, distributed forwarding information, physical infrastructure, and the separation of responsibilities across layers.

### Seven questions for tracing network communication

1. **Where am I?** Which device, network, and protocol layer am I examining?
2. **Who owns this state?** Which device or protocol maintains the relevant information?
3. **Who initiates the next action?** What event triggers transmission or processing?
4. **What crosses the boundary?** Which PDU, frame, packet, or physical signal is involved?
5. **What survives?** Which information is preserved, transformed, removed, or replaced?
6. **What determines the next transition?** Which protocol rule, address, or forwarding decision governs the next step?
7. **When does the process stop?** What condition constitutes successful delivery, termination, or failure?

**Central principle of Lesson 1:** The Internet works because independent systems coordinate through standardized protocols, hierarchical addressing, layered responsibilities, and distributed forwarding decisions—without requiring shared memory or a single controller for the entire network.

# LS170 — Lesson 2: The Transport Layer
## Notes 1: Process Communication, Ports, and Sockets

### 1. The Purpose of the Transport Layer

The Internet Protocol (IP) provides host-to-host communication, allowing data to travel from one computer to another. However, multiple applications or processes may be communicating over the network simultaneously on the same host. Delivering data to the correct computer is therefore insufficient: the operating system must also determine which application should receive it. The transport layer provides **process-to-process communication**, using port numbers to identify communication endpoints. It can also provide additional services, such as reliable delivery, depending on the transport protocol.

**Central distinction:** IP addresses identify network interfaces associated with hosts; port numbers identify communication endpoints within those hosts.

### 2. Ports, Multiplexing, and Demultiplexing

A **port number** is a 16-bit identifier used by transport protocols to distinguish communication endpoints. A host can support numerous simultaneous network communications because different applications and connections can be associated with different ports.

**Multiplexing** occurs on the sending side, where data from multiple application communications is passed through the transport layer for transmission. **Demultiplexing** occurs on the receiving side, where the operating system uses transport-layer information to deliver incoming data to the appropriate socket.

For example, a browser might use local port `53001` to communicate with a web server on remote port `443`. For incoming data returning to the browser, the source port is `443` and the destination port is `53001`.

### 3. TCP Connections and the Four-Tuple

A TCP connection is identified by a combination of four values, commonly called a **four-tuple**:

- Source IP address
- Source port number
- Destination IP address
- Destination port number

This is important because multiple clients can connect to the same server IP address and port simultaneously. The server does not require a different listening port for each client. Instead, the unique combination of endpoint addresses and ports distinguishes the established TCP connections.

For example, two clients may connect to server `203.0.113.50:443`, while using different source addresses or source ports. Both connections share the same server endpoint but have distinct four-tuples.

### 4. Listening Sockets and Connected Sockets

A **socket** is an operating-system-managed communication endpoint exposed to applications through a socket API.

A server begins by requesting a socket, binding it to a local address and port, and putting it into a listening state. The listening socket makes the server available for incoming TCP connection requests but does not itself represent an individual established client conversation.

When a client initiates a connection, the client and server operating systems perform TCP's three-way handshake:

**SYN → SYN-ACK → ACK**

During this exchange, the operating systems establish and maintain connection-specific state. Once the connection is established, it can wait in the server's queue of completed connections until the application accepts it.

The server application calls `accept()` on the listening socket. This operation returns a **new connected socket**, which the application uses to communicate with that particular client. The original listening socket remains available for additional connections.

Consequently, one server can simultaneously maintain a listening socket and multiple connected sockets, all sharing the same local port but representing different TCP connections.

### 5. State Ownership and Runtime Boundaries

The **application** maintains references to socket objects and uses socket API operations to request communication.

The **operating system** manages the underlying sockets, TCP connection states, send and receive buffers, and connection queues.

The **TCP segments** carry addressing information, control information, and potentially application data. They do not themselves store the entire ongoing connection state.

Ordinary IP routers forward packets toward their destinations; they do not maintain the endpoints' TCP connection state.

An established TCP connection is not a reserved physical route through the network. It is a logical relationship supported by state maintained at the two endpoints. Individual packets may still follow different network paths.

### 6. Runtime Sequence: Establishing a Server Connection

1. **Socket creation:** The server application asks its OS to create a socket.
2. **Binding:** The application associates the socket with a local address and port.
3. **Listening:** The socket becomes available to accept incoming TCP connection requests.
4. **Client initiation:** A remote client requests a connection.
5. **TCP handshake:** The endpoint operating systems establish the connection and its state.
6. **Acceptance:** The server application calls `accept()` and obtains a connected socket for that client.
7. **Communication:** The application reads and writes data through the connected socket, while the OS manages the TCP protocol.

The operating system can complete the TCP handshake and buffer incoming data before the server application calls `accept()`.

### Governing Principles

**Host delivery is not process delivery.** The transport layer provides the additional mechanism needed to direct data to the correct communication endpoint.

**A listening socket is not an established connection.** It provides the entry point through which new connections can be accepted.

**A shared local port does not imply shared connection state.** TCP distinguishes simultaneous connections by their complete four-tuples.

**Protocol execution is distinct from application execution.** The operating system can establish and maintain TCP connections independently of when the application chooses to interact with them.

# LS170 — Lesson 2: The Transport Layer
## Notes 2: Network Reliability

### 1. Reliability Is Engineered

The underlying network is inherently unreliable. IP packets can be lost, corrupted, or delivered out of order. IP itself does not guarantee recovery from these failures.

A reliable transport protocol must therefore establish additional rules to detect missing or duplicate data, recover from losses, and provide ordered delivery.

**Governing principle:** Reliability is not an inherent property of transmission. It emerges from coordinated behavior between sender and receiver.

### 2. Building a Reliable Protocol

Launch School develops a simplified protocol incrementally, introducing mechanisms as problems arise.

**Version 1 — Acknowledgments (ACKs)**

The sender transmits one message and waits for acknowledgment before proceeding. The receiver sends an ACK when it successfully receives the message.

Problem: If either the message or its acknowledgment disappears, the sender can wait indefinitely.

**Version 2 — Timeouts and Retransmission**

The sender starts a timer when transmitting. If no acknowledgment arrives before the timeout expires, it retransmits the message.

Problem: An acknowledgment might be lost even though the receiver successfully received the original message. Retransmission can therefore create duplicates.

**Version 3 — Sequence Numbers**

Messages receive identifiers called sequence numbers. The receiver can recognize retransmitted messages and discard duplicates while acknowledging their receipt.

Together, acknowledgment, timeout, retransmission, and sequence-number mechanisms address the fundamental problems of reliable data delivery.

### 3. Sender and Receiver State

Reliability requires state at both endpoints.

**Sender state:** Tracks transmitted but unacknowledged data, retains copies for possible retransmission, maintains sequence-number information, and manages retransmission timers.

**Receiver state:** Tracks received data and sequence numbers, detects duplicates or missing data, and generates acknowledgments.

The protocol's next action depends on events such as receiving data, receiving an acknowledgment, or a timeout expiring.

A timeout does not prove that data was lost. It establishes that confirmation has not arrived within the expected interval.

**Timeout trade-off:** A timeout that is too short causes unnecessary retransmissions and network traffic; one that is too long delays recovery from genuine loss. TCP uses network timing measurements to adapt its retransmission timeout.

### 4. Stop-and-Wait Versus Pipelining

**Stop-and-wait** allows only one outstanding message at a time. Although straightforward, it wastes transmission capacity while the sender waits for acknowledgments, particularly when round-trip time is large.

**Pipelining** permits multiple transmissions before their acknowledgments arrive. This improves throughput but requires tracking several outstanding messages simultaneously.

A **sliding window** limits how much unacknowledged data may be in flight. As acknowledgments arrive, the window advances, permitting further transmission.

Launch School introduces Go-Back-N and Selective Repeat as two approaches to pipelined reliable delivery.

### 5. TCP Byte Sequencing and Cumulative Acknowledgments

Our discussion extended the simplified message-based protocol to TCP's actual byte-stream model.

TCP sequence numbers identify positions in a stream of bytes, rather than numbering whole application messages.

A **cumulative ACK** identifies the next byte expected in sequence.

Example:

- Bytes 0–99 received.
- Bytes 100–199 missing.
- Bytes 200–299 received out of order.

The cumulative ACK remains **100**, because that is the earliest missing byte.

If bytes 100–199 subsequently arrive, the ACK can advance directly to **300**, because bytes through 299 are now present in a continuous sequence.

Receiving later bytes does not mean the receiver can expose them to the application before the missing earlier bytes have arrived. TCP may buffer out-of-order bytes until the gap is resolved.

### 6. Transport Reliability Versus Application Success

A TCP acknowledgment establishes receipt at the transport layer, not completion of the receiving application's work.

For example, an order may reach a restaurant server's TCP receive buffer and be acknowledged, but the server could crash before the kitchen processes it.

TCP retransmission and application-level retries are therefore different problems. TCP recognizes duplicate bytes within a connection; the application must recognize duplicate logical operations, such as submitting the same order twice.

**Governing distinction:** Successful delivery of bytes does not guarantee successful processing of their meaning.

### 7. The Central Trade-Off

Reliable delivery introduces additional state, buffering, acknowledgments, timers, retransmissions, and potential latency. Pipelining improves efficiency, but makes state management more complex.

The engineering challenge is to deliver data reliably while making efficient use of network capacity.

**Core model:**

SEND → RETAIN → WAIT FOR ACK

- ACK received → mark data acknowledged and advance.
- Timeout → retransmit unacknowledged data.
- Duplicate received → recognize and discard duplicate data.
- Window capacity available → permit additional transmission.

# LS170 — Lesson 2: The Transport Layer
## Notes 3: TCP — Connection Establishment, Flow Control & Congestion Control

### 1. Transmission Control Protocol (TCP)

TCP is a **connection-oriented, reliable, full-duplex transport protocol**. It provides applications with an ordered stream of bytes, despite operating over an IP network that does not guarantee delivery or ordering.

TCP implements many of the reliability mechanisms introduced in 02_03, including sequence numbers, acknowledgments, retransmission, timeouts, and sliding windows.

**Connection-oriented** means that the endpoints establish a logical connection and maintain connection-specific state before ordinary data exchange.

**Full-duplex** means both endpoints can transmit and receive data simultaneously. Each direction has independent sequence numbers and acknowledgment tracking.

### 2. TCP Segments

TCP transmits data in units called **segments**, consisting of a TCP header and a payload.

Important TCP header fields include:

| Field | Purpose |
|---|---|
| Source / destination ports | Identify communication endpoints |
| Sequence number | Identifies the position of data in the byte stream |
| Acknowledgment number | Identifies the next expected byte from the other endpoint |
| Control flags | Indicate protocol actions such as SYN, ACK, and FIN |
| Window size | Advertises receiving capacity |
| Checksum | Detects corruption of the TCP segment |

These fields provide the information needed to identify connections, track transmitted data, manage reliability, and coordinate communication between endpoints.

### 3. TCP Connection Establishment: Three-Way Handshake

Before ordinary data communication, TCP establishes a connection through a **three-way handshake**:

**SYN → SYN-ACK → ACK**

1. **Client sends SYN:** The client initiates connection establishment and communicates its initial sequence number. Its state becomes `SYN-SENT`.
2. **Server sends SYN-ACK:** The server acknowledges the client's SYN and communicates its own initial sequence number. Its state becomes `SYN-RECEIVED`.
3. **Client sends ACK:** The client acknowledges the server's SYN. The client enters `ESTABLISHED`; the server enters `ESTABLISHED` upon receiving the final ACK.

The server's SYN-ACK performs two functions: acknowledging the client's initiation and establishing the server's own sequence-number space. It does not initiate a second TCP connection.

**Governing principle:** One TCP connection contains two independently numbered directions of communication.

### 4. Connection State Is Distributed

Each endpoint's operating system independently maintains its own TCP connection state.

The two endpoints therefore do not necessarily transition between states simultaneously.

For example, suppose the client's final ACK is lost:

- The client has sent its ACK and entered `ESTABLISHED`.
- The server has not received the ACK and remains in `SYN-RECEIVED`.
- The server can retransmit its SYN-ACK after a timeout.
- The client can acknowledge the retransmitted SYN-ACK, allowing the server to enter `ESTABLISHED`.

The server can also complete establishment when it receives a suitable acknowledgment accompanying subsequent client data.

**Important distinction:** A TCP connection is not a dedicated physical route. It is a logical communication relationship maintained through state at the endpoints. Routers forward IP packets without maintaining the endpoints' TCP connection states.

The next state transition is determined by incoming TCP segments, application operations, and timer events.

### 5. Flow Control: Protecting the Receiver

**Flow control prevents a fast sender from overwhelming a slower receiver.**

Incoming data is temporarily held in the receiving operating system's **receive buffer** until the application consumes it through operations such as `recv()`.

Because buffer capacity is finite, the receiver must communicate how much additional data it can accommodate.

TCP uses an advertised **receive window (`rwnd`)** for this purpose.

The fundamental sequence is:

1. The sender transmits data.
2. The receiver's OS places incoming bytes in its receive buffer.
3. Available buffer capacity decreases.
4. The receiver advertises its available capacity to the sender.
5. The receiving application calls `recv()`, consuming buffered bytes.
6. Buffer space becomes available again, allowing the receiver to advertise a larger window.

The sending TCP implementation uses the advertised window to limit outstanding data.

If the receiver advertises a **zero window**, the sender stops transmitting additional ordinary data until capacity becomes available.

#### Zero-Window Recovery

A problem can arise if the receiver frees buffer space but its updated window advertisement is lost.

The sender still believes that the receive window is zero, although the receiver now has capacity.

TCP addresses this situation through a **persist timer** and zero-window probes, allowing the sender to solicit updated information rather than waiting indefinitely.

**Governing principle:** Flow control depends on the receiver communicating its available capacity, not merely possessing that capacity.

### 6. Congestion Control: Protecting the Network

Flow control addresses the receiving host's limitations, but the network itself also has finite capacity.

Routers and network links can become congested when traffic arrives faster than it can be forwarded. Congestion can produce queueing delays and packet loss.

**Congestion control regulates the sender's transmission behavior in response to network conditions.**

TCP maintains a **congestion window (`cwnd`)**, which constrains the amount of outstanding data permitted by its congestion-control algorithm.

Unlike the receive window, which reflects the receiver's available capacity, the congestion window reflects the sender's assessment of network conditions.

| Flow Control | Congestion Control |
|---|---|
| Protects the receiver | Protects the network |
| Concerned with receive-buffer capacity | Concerned with network capacity and congestion |
| Uses advertised receive window (`rwnd`) | Uses congestion window (`cwnd`) |
| Receiver communicates available capacity | Sender adjusts its behavior based on congestion signals |

TCP must respect both limitations. In simplified terms, its permitted outstanding data is constrained by:

**Effective window = min(rwnd, cwnd)**

A large receive window does not solve network congestion. Likewise, an uncongested network cannot compensate for a receiver whose buffer is full.

### 7. Runtime and State Ownership

**Application layer:** Produces and consumes meaningful data. The receiving application initiates reads through the socket API.

**Sender OS:** Maintains transmitted and unacknowledged data, TCP sequence numbers, retransmission timers, connection state, and congestion-control state.

**Receiver OS:** Maintains connection state, received data, receive-buffer capacity, acknowledgment information, and the advertised receive window.

**Network:** Carries packets between endpoints. It may introduce loss, delays, reordering, or congestion.

No single participant possesses complete information about the entire system. TCP coordinates endpoint behavior by exchanging control information and reacting to events.

### 8. Consolidated Principles

**Connection establishment:** TCP uses a handshake to establish endpoint state and synchronize sequence-number information.

**Reliability:** Sequence numbers, acknowledgments, buffering, timers, and retransmission allow TCP to recover from unreliable delivery.

**Flow control:** The sender must not exceed the receiving endpoint's advertised capacity.

**Congestion control:** The sender must also account for limitations in the intervening network.

**State ownership:** TCP connection state exists at the endpoints, and each endpoint updates its own state independently.

**Overall model:**

APPLICATION WRITES → TCP MANAGES TRANSMISSION → NETWORK CARRIES PACKETS → RECEIVING TCP BUFFERS DATA → APPLICATION READS

TCP manages the mechanics of reliable, ordered byte delivery. The applications remain responsible for interpreting and processing the data.

# LS170 — Lesson 2: Transport Layer
## Expanded Study Notes — November 6, 2026

### 1. The governing transport-layer model

The network layer, through IP, provides communication between hosts. The transport layer extends that service to communication between processes.

**Application → Transport → IP → Network → IP → Transport → Application**

The application produces or consumes meaningful data. The transport protocol defines how data is represented and delivered between application endpoints.

Transport-layer port numbers support process-to-process communication. The operating system uses sockets to expose transport services to applications.

The two principal transport protocols studied in this lesson are:

- **TCP:** Connection-oriented, reliable, ordered byte-stream service.
- **UDP:** Connectionless, best-effort datagram service.

The fundamental design difference is which responsibilities the transport protocol assumes and which remain with the application.

---

### 2. TCP connection termination

TCP is full-duplex: the two endpoints can send data independently in both directions.

Therefore, closing one direction does not automatically mean the other direction must close at the same instant.

A typical graceful termination involves:

1. Endpoint A sends `FIN`, indicating that it has finished sending application data.
2. Endpoint B acknowledges with `ACK`.
3. B may continue sending its remaining data.
4. B eventually sends its own `FIN`.
5. A acknowledges B's `FIN`.

**Half-close:** One endpoint has finished sending but can still receive data from the other endpoint.

**TIME-WAIT:** After the active closer acknowledges the other endpoint's FIN, it ordinarily remains in TIME-WAIT for a period rather than immediately discarding all connection-related state.

This helps the endpoint acknowledge a retransmitted FIN if the final ACK was lost and allows delayed packets from the old connection to expire.

**State transition principle:** A connection does not become fully finished merely because one application has stopped sending. TCP must manage both directions and complete the termination protocol.

---

### 3. Where TCP lives and who owns the state

TCP is ordinarily implemented within the operating system's networking stack.

The application interacts with TCP through the socket API. The kernel maintains the transport state required to manage communication.

**Application responsibilities:**
- Produce the data to send.
- Read received data.
- Decide what the data means.
- Determine whether an application operation succeeded.

**TCP implementation responsibilities:**
- Maintain connection state.
- Track sequence and acknowledgment numbers.
- Manage send and receive buffers.
- Retransmit unacknowledged data when appropriate.
- Maintain timers.
- Implement flow control and congestion control.

A TCP connection can be established but idle. TCP does not invent application data or transmit additional data merely because window capacity is available.

**Governing rule:** The application decides what to communicate. TCP manages the transport behavior.

---

### 4. Outstanding data

**Outstanding data** consists of bytes transmitted by TCP but not yet acknowledged.

It includes data that may already have arrived at the receiver but whose acknowledgment has not yet reached the sender.

Outstanding data is different from unsent application data waiting in the sender's buffer.

Example:

- Application supplies 10,000 bytes.
- TCP transmits 3,000 bytes.
- No acknowledgments have arrived yet.
- 3,000 bytes are outstanding.
- 7,000 bytes remain unsent.

When acknowledgments arrive, the sender can advance its understanding of which bytes have been received and free the corresponding outstanding-data allowance.

---

### 5. Flow control versus congestion control

These mechanisms regulate transmission for different reasons.

| | Flow control | Congestion control |
|---|---|---|
| Main concern | Receiving host capacity | Network congestion |
| Window | `rwnd` | `cwnd` |
| Information source | Receiver | Sender's network observations |
| Immediate purpose | Avoid overflowing the receiving TCP buffer | Avoid excessive outstanding traffic in the network |

**Receive window (`rwnd`)**

The receiving TCP implementation advertises how much additional data it can accept.

If the receiving application is slow to consume data, its operating system's receive buffer can fill, shrinking the advertised receive window.

When the application reads buffered data, capacity may become available again.

**Congestion window (`cwnd`)**

The sender's TCP implementation maintains a congestion window based on congestion-control feedback.

It reflects the sender's current transmission allowance, not a direct measurement of the path's total capacity.

**Effective outstanding-data limit ≈ `min(rwnd, cwnd)`.**

This is a limit on permission, not an instruction to transmit. TCP must also have data available to send.

---

### 6. Slow start and congestion avoidance

TCP cannot assume that the network can safely accommodate unlimited outstanding data.

It therefore needs a method for probing usable capacity and responding to feedback.

**Slow start** begins with a limited congestion window and increases the permitted outstanding data rapidly as acknowledgments arrive.

In a simplified example, the window may approximately double over successive round-trip times:

`1 → 2 → 4 → 8 → 16`

The numbers are illustrative; actual implementations and initial window sizes vary.

As TCP moves into **congestion avoidance**, growth becomes more cautious.

When a congestion-control algorithm detects congestion, it may reduce the sender's congestion window.

#### Temporal ordering

1. Application data is available.
2. TCP checks its current sending allowance.
3. TCP transmits permitted data.
4. Feedback arrives, or congestion is inferred.
5. TCP updates its congestion-control state.
6. The updated allowance constrains subsequent transmission.

**A window reduction cannot recall bytes already transmitted.** It restricts new transmissions until sufficient capacity becomes available.

The application data still awaiting transmission generally remains buffered.

The essential feedback loop is:

**Transmit → Observe feedback → Update state → Adjust future transmission.**

---

### 7. TCP's costs and limitations

TCP's services require additional machinery.

**Connection-establishment latency:** A three-way handshake establishes the connection before the ordinary TCP data exchange.

**State and processing overhead:** TCP must track acknowledgments, sequence numbers, windows, buffers, and retransmission timers.

**Head-of-line blocking:** TCP provides an ordered byte stream. If an earlier range of bytes is missing, TCP cannot deliver later bytes ahead of that missing range to the application, even when those later bytes have already arrived.

This is not an accidental weakness. It follows from the ordered-delivery guarantee TCP promises.

**Design principle:** Reliability and ordering provide important benefits, but they introduce constraints and costs.

---

### 8. UDP — User Datagram Protocol

UDP provides connectionless, best-effort, process-to-process communication.

Unlike TCP, it does not establish a transport connection through a handshake before sending application data.

UDP provides:

- Source and destination port numbers.
- Datagram length information.
- A checksum for error detection.
- Preservation of individual datagram boundaries.

UDP does **not** provide:

- Guaranteed delivery.
- Guaranteed ordering.
- Automatic retransmission of lost datagrams.
- TCP-style acknowledgment and sliding-window mechanisms.
- Built-in TCP-like congestion control.

A datagram can be lost, duplicated, or delivered out of order. UDP does not automatically repair these conditions.

The receiving operating system still maintains sockets and buffers. *Connectionless* does not mean that no local operating-system state exists.

#### UDP runtime

1. An application supplies a message and destination.
2. UDP adds its header to form a datagram.
3. IP attempts delivery to the destination host.
4. If the datagram arrives and is accepted, UDP identifies the appropriate receiving socket.
5. The application reads and interprets the message.

No TCP-style acknowledgment or connection-state transition is required between datagram transmissions.

---

### 9. Byte streams versus datagrams

**TCP is byte-stream-oriented.**

If an application makes two writes:

`HELLO`

`WORLD`

The receiver observes an ordered stream of bytes containing `HELLOWORLD`, but its read operations need not correspond to the two original writes.

The application must define its own message boundaries when necessary.

**UDP is datagram-oriented.**

Each datagram is a separate message. If both datagrams arrive and are read with adequate buffers, the application can receive `HELLO` and `WORLD` as distinct messages.

However, UDP does not guarantee that both arrive or that `HELLO` arrives first.

This is a difference in the representation presented to the application, not just a difference in reliability.

---

### 10. Selective reliability and application design

UDP permits applications to determine which messages deserve additional protection.

Consider a multiplayer game:

**Position updates**

A newer position may make an older position obsolete. If an intermediate update is lost, the receiving application might continue using the latest valid position.

Sequence numbers or timestamps can help identify stale data. Interpolation can estimate missing intermediate movement.

**Inventory changes**

A rare item, currency transfer, or earned reward cannot necessarily be discarded simply because a later message arrives.

The application may require confirmation, retries, unique transaction identifiers, and durable storage.

**Dependent events**

An attack may depend on the player's position or another aspect of game state.

UDP does not know the semantic relationship between these messages. The application must decide whether to accept the attack, reject it, or evaluate it against previously maintained state.

Thus:

**Transport-layer knowledge:** Ports, datagrams, length, integrity information.

**Application-layer knowledge:** Players, inventory, movement, attacks, rules, and dependencies.

UDP does not eliminate the need for reliability mechanisms when an application requires them. It allows the application to implement those mechanisms selectively.

Applications using UDP must also consider congestion and responsible sending behavior.

---

### 11. Transport reliability versus successful application operations

A major boundary distinction emerged from the game-progress example.

There are at least three different events:

**1. Network delivery**

Did the necessary bytes or datagram reach the destination transport implementation?

TCP provides reliable, ordered byte delivery while the connection operates successfully.

**2. Application processing**

Did the server application receive, validate, and successfully apply the requested change?

A TCP acknowledgment alone cannot establish this.

**3. Durable persistence**

Did the server save the resulting change so it would survive a crash, restart, or recovery?

Neither TCP nor UDP guarantees this.

A server might receive a reward event and modify an in-memory inventory, then crash before saving it.

If the client does not receive application-level confirmation, the outcome may be uncertain. A retry could be appropriate, but repeating an operation carelessly could duplicate its effects.

An application can use unique operation identifiers and idempotent handling to manage retries safely.

**TCP retransmission timeout:** Concerns missing transport acknowledgments.

**Application timeout:** Concerns missing confirmation of an application operation.

These timeouts operate at different boundaries and address different uncertainties.

**Governing rule:** Reliable transmission is not equivalent to reliable processing or durable storage.

---

### 12. Final TCP/UDP comparison

| Property | TCP | UDP |
|---|---|---|
| Connection model | Connection-oriented | Connectionless |
| Data abstraction | Ordered byte stream | Individual datagrams |
| Delivery guarantee | Reliable while successfully operating | Best effort |
| Ordering | Guaranteed | Not guaranteed |
| Retransmission | Built in | Not built in |
| Flow control | Built in | Not built in |
| Congestion control | Built in | Not built in |
| Handshake | Yes | No |
| Typical design motivation | Completeness and ordered delivery | Simplicity, timeliness, application control |

Neither protocol is universally better.

The choice depends on what the application needs, what failures it can tolerate, and which guarantees are appropriate at the transport boundary.

## Final systems model

**Sender → Protocol → Representation → Transmission → Receiver**

For every networking interaction, identify:

- **State:** What must be remembered, and where does it live?
- **Ownership:** Which layer or participant is responsible?
- **Initiation:** Who starts the action?
- **Boundary:** What information crosses from one layer to another?
- **Transition:** What event determines the next action?
- **Guarantee:** What does this layer actually promise?
- **Failure:** What happens when that promise is insufficient?

The enduring lesson is not simply that TCP is reliable and UDP is unreliable.

It is that **networking systems divide responsibilities across layers**, and each layer's guarantees have a defined scope.

Understanding those boundaries makes it possible to reason about performance, protocol design, failures, and eventually security.


# LS170 Lesson 3 · Introduction to HTTP

**Study status:** First-pass teaching, hands-on investigations, Launch School quiz and debrief, and a guided end-to-end walkthrough completed. Formal lesson closure is pending. Independent recall and transfer still need verification.

## Sources and scope

- **Launch School primary material.** The course reading anchors the application-layer model, clients and servers, resources, URLs, requests and responses, stateful applications, and Web security. The book's Preparations chapter introduces GUI and command-line tools. Its request, response, state, and security chapters cover GET and POST, headers and status codes, sessions, cookies, AJAX, HTTPS, same-origin policy, introductory CORS, session hijacking, and XSS. The seven lesson screenshots are referenced in the recovered transcript, whose attachment entries omit the image contents. Exact assignment numbering and complete question-box coverage remain unverified. [Launch School course outline](https://d24f1whwu8r3u4.cloudfront.net/curriculum/courses/8cb220e7) · [Launch School's Introduction to HTTP](https://launchschool.com/books/http/read/introduction)
- **Supplementary explanations.** HTTP/1.1 framing, safe and idempotent semantics, cache validation, the TLS 1.3 handshake, CORS preflight and credentials, CSRF, and the runtime graphs below expand the lesson model. References appear with the relevant sections.
- **Observed experiments.** The evidence section records what the learner reported in the lesson chat. It contains selected fields and outcomes from that run. The bookstore, email-server mismatch, and attack scenarios are hypothetical. [Lesson 3 study conversation](chatgpt-conversation://6aedec17-363c-83ed-bff0-43e4777f5167)

## 1. Application layer, Internet, and Web

The **Internet** is a network of interconnected networks. IP addresses and routes packets across it. TCP provides a reliable, ordered byte stream between endpoints. The **Web** is a system of linked resources and applications commonly accessed with HTTP or HTTPS. Email using SMTP and file transfer using FTP are examples of other services that can use the Internet. A webmail interface can use HTTPS between browser and provider while the provider uses email protocols elsewhere.

An **application** is software such as a browser or mail server. An **application-layer protocol** defines how communicating peers represent messages and interpret them. HTTP specifies what a request asks for and how a response reports the result. In the lesson's hypothetical protocol mismatch, TCP could successfully deliver HTTP bytes to an SMTP listener, and the listener could still reject them because it expects SMTP commands. Delivery and interpretation are separate outcomes.

A **client** initiates an HTTP exchange and a **server** handles it. These are roles for an exchange. A reverse proxy can receive a request as a server and act as a client to an upstream service. “Server” can refer to a host, a process listening for connections, or the logical service. A reverse proxy or web server can terminate TLS, serve static resources, or forward requests. An application can route requests and apply business rules. A data store can persist records. One program can perform several of these roles.

A **resource** is the thing identified by a URI, such as a book, an order collection, or an image. A **representation** is the data and metadata that describe a resource in a given exchange. A resource can have HTML and JSON representations. The application can generate a representation dynamically from a route and database query, so a path can identify a resource without corresponding to a file. [Launch School HTTP book](https://launchschool.com/books/http/read/introduction) · [RFC 9110, HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)

## 2. URL anatomy and encoding

A URI identifies a resource. A URL is an identifier that also describes how to locate or access it. For the illustrative URL `https://bookstore.example:8443/books/42?format=hardback&sort=recent#reviews`:

| Component | Example | Role |
| --- | --- | --- |
| Scheme | `https` | Selects the access scheme |
| Hostname | `bookstore.example` | Identifies the host in the authority |
| Port | `8443` | Explicit connection port. Defaults are 443 for HTTPS and 80 for HTTP |
| Path | `/books/42` | Identifies a resource within the origin. A router might extract `42` as a path parameter |
| Query | `format=hardback&sort=recent` | The component after `?` and before `#`. Here it contains two query parameters |
| Fragment | `reviews` | Client-side reference, commonly to a document section. The browser omits it from the HTTP request target |

The **query string** is the whole query component. **Query parameters** are the entries an application parses from it. `name=value&name=value` is a common convention, and repeated names are possible. “Parameters” can also refer to values extracted from a route or body. For the quiz question about passing application input in the URL, the intended pair was **path and query parameters**. Scheme, host, and port govern access and can also influence routing.

A browser gets a URL from an address, link, form action, script, redirect, or resource reference. It resolves relative references against the document's base URL. For example, a root-relative `/books/42` on `https://bookstore.example/shop/` resolves to `https://bookstore.example/books/42`.

**Percent-encoding** represents a byte as `%HH`. Under UTF-8, `é` can be encoded as `%C3%A9`. Encode data within the component it belongs to so a literal delimiter stays data. `Cats & Dogs` can appear as `?q=Cats%20%26%20Dogs`. Under `application/x-www-form-urlencoded` parsing, `?q=Cats+%26+Dogs` decodes to the same value. That convention serializes spaces as `+`, also accepts `%20` on decoding, and uses `%2B` for a literal plus. A plus in a URL path stays a plus under ordinary percent-decoding. For example, `new URLSearchParams({q: 'C++ & Rust'}).toString()` produces `q=C%2B%2B+%26+Rust`.

Percent-encoding preserves structure. HTTPS encrypts the path, query, headers, and body between TLS endpoints. URLs can still surface in history, logs, and sometimes referrer data. Request bodies can also appear in application or diagnostic logs. [WHATWG URL Standard](https://url.spec.whatwg.org/) · [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)

## 3. HTTP/1.1 messages

A request starts with `METHOD request-target HTTP-version`. A response starts with the version, a three-digit status code, and an optional reason phrase. Field lines follow as `Name: value`. Field names are case-insensitive. HTTP/1.1 uses CRLF line endings, and an empty line ends the header section. Message framing determines whether a body follows and how long it is. The following display is illustrative.

```http
POST /orders HTTP/1.1
Host: bookstore.example
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Content-Length: 10

book_id=42
```

```http
HTTP/1.1 201 Created
Location: /orders/105
Content-Type: application/json
Content-Length: 16

{"order_id":105}
```

- In a typical direct request, the **request target** carries the path and optional query, while `Host` carries the target authority. A non-default port appears in `Host` when present in that authority. Other target forms exist, such as an absolute URL sent to an HTTP proxy.
- `Accept` describes response media types the client can accept. `Content-Type` describes the content carried by that message. `Content-Length` normally gives its length in bytes. A GET usually has no request body. Responses to HEAD and responses with status 204 or 304 carry no message body. HEAD can still report metadata, including the length a corresponding GET would have sent.
- HTTP/1.1 can use a length, chunked transfer coding, or, for certain responses, connection close to delimit content. HTTP/2 and HTTP/3 preserve the HTTP semantics and use framed wire formats with pseudo-headers for fields such as the method or status. Readable tool output can reconstruct the exchange without showing the wire format. HTTP/1.1 field lines are text in the HTTP message, and TLS encrypts them in transit.

[RFC 9112, HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112) · [RFC 9110, HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)

## 4. Methods, forms, safety, and idempotency

The **method** specifies the requested operation. The **request target** identifies the resource to which it applies. The client chooses the method through its initiating action or configuration. Link navigation normally issues GET, a form uses its configured method, and a script or HTTP client can choose a method explicitly. A server can respond `405 Method Not Allowed` with an `Allow` field when a recognized method is unavailable for the target.

| Method | Typical semantics | Safe | Idempotent |
| --- | --- | --- | --- |
| GET | Retrieve a representation, such as a page or search results | Yes | Yes |
| HEAD | Retrieve GET-style response metadata without the body | Yes | Yes |
| OPTIONS | Ask what communication options are available | Yes | Yes |
| POST | Submit content for resource-specific processing, such as a login or order creation | No | No guarantee |
| PUT | Create or replace the state of a specified resource | No | Yes |
| PATCH | Apply a set of changes to a resource | No | No guarantee |
| DELETE | Remove the association between the target URI and its current functionality, such as removing a cart item | No | Yes |

**Safe** means the requested semantics are read-only. Logging or analytics may still occur as incidental effects. **Idempotent** means repeating the same request has the same intended server-side effect as making it once. A repeated DELETE may return a different status after the first removal. An order POST can create duplicates on retry unless the application provides a deduplication contract, such as an idempotency key. A timeout can occur after the server has already applied the request. DELETE never grants permissions by itself. The application decides whether the caller can act on the target.

**Illustrative form.** With `action="/orders"`, a successful named control `book_id=42`, and `method="get"`, the browser produces `GET /orders?book_id=42 HTTP/1.1`. With `method="post"` and the default form encoding, it produces `POST /orders HTTP/1.1` with `book_id=42` in the body. Forms use GET by default. A POST URL can also have a query. GET query inputs and POST body inputs describe common placement choices and are independent of the method's definition. [RFC 9110, methods](https://www.rfc-editor.org/rfc/rfc9110#section-9) · [WHATWG HTML, forms](https://html.spec.whatwg.org/multipage/forms.html)

## 5. Integrated runtime sequence and graph of references

**Hypothetical bookstore walkthrough.** The customer clicks `<a href="/account/orders?sort=recent">My Orders</a>` on `https://bookstore.example`. Assume a fresh connection, a valid session, and a permitted request. `K7` is an illustrative session ID.

```text
link href + document base URL
  → https://bookstore.example/account/orders?sort=recent
  → DNS lookup as needed → TCP connection → TLS handshake
  → GET /account/orders?sort=recent + Host + eligible Cookie: sid=K7
  → server parses the request and dispatches to application code
       method + path → orders route
       query sort=recent → sort order
       cookie value K7 → server session record → account 42
       account 42 + permission check → authorized order lookup
  → data store returns order records → application builds HTTP response
  → navigation interprets HTML → creates DOM → discovers resource URLs
  → browser retrieves CSS, scripts, and images as needed
```

1. The browser resolves the link and identifies the authority. For a new TCP-based HTTPS connection, it obtains an IP address as needed, connects, then negotiates TLS and verifies the server identity. A usable connection or cached result can bypass some steps. HTTP/3 runs over QUIC over UDP and incorporates TLS 1.3 into the QUIC handshake.
2. The browser builds a request and selects cookies eligible for this URL and request context. The HTTP/1.1 view would show `GET /account/orders?sort=recent HTTP/1.1`, `Host: bookstore.example`, and `Cookie: sid=K7`.
3. A server component receives and parses the message. An application routes it, validates inputs, looks up the session, and checks authorization. Authentication can run in middleware before the handler. The precise order and process boundaries depend on deployment.
4. The orders handler retrieves the authorized account's data, applies the requested sorting, and builds a response such as `200 OK` with `Content-Type: text/html`. A failure can instead lead to an error response or login redirect, depending on the application.
5. For navigation, the browser can parse returned HTML into a new DOM. URLs in HTML and CSS can lead to further requests, often in parallel or satisfied from cache. If script initiates the exchange using `fetch()`, it can parse a returned representation and modify the current DOM. The initiating context and response handling govern the result.

The graph crosses state boundaries at two especially useful references. The cookie value points to a session record and the resulting account identity governs the data lookup. The document contains resource URLs that the browser resolves into later fetches. `sort=recent` controls the ordering of results. [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) · [RFC 9114, HTTP/3](https://www.rfc-editor.org/rfc/rfc9114)

## 6. Responses, redirects, and caching

| Class | Meaning and examples |
| --- | --- |
| 1xx | Informational, such as `100 Continue` |
| 2xx | Success, such as `200 OK`, `201 Created`, or `204 No Content` |
| 3xx | Redirection or reuse of a stored representation, such as `302 Found` or `304 Not Modified` |
| 4xx | Request could not be fulfilled as sent, such as malformed input (`400`), missing or invalid authentication (`401`), refusal (`403`), or unavailable or undisclosed resource (`404`) |
| 5xx | Server or upstream failure, such as `500`, `502`, or `503` |

A redirect usually supplies a `Location` that the client resolves into a new URL. A client that follows it makes a new request. `301` and `308` are permanent. `302` and `307` are temporary. Clients may change POST to GET for `301` and `302`. `303 See Other` directs a retrieval, typically GET after a form POST. `307` and `308` preserve method and body when followed. Follow a redirect chain one request at a time to see changes to origin, method, and cookie eligibility.

A cache can reuse a fresh stored response. `Cache-Control: max-age=60` provides a freshness lifetime of 60 seconds. `no-cache` requires validation before reuse. `no-store` directs caches to avoid storing the response. `private` restricts storage to private caches. `Vary` identifies request fields that affect representation selection. For conditional GET, a client may send `If-None-Match` with an earlier `ETag`, or `If-Modified-Since` with a `Last-Modified` date. `304` lets the client use the stored body and update metadata. If the condition permits a fresh transfer, the server can return `200` and the representation. An HTTP cache and a cookie store preserve different types of state. [RFC 9111, HTTP caching](https://www.rfc-editor.org/rfc/rfc9111) · [RFC 9110, status codes](https://www.rfc-editor.org/rfc/rfc9110#section-15)

## 7. Stateless HTTP, cookies, and sessions

Each HTTP request needs enough context for the server to handle it independently, including any credentials or references needed to recover application state. HTTP does not automatically associate a new request with an earlier login. A connection can carry multiple requests, and a server can maintain durable state such as account records, inventory, carts, and orders. Checkout still has to validate current inventory, even when a previous page displayed availability.

In a typical server-side session design, successful login creates a record such as `K7 → account 42`. The server sends `Set-Cookie: sid=K7; Secure; HttpOnly; SameSite=Lax; Path=/`. The browser stores the name, value, and attributes in its profile's cookie store. On a later eligible request, it sends `Cookie: sid=K7`. The application uses the opaque identifier to look up the session and then checks permission for the specific operation. Some applications use signed or encrypted tokens that carry session information. The bookstore models a server-side record.

| Cookie attribute | Effect |
| --- | --- |
| Domain | Selects eligible domain and subdomains within browser rules. Omit it for a host-only cookie |
| Path | Limits eligible request paths. This is a delivery rule, not a security boundary |
| Secure | Restricts delivery to secure transport such as HTTPS, with browser-specific localhost handling |
| HttpOnly | Prevents ordinary JavaScript cookie APIs from reading the value. Eligible requests initiated by JavaScript can still carry it |
| SameSite | `Strict` limits cross-site use most strongly. `Lax` allows certain cross-site top-level safe navigations. `None` allows broader cross-site use, requires `Secure`, and is subject to browser policy |
| Expires / Max-Age | Absolute expiration / lifetime in seconds. When both are present, Max-Age takes precedence |

The outgoing `Cookie` header carries eligible name/value pairs. Attributes stay with browser storage. A blank SameSite field can mean no explicit attribute was set, with the browser applying its default. “Same-site” for cookies generally concerns the scheme and registrable domain. It differs from the origin comparison in §10.

Cookie lifetime and server session lifetime are independent. Removing the browser cookie breaks the reference even if the server record survives. Revoking the server-side record makes an old identifier unusable even if a copy remains. Without an explicit expiration, browser session restore may retain a session cookie. [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [Chrome DevTools cookie documentation](https://developer.chrome.com/docs/devtools/application/cookies)

## 8. AJAX and the browser DOM

**AJAX** is the historical name for asynchronous browser requests made by JavaScript to process results without requiring a full navigation. It uses HTTP, commonly through `fetch()` or `XMLHttpRequest`. JSON, XML, HTML, and text are possible response formats. The **DOM** is the browser's in-memory representation of the document, exposed through JavaScript APIs.

In the actual exercise, the learner used the Chrome Console on `https://httpbingo.org/get` to issue a same-origin GET. The working lesson example was:

```javascript
fetch('/get?book_id=42')
  .then(response => response.json())
  .then(data => {
    const message = document.createElement('p');
    message.textContent = `Server returned book_id: ${data.args.book_id[0]}`;
    document.body.prepend(message);
  });
```

The browser performs the request and fulfills the first promise when a response is available. `response.json()` reads and parses the body asynchronously. JavaScript creates the element and the browser renders it in the current document. An HTTP `404` ordinarily resolves to a response, so application code should check `response.ok` or `response.status` before using the body. Network or CORS failures can reject the fetch, and invalid JSON can reject parsing. The added paragraph lives in the current DOM. A normal reload would be expected to discard it. That prediction was untested in the session. [WHATWG Fetch Standard](https://fetch.spec.whatwg.org/)

## 9. HTTPS, TLS 1.3, and certificates

HTTPS protects HTTP with encryption and integrity between TLS endpoints and ordinarily authenticates the server. For the fresh, certificate-authenticated TLS 1.3 connection over TCP observed in the lesson:

1. **ClientHello** proposes versions and cryptographic parameters, offers a key share and ALPN protocols, and normally includes the requested hostname via SNI.
2. **ServerHello** selects the parameters and supplies a key share. The peers derive handshake traffic keys from the key exchange and transcript. The following server handshake messages are encrypted.
3. **EncryptedExtensions** carries negotiated extensions such as the ALPN selection. **Certificate** provides the server's certificate chain material. The client validates trust and time validity and matches the requested hostname against the certificate's identity, normally a DNS subject alternative name for a DNS hostname.
4. **CertificateVerify** signs the handshake transcript and proves possession of the certificate's private key. **Finished** authenticates the handshake transcript using derived keys. The client verifies the server's messages and sends its own Finished. The normal HTTP exchange uses application traffic keys.

ALPN selects the application protocol, such as HTTP/1.1 or HTTP/2. Certificate verification and hostname matching concern the endpoint's identity. Application login and authorization happen separately. TLS termination at a proxy is an endpoint for that leg, with any upstream protection determined independently. Network observers can still see metadata such as endpoint IP addresses and timing. DNS or SNI can expose names depending on the setup. Connection reuse, resumption, and early data can change the sequence. [RFC 8446, TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) · [RFC 9525, service identity](https://www.rfc-editor.org/rfc/rfc9525)

## 10. Browser security boundaries

### Same-origin policy and CORS

For ordinary HTTP(S) URLs, origin is **scheme + hostname + effective port**. `https://bookstore.example/books` and `https://bookstore.example:443/cart` share an origin. `http://bookstore.example`, `https://api.bookstore.example`, and `https://bookstore.example:8443` each differ from `https://bookstore.example`. Paths, queries, and fragments are outside the comparison. Same-origin policy restricts what a document or script from one origin can read or manipulate across origins. Browsers still allow various cross-origin navigations, embeddings, and form submissions under their applicable rules.

**CORS** lets a server opt into exposing a cross-origin HTTP response to browser JavaScript. The browser evaluates response headers such as `Access-Control-Allow-Origin`. Some requests first trigger an `OPTIONS` preflight asking whether the method and headers are allowed. A failed preflight prevents the intended request. For a request that can proceed without preflight, the server may receive it and act before the browser blocks script access to the response. Credentialed cross-origin fetch requires appropriate client credentials settings, cookie eligibility and browser policy, a specific allowed origin, and `Access-Control-Allow-Credentials: true` for response exposure. A wildcard origin is insufficient for credentialed exposure. For example, a browser request from the hypothetical bookstore page to its separate API can carry `Origin: https://bookstore.example`. An API response can opt in with `Access-Control-Allow-Origin: https://bookstore.example`. CORS leaves the origin tuple unchanged. Command-line clients such as curl do not enforce browser CORS. [Launch School, Security](https://launchschool.com/books/http/read/security) · [WHATWG Fetch, CORS protocol](https://fetch.spec.whatwg.org/#http-cors-protocol)

### XSS, CSRF, and session hijacking

| Threat | Hypothetical mechanism | Main protections |
| --- | --- | --- |
| Cross-site scripting (XSS) | A bookstore stores a malicious review, inserts it as executable markup, and a later visitor's browser runs it in the bookstore origin. Reflected XSS returns malicious input in a response. DOM-based XSS can arise from unsafe client-side handling | Context-specific output encoding, safe DOM APIs such as `textContent` for text, sanitization for deliberately allowed HTML, and Content Security Policy as defense in depth |
| Cross-site request forgery (CSRF) | An attacker induces a signed-in browser to send a state-changing request. If the browser attaches an eligible cookie and the server accepts the action, the attacker can succeed without reading the response | Server-validated CSRF tokens, appropriate Origin or Referer checks, SameSite as defense in depth, and safe semantics for GET |
| Session hijacking | An attacker obtains a valid bearer session credential and replays it. If the server still accepts it, the attacker may act with that session's permissions | HTTPS, secure cookie attributes, unpredictable IDs, rotation on login or privilege change, expiration and server-side revocation. After revocation, the user can reauthenticate to establish a new session |

An XSS payload can act within the victim's origin and make authenticated requests even when HttpOnly hides the cookie value. CSRF uses the victim browser to submit a request. Session hijacking can let another client present the credential directly. Authorization still applies to each action. These mechanisms were discussed conceptually in the lesson. [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) · [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) · [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

## 11. Hands-on evidence from the lesson

These observations are from the learner's reported output. Public endpoints, certificate details, and browser state can change between runs. The selected curl fields below omit client addresses and cookie values.

| Investigation | Reported observation | What the evidence establishes |
| --- | --- | --- |
| Chrome Network, example.com document | GET `https://example.com/?utm_source=chatgpt.com` returned `304`. No `Content-Type` was visible. After disabling cache and reloading, the learner reported `200 OK` and `text/html; charset=utf-8` | The first response was consistent with cache revalidation and the follow-up delivered an HTML representation. The exact validator and whether the follow-up kept the same query were unrecorded |
| `curl -i https://example.com/` | `HTTP/2 200`, HTML content type, and HTML after the header section in curl's output | curl displayed the response status, fields, and content in a readable format |
| `curl --http1.1 -v -o /dev/null https://example.com/` | `GET / HTTP/1.1`, `Host: example.com`, `User-Agent: curl/8.7.1`, `Accept: */*` | The URL supplied the authority and path. curl supplied other fields. Verbose output described the exchange at the client |
| HTTPBingo POST | `POST /post HTTP/1.1`, `Content-Length: 10`, `Content-Type: application/x-www-form-urlencoded`. Response JSON reported `"method": "POST"`, `"data": "book_id=42"`, and a `form.book_id` entry containing `"42"` | The field traveled in the request body. HTTPBingo parsed it and reported it in the response body |
| HTTPBingo GET | Response JSON included `args.book_id` with string `"42"`. The comparison request placed `book_id=42` in the query | Both responses can contain the same value in JSON. Its placement in the incoming request is the distinction. JSON field ordering provides no evidence of that placement |
| Chrome Application → Storage → Cookies and Network → Cookies column, Amazon Kindle Daily Deals | 15 stored cookies in the view, including names `session-id` and `session-token`. Some displayed explicit `SameSite=Lax`. One network row showed zero sent cookies, and several others showed nonzero counts | Cookie storage and request delivery are independently observable. The zero row's cause, the cookie identities sent on nonzero rows, and Amazon's session implementation remain undetermined. The displayed timestamp associated with `session-id-time` was not tied to a verified column |
| Chrome Fetch/XHR, HTTPBingo | `/get?book_id=42` appeared in Network. The current page then displayed “Server returned book_id: 42” at the top | JavaScript initiated HTTP, processed the JSON response, and updated the current DOM without navigating |
| curl TLS diagnostic, example.com | ClientHello → ServerHello → `Unknown (8)` → Certificate → `CERT verify (15)` → server Finished → client Finished. curl reported TLS 1.3, ChaCha20-Poly1305/SHA-256, ALPN `http/1.1`, a matching `example.com` SAN, issuer Cloudflare TLS Issuing ECC CA 3, and successful certificate verification | The trace matches the full handshake discussed in §9. Type 8 is EncryptedExtensions. `CERT verify (15)` names a handshake message, while `SSL certificate verify ok` reports the client's validation result. The diagnostic prefix `(304)` belongs to the TLS output. The separate Chrome `304` was an HTTP status |

### Reproduction commands used in the lesson

```bash
curl -i https://example.com/
curl --http1.1 -v -o /dev/null https://example.com/
curl --http1.1 -v --data 'book_id=42' https://httpbingo.org/post
curl --http1.1 -v --get --data 'book_id=42' https://httpbingo.org/get
```

With curl, `-i` includes response headers, `-I` issues HEAD, and `-v` shows client diagnostics. In verbose HTTP/1.1 output, `>` marks outgoing fields, `<` incoming fields, and `*` connection or TLS messages. `-o /dev/null` discards the response body from standard output. `--data` normally selects POST and places data in its body. `--get` moves the supplied data to the query and uses GET in this example. [curl manual](https://curl.se/docs/manpage.html)

## 12. Troubleshooting by boundary

| Symptom | What to inspect |
| --- | --- |
| No expected request in Chrome | Open Network before reproducing. Check filters, initiator, navigation, and cache or service worker involvement. Preserve the log for redirects |
| DNS, connection, or certificate error | Check the hostname, resolved address, destination port, TCP or QUIC connection, then TLS diagnostics. A failure here can occur before any HTTP response |
| Wrong endpoint or unexpected status | Compare the resolved URL, request method, path, query, body, and content type. Inspect the redirect chain and the final target. Match the server route and application logs if available |
| HTML appears but the row says `304` | Inspect cache validators and compare with a fresh request to the exact same URL |
| Signed-in request acts anonymous | Compare the stored cookie's scope and lifetime with the request URL and context. Check the outgoing cookie's presence and the server session's validity. Omit credential values from shared logs |
| curl succeeds but browser fetch fails | Compare URL, credentials, request headers and method, and cookies. Inspect Console for CORS errors and Network for preflight and response headers |
| Fetch succeeded but the page did not change | Check HTTP status, body format, JSON parsing, promise errors, expected data shape, and the DOM operation |

**Tool choice.** Chrome DevTools shows real browser behavior, including Network, cache, storage, and DOM. curl constructs controlled exchanges. Insomnia is a GUI HTTP client for constructing requests and examining responses. Wireshark is a packet analyzer that can show transport and TLS traffic. Inspecting encrypted HTTP content in a capture requires suitable decryption material. The lesson record confirms Chrome and curl use. Insomnia and Wireshark were discussed without a confirmed hands-on capture or run. The HTML form and cross-origin examples were reasoned through. No security attack was run. [Chrome Network reference](https://developer.chrome.com/docs/devtools/network/reference) · [curl manual](https://curl.se/docs/manpage.html)

## 13. Quiz debrief and remaining questions

| Topic | What to retrieve independently |
| --- | --- |
| URL inputs and encoding | Path and query parameters can both carry application input. Distinguish query component from individual parameters and recall both `+` and `%20` under form decoding |
| Method versus target | The learner identified the method as the kind of operation. The quiz reportedly also accepted wording about the resource being fetched. In protocol terms, the target identifies the resource and the method supplies the semantics |
| GET and POST | The learner selected the general purposes and omitted a second accepted answer with examples. Recall both the definitions and the common page-view and login examples |
| Header syntax | Recall `Name: value`, where the colon separates the field name and value in HTTP/1.1. TLS protects those bytes in HTTPS |
| Statelessness | The missed option asked for each request to provide enough information for fulfillment. That information can include an identifier used to retrieve server-side state |
| Same-origin policy | Two of three conditions were selected. Retrieve and check all three independently: scheme, hostname, effective port |

Several misses were incomplete multi-select answers. Evaluate each choice on its own, including examples if the prompt asks what applies. The walkthrough showed independent recall of receive → route → handler and recognition of navigation versus script-driven processing. Connecting the starting link, transport, session reference, authorization, and response into one traversal needed prompting. That evidence supports first-pass coverage and points to where independent retrieval and transfer remain to be demonstrated.

The exact browser cache validator, the reason for the zero-cookie row, and the reload prediction for the temporary DOM change remain open. The transcript also leaves full question-box coverage unverified. A later reconstruction can start at an unfamiliar entry point and account for the state owner, reference, and next action at each step.

