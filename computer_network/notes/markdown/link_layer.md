[![white.png](https://i.loli.net/2019/04/11/5cae134487910.png)](https://github.com/i1123581321/NJU-open-resource)

# 链路层

## Link Service and Framing

### Link layer

Link 种类：

* Wired
  * point-to-point
  * multiple access (LAN)
* Wireless (WIFI)

链路层硬件（终端）：网络适配器（Adapter），网卡（NIC, Network Interface Card）

### Link layer service

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

帧结构由链路层协议决定

#### Link Access

媒体访问控制（Medium Access Control, MAC）协议规定了 frame 在链路上传递的规则。点对点的 MAC 较简单（或是不存在），而当多个节点共享单个广播链路时（LAN），即多路访问问题，MAC 协议用于协调多个节点的 frame 传输

#### Reliable Delivery

通过**确认与重传**保证可靠交付，通常用于差错率较高的链路，如无线网络，在低差错的链路（光纤，同轴电缆，双绞铜线）中一般不提供可靠交付服务

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

#### Error Detection and Correction

在 frame 中插入差错检测位，由接收方检测及纠正（如果可以的话）frame 中的错误。通常由硬件实现

## Error Detection and Reliable Transmission

链路层的差错校验是比特级的

奇偶校验（单 Bit，二维）

### 循环冗余校验 CRC

设数据为 $D$ ，CRC 位 $R$ 为 $r$ 位，选择 $r + 1$ 位的生成多项式 $G$
$$
D \times 2^r = a \times G \oplus R, \quad D \times 2^r \oplus R = a \times G \\
R = remainder(\frac{D \times 2^r}{G})
$$
CRC 算法伪代码：

* 将 CRC 寄存器赋 0
* 将数据左移 $r$ 位（末尾补 $r$ 个 0）
* 当数据未处理完时
  * 寄存器左移一位，空位读入 1 位数据
  * 如果上一步左移移出位为 1
    * CRC 寄存器异或生成多项式

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
* 每个 node 传输数据平均时间为 $T'$

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

理想的 Multiple Access Protocol 的特点（假设广播信道的带宽为 $R$）：

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

## Network Performance

### Delay

#### Source of delay

* Transmission
  * 带宽为 $R$
  * 分组长度为 $L$
  * Transmission Delay = $\dfrac{L}{R}$
* Propagation
  * 物理链路长度为 $d$
  * 传播速度为 $s$
  * Propagation Delay = $\dfrac{d}{s}$
* Nodal Processing
  * 检查比特错
  * 决定出链路
* **Queuing**
  * 在出链路等待传输的时间
  * 取决于路由器的拥塞程度

#### Queuing Delay

* 带宽为 $R$
* 分组长度为 $L$
* 分组平均到达速率为 $\alpha$
* **Traffic intensity** $\rho = \dfrac{L \times \alpha}{R}$

$\rho \rightarrow 1$ 时 Queuing Delay $\rightarrow \infin$

### Packet loss and Throughput

#### Packet loss

当路由链路的 buffer 满时便会导致新到的分组丢包

#### Throughput

发送方与接收方之间的数据传输速率

常常被链路中的瓶颈链路所**限制**

### Network Performance

Media Utilization
$$
U = \frac{\text{Time for frame transmission}}{\text{total time for a frame}}
$$
Relative Propagation Time
$$
\alpha = \frac{\text{propagation time}}{\text{transmission time}}
$$

#### Point-to-Point Link with no ACK

* frame transmission time: 1
* end to end propagation time: $\alpha$
* number of stations: $N$

Max Utilization
$$
U = \frac{1}{1+\alpha}
$$

#### Ring LAN

* Average time to transmit a frame: $T_1$
* Average time to pass the token after transmission: $T_2$
* number of stations: $N$

Max Utilization
$$
U = \frac{T_1}{T_1+T_2} = 
\begin{cases}
\dfrac{1}{1+\frac{\alpha}{N}}, \quad (\alpha < 1, \text{frame is longer than ring}) \\
\dfrac{1}{\alpha + \frac{\alpha}{N}}, \quad (\alpha > 1, \text{frame is shorter than ring})
\end{cases}
$$

#### Slotted ALOHA

假设有 $N$ 个结点，每个传输的概率为 $p$

* 一个结点成功传输的概率：$p(1-p)^{N-1}$
* 任意一结点成功传输的概率：$A = Np(1-p)^{N-1}$

$p = \dfrac{1}{N}$ 时 $A$ 取得最大值 $\left(1-\dfrac{1}{N}\right)^{N-1}$

对于一个成功发送的 slot，Utilization 为
$$
U_S = \frac{1}{1+2\alpha} \approx 1 \quad (\alpha \ll 1)
$$
发送前使用 $\alpha$ 的时间检测碰撞，发送后以 $\alpha$ 的时间确认 ACK

Max Utilization
$$
\begin{align}
& U = U_S \times A \approx \left(1 - \dfrac{1}{N}\right)^{N-1}\\
& \text{Let } N \rightarrow \infin \\
& U \approx e^{-1} = 0.367879
\end{align}
$$

#### Pure ALOHA

成功概率
$$
\begin{align}
A = N &\times P \{\text{one transmit in the slot}\} \\
&\times P\{\text{no other node transmit in }[t_{0-1}, t_0] \} \\
&\times P\{\text{no other node transmit in }[t_0, t_{0+1}] \} 
\end{align}
$$
Max Utilization
$$
\begin{align}
U &\approx A = Np(1-p)^{2N - 1} \\ 
&\approx \dfrac{1}{2}\left(1 - \dfrac{1}{2N} \right)^{2N - 1} \quad (p = \dfrac{1}{2N}) \\
&\approx \dfrac{1}{2e} = 0.183940 \quad (N \rightarrow \infin)
\end{align}
$$

#### CSMA\CD

* banwidth: $B$
* length of link: $L$
* Propagation speed: $V$
* frame size: $Size$
* Propagation time: $T_a = \dfrac{L}{V}$
* Transmission time: $T_b = \dfrac{Size}{B}$

最差情况下需要 $2T_a$ 的时间才能检测到碰撞，（Minimum contention interval）

Minimum frame size
$$
T_b \geqslant 2T_a\\
Size \geqslant \dfrac{2 \times L \times B}{V}
$$
对于 p-persistent CSMA/CD（传输概率为 $p$）

成功传输概率
$$
A = Np(1-p)^{N-1}\\
p = \dfrac{1}{N}, A = \left(1 - \dfrac{1}{N} \right)^{N - 1} 
$$
则间隔 $j$ 个 slot 的概率为
$$
P\{j \text{ unsuccessful attempts} \} \times P\{\text{1 successful attempt}\} = A(1-A)^j
$$
延迟 slot 的期望为
$$
\sum^{\infin}_{j = 1} jA(1-A)^j = \frac{1-A}{A}
$$
Max Utilization
$$
\begin{align}
U &= \frac{\text{frame time}}{\text{frame time + propagation time + average contention interval}} \\
&=\frac{1}{1 + \alpha + 2\alpha \times \dfrac{1- A}{A}}\\
&= \frac{1}{1 + \dfrac{2 - A}{A} \alpha}
\end{align}
$$
Let $N \rightarrow \infin, A = \dfrac{1}{e}$
$$
U = \frac{1}{1 + (2e - 1)\alpha} \approx \frac{1}{1 + 4.44\alpha}
$$

## Bridge and Layer-2 switch

### Bridge

目标：扩展单个局域网，**提供 LANs/WANs 之间的互联**

Bridge 的需求：

* Store & Forward：读取 LAN 上传输的 frame，抽取 MAC 地址，选择性地缓存地址为其他 LAN 的 frame，然后使用第二个 LAN 的 MAC 协议，重传各个 frame
* Transparent：对于结点来说 Bridge 是透明的
* Plug-and-play, self-learning：即插即用，自学习，减少配置复杂度

Bridge Protocol（IEEE 802.1D）

* 处于链路层，使用 MAC 地址寻址
* 不需要 LLC layer
* 能通过外部的 WAN 传输 frame

### Routing for Bridges

Bridge 需要决定是否转发以及向何 LAN 转发，因此需要一个转发表

而 Fix routing（即事先分配每个结点之间的路由）是没有实践性的

Bridge Protocol 的目标：

* 自动生成转发表
* 在发生变动时自动更新转发表 

#### Transparent Bridge

##### Frame Forwarding

转发表由三元组 `<MAC address, Port, Timestamp>` 组成

对于来自 Port X 的 frame，在转发表中搜索目的 MAC 地址对应的 Port

* 如果没有找到，则向 Port X 以外的所有 Port 转发该 frame
* 若转发表中的 Port 是 X，则丢弃该 frame（LAN 内）
* 若转发表中的 Port 是 Y，检查 Y 是 Block 状态还是 Forwarding 状态，如果是 Forwarding 状态则转发

问题：转发会产生循环，解决方法：使用生成树

##### Address Learning

原理：当 Port X 有 frame 时，这个 frame 是从与 Port X 相连的 LAN 来的。

故 **使用源地址更新转发表**

转发表中每个表项有对应的计时器，到时间则删去对应表项。每次有帧来时更新转发表，以此实现自学习和动态更新

##### Spanning Tree

为每个 Bridge 分配唯一的标识，Bridge 之间交换信息建立生成树

* 在 bridge 中选择一个 root bridge
* 为其余 bridge 选择一个 root port（到 root 最短路径的 port）
* 为每个 LAN 选择一个 designated bridge（到 root 最短路径的 bridge）
* LAN 和 designated bridge 之间连接的 port 为 designated port
* 所有 root port 和 designated port 置为 forwarding state
* 其余 port 置为 block state

#### Source Routing Bridge

用于连接 Token Ring

源结点决定路由，路由信息插入在 frame 中

路由过程：

* 每个结点广播一个 single-route broadcast frame，遍历所有 LAN 最终到达 destination
  * Bridge 必须配置为一个生成树（见上小节）
  * source 发送的 single-route frame 没有 route designator 字段
  * 第一跳的 bridge 添加 `<incoming LAN #, bridge #, outgoing LAN #>`
  * 之后的 bridge 在之后附加 `<bridge #, outgoing LAN #>`
* destination 发送 all-routes broadcast frame，生成到 source 的所有 route 路径
  * 第一跳的 bridge 添加 `<incoming LAN #, bridge #, outgoing LAN #>`
  * 之后的 bridge 在之后附加 `<bridge #, outgoing LAN #>`
  * 转发前检查 outgoing LAN 是否已经在 designator 字段，若在则停止转发（避免成环）
* source 在其中选择最佳 route

### Hubs

每个结点由两条线路连接到 hub（传输&接收）

hub acts as a reapter：当一个结点传输时，hub 将其信号发到其他所有节点

**Hub 物理上是星型拓扑，逻辑上是总线拓扑**

* 任何结点传输的 frame 会被其他所有结点收到
* 两个结点同时传输时发生碰撞（single collision domain）

### Layer-2 Switch

具有 Bridge 的功能，兼容 hub 和 bridge（均使用以太网 MAC 协议）

* Store & Forwarding
* Transparent
* Plug-and-play, self-learning

与 Bridge 的不同：

* Bridge：连接 LANs，通常只有 2-4 个 port
* Switch：连接多个主机/子网，有大量端口，且能提供**无碰撞传输**

#### multiple simutaneous transmission

* 每个结点有专用的线路连接到 switch
* switch 缓存并转发 frame
* 全双工，无碰撞（每个链路有独自的碰撞域，而由于 switch 缓存分组，故不会碰撞）
* 总传输速率为各端口传输速率之和

#### Types of Layer-2 Switch

Store-and-forward switch

* 从输入线路接收 frame
* **缓存**并向输出线路转发
* 产生 delay

Cut-through switch

* 适用于目的地址在帧开头的情况
* 识别出目的地址后立即在输出线路转发 frame
* 最高的吞吐量
* 可能会转发损坏的帧：不检查 CRC

### Layer-3 Switch

随着网络规模的增长，Layer-2 Switch 开始出现不足

**Broadcast overload**：由 Layer-2 Switch 连接起来的的 LANs 物理上成为一个网络，所有节点共享 MAC 广播地址，broadcast frame 会发送到所有连接的主机，广播情况下 switch 效率降低到 hub 级别，而 IP 协议会产生很多广播（ARP, DHCP, IGMP）

Lack of multiple paths：Layer-2 Switch 路由时为了不产生循环，使用生成树，任意两个节点间只有一条路径，限制了网络性能和可靠性

Layer-3 Switch：硬件上实现了转发 IP 包的逻辑

解决方法：

* 将 LAN 划分为不同的子网，子网间使用 Layer-3 Switch（带路由功能的 switch） 连接
* MAC broadcast frame 范围限制在子网内
* 允许子网间的多路径

Two Categories of Layer-3 Switch

* Packet by packet：工作方式与传统路由器相同， 但性能比基于软件的路由器提升一个量级
* Flow-based：提升 IP 分组流的性能

## Wireless Networks

### Wireless Networks

#### Elements of a Wireless Network

Wireless Hosts：终端，PC/手机/PDA等

Base Station：连接至有线网络，在有线网络和 Wireless Hosts 之间传播数据

Wireless Link：连接 host 和 base station，需要 MAC 协议

Handoff：base station 之间由有线网络连接， mobile host 移动中会更换 base station

#### Wireless Link Characteristics

Decreased signal strength：信号强度随着传播距离迅速衰减

Multipath propagation：广播信号会在物体上反射，在不同时间到达 destination（self-interfering）

Interference form other sources：2.4Ghz 的频率会被手机/微波炉等干扰

Robustness and security：容易被窃听

#### SNR & BER

SNR：signal-to-noise ratio，信噪比，越大越容易提取出信号

BER：bit error ratio，误码率，越低越好

对于给定的功率，提升功率 $\rightarrow$ 提升 SNR  $\rightarrow$ 降低  BER $\rightarrow$ 电池与温度限制

#### Ad-hoc Networking

peer-to-peer，没有 base station，节点间自己组织成网络

|                   |                          single hop                          |                         multiple hop                         |
| :---------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  infrastructure   | host connects to base station (WiFi, WiMAX, cellular) which connects to larger Internet | host may have to relay through several wireless nodes to connect to larger Internet: mesh net |
| no infrastructure | no base station, no connection to larger Internet (Bluetooth) | no base station, no connection to larger Internet. May have to relay to reach other a given wireless node MANET, VANET |

### WiFi - IEEE 802.11 Wireless LANs

#### IEEE 802.11 Architecture

Station: device with IEEE 802.11 conformant MAC and physical layer

Access Point (**AP**): Provides access to the distribution system via the wireless medium

Basic Service Set (BSS):
A single cell coordinated by one access point (base station)

Extended Service Set (ESS):

* Multiple BSSs interconnected by **Distribution System**(DS)
* DS can be a switch, wired network, or wireless network
* An ESS appearsas a **single logical LAN**
* Portals (routers) provide access to Internet

Distribution System (DS):
A system used to interconnect a set of BSSs and integrated LANs to create an (ESS)

参见 [IEEE 802.11][802.11]

#### IEEE 802.11: Channels, association

802.11b：2.4Ghz-2.485Ghz 的频率被分为 11 个不同的 channel，每个 AP 选择一个 channel，相邻 AP 若 channel 相同则会发生干扰（一般选择首尾和中间的 channel，最大程度避免干扰）

结点与 AP 的关联过程：

* 监听 channel 上的 AP 发出的 beacon frame（包含 AP 的 SSID 和 MAC 地址）
* 选择 AP 与之关联
* 认证（可选）
* 使用 DHCP 获得 AP 的子网中的 IP 地址

Passive Scanning：

* AP 发送 beacon frame
* 结点发送 Association Request
* AP 发送 Association Response

Active Scanning：

* 结点广播 Probe Request frame
* AP 回复 Probe Response frame
* 结点发送 Association Request
* AP 发送 Association Response

#### IEEE 802.11 Service

Distribution service: 通过 DS 在不同 BSS 间交换 frame

Integration service: 在 802.11 LAN 和 802.x LAN 之间传输数据

Authentication/Deauthentication: 连接中的认证

Privacy: 编码数据，防止窃取

Handoff 相关：

Association:

* 结点与 AP 间建立关联
* 确认身份和地址
* AP 与 其余 AP 通过 ESS 交流信息

Reassociation:

* 将建立的关联发送给其他 AP
* 允许结点在 BSS 间转移

Disassociation:

* 终止关联
* **ESS 之间的 handoff 不支持**

#### Hidden terminal

产生的问题：

* Hidden terminal & Signal fading：假设三个终端 A, B, C，BC, BA 间可互相听到，但 AC 间不能互相听到，A, C 同时向 B 传输时便会在 B 处产生干扰
* Exposed terminal：可以同时传输的情况下误以为会产生干扰，降低网络效率

解决方法：4 Frame Exchange（RTS/CTS）

* 源节点发送 Request to send（RTS）
* 目的节点回复 Clear to send（CTS）
* 收到 CTS 后源结点发送数据
* 目的节点回复 ACK

### IEEE 802.11 MAC

#### Media Access Control

Distributed coordination function(DCF): 分布式协调功能，分布式控制，传输异步数据，优先级最低

Point coordination function(PDF): 点协调功能，集中式控制，发送实时数据，优先级仅次于控制帧

#### 3-level Priority

帧间隔决定了帧的优先级

* SIFS (Short Inter Frame Space)
  * 优先级最高
  * 所有即时的回复
* PIFS (point coordination function IFS)
  * 中等长度 IFS，中等优先级
  * 用于 PCF 中的轮询
* DIFS (distributed coordination function IFS)
  * 最长的 IFS，优先级最低
  * 用于其他异步传输的数据

SIFS 的帧

* ACK
* Delivery of multiple frame LLC PDU：第一个帧正常 IFS，之后的序列使用 SIFS
* Poll response
* CTS：RTS 使用正常 IFS，CTF 则是 SIFS

PIFS 的帧（用于集中化控制）

* 发送轮询
* 优先于异步争抢
* SIFS 的帧优先于 PCF 的轮询

DIFS 的帧：其他一般的异步争用

#### Point Coordination Function (PCF)

由集中控制中心（点协调器）发布轮询（使用 PIFS），轮询时占据信道，阻塞其他异步通信

参见 [Point coordination function][PCF]

* 点协调器轮流询问结点
* 发布轮询请求时结点可使用 SIFS 回复
* 收到回复时，点协调器使用 PIFS 发送另一个请求
* 如果在时间内没有回复，询问下一个结点

Super frame：点协调器发布轮询时会占据信道封锁异步通信，为避免这种情况，定义 super frame，前半段时间点协调器轮询，后半段时间异步通信争用接入

#### Distributed Coordination Function (DCF) and CSMA/CA

使用 **CSMA/CA**，结点监听信道，**碰撞避免**

参见 [Carrier-sense multiple access with collision avoidance][CSMA/CA]

为何不是碰撞检测：

* 无线网络不是全双工，在发送时难以接收信号
* 发送结点不能区别收到的信号是否来自于噪声或自身传输的副作用
* 不能检测到所有碰撞的情况：Hidden terminal
* 使用 ACK 确认传输状态

CSMA/CA 流程

发送方：要发送 frame 的结点监听信道

* 如果空闲，等待 1 IFS 后监听是否仍空闲，如果空闲，则立即发送（不做碰撞检测）
* 如果繁忙，监听当前传输结束，**等待 1 IFS**
  * 如果仍空闲，退避随机时间后再次监听（[binary exponential backoff](#Binary exponential backoff)）
    * 如果退避后仍空闲，传输
    * 如果退避时信道繁忙，则暂停退避的计时，待空闲后继续，如果计时结束，则发送
    * 如果发送后没有收到 ACK，增大退避的时间，然后尝试重传

接收方：如果帧正常，以 SIFS 发送 ACK

#### Virtual Carrier Sensing

MPDU：Mac Protocol Data Unit，无线设备交换数据基本单元

**NAV**：Network Allocation Vector，MPDU 中的一个字段，标识传输这个 MPDU 需要多久

Virtual Carrier Sensing：

* 在 MPDU 中插入 NAV（标识信道将被占据的时间）
* 其他结点根据 NAV 中的值休眠一段时间，在此时间内不监听信道

#### IEEE 802.11 MAC Frames

##### Management frames

用于结点和 AP 之间交流

* Association & Disassociation
* Authentication & Deauthentication
* Timing & Synchronization

##### Control frames

* Power-Save Poll (PS-Poll): 结点发给 AP，当结点处于休眠状态时 AP 缓存传输给其的 frame
* RTS
* CTS
* ACK
* Contention-Free-End (CF-end): PCF 的 contention free 阶段结束的告知
* CF-end + CF-ACK

##### Data Frames - Data Carring

4 种，携带上层信息

* Data
* Data + CF-ACK
* Data + CF-Poll
* Data + CF-ACK + CF-Poll

4 种不携带信息

* Null function: 不携带信息，在控制字段携带 power management bit，告知结点进入低电量状态
* CF-ACK
* CF-Poll
* CF-ACK + CF-Poll

### Cellular Network

不做要求

Architecture

* base station
* mobile user
* MSC (mobile switching center)

多路技术：

* FDMA 与 TDMA 结合
* CDMA

2g，3g，4g

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

[802.11]: https://en.wikipedia.org/wiki/IEEE_802.11	"IEEE 802.11"

[PCF]: https://en.wikipedia.org/wiki/Point_coordination_function	"Point coordination function"

[CSMA/CA]: https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_avoidance	"Carrier-sense multiple access with collision avoidance"