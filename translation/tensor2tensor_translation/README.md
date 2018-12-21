# AI_Challenger 
训练基本中去掉了batch_size项，改用 --worker_gpu_memory_fraction 可以免去内存溢出风险。

# Requirenments

- python 3.6
- TensorFlow 1.12.0
- tensor2tensor
- jieba 0.39
 mkdir    t2t_tmp   t2t_data  raw_data
1、下载数据
解压后放入raw_data，所有官方数据都放入一个文件夹以方便处理
unzip  raw_data.zip   -C raw_data

2 定义新问题
 参考  https://blog.csdn.net/hpulfc/article/details/81172498
 新问题在./ai_data目录
 
3、语料预处理与向量化
sh  ./prepare.sh
sh  ./data_gen.sh

4、 训练模型 big 效果好于 base
big 模式   sh  train_big.sh
base 模式   sh  train_base.sh

5、翻译
将t2t_data里面的字典文件拷贝到 ./dict_path （一定要用自己的）,然后预测。（因为翻译时只用到字典，也可指定t2t_data目录）
big 模式   sh  decode_big.sh
base 模式   sh  decode_base.sh

后续提交处理参照
https://github.com/dreamnotover

# References

https://github.com/dreamnotover

Attention Is All You Need

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin

Full text available at: https://arxiv.org/abs/1706.03762

Code availabel at: https://github.com/tensorflow/tensor2tensor

parameter   https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/utils/flags.py
