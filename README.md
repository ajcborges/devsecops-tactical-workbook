# cloudlab

## Images

The images at pixabay.com are free for commercial use.

Down load the images to docs/images and save the HTML credits
for the photograph as a file with .html extension. Then run the
`generate_pic_ref.sh` script to make the picture credits file
in the references section.

## To generate PDF of book

```bash
cd docs
sphinx-build -M latexpdf . _build
```

PDF will be in `cloudlab/docs/_build/latex/cloudlab.pdf`

[200~##################
H1: document title
##################

Introduction text.


*********
Sample H2
*********

Sample content.


**********
Another H2
**********

Sample H3
=========

Sample H4
---------

Sample H5
^^^^^^^^^

Sample H6
"""""""""
