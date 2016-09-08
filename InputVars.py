# Select Variables To use in training

# On the JigSaw Dataset Fields will be the following:
#

FieldGroups = [    
    ['mP', 'mC', 'mX', 'METx', 'METy', 'L1_pT', 'L1_M', 'L2_pT','L2_M', 'B1_pT','B1_M', 'B2_pT','B2_M', 'MPP_AA', 'Eb_a_AA', 'Eb_b_AA', 'El_a_AA', 'El_b_AA', 'MPP_BB', 'Eb_a_BB', 'Eb_b_BB', 'El_a_BB', 'El_b_BB','MPP_AB', 'Eb_a_AB', 'Eb_b_AB', 'El_a_AB', 'El_b_AB', 'MPP_BA', 'Eb_a_BA', 'Eb_b_BA', 'El_a_BA', 'El_b_BA'],
    ['L1_eta', 'L2_eta',  'B1_eta','B2_eta'],
    ['L1_phi', 'L2_phi','B1_phi', 'B2_phi'],
    ['cosPP_AA', 'cosPa_AA', 'cosPb_AA', 'cosCa_AA', 'cosCb_AA','cosPP_BB', 'cosPa_BB', 'cosPb_BB', 'cosCa_BB', 'cosCb_BB','cosPP_AB', 'cosPa_AB', 'cosPb_AB', 'cosCa_AB', 'cosCb_AB','cosPP_BA', 'cosPa_BA', 'cosPb_BA', 'cosCa_BA', 'cosCb_BA'],
    ['dphi_PP_Pa_AA', 'dphi_PP_Pb_AA', 'dphi_Pa_Ca_AA', 'dphi_Pb_Cb_AA', 'dphi_PP_Pa_BB', 'dphi_PP_Pb_BB', 'dphi_Pa_Ca_BB', 'dphi_Pb_Cb_BB', 'dphi_PP_Pa_AB', 'dphi_PP_Pb_AB', 'dphi_Pa_Ca_AB', 'dphi_Pb_Cb_AB','dphi_PP_Pa_BA', 'dphi_PP_Pb_BA', 'dphi_Pa_Ca_BA', 'dphi_Pb_Cb_BA'] ]

SelectedFields = [
    ['mP', 'mC', 'mX',  'L1_pT', 'L1_eta', 'L1_phi', 'L1_M', 'L2_pT', 'L2_eta', 'L2_phi', 'L2_M', 'B1_pT', 'B1_eta', 'B1_phi', 'B1_M', 'B2_pT', 'B2_eta', 'B2_phi', 'B2_M', 'MPP_AA', 'Eb_a_AA', 'Eb_b_AA', 'El_a_AA', 'El_b_AA', 'cosPP_AA', 'cosPa_AA', 'cosPb_AA', 'cosCa_AA', 'cosCb_AA', 'dphi_PP_Pa_AA', 'dphi_PP_Pb_AA', 'dphi_Pa_Ca_AA', 'dphi_Pb_Cb_AA', 'MPP_BB', 'Eb_a_BB', 'Eb_b_BB', 'El_a_BB', 'El_b_BB', 'cosPP_BB', 'cosPa_BB', 'cosPb_BB', 'cosCa_BB', 'cosCb_BB', 'dphi_PP_Pa_BB', 'dphi_PP_Pb_BB', 'dphi_Pa_Ca_BB', 'dphi_Pb_Cb_BB', 'MPP_AB', 'Eb_a_AB', 'Eb_b_AB', 'El_a_AB', 'El_b_AB', 'cosPP_AB', 'cosPa_AB', 'cosPb_AB', 'cosCa_AB', 'cosCb_AB', 'dphi_PP_Pa_AB', 'dphi_PP_Pb_AB', 'dphi_Pa_Ca_AB', 'dphi_Pb_Cb_AB', 'MPP_BA', 'Eb_a_BA', 'Eb_b_BA', 'El_a_BA', 'El_b_BA', 'cosPP_BA', 'cosPa_BA', 'cosPb_BA', 'cosCa_BA', 'cosCb_BA', 'dphi_PP_Pa_BA', 'dphi_PP_Pb_BA', 'dphi_Pa_Ca_BA', 'dphi_Pb_Cb_BA'],

    ['MPP_AA', 'Eb_a_AA', 'Eb_b_AA', 'El_a_AA', 'El_b_AA', 'cosPP_AA', 'cosPa_AA', 'cosPb_AA', 'cosCa_AA', 'cosCb_AA', 'dphi_PP_Pa_AA', 'dphi_PP_Pb_AA', 'dphi_Pa_Ca_AA', 'dphi_Pb_Cb_AA', 'MPP_BB', 'Eb_a_BB', 'Eb_b_BB', 'El_a_BB', 'El_b_BB', 'cosPP_BB', 'cosPa_BB', 'cosPb_BB', 'cosCa_BB', 'cosCb_BB', 'dphi_PP_Pa_BB', 'dphi_PP_Pb_BB', 'dphi_Pa_Ca_BB', 'dphi_Pb_Cb_BB', 'MPP_AB', 'Eb_a_AB', 'Eb_b_AB', 'El_a_AB', 'El_b_AB', 'cosPP_AB', 'cosPa_AB', 'cosPb_AB', 'cosCa_AB', 'cosCb_AB', 'dphi_PP_Pa_AB', 'dphi_PP_Pb_AB', 'dphi_Pa_Ca_AB', 'dphi_Pb_Cb_AB', 'MPP_BA', 'Eb_a_BA', 'Eb_b_BA', 'El_a_BA', 'El_b_BA', 'cosPP_BA', 'cosPa_BA', 'cosPb_BA', 'cosCa_BA', 'cosCb_BA', 'dphi_PP_Pa_BA', 'dphi_PP_Pb_BA', 'dphi_Pa_Ca_BA', 'dphi_Pb_Cb_BA'],

    ['METx', 'METy', 'L1_pT', 'L1_eta', 'L1_phi',  'L2_pT', 'L2_eta', 'L2_phi', 'B1_pT', 'B1_eta', 'B1_phi',  'B2_pT', 'B2_eta', 'B2_phi'],

    ['MPP_AA', 'Eb_a_AA', 'Eb_b_AA', 'El_a_AA', 'El_b_AA', 'cosPP_AA', 'cosPa_AA', 'cosPb_AA', 'cosCa_AA', 'cosCb_AA', 'dphi_PP_Pa_AA', 'dphi_PP_Pb_AA', 'dphi_Pa_Ca_AA', 'dphi_Pb_Cb_AA'],

    ['mP', 'mC', 'mX','METx', 'METy', 'L1_pT', 'L1_eta', 'L1_phi',  'L2_pT', 'L2_eta', 'L2_phi', 'B1_pT', 'B1_eta', 'B1_phi',  'B2_pT', 'B2_eta', 'B2_phi'],
]
