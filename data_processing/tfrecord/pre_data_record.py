import tensorflow as tf
import codecs


def _int64_feature(value):
    """生成整数数据属性"""
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


def _float32_feature(value):
    """生成浮点数数据属性"""
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def _bytes_feature(value):
    """生成字符型数据属性"""
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))


def _read_vocab(filename):
    """读取词汇列别"""
    words = list(map(lambda line: line.strip(), codecs.open(filename, 'r', encoding='utf-8').readlines()))
    word_to_id = dict(zip(words, range(len(words))))
    return words, word_to_id


# def get_data(origin_data, num_word):
#     """将大文件拆分"""
#     flag = 0
#     name = 0
#     data_list = []
#     filename_list = []
#     with open(origin_data, 'r', encoding='utf-8')as f:
#         for line in f.readlines():
#             flag += 1
#             data_list.append(line)
#             if flag == num_word:
#                 with open('re_data_' + str(name), 'w+', encoding='utf-8')as f1:
#                     for data in data_list:
#                         f1.write(data)
#                 filename_list.append('re_data_' + str(name))
#                 name += 1
#                 flag = 0
#                 data_list = []
#     with open('re_data_' + str(name), 'w+', encoding='utf-8')as f1:
#         for data in data_list:
#             f1.write(data)
#     filename_list.append('re_data_' + str(name))
#     return filename_list


# def write_record(vocab_path, filename_list, max_len):
#     """将每个文件做成tfrecord"""
#     _, word_to_id = _read_vocab(vocab_path)
#     for i in range(len(filename_list)):
#         writer = tf.python_io.TFRecordWriter('record_' + str(i))
#         with codecs.open(filename_list[i], 'r', encoding='utf-8') as f:
#             for line in f.readlines():
#                 try:
#                     vocab_list = line.split(" ")
#                     features = [word_to_id[x] if x in word_to_id else word_to_id["UNK"] for x in vocab_list]
#
#                     if len(features) >= max_len:
#                         x_pad = features[0:max_len]
#                     else:
#                         x_pad = features + [0] * (max_len - len(features))
#                     example = tf.train.Example(
#                         features=tf.train.Features(
#                             feature={'input': _int64_feature(x_pad)}))
#                     serialized = example.SerializeToString()
#                     writer.write(serialized)
#                 except Exception as e:
#                     print(e)
#         writer.close()
#     print("finish")


# def read_and_decode(filename_queue):
#     # 创建一个reader来读取TFRecord文件中的样例
#     reader = tf.TFRecordReader()
#     # 从文件中读出一个样例
#     _, serialized_example = reader.read(filename_queue)
#     # 解析读入的一个样例
#     features = tf.parse_single_example(serialized_example, features={
#         'input': tf.FixedLenFeature([50], tf.int64)})
#
#     x = tf.cast(features['input'], tf.int32)
#
#     return x


# def inputs(file, batch_size, num_epochs):
#     if not num_epochs:
#         num_epochs = None
#     filename_queue = tf.train.string_input_producer([file])
#     text_raw = read_and_decode(filename_queue)
#     x = tf.train.shuffle_batch([text_raw], batch_size=batch_size, capacity=300, min_after_dequeue=10)
#
#     return x


# if __name__ == '__main__':
#     filename_list = get_data('train.word', num_word=1000000)
#     write_record('./vocab', filename_list=filename_list, max_len=50)
#     x_train = inputs('./train.records', batch_size=30, num_epochs=3)
#     with tf.Session()as sess:
#         init = tf.global_variables_initializer()
#         sess.run(init)
#         coord = tf.train.Coordinator()
#         tf.train.start_queue_runners(coord=coord, sess=sess)
#         for i in range(64):
#             text_val = sess.run(x_train)
#             print(text_val)
