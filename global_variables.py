#!/usr/bin/env python

# File with most used
# variables in this project.
# File paths, file names, etc.

# Data files paths
model_path          = './'
file_HETDEX         = 'predicted_rAGN_HETDEX.parquet'  # 15136878 objects (1.5e7)
file_S82            = 'predicted_rAGN_S82.parquet'     # 3590306 objects (3.6e6)

# Uncalibrated models
AGN_gal_model      = 'classification_AGN_galaxy_dec_18_2022'
radio_model        = 'classification_LOFAR_detect_dec_19_2022'
full_z_model       = 'regression_z_dec_20_2022'
high_z_model       = 'regression_high_z_dec_121_2022'

# Calibrated models
cal_AGN_gal_model  = 'cal_' + AGN_gal_model + '.joblib'
cal_radio_model    = 'cal_' + radio_model   + '.joblib'

# Classification calibrated thresholds
cal_AGN_thresh     = 0.34895396724527294
cal_radio_thresh   = 0.2046047064139296