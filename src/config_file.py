config_main = {

    'experiment_name': 'v0_knn30_MLP20',
    'features_type': 'CNN', # CNN or MFCC
    'model_type': 'ELM', # linearSVM, ELM, SVM, MLP, KNN or linear
    'load_extracted_features': False,
    'sampling_rate': 12000,

    #'dataset': 'Extended Ballroom',
    #'audio_path': '/datasets/MTG/users/jpons/extended_ballroom/',
    #'save_extracted_features_folder': '../data/Extended_Ballroom/features/',
    #'results_folder': '../data/Extended_Ballroom/results/',
    #'train_set_list': None,
    #'val_set_list': None,
    #'test_set_list': None,
    #'audios_list': '/datasets/MTG/users/jpons/extended_ballroom/all_files.txt',
    #'fix_length_by': 'crop', # 'zero-pad', 'repeat-pad' or 'crop'

    #'dataset': 'Ballroom',
    #'audio_path': '/datasets/MTG/users/jpons/ballroom/BallroomData/',
    #'save_extracted_features_folder': '../data/Ballroom/features/',
    #'results_folder': '../data/Ballroom/results/',
    #'train_set_list': None,
    #'val_set_list': None,
    #'test_set_list': None,
    #'audios_list': '/datasets/MTG/users/jpons/ballroom/allBallroomFiles.txt',
    #'fix_length_by': 'crop', # 'zero-pad', 'repeat-pad' or 'crop'

    'dataset': 'GTZAN',
    'audio_path': '/datasets/MTG/users/jpons/GTZAN/',
    'save_extracted_features_folder': '../data/GTZAN/features/',
    'results_folder': '../data/GTZAN/results/',
    'train_set_list': '/datasets/MTG/users/jpons/GTZAN_debug_partitions/train_filtered.txt',
    'val_set_list': '/datasets/MTG/users/jpons/GTZAN_debug_partitions/valid_filtered.txt',
    'test_set_list': '/datasets/MTG/users/jpons/GTZAN_debug_partitions/test_filtered.txt',
    'audios_list': False,
    'fix_length_by': 'crop', # 'zero-pad', 'repeat-pad' or 'crop'

    #'dataset': 'UrbanSound8K',
    #'audio_path': '/datasets/MTG/users/jpons/urban_sounds/UrbanSound8K/',
    #'save_extracted_features_folder': '../data/UrbanSound8K/features/',
    #'results_folder': '../data/UrbanSound8K/results/',
    #'train_set_list': None,
    #'val_set_list': None,
    #'test_set_list': None,
    #'audios_list': '/datasets/MTG/users/jpons/urban_sounds/UrbanSound8K/allFiles.txt',
    #'fix_length_by': 'repeat-pad', # 'zero-pad', 'repeat-pad', 'crop' or False

    'CNN': {
        'n_mels': 96,
        'n_frames': 1376, # GTZAN: 1404, OLD: 1360, BALLROOM: 1376, US8K: 101/188
        'batch_size': 5,

        #'architecture': 'cnn_small_filters',
        #'num_filters': 32, # 717 or 32
        #'selected_features_list': [0, 1, 2, 3, 4]

        #'architecture': 'cnn_music',
        #'num_filters': 256, # 256, 128, 64, 32, 16, 8 or 4
        #'selected_features_list': [1] # timbral [0], temporal [1] or both [0, 1]

        'architecture': 'cnn_single',
        'num_filters': 160, # 160
        'selected_features_list': [0], # conv-layer [0], pooling-layer [1] or both [0, 1]
        'filter_shape': [7,81], # [t,f]: [7,96]
        'pool_shape': [1,1] # [t,f]: [1,1]
    },

    'MFCC': {
        'number': 20,
        'fixed_length': 2048
    },

    'SVM_verbose': 1
}

"""

DOCUMENTATION 


'experiment_name': personal string to easily identify an experiment.
 -- EXAMPLE: 'v0_final3_true'
'dataset': dataset identifier.
 -- VALUES: 'UrbanSound8K'


'audio_path': directory where audios are stored.
 -- EXAMPLE: '/data/UrbanSound8K/'
'results_folder':  directory where results are stored.
 -- EXAMPLE: '../data/UrbanSound8K/results/'
'save_extracted_features_folder': directory where extracted features are stored.
 -- EXAMPLE: '../data/UrbanSound8K/features/'


'load_extracted_features': False or path where the extracted features were saved.
 -- VALUES: False or '../data/UrbanSound8K/features/'


'audios_list': set 'audios_list' to FALSE to specify partitions in 'train/val/test _set_list'.
 -- EXAMPLE: '/data/UrbanSound8K/allFiles_debug.txt' or False

'train_set_list': read 'audios_list' above.
 -- EXAMPLE: None or '/home/jpons/GTZAN_partitions/train_filtered.txt'
'val_set_list': read 'audios_list' above.
 -- EXAMPLE: None or '/home/jpons/GTZAN_partitions/valid_filtered.txt'
'test_set_list': read 'audios_list' above.
 -- EXAMPLE: None or '/home/jpons/GTZAN_partitions/test_filtered.txt'


'fix_length_by': audios can be of different length, set it differently to pad and/or crop the audio.
 -- VALUES CNN: 'zero-pad', 'repeat-pad' or False
 -- EXPLANATION CNN: pad to a defined length, or crop (False) to a defined minimum length.
 -- VALUES MFCC: 'zero-pad', 'repeat-pad', 'crop' or False
 -- EXPLANATION MFCC: pad to a minimum length, crop to a max length or do nothing.


'sampling_rate': sampling rate at which we process the audio.
 -- VALUE: 12000

'SVM_verbose': verbose value for the SVM grid search.
 -- VALUE: 2

'model_type': select the classification model.
 -- VALUES: 'SVM', 'MLP' or 'KNN'

'features_type': select if the features to extract are CNN or MFCC based.
 -- VALUES: 'CNN' or 'MFCC'
 -- SEE HOW TO SET CNN and MFCC PARAMETERS:

    'CNN': {
        'n_mels': 96,
        'n_frames': 111, # GTZAN: 1404, old: 1360  ## BALLROOM: 1376  ### US8K: 101/188
        'batch_size': 5,

        'architecture': 'cnn_music',
        'num_filters': 4, # 256, 128, 64, 32, 16, 8 or 4
        'selected_features_list': [0,1] # timbral [0], temporal [1] or both [0, 1]
    }

    or

    'CNN': {
        'n_mels': 96,
        'n_frames': 111, # GTZAN: 1404, old: 1360  ## BALLROOM: 1376  ### US8K: 101/188
        'batch_size': 5,

        'architecture': 'cnn_small_filters',
        'num_filters': 32, # 717, 90 or 32
        'selected_features_list': [0, 1, 2, 3, 4]

    }

    or

    'MFCC': {
        'number': 20,
        'fixed_length': 2048 # for, at least, 3 MFCC frames.
    }


'CNN'/'n_frames': length in frames of the input spectrogram
 -- VALUES OLD: 1360
 -- VALUES GTZAN: 1404
 -- VALUES BALLROOM: 1376
 -- VALUES EXTENDED BALLROOM: 1376
 -- VALUES URBANSOUND8K: 188 (4sec), 128 (Justin), 101 (Karol), 41 (Karol)

'CNN'/'architecture': length in frames of the input spectrogram
 -- VALUES: 'cnn_small_filters' or 'cnn_music'
 -- EXAMPLE: see 'features_type' example

"""
