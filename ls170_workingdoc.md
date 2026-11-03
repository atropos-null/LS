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