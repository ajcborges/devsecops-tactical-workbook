# DevSecOps Quickstart

![Docker Image CI](https://github.com/thedevilsvoice/devsecops_quickstart/workflows/Docker%20Image%20CI/badge.svg?branch=master)

## Images

The images at pixabay.com are free for commercial use.

Down load the images to docs/images and save the HTML credits
for the photograph as a file with .html extension. Then run the
`generate_pic_ref.sh` script to make the picture credits file
in the references section.

## To generate PDF of book

Should be done from inside the Docker container.

```bash
make docker
cd docs
sphinx-build -M latexpdf . _build
```

- PDF will be in `docs/_build/latex/devsecopsquickstart.pdf`
- Find the file in `file:///home/thedevilsvoice/workspace/devsecops_quickstart/docs/_build/latex/devsecopsquickstart.pdf`
  - If you open in firefox you get a nice nav bar on the left side.

## Epub

```bash
sudo apt -y install calibre sigil
```

https://www.amazon.com/gp/feature.html?docId=1000765211

Should be done from inside the docker container.

```bash
make docker
cd docs && make epub
```

## Kindle

Now you can generate the kindle .mobi file

```bash
kindlegen _build/epub/CloudLab.epub
```

Results in a file called `CloudLab.mobi`
