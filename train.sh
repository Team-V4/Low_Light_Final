## train uncertainty model
python train.py -uncertainty --config ./config/llie_train_u.json --dataset ./config/customized_dataset.yml 

## train global structure-aware diffusion
python train.py --config ./config/customized_dataset_train.json --dataset ./config/customized_dataset.yml