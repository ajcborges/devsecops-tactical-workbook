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
