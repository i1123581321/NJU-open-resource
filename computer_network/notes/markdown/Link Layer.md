# $链路层$

## Link Service and Framing

### 链路层实现

Link 种类：

* Wired
  * point-to-point
  * multiple access (LAN)
* Wireless (WIFI)

链路层硬件（终端）：网络适配器（Adapter），网卡（NIC, Network Interface Card）

### 链路层服务

* **Framing**
* **Link Access**
  * 多路访问
  * MAC 地址
  * [双工][Duplex]
* Reliable Delivery（可选）
  * Flow control
* Error Detection and Correction（可选）

#### Framing

发送方将 datagram 封装为 frame，添加纠错位、控制位等

接收方检查错误，解封 datagram 并传到上层

#### Reliable Delivery

使用 Flow control 确保接收方不会过载

##### Stop and Wait

* 发送方：发送 frame
* 接收方：接受 frame，回复 ACK
* 发送方：等待 ACK ，进行下一次发送

对于较大的 frame 效果较好

##### Sliding Window

接收方有大小为 Win 的缓冲区

发送方无需 ACK 可发送最多 Win 的frame

每个 frame 有编号

ACK 包括了期望接收到的下一 frame 的序号和当前窗口大小

[![1554020731977.png](https://i.loli.net/2019/04/03/5ca4836e7381d.png)](https://i.loli.net/2019/04/03/5ca4836e7381d.png)

对于错误有 Go Back N 和 Selective Reject 两种处理方式

更多参见 [Sliding Window Protocol][SWP]

## Error Detection and Reliable Transmission

奇偶校验（单 Bit，二维）

### 循环冗余校验 CRC

设数据为 $D$ ，CRC 位 $R$ 为 $r$ 位，选择 $r + 1$ 位的生成多项式 $G​$
$$
D \times 2^r = a \times G \oplus R, \quad D \times 2^r \oplus G = a \times G \\
R = remainder(\frac{D \times 2^r}{G})
$$
CRC 算法伪代码：

* 将 CRC 寄存器赋 0
* 将数据左移 $r$ 位（末尾补 $r$ 个 0）
* 当数据未处理完时
  * 寄存器左移一位，空位读入 1 位数据
  * 如果上一步左移移出位为 1
    * CRC 寄存器异或生成多项式

Haskell 实现：

```haskell
crc::String -> String -> String -> String
crc [] a _ = a
crc (_:_) [] _     = []
crc (_:_) (_:_) [] = []
crc (d:ds) reg@(r:_) gen@(_:gs) = let newReg = if r == '1'
                                               then xor (sl reg d) gs
                                               else sl reg d
                                  in crc ds newReg gen
```

参见 [Cyclic Redundancy Check][CRC]

## HDLC, PPP, and SONET

直接相连技术

### HDLC: High-Level Data Link Control

使用 `01111110` 作为帧开始与结束的分隔符

如何不与数据内同样的序列冲突：**Bit Stuffing**

* 发送方：在每五个连续的 1 后面插入一个 0
* 接收方：在每五个连续的 1 后，如果第六个是 0，删去 0，如果第六个是 10，则是分隔符

参见 [High-Level Data Link Control][HDLC]

### PPP: Point-to-Point Protocol

flag 同样是 `01111110`

**Byte Stuffing**：

* 发送方：在 `01111110` 之前加入 `01111101`
* 接收方：
  * 收到 `<01111101, 01111110>` 丢弃第一个 Byte，继续接收
  * 收到 `<01111101, 01111101>` 丢弃第一个 Byte，继续接收
  * 收到单独的 `01111110` ，分隔符

参见 [Point-to-Point Protocol][PPP]

### SONET: Synchronous Optical Network

## Token Ring

LAN 的网络拓扑

* Bus
* Ring
* Tree
* Star

### Token Ring

一种局域网协议，IEEE 802.5

**repeater（接入点）** 两两间由单向网络连接

数据以 bit 为单位在 repeater 之间传输（数据的插入、接受、删除）

frame 在**绕环一周后**由发送方删除

### Repeater States

#### Listen State

* Scan passing bit stream
  * 相连 station 地址与目标地址
  * Token 状态（发送许可）
* 复制一份副本并转发
  * 若地址匹配传给对应 station
* 修改 bit 流
  * 接收到时尾部附加 ACK
  * 或是反转

#### Transmit State

* 接受 frame ，传给发送的 station 检查 ACK
* 可能会缓存其他 frame

#### Bypass State

* 仅仅作为中转点

### 802.5 MAC Protocol

#### 协议

空闲时：Token 在环路中循环

发送时：修改 Token 中一位使之成为 SOF(Start Of Frame)，在 Token 之后添加数据 frame

发送完成后由发送结点丢弃 frame 并在环路中插入新的 Token

参见 [Token ring][TR]

#### 平均等待时间

* 设环中有 $N$ 个结点
* Token 绕环一圈的时间为 $T$
* 每个 node 传输数据平均时间为 $T'​$

则平均等待时间为
$$
\frac{1}{N} \times 0 + \frac{1}{N} \times (T' + \frac{T}{N}) + \frac{2}{N} \times (T' + \frac{T}{N}) + \dots + \frac{N - 1}{N} \times (T' + \frac{T}{N}) \\
= \frac{N-1}{2} \times (T' + \frac{T}{N})
$$

#### 释放 Token 的时机

* 常规释放：发送方收到 ACK 后释放
* 早期释放：发送方发送完最后 1 bit 之后直接释放

### FDDI Token Ring

使用双环结构，传输方向相反。内环空闲，出错时切换到内环

## Ethernet

主流使用的局域网技术，比 Token ring，ATM 更简单也更便宜

### Multiple Access Protocol

#### Multiple Access

数据链路可分为点对点与广播两类

Multiple Access Links 的特点：

* **一条**公用的广播信道
* 两个及以上的结点传输会发生干扰
* **碰撞**：结点同时收到两个及以上的信号

理想的 Multiple Access Protocol 的特点（假设广播信道的带宽为 $R​$）：

1. 只有一个结点传输时，速率为 $R$
2. $M$ 个结点传输时，每个结点的平均传输速率为 $\dfrac{R}{M}$
3. 完全分布式
   * 没有一个特殊结点协调传输
   * 没有同步时钟或时隙
4. 简单

Multiple Access Control 可分为三类

* Channel Partitioning
* Taking Turns
* Random Access

#### Channel Partitioning

基本思想：将信道分成小的片段（时分，频分，码分），为每个结点专门分配片段

##### TDMA

按照时间将信道分为一个个 slot，每轮每个结点独占一个 slot

##### FDMA

按频率将信道分为不同频段，每个结点分得固定频段

##### CDMA (Code Division Multiple Access)

一般用于无线广域网

每个结点共享频率，但结点有独特的 chipping sequence 用于编码数据

编码信号 = （原始数据）$\times$ （chipping sequence）

解码：编码信号与 chipping sequence 的**内积**

参见 [Code-division multiple access][CDMA]

#### Taking Turns

基本思想：结点轮流传输，传输量较多的结点需要更多的回合

##### Polling

Master 结点轮询 Slave 结点，适用于 dumb slave 的情况

* 轮询开销
* 延时
* Single point failure

e.g. 蓝牙

##### Token passing

控制 Token 在结点间传递

e.g. Token Ring，FDDI

#### Random Access

结点发送时占用全部带宽，不划分信道

两个以上结点同时发送时即发生**碰撞**

* 如何检测/避免碰撞
* 如何从碰撞中恢复

不同的 Random Access MAC Protocol：

* ALOHA, Slotted ALOHA
* CSMA, CSMA/CD, CSMA/CA

##### ALOHA (Additive Link On-line HAwaii system)

发送方：

* 结点有 frame 时，发送
* 若接收到 ACK，则成功发送
  * 否则有 $p$ 的概率重传，有 $(1-p)$ 的概率等待
* 如果重传后还是没有 ACK，则放弃

接收方：

* 检测帧
* 若完好且地址符和，则发送 ACK

ALOHA 的帧损坏可能由帧重叠导致

##### Slotted ALOHA

与 ALOHA 的不同：

* 所有的 frame 大小相同
* 时间划分为相等的时隙（帧传输时间）
* 结点同步（中央时钟或其他同步机制实现）
* 传输开始于时隙的边界
* frames 或者成功传输或者完全重叠

发送操作：当有 frame 时在下一个 slot 发送

* 若无碰撞则在下一个 slot 发送
* 若发生碰撞，则在接下来的 slot 以概率 $p$ 重传，直至成功

参见 [ALOHAnet][ALOHA]

### CSMA

CSMA (Carrier Sence Multiple Access) 载波侦听多路访问

基本思想：

* 在传输前监听
* 若信道空闲，传输
* 若信道繁忙则等待一段时间（往返时间）
* 如果没有收到 ACK 则重传

对于较大的帧和较短的传播时延效果较好

参见 [Carrier-sense multiple access][CSMA]

#### CSMA mode

##### Nonpersistent CSMA

想要传输 frame 的结点监听信道

1. 若信道空闲，传输，否则 2
2. 若信道繁忙，等待一段**随机**的时间，重复 1

随机长度的时延降低了碰撞的几率，但也降低了信道的利用率（传输后仍会空闲一段时间）

##### 1-persistent CSMA

想要传输 frame 的结点监听信道

1. 若信道空闲，传输，否则 2
2. 若信道繁忙，等待至空闲，**立即传输**

selfish，多个节点等待传输时会发生碰撞

##### p-persistent CSMA

在碰撞与空闲之间做出妥协

time unit：最大传播时延

1. 若信道空闲，以 $p$ 的概率传输，以 $(1-p)$ 的概率延迟 1 个 time unit
2. 若信道繁忙，监听直至空闲，重复 1
3. 若传输延迟了 1 个 time unit，重复 1

概率 $p$ 的选择至关重要，对于 $N$ 个结点最佳的 $p$ 是 $\dfrac{1}{N}$

#### CSMA/CD

##### 处理流程

想要传输的结点监听信道

1. 若信道空闲，传输，否则 2
2. 若信道繁忙，等待至空闲，立即传输
3. 若检测到碰撞，发送 **Jam signal**，然后终止传输
   * Jam signal 是全 1 的信号，一般为 32~48 bit，旨在加强碰撞，使其余设备易于检测
4. 在发送 Jam 后，等待随机时间，从 1 开始

对于 IEEE 802.3 ，使用 **1-persistent**

参见 [Carrier-sense multiple access with collision detection][CSMA/CD]

##### Binary exponential backoff

尝试在碰撞后重复传输。结点的实际等待时间为 $K \times $ 512 bit 时间（发送 512 bit 进入以太网的时间，以太网中两台机器之间最大的 rtt）

* 在 $n$ 次碰撞后，随机从 $\{0, 1, 2, \dots, 2^n - 1\}$ 中等概率地选择 $K$ 值
* 10 次或更多次碰撞后，从 $\{0, 1, 2, \dots , 1023\}$ 中等概率地选择 $K$ 值
* 16 次碰撞后放弃传输并报告错误

有 LIFO 效应：后到的碰撞退避时间短

### IEEE 802.3

#### Ethernet Frame Format

* Preamble（8 octets）：7 octets with pattern 10101010 followed by 1 octet with pattern 10101011，用于同步发送方接收方的时钟频率
* SFD：Start of Frame Delimiter
* Address（12 octets）：6 octets MAC address，Source and Destination
* Type/Length（2 octets）：标明上层协议
  * 若小于 1536，则为长度字段，为 IEEE802.3 frame
  * 若大于等于 1536，为类型字段，为 DIXv2 frame
* Data（46~1500 octets）
* FCS（4 octets）：Frame Check Sequence（CRC）

以太网帧最短为 64 Bytes，即 14(Header) + 46(Data) + 4(FCS)

#### Logical Link Control

以太网

* 不可靠：不发送 ACK/NAK
* 无连接：没有握手（连接建立）

LLC：

* 处理结点间的逻辑链路
* 流控制及错误检测

LLC 很少用于以太网，但常用于 WiFi（IEEE 802.11）和 Token Ring（IEEE 802.5）

LLC 基于 HDLC 的服务：

* Unacknowledged connectionless service
  * Nothing added
* Acknowledged connectionless service
  * Add ACK and NAK, stop-and-wait
* Connection mode service
  * HDLC in Asynchronous balanced mode

#### 802.3 Physical Layer

不同的以太网标准

* 相同 MAC 协议，帧格式
* 不同速度：2Mbps，10Mbps，100Mbps，1Gbps
* 不同物理媒介：光纤，铜缆

### High-Speed Ethernet

仍然使用 IEEE 802.3 的 MAC 协议和帧格式

**星型拓扑**

[Duplex]: https://en.wikipedia.org/wiki/Duplex_(telecommunications)	"Duplex"

[SWP]: https://en.wikipedia.org/wiki/Sliding_window_protocol	"Sliding Window Protocol"

[CRC]: https://en.wikipedia.org/wiki/Cyclic_redundancy_check	"Cyclic Redundancy Check"

[HDLC]: https://en.wikipedia.org/wiki/High-Level_Data_Link_Control	"High-Level Data Link Control"

[PPP]: https://en.wikipedia.org/wiki/Point-to-Point_Protocol	"Point-to-Point Protocol"

[TR]: https://en.wikipedia.org/wiki/Token_ring	"Token ring"

[CDMA]: https://en.wikipedia.org/wiki/Code-division_multiple_access	"Code-division multiple access"

[ALOHA]: https://en.wikipedia.org/wiki/ALOHAnet#ALOHA_protocol	"ALOHAnet"

[CSMA]: https://en.wikipedia.org/wiki/Carrier-sense_multiple_access	"Carrier-sense multiple access"

[CSMA/CD]: https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_detection	"Carrier-sense multiple access with collision detection"