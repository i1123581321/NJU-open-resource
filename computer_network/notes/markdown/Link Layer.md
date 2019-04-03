# 链路层

## Link Service and Framing

### 链路层实现

Link 种类：

* Wired
  * point-to-point
  * multiple access (LAN)
* Wireless (WIFI)

链路层硬件：网络适配器（Adapter），网卡（NIC, Network Interface Card）

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

* 常规释放：收到 ACK 后释放
* 早期释放：发送完最后 1 bit 之后直接释放

### FDDI Token Ring

使用双环结构，传输方向相反。内环空闲，出错时切换到内环

[Duplex]: https://en.wikipedia.org/wiki/Duplex_(telecommunications)	"Duplex"
[SWP]: https://en.wikipedia.org/wiki/Sliding_window_protocol	"Sliding Window Protocol"
[CRC]: https://en.wikipedia.org/wiki/Cyclic_redundancy_check	"Cyclic Redundancy Check"

[HDLC]: https://en.wikipedia.org/wiki/High-Level_Data_Link_Control	"High-Level Data Link Control"
[PPP]: https://en.wikipedia.org/wiki/Point-to-Point_Protocol	"Point-to-Point Protocol"
[TR]: https://en.wikipedia.org/wiki/Token_ring	"Token ring"

