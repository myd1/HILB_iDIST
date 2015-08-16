# Hilb and iDist

Hilb and iDist are two data anonymization algorithm for relational dataset, proposed by Gabriel Ghinita in his papers[1]. To our knowledge, HILB and IDIST are the best anonymization algorithm for relational dataset, which run very fast at the same time.  I got the C++ implementation from Gabriel Ghinita, and covert it to python.(Thanks to Gabriel Ghinita!).

This repository is an **open source python implementation for HILB and iDIST**. I implement this algorithm in python for further study.

### Motivation

Researches on data privacy have lasted for more than ten years, lots of great papers have been published. However, only a few open source projects are available on Internet [2-3], most open source projects are using algorithms proposed before 2004! Fewer projects have been used in real life. Worse more, most people even don't hear about it. Such a tragedy! 

I decided to make some effort. Hoping these open source repositories can help researchers and developers on data privacy (privacy preserving data publishing).

### Attention

I used **both adult and INFORMS** dataset in this implementation. For clarification, **we transform NCP to percentage**. This NCP percentage is computed by dividing NCP value with the number of values in dataset (also called GCP[1]). The range of NCP percentage is from 0 to 1, where 0 means no information loss, 1 means loses all information (more meaningful than raw NCP, which is sensitive to size of dataset). 



### Usage and Parameters:

My Implementation is based on Python 2.7 (not Python 3.0). Please make sure your Python environment is collectly installed. You can run Mondrian in following steps: 

1) Download (or clone) the whole project. 

2) Run "anonymized.py" in root dir with CLI.

Parameters:

	# run Mondrian with adult data and default K(K=10)

	python anonymizer.py 

	

	# run Mondrian with adult data K=20

	python anonymized.py a 20

	a: adult dataset, i: INFORMS ataset

	k: varying k, qi: varying qi numbers, data: varying size of dataset, one: run only once



### For more information:

[1] G. Ghinita, P. Karras, P. Kalnis, N. Mamoulis. Fast data anonymization with low information loss. Proceedings of the 33rd international conference on Very large data bases, VLDB Endowment, 2007, 758-769

[2][UTD Anonymization Toolbox](http://cs.utdallas.edu/dspl/cgi-bin/toolbox/index.php?go=home)

[3][ARX- Powerful Data Anonymization](https://github.com/arx-deidentifier/arx)

==========================

by Qiyuan Gong

qiyuangong@gmail.com

2015-1-21