# LatinBERT
Simple overview of use/purpose.

## Description

An in-depth paragraph about your project and overview of use.


# Table Of Contents
-  [Requirements](# Requirements)
-  [In Details](#in-details)
-  [Future Work](#future-work)
-  [Contributing](#contributing)
-  [Acknowledgments](#acknowledgments)

# Requirements
- [PyTorch](https://pytorch.org/) (An open source deep learning platform) 

# In Details
```
├──  latin_library_text  -  bigger database of txt files
│
├──  library reduced and super_reduced  -  smaller version of database
│
├──  corpus0 and corpus2  -  contain similar text to Gallus, specific authors
│
├──  pickle_gallus_related  -  contain the processed vectors from the text of corpus2. how to use the pickle files is in Gallus Notebook.
│
├──  pickle_latin_library_text  -  contain the processed vectors from the text of library_reduced.
│
├──  analysis  -  contain different notebooks of analysis
│
├──  utils  -  contains different python scripts 

    │
    └────  script_generator.py  -  is a python script for generate the bash script that compute the bert representation of the given texts and it saves the representation in a convenient way that is pickle files. in this file you have to set the source folder, the output folder and the folder in which the Bert Model is contained.
    │
    └────  script_generator_colab   -  is the same python script but adapted for colab usage
    │
    └────  text_to_pickle.py   -  is the python script that is called by the bash script.sh.you dont have to set anything in this file.
    │
    └────  script.sh   -  the bash script. it's automatically generated from the script_generator.py
    │
    └────  Berts_model_colab.ipynb  -  is the google Colab implementation of the python script_generator and the bash script. Moreover you can automatically download the pickle files.
    │
    └────  analysis_from_pickles.ipynb  -  is the first draft of analysis using cosine similarity
```

### Pipeline

1. Edit the script_generator.py with the source folder, the output folder and the folder in which the Bert Model is contained.
Example:

        import os

        path='library_super_reduced' 
        bertpath='/latin_bert' 
        output='pickle'

  
2. Run the script_generator.py 

        python3 script_generator.py
    
    
3. Run the bash script.sh generated from the script_generator(after allowing to run it as executable)
        
        bash script.sh
        
4. You'll find the pickle databases in the output folder and from here you can start your analysis of the bert representations.
    

  
<!-- #Future Work -->

# Contributing
Any kind of enhancement or contribution is welcomed.

## Authors

[Pietro Sillano](https://github.com/pietro-sillano) et. Al


## References


  
  
  
  
  
  
  
  
