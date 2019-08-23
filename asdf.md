朱杰夫（总体）实习总结与评价表
   
实习生姓名/工号	朱杰夫 z50002506	部门	终端芯片方案平台开发部
思想导师姓名/工号	吕勇 l00203185	主管姓名/工号	王鹤鸣 w00210065
实习期培养目标：
序号	实习期培养目标
1	完成SLI识别小型化
2	完成SLI识别准确率95%
实习生总结	实习工作与培养总结（由实习生本人填写）                                            
工作任务及完成情况（工作输出、完成情况、创新及改进、待改进点）
6月成果：
1，	熟悉HiBerry和ADAS设计业务，学习caffe框架使用，着手开展对路标识别模型调优。
2，	分析数据集得出准确率提升空间在于解决路标类别分布不均问题，部分常见路标数据集占比远高于其他路标；模型较难以区分限速标志限重标志，因为从外观上这几种标志非常相近，需要做负样本处理。
3，	截至月末对模型完成初步裁剪，性能上升两倍有余，同时对数据集进行了粗糙分析和处理，使准确率不降反升，对部分图片占比特别小的路标检测置信度提升显著。然而同时引发了一个弊端，在检测时出现了一部分目标标定了多个检测框的问题，这是由于推理脚本未做NMS极大值抑制导致的，后期部署到单板上可做出相应优化。
4，	拟定了ADAS第二阶段车辆检测目标的实施方案：先用 caffe-ssd 原模型对 KITTI 单独训练车辆识别，在用此训练好的模型对 TT100K 数据集中的车辆进行预测和标注，这样 TT100K 数据集就同时拥有路标和车辆的标注了，最后再将两个数据集以合适比例混合加入训练，截止到实习结束此阶段目标仍在尝试中。
7月成果：
1，	应7月初因芯片性能限制提出的模型大小规格，完成对模型的裁剪，使模型由90M缩小为2.5M，精确度有中幅下滑，7月主要工作便为提高小模型精度。
2，	针对测试结果和场景分析，部署并优化DenseNet+SSD模型，在17类限速标志数据集上识别精确度达95.4%（原90M模型为89%），提前完成最终95%的目标，最小可识别目标为12x12px，高于15x15px的规格要求，目前模型在测试码流上表现良好。
3，	完成一体化生成数据集脚本的编写，并确定tt100k数据集优化切割版本。
4，	协助负责测试的项目组成员进行测试集生成和处理，完成对数据集特征的精确统计。
5，	总结华山平台（云训练平台）的使用经验，完成《华山平台使用手册》编写并分享到项目组。
8月成果：
1，	对测试结果进一步分析，发现所用数据集中的原始标注错误已经切图算法不完善所致的图片边缘GroundTruth错误，对数据集完成除错，修改切图算法。在最终训练集上训练结果可得GRP-DOSD模型精度达97.5%，SSD达93.8%。然而由于GRP-DSOD算法中存在大量上下采样操作和1x1卷积核，导致实时性严重不够，可能需要退而求其次使用SSD算法。
2，	完成模型效果对比表的撰写，详细记录了相关参数的调试以及对应的结果，相应将各模型最佳结果已超链接形式保存并归档。
3，	完成caffe记录每层的推理所需时间统计，caffemodel权值可视化。
4，	接手新任务，为融合网开始对车道线检测算法的调研，因为传统算法所耗资源少响应快的优点，同时NPU上尽量不要跑并行的深度学习任务，首先尝试使用传统算法对车道线检测。通过阅读大量论文，尝试近三年发表的算法，发现传统算法的弊端是在图像变形矫正这一步传统算法鲁棒性极差，在获得视角转换的过程中需要在原图中确定四个点（这四个点在视角转换之后为矩形），需要应对不同场景和路况甚至行车记录仪安装位置手动进行调节，同时传统算法几乎不具备对被遮挡的车道线进行预测的能力。调研可总结为传统的车道检测方法依赖于高度定义化，手工特征提取和启发式方法，通常是需要后处理技术，而这往往会使得计算量大，不利于道路场景多变下的应用扩展，因此大致放弃传统算法的车道线检测。
5，	开始对基于深度学习算法的车道线检测调研，尝试State-of-Art的Lanenet和SCNN。发现基于Tusimple数据集训练的主干网为VGG的Lanenet对于其他场景的数据集鲁棒性极差，SCNN鲁棒性较好。但是由于这两个算法参数空间太大同时实时性也很差，我尝试将Lanenet的主干网更换成Enet并将两个车道线数据集融合训练，所得效果较为理想。然而算法仍有瑕疵，到Lanenet聚类这一步检测都没有问题，但是用Hnet拟合车道线出现较大偏差。结论为基于深度学习的车道线检测算法中，将SCNN和Lanenet的主干网替换为轻量化的Enet或是darknet都具有使用价值，需根据需求对数据集处理和融合再进行训练。
6，	截至实习期结束一共贡献了21份深度学习模型算法，在华山平台上进行了约86次训练任务，上传了37个数据集版本。
7，总结学术界的车道检测算法研究进展的调研结果，输出实习所得经验和成果，完成工作交接以及汇报展示。
工作交接展望：
1，	若需进一步提高SSD精度，需要重新再ImageNet上预训练模型，同时增加数据集对mAP的增加是最明显的，Aspect Ratio尺度增加也有提升，但是会增加先验框数量，拖慢推理速度。
2，	目前目标检测数据增强这一块缺少仿射变换，旋转增强
3，	贴图脚本已经完善且视觉效果合理，但是用补充的贴图对模型进行Finetune效果较差，原因未知，有待进一步考察。
4，	训练所得的Lanenet模型可轻松转换为caffemodel部署到单板上。
5，	车辆检测任务任重而道远，目前结果来看Yolo和SSD在Kitti车辆数据集上训练所得模型的精确度和鲁棒性均不理想，考虑到第二阶段需要同时检测车辆和路标，还需对网络结构做出较大调整。
思想导师评价	实习生在实习期的工作表现对其劳动态度和工作绩效进行评价：        
实习生在职期间，对待工作任务积极主动，对问题解决能够举一反三，进行了深入思考，并落实在实际工作中;对短时间内有挑战性的新目标，逻辑清晰，快速有效的输出模型训练结果，主动积极进行性能对比评估和性能优化；对项目工作进度做出了重要贡献，个人认为可评价为优秀实习生。

关键事件举证：
1.	在平台flash内存存在硬限制条件下，敢于深入尝试，通过通道深度裁剪压缩，满足精度不下降和模型大小小于2M的限制，最小达到了900k
2.	针对小模型下部分图片无法识别问题，广泛收集可行性方案，分析论文，通过限制mini ratio大小进行模型调优，数据集优化，解决了跳帧漏识别问题
3.	对提升模型识别精度到95%的要求，实习生表现出很大积极性和主动性，进行了大量ssd现状最优模型分析，在小模型限制条件下，通过densenet+ssd部署初步实现了目标。
4.	善于主动总结，输出数据处理通用脚本，华山平台使用指导，积极输出当前训练所有检测模型对比分析结果。
5.	分析网络测试结果，优化切图算法，完善测试集测试准确度，并进一步通过GRP-DOSD优化当前SSD网络，训练集上模型精度最高可达到97.5%
6.	独立验证了基于传统opecncv算法和深度学习算法的车道线检测的实际效果，分析输出传统算法优缺点，并对深度算法State-of-Art的文章进行了实例验证和对比分析，基于分析结果进行了性能和准确率方向的网络优化，为后续功能实际产品化提供的珍贵的参考输入。
7.	上述”实习生总结”内容真实反映了实习期间的工作成果。



姓名：                   
项目组长评价	













姓名：                   
项目经理评价	积极主动、动手能力强，工作聚焦并且效率高。输出成果对本项目后续重点特性ADAS的交付起到原型验证和关键技术突破的作用，其中目标检测网络小型化方面的成果可直接落入后续交付版本，车道线检测原型验证等工作对后续方案选型起到重要作用。

姓名：                   
部门主管评价	

















姓名：                   

日期：   2019  年 08 月 23 日
说明：
本表为实习生实习总结与评价，先由实习生完成实习总结，再由思想导师给出实习评价，最后部门主管给出总体评价，并给出实习录用建议。
此表格即可用实习生月度总结，也可用于实习期总体总结。























######################################################
朱杰夫（总体）实习总结与评价表
   
实习生姓名/工号	朱杰夫 z50002506	部门	终端芯片方案平台开发部
思想导师姓名/工号	吕勇 l00203185	主管姓名/工号	王鹤鸣 w00210065
实习期培养目标：
序号	实习期培养目标
1	完成SLI识别小型化
2	完成SLI识别准确率95%
实习生总结	实习工作与培养总结（由实习生本人填写）                                            
工作任务及完成情况（工作输出、完成情况、创新及改进、待改进点）
6月成果：
1，	熟悉HiBerry和ADAS设计业务，学习caffe框架使用，着手开展对路标识别模型调优。
2，	分析数据集得出准确率提升空间在于解决路标类别分布不均问题，部分常见路标数据集占比远高于其他路标；模型较难以区分限速标志限重标志，因为从外观上这几种标志非常相近，需要做负样本处理。
3，	截至月末对模型完成初步裁剪，性能上升两倍有余，同时对数据集进行了粗糙分析和处理，使准确率不降反升，对部分图片占比特别小的路标检测置信度提升显著。然而同时引发了一个弊端，在检测时出现了一部分目标标定了多个检测框的问题，这是由于推理脚本未做NMS极大值抑制导致的，后期部署到单板上可做出相应优化。
4，	拟定了ADAS第二阶段车辆检测目标的实施方案：先用 caffe-ssd 原模型对 KITTI 单独训练车辆识别，在用此训练好的模型对 TT100K 数据集中的车辆进行预测和标注，这样 TT100K 数据集就同时拥有路标和车辆的标注了，最后再将两个数据集以合适比例混合加入训练，截止到实习结束此阶段目标仍在尝试中。
7月成果：
1，	应7月初因芯片性能限制提出的模型大小规格，完成对模型的裁剪，使模型由90M缩小为2.5M，精确度有中幅下滑，7月主要工作便为提高小模型精度。
2，	针对测试结果和场景分析，部署并优化DenseNet+SSD模型，在17类限速标志数据集上识别精确度达95.4%（原90M模型为89%），提前完成最终95%的目标，最小可识别目标为12x12px，高于15x15px的规格要求，目前模型在测试码流上表现良好。
3，	完成一体化生成数据集脚本的编写，并确定tt100k数据集优化切割版本。
4，	协助负责测试的项目组成员进行测试集生成和处理，完成对数据集特征的精确统计。
5，	总结华山平台（云训练平台）的使用经验，完成《华山平台使用手册》编写并分享到项目组。
8月成果：
1，	对测试结果进一步分析，发现所用数据集中的原始标注错误已经切图算法不完善所致的图片边缘GroundTruth错误，对数据集完成除错，修改切图算法。在最终训练集上训练结果可得GRP-DOSD模型精度达97.5%，SSD达93.8%。然而由于GRP-DSOD算法中存在大量上下采样操作和1x1卷积核，导致实时性严重不够，可能需要退而求其次使用SSD算法。
2，	完成模型效果对比表的撰写，详细记录了相关参数的调试以及对应的结果，相应将各模型最佳结果已超链接形式保存并归档。
3，	完成caffe记录每层的推理所需时间统计，caffemodel权值可视化。
4，	接手新任务，为融合网开始对车道线检测算法的调研，因为传统算法所耗资源少响应快的优点，同时NPU上尽量不要跑并行的深度学习任务，首先尝试使用传统算法对车道线检测。通过阅读大量论文，尝试近三年发表的算法，发现传统算法的弊端是在图像变形矫正这一步传统算法鲁棒性极差，在获得视角转换的过程中需要在原图中确定四个点（这四个点在视角转换之后为矩形），需要应对不同场景和路况甚至行车记录仪安装位置手动进行调节，同时传统算法几乎不具备对被遮挡的车道线进行预测的能力。调研可总结为传统的车道检测方法依赖于高度定义化，手工特征提取和启发式方法，通常是需要后处理技术，而这往往会使得计算量大，不利于道路场景多变下的应用扩展，因此大致放弃传统算法的车道线检测。
5，	开始对基于深度学习算法的车道线检测调研，尝试State-of-Art的Lanenet和SCNN。发现基于Tusimple数据集训练的主干网为VGG的Lanenet对于其他场景的数据集鲁棒性极差，SCNN鲁棒性较好。但是由于这两个算法参数空间太大同时实时性也很差，我尝试将Lanenet的主干网更换成Enet并将两个车道线数据集融合训练，所得效果较为理想。然而算法仍有瑕疵，到Lanenet聚类这一步检测都没有问题，但是用Hnet拟合车道线出现较大偏差。结论为基于深度学习的车道线检测算法中，将SCNN和Lanenet的主干网替换为轻量化的Enet或是darknet都具有使用价值，需根据需求对数据集处理和融合再进行训练。
6，	截至实习期结束一共贡献了21份深度学习模型算法，在华山平台上进行了约86次训练任务，上传了37个数据集版本。
7，总结学术界的车道检测算法研究进展的调研结果，输出实习所得经验和成果，完成工作交接以及汇报展示。
工作交接展望：
1，	若需进一步提高SSD精度，需要重新再ImageNet上预训练模型，同时增加数据集对mAP的增加是最明显的，Aspect Ratio尺度增加也有提升，但是会增加先验框数量，拖慢推理速度。
2，	目前目标检测数据增强这一块缺少仿射变换，旋转增强
3，	贴图脚本已经完善且视觉效果合理，但是用补充的贴图对模型进行Finetune效果较差，原因未知，有待进一步考察。
4，	训练所得的Lanenet模型可轻松转换为caffemodel部署到单板上。
5，	车辆检测任务任重而道远，目前结果来看Yolo和SSD在Kitti车辆数据集上训练所得模型的精确度和鲁棒性均不理想，考虑到第二阶段需要同时检测车辆和路标，还需对网络结构做出较大调整。
思想导师评价	实习生在实习期的工作表现对其劳动态度和工作绩效进行评价：        
实习生在职期间，对待工作任务积极主动，对问题解决能够举一反三，进行了深入思考，并落实在实际工作中;对短时间内有挑战性的新目标，逻辑清晰，快速有效的输出模型训练结果，主动积极进行性能对比评估和性能优化；对项目工作进度做出了重要贡献，个人认为可评价为优秀实习生。

关键事件举证：
1.	在平台flash内存存在硬限制条件下，敢于深入尝试，通过通道深度裁剪压缩，满足精度不下降和模型大小小于2M的限制，最小达到了900k
2.	针对小模型下部分图片无法识别问题，广泛收集可行性方案，分析论文，通过限制mini ratio大小进行模型调优，数据集优化，解决了跳帧漏识别问题
3.	对提升模型识别精度到95%的要求，实习生表现出很大积极性和主动性，进行了大量ssd现状最优模型分析，在小模型限制条件下，通过densenet+ssd部署初步实现了目标。
4.	善于主动总结，输出数据处理通用脚本，华山平台使用指导，积极输出当前训练所有检测模型对比分析结果。
5.	分析网络测试结果，优化切图算法，完善测试集测试准确度，并进一步通过GRP-DOSD优化当前SSD网络，训练集上模型精度最高可达到97.5%
6.	独立验证了基于传统opecncv算法和深度学习算法的车道线检测的实际效果，分析输出传统算法优缺点，并对深度算法State-of-Art的文章进行了实例验证和对比分析，基于分析结果进行了性能和准确率方向的网络优化，为后续功能实际产品化提供的珍贵的参考输入。
7.	上述”实习生总结”内容真实反映了实习期间的工作成果。



姓名：吕勇 00203185
项目组长评价	













姓名：            
项目经理评价	积极主动、动手能力强，工作聚焦并且效率高。输出成果对本项目后续重点特性ADAS的交付起到原型验证和关键技术突破的作用，其中目标检测网络小型化方面的成果可直接落入后续交付版本，车道线检测原型验证等工作对后续方案选型起到重要作用。

姓名：吉沐舟 00375055 
部门主管评价	

















姓名：            

日期：   2019  年 08 月 23 日
说明：
本表为实习生实习总结与评价，先由实习生完成实习总结，再由思想导师给出实习评价，最后部门主管给出总体评价，并给出实习录用建议。
此表格即可用实习生月度总结，也可用于实习期总体总结。
#######################################
实习证明


兹证明：
北京邮电  大学 电子工程  学院 电子信息科学与技术  专业  朱杰夫  同学（学号：2016210843），身份证号 310110199804113214 ，于2019年6月3日至2019年8月23日在华为技术有限公司实习，该同学的实习职位是：通用软件开发工程师。
该同学在实习期间严格遵守我公司的各项规章制度，服从实习安排，积极完成实习任务，实习表现优秀，特出具此实习证明函。



证明人：    吕勇   电话（13621713912）
      2019年08月23日
