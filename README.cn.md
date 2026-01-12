# Blender 扩展: Auto Dance Camera
一个舞蹈动画经常有5000-7000帧，如果手动创建镜头运动会非常麻烦。  

**该Blender扩展能够一键生成整个跳舞动画的镜头数据。它生成专业水准的镜头，并包含4x3x3x3x5=540种镜头组合方式。**  

**因此，你再也不用找镜头数据，或手动为跳舞动画制作镜头运动了。**  

![英文](img/addon_en.jpg)  ![中文](img/addon_cn.jpg)  


# 演示视频
[![Demo Video](img/AutoDanceCamera-Thumb-270P.jpg)](https://youtu.be/pPet4skBmNw)  
b站：  
[https://www.bilibili.com/video/BV1HR4y1A7TG/](https://www.bilibili.com/video/BV1HR4y1A7TG/)  

一整首歌的镜头演示视频:  
[![Full Song Demo](img/ChunQin7086_thumb.jpg)](https://www.youtube.com/watch?v=K-Qp99zPrwA)  
b站：  
[https://www.bilibili.com/video/BV15T4y167xg](https://www.bilibili.com/video/BV15T4y167xg)  

**导出Vmd文件，用于MMD的演示视频：**   
[![Export Vmd Demo](img/AutoDanceCamera-Thumb-2-270p.png)](https://youtu.be/D4ruacU49bM)   
b站：  
[https://www.bilibili.com/video/BV14T411N7oF](https://www.bilibili.com/video/BV14T411N7oF)  

# 关键信息
### 下载
**爱发电：**  
[https://afdian.net/item/788e0fa4d2c411ed8e0752540025c377](https://afdian.net/item/788e0fa4d2c411ed8e0752540025c377)  
购买后，会收到站内信，里面是网盘下载地址  

**Blender市场：**  
[https://blendermarket.com/products/auto-dance-camera](https://blendermarket.com/products/auto-dance-camera)  

微博专栏：（已废弃，不推荐）:  
[微博专栏](https://m.weibo.cn/c/wbox?id=wqh75bb2ni&appName=%E6%96%87%E7%AB%A0%E4%B8%93%E6%A0%8F&appIcon=&topNavMode=0&cid=7621648315881473&click_from=share)  

如果爱发电没有问题，微博渠道将在1个月后撤销，已经购买的用户不受影响。  

以上3种方式均可，一样的。


### Github
Github项目池只有文档，用于交流，不含有扩展代码  
[https://github.com/butaixianran/Blender-Auto-Dance-Camera](https://github.com/butaixianran/Blender-Auto-Dance-Camera)  

### 版本
本扩展: 2.4.3  
Blender: 3.0或以上

# 功能
* **全自动为舞蹈动画，生成摄像机运动**
* **（新）导出摄像机运动为vmd文件，可用于MMD中**
* **（新）导出摄像机运动为duf文件，可用于Daz Studio**
* **（新）从歌曲提取节奏，来生成适配音乐的镜头运动(仅限Windows 64位)**
* 可重新生成指定片段的镜头运动
* 可调节镜头移动速度，最大最小镜头长度，因此既能用于跳舞动画，也能用于抒情慢歌 
* 允许只生成正面镜头(利于合成)
* 结合4x3x3x3x5=共540种镜头组合，但不合适的会过滤掉，只会生成和人物当前姿势匹配的动作
* 跟踪人眼，以防止人物跑出画面
* 自定义偏移，从而适配各种人模

# 安装
* 安装你得到的.zip文件
* 在扩展列表中，搜索 "Auto Dance Camera" 并启用
* 视图区域按N，右侧点开"Auto Dance Camera"面板即可

如果你是Blender新手，不知道如何安装扩展，请网络搜索"Blender 安装扩展"  

# 支持的人模
**任何类型。** 本扩展内建支持人模：**Daz, CC3, MMD, Rigify, Mixamo**  

如果你的人模不是其中一种，只需在扩展面板勾选"Pick Bone"，并选择对应骨骼后，即可使用。    
![pick bone](img/addon_pick_bone.jpg)


# 使用方法
## 生成摄影机运动
* 在扩展面板上，用吸管选择你的人模
* 点击下方 "生成" 按钮，完成

在你当前Collection下，会新建一个叫"Auto Dance Camera"的相机，带有运动数据，并自动设置为当前相机。  

## 导出到MMD
* **选择一个摄影机**（或它的空父亲对象，也可以）
* 点击"导出Vmd"，保存，完成

现在，你选择的摄影机上的运动，就保存在了这个vmd文件中，可以用于mmd。  

## 导出到Daz Studio
* **选择一个摄影机**（或它的空父亲对象，也可以）
* 点击"导出到Daz"，保存，完成
* Daz中， **选择一个摄影机**, 加载刚才保存的.duf文件  

**不是本扩展生成摄影机，也可以导出！** 这意味着，你可以通过Vmd Retargeting扩展导入MMD的摄影机，再通过本扩展导出到Daz Studio。  

## 使用歌曲的节奏(仅限Windows 64位)
现在，本扩展提供了一个工具，能从音频中提取节奏，并保存为一个节奏文件。   

然后，在本Blender扩展中，你可以加载这个节奏文件，来生成适配这个音乐的摄影机动作。   
![pick bone](img/audio_beat.jpg)    

我们专门为此制作了一个视频教程：  
[https://youtu.be/o__1969y688](https://youtu.be/o__1969y688)   
b站：  
[https://www.bilibili.com/video/BV1j24y197jv/](https://www.bilibili.com/video/BV1j24y197jv/)  

首先，在你下载扩展的地方，文件列表中，有个叫"**Audio Beat**"的zip文件。下载后，解压，运行。  

工具界面上，选择你的歌曲，点击"Generate Beats"，并等待。  

完成后，节奏文件会保存在你的歌曲同目录下，名命为："歌曲文件名_beat.npy"。  

现在，在Blender中，在Auto Dance Camera扩展面板上，勾选"使用节奏文件"，并加载这个节奏文件。然后，就可以点击生成了。  

对于同一首歌，你可以反复用这个节奏文件，而无需重复提取。  

### Audio Type (音频类型)
工具上，音频类型选项，有3种：song (歌曲), vocal (纯人声), music (纯音乐)。选择正确的类型，才能得到更好的提取结果。  

### 通过机器学习的AI提取人声
这个叫audio_beat的工具，需要依靠从歌曲中提取人声，来得到音乐节奏。  

本工具内置是用音频过滤器实现的，而不是靠机器学习的AI。所以，有时候提取结果就不是很好。  

但是，如果我打包AI到这个工具中，这个工具就会有大约3.5GB。对于这种小工具来说，太夸张了。  

**所以，如果你真的需要得到最佳的节奏，你可以使用其他基于AI的音频工具，从歌曲中提取人声。然后把提取的纯人声，用于这个audio_beat工具，来生成节奏。**  


**有两种方法，来从歌曲中提取人声**  
1. 免费的基于AI的网络服务 (推荐)  
有很多网站提供这种免费服务。只需要上传歌曲，下载提取的人声和音乐即可。比如：  
[https://vocalremover.org/](https://vocalremover.org/)  

2. 或者，下载免费的基于AI的音频处理工具到的电脑上。   
同样有大量免费工具。比如:  
[https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README_CN.md](https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README_CN.md)  

注意，基于AI的音频处理工具，工具尺寸一般都在3GB以上。请自己斟酌。      

当你得到分离的人声和音乐后，该把哪个用于audio_beat工具？  

**大部分时候，用纯人声效果最好。但如果你不确定的话，可以选择Audio Type为Both，就是两个都用。然后分别选择AI提取的纯人声和音乐文件。**   
![pick bone](img/audio_beat_audio_type_both.jpg)    


# 技巧
* **移动相机的空父亲对象**，可整体调整镜头  
* **可多次点击生成按钮**，然后从生成的镜头中，选择你最喜欢的
* **对于抒情慢歌**，设置镜头长度为最小3秒，最大5秒，速度为0.004比较好
* 选择生成的摄影机，勾选"使用已选择的摄影机"，设置起始帧，**就能反复重新生成这一小段**，直到得到你喜欢的镜头


## Apply Transform 问题
如果你使用Mixamo，或任何其他在导入时没有替你"Apply Transform Rotation"的人模，那么你在使用人模前，需要应用transform。  

只需选择人模骨架，按`ctrl+A`，选择`Rotation`即可完成转换

# 支持的摄像机运动方式
扩展会尝试把人眼放在镜头的上1/3区域，就像专业摄影师那样。  

如果人模在单个镜头中快速移动，它会尝试跟随  

* 支持的镜头类型有：全景，中景，下半身中景，近景  
* 支持的旋转类型有：固定，上下左右4个方向旋转  
* 支持的移动方式有：固定，缩放，左右平移，上移  


扩展会分析人模的姿势，并排除不适合该姿势的镜头组合，然后从剩下的组合中随机选择。  

镜头长度也是随机生成。  

# 非跳舞动画
把镜头持续时间设置得更长，就能用于其他场合。  


# 选项
## 选择骨骼
如果你的人模不是 "`Daz, CC3, MMD, Rigify, Mixamo`" 中的一种，你就需要勾选这个选项，并选择对应骨骼名字，本扩展才能用    

![pick bone](img/pick_bone.jpg)  

## 镜头长度
最大最小镜头长度，单位是秒。扩展会根据你项目的fps设置，换算成帧数  

默认值用于跳舞歌曲，用于抒情慢歌的话，最小长度为3秒，最大为5秒，会比较好  

## 镜头移动速度
默认是每帧0.008米，这是跳舞歌曲的设置。抒情慢歌的话，设为0.004比较好  

## 允许旋转
去掉后，就只会生成正面镜头。有利于做合成视频。  

## 偏移
可以指定偏移，或，直接调整生成的摄影机的空父亲对象  

## 镜头出现概率
下半身镜头对准腿部，既可能显得性感，也可能是很差的镜头选择。因此，有时候你会希望减少下半身镜头数量   

它的出现概率，是0.25/本选项的数值。也就是说，本选项的数值越大，出现的该镜头就越少。    

近景镜头概率选项也是同理  

## 上半身镜头出现倍率
这个值越大，上半身镜头就越多。  

默认值是2。如果设为3，差不多有一半镜头就是上半身镜头。很多时候，这是好事。在很多真实MV中，有超过1/3的镜头是上半身镜头。因为这样有助于突出歌手。    

## 使用项目帧范围
去掉勾选后，可以指定要生成的帧范围  

## 使用当前选择的摄影机
这个选项非常强大，勾选后，它能够将生成的运动，添加到你当前选择的摄像机。  

如果这个摄像机上，已经有镜头运动了，比如，一个本扩展生成的摄像机。那么，扩展会只清除你指定范围内的帧数据，并把新的运动，只添加到这个范围内。  

这意味着，如果生成的完整数据中，有某个镜头你不喜欢，你可以选择这一小段，反复点击本扩展的生成按钮，直到生成一个能接受的镜头  


# 常见问题
## 人物跑出画面
本扩展并不是在每一帧都跟踪眼球。而是只在每个镜头的第一帧 和 最后一帧检查眼球位置。  

所以，如果人物在单个镜头内，快速移动离开镜头，又快速回来。那么本扩展将无法察觉。  

每帧都追踪眼球将导致生成巨慢无比，不可接受。比较高效的办法，是对于这种情况，直接重新生成一个全身镜头即可。  


# 更新日志
## 2.4.3
* 允许beat文件用于指定的摄影机

## 2.4.1
* 修复bug，当生成最后一个镜头移动以后，如果剩余的帧数不足以生成下一个镜头移动，则延长前一个镜头移动到结尾

## 2.4.0
* 支持Blender 5
* Blender 5开始，Action下多了一层Slot。本扩展只处理第一个Slot
## 2.3.1
* 防止摄影机落到地面下方

## 2.3
* 支持导出相机到Daz

## 2.2
* 支持从音乐提取的节奏，来生成摄影机运动
* 添加上半身镜头出现倍率

## 2.0.1
* 修复当人物一直保持坐姿时，才会出现的多个随机方法bug。

## 2.0.0
* 支持导出摄影机运动为 vmd 文件，从而用于mmd中

## 1.0.0
* 添加i18n
* 添加"Pick bone"选项
* 第一个发布版本


