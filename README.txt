README:

All the code is written in jupyter notebooks. To run these notebooks, run the following command from the root folder:
> jupyter notebook
Sequentially run all the code in the notebook to get the desired outputs.
The code for part 1 (IBM model 1) is in the notebook 'IBM model 1.ipynb'.
The code for part 2 (IBM model 2) is in the notebook 'IBM model 2.ipynb'.
The code where we generate the alignments from the other direction is in the notebook 'IBM model 2 languages exchanged.ipynb'
The code for part 3(Growing Alignments ) is in the notebook 'Part 3.ipynb'.
The code for the bonus part (another heuristic for growing alignments) is in the notebook 'bonus.ipynb'.

The notebook uses corpus.en and corpus.es and dev.en and dev.es files, and stores the intermediate outputs (t and q parameters) as pickle files. It also stores the alignments in text files in similar format as the dev.key files. There is also provision to call the eval_alignments.py file directly from the notebook itself, and display the results in the notebook itself, using subprocess, the Python module.