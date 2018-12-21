## Usage ##

### Dataset ###
Download the yelp sentiment dataset with the following cmd:
```
python prepare_data.py
```

### Train the model ###

Train the model on the above data to do sentiment transfer.
```
python main.py --config config
```

[config.py](./config.py) contains the data and mode configurations. 

* The model will first be pre-trained for a few epochs (specified in `config.py`). During pre-training, the `Encoder-Decoder` part is trained as an autoencoder, while the `Classifier` part is trained with the classification labels.
* Full-training is then performed for another few epochs. During full-training, the `Classifier` part is fixed, and the `Encoder-Decoder` part is trained to fit the classifier, along with continuing to minimize the autoencoding loss.

where:
- `loss_d` and `accu_d` are the classification loss/accuracy of the `Classifier` part.
- `loss_g_clas` is the classification loss of the generated sentences.
- `loss_g_ae` is the autoencoding loss.
- `loss_g` is the joint loss `= loss_g_ae + lambda_g * loss_g_clas`.
- `accu_g` is the classification accuracy of the generated sentences with soft represetations (i.e., Gumbel-softmax).
- `accu_g_gdy` is the classification accuracy of the generated sentences with greedy decoding.
- `bleu` is the BLEU score between the generated and input sentences.