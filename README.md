## Environment Setup

* `Python3.6`
* `Pytorch 0.4.0` or higher

Install Python dependency via `pip install -r requirements.txt` when the environment of Python and Pytorch is setup.

## Running Code

#### Data preparation


* Download [Glove Embedding](https://nlp.stanford.edu/data/wordvecs/glove.42B.300d.zip) and put `glove.42B.300d` under `./data/` directory
* Download [Pretrained IRNet](https://drive.google.com/open?id=1VoV28fneYss8HaZmoThGlvYU3A-aK31q) and put `
IRNet_pretrained.model` under `./saved_model/` directory
* Download preprocessed train/dev datasets from [here](https://drive.google.com/open?id=1YFV1GoLivOMlmunKW0nkzefKULO4wtrn) and put `train.json`, `dev.json` and 
`tables.json` under `./data/` directory

##### Generating train/dev data by yourself
You could process the origin [Spider Data](https://drive.google.com/uc?export=download&id=11icoH_EA-NYb0OrPTdehRWm_d7-DIzWX) by your own. Download  and put `train.json`, `dev.json` and 
`tables.json` under `./data/` directory and follow the instruction on `./preprocess/`

#### Training

Run `train.sh` to train IRNet.

`sh train.sh [GPU_ID] [SAVE_FOLD]`

#### Testing

Run `eval.sh` to eval IRNet.

`sh eval.sh [GPU_ID] [OUTPUT_FOLD]`

## Citation

If you use IRNet, please cite the following work.

```
@inproceedings{GuoIRNet2019,
  author={Jiaqi Guo and Zecheng Zhan and Yan Gao and Yan Xiao and Jian-Guang Lou and Ting Liu and Dongmei Zhang},
  title={Towards Complex Text-to-SQL in Cross-Domain Database with Intermediate Representation},
  booktitle={Proceeding of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2019},
  organization={Association for Computational Linguistics}
}
```

## Thanks
We would like to thank [Tao Yu](https://taoyds.github.io/) and [Bo Pang](https://www.linkedin.com/in/bo-pang/) for running evaluations on our submitted models.
We are also grateful to the flexible semantic parser [TranX](https://github.com/pcyin/tranX) that inspires our works.
