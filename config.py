from omegaconf import OmegaConf

config = {
    'general': {
        'experiment_name': '200e',
        'seed': 0xFACED,
        'num_classes': 250, 
    },
    'paths': {
        'path_to_csv': '/home/toefl/K/asl-signs/train.csv',
        'path_to_data': './feature_data/feature_data_dist.pickle',
        'path_to_labels': './feature_data/feature_labels_dist.pickle',
        'path_to_json': '/home/toefl/K/asl-signs/sign_to_prediction_index_map.json',
        'path_to_folder': '/home/toefl/K/asl-signs/',
        'pq_path': '/home/toefl/K/asl-signs/train_landmark_files/53618/1001379621.parquet',
        'path_to_checkpoints': './checkpoints/${general.experiment_name}', 
    },
    'training': {
        'num_epochs': 200,
        'early_stopping_epochs': 100,
        'lr': 1e-4 / 100,

        'mixed_precision': True,
        'gradient_accumulation': False,
        'gradient_clipping': False,
        'gradient_accumulation_steps': 8,
        'clip_value': 2,
        
        'warmup_scheduler': True,
        'warmup_epochs': 5,
        'warmup_multiplier': 100,

        'debug': False,
        'number_of_train_debug_samples': 5000,
        'number_of_val_debug_samples': 1000,
        
        'device': 'cuda',
        'save_best': True,
        'save_last': False,
        'verbose_plots': False,
        'resume_from_latest_checkpoint': False,
    },
    'dataloader_params': {
        'batch_size': 64,
        'num_workers': 8,
        'pin_memory': False,
        'persistent_workers': True,
        'shuffle': True,
        'drop_last': True,
    },
    'split': {
        'all_data_train': False,
        'n_splits': 5,
        'folds_to_train': [2, 3, 4, 0, 1],
        'folds_to_submit': [2, 3, 4, 0, 1],
        'already_split': False,
    },
    'model': {           
        'freeze_batchnorms': False,
        'converter_sample_input_shape': [384, 543, 3],
        'model_sample_input_shape': [384, 828],
        'params': {
            "max_length": 384,
            "embed_dim": 512, 
            "num_point": 828,
            "num_head": 16,
            "num_class": '${general.num_classes}',
            "num_block": 1, 
        },
    },
    'augmentations': {
        'scale': (0.8,1.5),
        'shift': (-0.1,0.1),
        'degree': (-15,15),
        'p': 0.5,
    },
    'optimizer': {
        'name': '/custom/Ranger',
        'params': {
            'lr': '${training.lr}',
        },
    },
    'scheduler': {
        'name': 'CosineAnnealingLR', 
        'interval': 'epoch',
        'params': {
            'T_max': 195,
            'eta_min': 1e-8,
        },
    },
    'loss': {
        'name': '/custom/ArcFaceLoss',
        'params': {
            's': 45,
            'm': 0.4,
            'crit': 'bce',
            'class_weights_norm': "batch",
        }
    },
    'metric': {
        'name': 'accuracy_score',
        'params': {
        },
    },
    'logging': {
        'prints': True,
        'txt_file': True,
        'wandb': False,
        'telegram': True,
        'wandb_username': 'toefl',
        'wandb_project_name': 'GISLR',
    }, 
}

config = OmegaConf.create(config)