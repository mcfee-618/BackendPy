
## info 命令

Redis Info 命令以一种易于理解和阅读的格式，返回关于 Redis 服务器的各种信息和统计数值。

* 主要信息构成：server一般 Redis 服务器信息、clients已连接客户端信息、memory内存信息、持久化信息、Stats信息、Replication信息、CPU信息、Keyspace信息

## object 命令
OBJECT 命令允许从内部察看给定 key 的 Redis 对象。OBJECT 命令有多个子命令：

* OBJECT REFCOUNT <key> 返回给定 key 引用所储存的值的次数。此命令主要用于除错。
* OBJECT ENCODING <key> 返回给定 key 锁储存的值所使用的内部表示(representation)。
* OBJECT IDLETIME <key> 返回给定 key 自储存以来的空转时间(idle， 没有被读取也没有被写入)，以秒为单位。

## debug 命令

debug object myhash

关于输出的项的说明：
```
    Value at：key的内存地址
    refcount：引用次数
    encoding：编码类型
    serializedlength：序列化长度
    lru_seconds_idle：空闲时间
```
注意事项：
```
serializedlength是key序列化后的长度(redis在将key保存为rdb文件时使用了该算法)，并不是key在内存中的真正长度。
这就像一个数组在json_encode后的长度与其在内存中的真正长度并不相同。不过，它侧面反应了一个key的长度，可以用于比较两个key的大小。
redis的官方文档不是特别建议在客户端使用该命令，可能因为计算serializedlength的代价相对高。所以如果要统计的key比较多，就不适合这种方法
```

## scan 命令


SCAN cursor [MATCH pattern] [COUNT count]
SCAN 命令的回复是一个包含两个元素的数组，第一个数组元素是用于进行下一次迭代的新游标，而第二个数组元素则是一个数组，这个数组中包含了所有被迭代的元素。scan 相比 keys 具备有以下特点:

* 复杂度虽然也是 O(n)，但是它是通过游标分步进行的，不会阻塞线程;
* 提供 limit 参数，可以控制每次返回结果的最大条数，limit 只是一个 hint，返回的结果可多可少;
* 同 keys 一样，它也提供模式匹配功能;
* 服务器不需要为游标保存状态，游标的唯一状态就是 scan 返回给客户端的游标整数;
* 返回的结果可能会有重复，需要客户端去重复，这点非常重要;
* 遍历的过程中如果有数据修改，改动后的数据能不能遍历到是不确定的;
* 单次返回的结果是空的并不意味着遍历结束，而要看返回的游标值是否为零;

```
迭代过程：当 SCAN 命令的游标参数被设置为0时，服务器将开始一次新的迭代， 而当服务器向用户返回值为0的游标时，表示迭代已结束。
count参数：因为这个 limit 不是限定返回结果的数量，而是限定服务器单次遍历的字典槽位数量(约等于)。
```