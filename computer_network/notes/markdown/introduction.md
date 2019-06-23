[![white.png](https://i.loli.net/2019/04/11/5cae134487910.png)](https://github.com/i1123581321/NJU-open-resource)

# Introduction

## Basic concepts

### Internet

Internet: network of networks

Internet 的组成包括

* 计算设备：包括主机（端系统）及其上的网络应用
* 通信链路：光纤，铜缆，电波，etc
* 路由器：在物理网络之间转发报文

Internet 提供的服务有

* 基础通信：允许分布式的应用间互相通信
* 通信服务：如可靠交付，尽力而为，保证延时和吞吐量等

Internet 中的协议有

* 网络协议：控制信息的发送和接收，如 HTTP, TCP, IP, PPP, Ethernet 等
* 网络标准：IETF, RFC

什么是协议：协议定义了网络实体间发送与接收的信息的格式与顺序，以及在消息发送和接收后采取的行动

### Access Internet

#### 网络边缘（Network edge）

**应用**和**端设备**，如主机和其上的 web 应用

应用模型有两种

* Client and Server：由 Client 发出请求，Server 回应请求并提供服务，如 web，e-mail
* Peer-to-peer：没有专门的服务器，每个端设备都可以请求服务和提供服务，如 Skype，BitTorrent

#### 网络接入（Access networks）

物理媒介（有线/无线），用于将端设备连接到边界路由器，如家庭网络，学校网络（LAN），无线网络等。使用带宽衡量性能，可以是专属或是共享的

端设备将应用的数据分成小的 chunk，将其传输到接入网络，链路的传输速率即链路带宽

物理媒介有电波，双绞铜线，光纤等

#### 网络核心（Network core）

互相连接的路由器组成的网络，network of networks

数据传输的方式可分为两类

* Circuit switching：每个通信独享一条电路，如电话网络
* Packet switching：端设备将数据分成 packet，每个 packet 在网络中的路由器之间转发至目的地

### Data transmission

网络层的两个基本功能：路由和转发，用于在网络间传输数据

#### Circuit switching

基本思想是在端系统通信时，预留了路径上的资源（链路带宽，缓存等），这些资源由该次通信独享，类似电话网络中的通信，需要预先建立一条连接，从源到目的地的途中的交换机都维护连接状态，同时预留了链路带宽，使得数据能以确定的速率传输

#### Packet switching

端系统将数据分成 packet 发送到网络中，packet 在交换机之间存储并转发（转发前必须收到整个 packet，因此要求对收到的数据缓存），每个 packet 按需使用网络中的资源，传输时使用全部的链路带宽

当 packet 通过一条链路传输时，设长度为 $L$ bit，链路传输速率为 $R$ bit/s，则传输时延为
$$
\frac{L}{R}
$$
由于存储转发的特性，当路径中有 $N$ 段链路时，总的传输时延为
$$
d = N\frac{L}{R}
$$
packet 之间会争用资源，当到达交换机的速率大于转发的速率时，就会在交换机缓存排队，产生**排队时延**，而若缓存不足，会丢弃一些 packet，产生**丢包**

#### Virtual Circuit

Virtual Circuit 是一种 **packet switching network**，使用了 circuit switching network 的思想，面向连接。VC 中端到端途中的路径是固定的，传输链路由网络中的 packet 共享，故使用拥塞控制来保证服务质量，可以预留资源以提供不同的服务，在通信时需要建立连接

|          | circuit switching | datagram network |    virtual circuit     |
| :------: | :---------------: | :--------------: | :--------------------: |
| 传输链路 |       专用        |       共享       |          共享          |
|  连续性  |       连续        |       分组       |          分组          |
|   带宽   |       固定        |       动态       |          动态          |
|   路由   |       固定        |       动态       |          固定          |
|   时延   |  通信建立的时延   |     传输时延     | 传输时延与通信建立时延 |
|  扩展性  |        差         |        好        |          较好          |

### Internet Structure

网络结构是层次的

* 中心是国家或国际的 ISP，以及大型内容提供者，如 Google，Microsoft
* 下一层是地区的 ISP，连接到多个大型 ISP，彼此之间直连或通过 ISP，IXP 连接
* 再下一层是本地的 ISP，最后一跳，距离端系统最近

上次 ISP 向下层 ISP 提供服务

## Protocol Layers and Service Model

网络是个复杂的系统，利用分层的体系结构，可以讨论网络中的某个特定的部分

在分层的结构中，每一层使用下层提供的接口，以及本层的内容，向上层提供服务，这也使得易于改变某一层的内容，只要保证其提供给上层的接口与服务不变，层内的实现改变就不会对上层造成影响。

在网络中用分层的体系结构组织不同的协议，每个协议属于某个层次，使用下层提供的服务，同时向上层提供服务，如某层的可靠报文交付服务就可能是使用下层的不可靠报文交付服务以及本次的检测与重传丢失报文所实现的。协议层中可以用软件，硬件或两者的结合来实现。

每一层的所有协议被称为协议栈（protocol stack）

有两个标准的协议分层结构，OSI 和 TCP/IP 协议组

### ISO-OSI

Open System Interconnection，由 ISO 产生，将网络分为七个层次。OSI 是个理论上的层次结构，从未被实现。

OSI 中每个层实现一个通信功能的子集，每层依赖于下层提供的更基础的功能，向上层提供服务，某一层实现的变化不应当影响到其他层

OSI 层次分为

* Application：应用使用 OSI 服务的接口
* Presentation：转换数据（格式&编码，压缩，加密等）
* Session：控制应用间的会话
* Transport：端系统间交换数据（进程间），提供可靠的流传输或快且简单的单块数据传输，可以保证：无差错，有序，无丢包，无副本，需要建立与维护连接
* Network：在多个链路/网络间传递数据，编址范围需要足够大，节点通过路由算法确定应当采取的路径，在节点间转发 packet，使用拥塞控制解决网络拥塞，如果是面向连接的网络，还需要连接的建立与消亡
* Data link：将 bit 组织成 frame，在直接相连的设备间传递 frame，LAN 中的媒介访问控制，检错和重传，以及端到端的流控制，向上层提供无错误的传输
* Physical：在链路间传递 bit，规范了通信链路的物理方面

### TCP/IP

在当前互联网中使用。分为五个层次

* Application：同 OSI 中的 Application，Presentation，Session 的功能，将这三个层次均整合进 Application 层
* Transport：提供进程-进程间的数据传输，如 TCP/UDP
* Internetwork：在网络间路由数据报，IP 协议
* Link：在相邻主机/路由器间传递数据，如 PPP，Ethernet
* Physical：链路上的 bit

PDU (Protocol Data Unit) 是每个层中的数据基本单位，如传输层将应用层的数据分为 segment ，加入本层的控制信息，然后在网络层封装为 datagram，在链路层封装为 frame，这些均是对应层的 PDU

### Network Security

网络中的攻击者可以

* 在主机中注入恶意程序，如病毒，木马，蠕虫等
* 攻击网络服务，如 DoS 攻击和 DDoS
* 嗅探分组，重放攻击或是伪装成他人