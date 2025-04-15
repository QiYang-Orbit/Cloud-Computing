# ☁️ What are the three core AWS services that boto3 can control: EC2 / S3 / IAM?

## 1️⃣ EC2 (Elastic Compute Cloud) = Virtual Computers in the Cloud 💻
EC2 provides scalable computing capacity in the AWS cloud. You can think of EC2 as:

Cloud servers on AWS, like a cloud version of your home computer, that you can start, log into, and use anytime.

### ✅ Main uses:
- Run your programs (like AnnTools)
- Launch a Flask web server
- Deploy a website or backend API
- Run large-scale tasks (like training models)

### ✅ Example:
In your assignment, you used:

- One EC2 instance to run the web upload page
- Another EC2 instance dedicated to running AnnTools annotation tasks

### 💡 Analogy:
EC2 is like a computer in the cloud. AWS manages the power, hard drive, and network cables,
while you just need to connect remotely and deploy what you want to run.

## 2️⃣ S3 (Simple Storage Service) = Cloud Storage 🗂️
S3 is one of AWS's most famous services. It's not an ordinary folder system, but:

An object storage system without a traditional folder structure, perfect for storing files!

### ✅ Purpose:
- Store uploaded original VCF files
- Store generated .annot.vcf result files
- Store log files (.log)
- Permanent storage, not affected when EC2 instances are shut down

### ✅ Characteristics:
- Each file is called an "Object"
- Files are uniquely identified by keys (strings), without a real directory structure
- Fast read/write, resilient to power outages or crashes
- Very cost-effective (pay for what you store and use)

### 💡 Analogy:
S3 is like a super-robust cloud drive provided by AWS,
which only cares about the "name" of files, not how you organize directories.

## 3️⃣ IAM (Identity and Access Management) = Permission Manager 🛂
IAM is AWS's "gatekeeper":

A permission system responsible for "who can do what," controlling access to EC2, S3, Lambda, databases, and other services.

### ✅ Purpose:
- Assign permissions to EC2 instances (e.g., whether they can access S3)
- Generate AWS Access Keys and Secret Keys (used for signing requests)
- Ensure different people/services can only access their own data

### ✅ Example:
Your EC2 instance can access S3 because you assigned it an IAM Role; your generated POST upload form works because you signed it with a secret key (IAM user's credentials).

### 💡 Analogy:
IAM is the "key manager" and "security chief" of the AWS world.
Without its access pass, even an EC2 instance cannot touch S3.

|         boto3 - Python SDK 🐬          |
|------------------------------------------|
| It can control these AWS cloud services: |
|                                          |
| 🖥️ EC2 = Cloud computers (run programs/websites) |
| 📦 S3  = Cloud storage (store files/results/logs) |
| 🛂 IAM = Permission manager (who can do what)     |

# ☁️ boto3 能控制的三个核心 AWS 服务：EC2 / S3 / IAM 到底是什么？

## 1️⃣ EC2（Elastic Compute Cloud）= 云端电脑 💻
你可以把 EC2 理解成：

AWS 上的"云服务器"，就像你家电脑的云版本，随时开启、登录、使用。

### ✅ 它的主要用途：
- 跑你写的程序（比如 AnnTools）
- 启动一个 Flask Web 服务器
- 部署一个网站或后端 API
- 跑大规模任务（比如训练模型）

### ✅ 举个例子：
在作业中你用了：

- 一个 EC2 实例运行 Web 上传页面
- 一个 EC2 实例专门负责跑 AnnTools 注释任务

### 💡类比：
EC2 就像云上的电脑，AWS 帮你管电源、硬盘、网线，
你只管开机远程连上去，部署你要跑的东西。

## 2️⃣ S3（Simple Storage Service）= 云硬盘 🗂️
S3 是 AWS 最出名的服务之一，它不是普通文件夹，而是：

一个没有文件夹结构的"对象存储系统"，超适合存文件！

### ✅ 它的作用：
- 存上传的原始 VCF 文件
- 存注释完生成的 .annot.vcf 结果文件
- 存日志文件 .log
- 永久保存，不怕 EC2 实例关掉

### ✅ 特点：
- 每个文件叫一个 "Object"
- 用 key（字符串） 唯一标识文件，没有真的目录结构
- 快速读写，不怕断电或宕机
- 非常便宜（按存多少、用多少付费）

### 💡类比：
S3 就像是 AWS 给你配的超级坚固网盘，
它只关心文件的"名字"，不管你怎么组织目录。

## 3️⃣ IAM（Identity and Access Management）= 权限管理员 🛂
IAM 是 AWS 的"守门员"：

负责"谁能干什么"的权限系统，控制 EC2、S3、Lambda、数据库等服务的访问权限。

### ✅ 它的作用：
- 给 EC2 实例分配权限（比如能不能访问 S3）
- 生成 AWS Access Key 和 Secret Key（你用它来做签名）
- 确保不同人 / 服务只能访问自己的数据

### ✅ 举个例子：
你的 EC2 实例能访问 S3，是因为你给它分配了一个 IAM Role； 你生成的 POST 上传表单能用，是因为你用 secret key（IAM 用户的密钥）签了名。

### 💡类比：
IAM 是 AWS 世界的"钥匙管理员"和"警卫队长"，
没有它发的通行证，哪怕你是 EC2 也不能碰 S3。

## 🔁 再来一张总结图助记：
|         boto3 - Python 小海豚 🐬          |
|------------------------------------------|
| 它能控制这些 AWS 云服务：                  |
|                                          |
| 🖥️ EC2 = 云端电脑（跑程序 / 网站）          |
| 📦 S3  = 云网盘（存文件 / 结果 / 日志）      |
| 🛂 IAM = 权限管理员（谁能干什么）            |
