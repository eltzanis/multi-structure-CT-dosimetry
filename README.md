# Multi-organ/tissue radiation dosimetry in CT
The aim of this project was the development of a machine learning-based methodology for the automated personalized radiation dosimetry in CT.
The developed pipeline combines a robust organ segmentation tool ([TotalSegmentator](https://github.com/wasserth/TotalSegmentator)) and dose prediction deep neural networks (DNNs) for the rapid and accurate estimation of radiation doses for 30 organs/tissues including sub-volumes of the heart and lungs.

Created at the Department of Medical Physics, School of Medicine, University of Crete.

Contributors: Dr. Eleftherios Tzanis, Prof. John Damilakis

# Usage
This repository provides the necessary code for the development and implementation of the proposed methodology.

The development of the dose prediction DNNs is performed with PyTorch. Users can create the organ/tissue-specific training arrays with the 'preprocessing_chest.ipynb' and 'preprocessing_abdomen.ipynb' notebooks. Then, for the training of the structure-specific DNNs, the 'training_abdomen.ipynb' and 'training_chest.ipynb' notebooks should be used. Organ/tissue-specific dose prediction DNNs will be produced for the esophagus, left atrium, right atrium, myocardium, left ventricle, right ventricle, aorta, left lung lower lobe, right lung lower lobe, right lung middle lobe, left lung upper lobe, right lung upper lobe, lungs, lung vessels, tracheobronchial tree, pulmonary artery, skin, left adrenal gland, right adrenal gland, colon, left kidney, right kidney, liver, pancreas, small bowel, spleen, stomach, urinary bladder, thyroid gland and spinal cord.

Validation notebooks can be used for the independent evaluation of the developed models. Moreover, the inference notebooks can be used for the implementation of the proposed pipeline.

For demonstration purposes we provide two anonymized CT examinations. Users can test the developed workflow by using the inference notebooks and the dose prediction DNNs available in 'abdomen_models' and 'chest_models' folders.
