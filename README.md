# AllenAI-Common

This repository is a copy-paste of the common components 
from the `1.1.0` version of [AllenNLP library](https://github.com/allenai/allennlp).


The following classes were extracted:

* `FromParams`
* `Params`
* `Lazy`
* `Registrable`

And freed from ML/DL/NLP dependencies (e.g. `scikit-learn`, `torch`, `nltk`, `spacy`, `tensorboardX`, `transformers`).


## Usage

```bash
pip install allenai-common
```

```python
from allenai_common import Registrable, Params, Lazy, FromParams

# Do something you would normally do when solving NLP tasks using AllenNLP
# But at this time use imported modules for non-NLP tasks
```