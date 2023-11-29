#!/usr/bin/env python

# File with most used
# functions and derived
# variables.

import numpy as np
import pandas as pd
from pycaret import classification as pyc
from pycaret import regression as pyr

def predict_AGN_gal(catalog_df, 
                    AGN_gal_model, 
                    cal_AGN_gal_model, 
                    threshold, 
                    cal_threshold, 
                    raw_score=True):
    catalog_df = pyc.predict_model(AGN_gal_model, 
                                   data=catalog_df, 
                                   probability_threshold=threshold, 
                                   raw_score=raw_score, 
                                   round=10)
    catalog_df = catalog_df.drop(columns=['Score_0'])
    catalog_df = catalog_df.rename(columns={'Label': 'pred_class', 'Score_1': 'Score_AGN'})
    catalog_df.loc[:, 'Score_AGN'] = np.around(catalog_df.loc[:, 'Score_AGN'], decimals=8)
    pred_probs = cal_AGN_gal_model.predict(catalog_df.loc[:, 'Score_AGN'])
    cal_class  = np.array(pred_probs >= cal_threshold).astype(int)
    catalog_df['Prob_AGN']       = pred_probs
    catalog_df['pred_class_cal'] = cal_class
    return catalog_df

def predict_radio_det(catalog_df, 
                      radio_model, 
                      cal_radio_model, 
                      threshold, 
                      cal_threshold, 
                      raw_score=True):
    catalog_df = pyc.predict_model(radio_model, 
                                   data=catalog_df, 
                                   probability_threshold=threshold, 
                                   raw_score=raw_score, 
                                   round=10)
    catalog_df = catalog_df.drop(columns=['Score_0'])
    catalog_df = catalog_df.rename(columns={'Label': 'pred_radio_AGN', 'Score_1': 'Score_radio_AGN'})
    catalog_df.loc[:, 'Score_radio_AGN'] = np.around(catalog_df.loc[:, 'Score_radio_AGN'], decimals=8)
    pred_probs = cal_radio_model.predict(catalog_df.loc[:, 'Score_radio_AGN'])
    cal_class  = np.array(pred_probs >= cal_threshold).astype(int)
    catalog_df['Prob_radio_AGN']     = pred_probs
    catalog_df['pred_radio_cal_AGN'] = cal_class
    return catalog_df

def predict_z(catalog_df, 
              redshift_model):
    catalog_df = pyr.predict_model(redshift_model, 
                                   data=catalog_df, 
                                   round=10)
    catalog_df = catalog_df.rename(columns={'Label': 'pred_Z_rAGN'})
    catalog_df.loc[:, 'pred_Z_rAGN'] = np.around(catalog_df.loc[:, 'pred_Z_rAGN'], decimals=4)
    return catalog_df