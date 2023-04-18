import subprocess
from pathlib import Path

import yaml
from requests import get

download_dir = Path(__file__).parent / "pdf"
docs_dir = Path(__file__).parent / "docs"
out_dir = Path(__file__).parent / "md"

INDEX_MD = """
.. toctree::
   :maxdepth: 3
   :caption: Indice dei contenuti
   :numbered:
"""


def test_generate_from_yaml():
    specs_yaml = Path(__file__).parent / "specs.yaml"
    specs = yaml.safe_load(specs_yaml.read_text())
    for d in [download_dir, docs_dir, out_dir]:
        if not d.exists():
            d.mkdir(exist_ok=True, parents=True)

    index_md = INDEX_MD

    for spec in specs["references"]:
        name = spec["name"]
        spec_pdf = Path(download_dir / name.replace(" ", "_")).with_suffix(".pdf")
        spec_md = (out_dir / spec_pdf.name).with_suffix(".md")
        process_spec(spec, spec_pdf)
        index_md += f"\n   ./docs/{spec_md.name}"

        docs_md = docs_dir / spec_md.name
        docs_md.write_text(
            f"# {spec['title']}\n\nThis document is an unreliable copy of the official one accessible at {spec['url']}. The goal of this copy is to be able to search across different, non-accessible documents and be able to identify the interesting ones.\n"
            + spec_md.read_text()
        )

    Path("index.rst").write_text(index_md)


def process_spec(spec: dict, spec_pdf: Path):
    """Given a specification dict with url, name and title,
    download the pdf file from the url, convert it to markdown and
    save it to a file named as the name in the spec dict.
    """
    url = spec["url"]
    spec["name"]
    spec["title"]

    if not spec_pdf.exists():
        content_pdf = get(url).content
        spec_pdf.write_bytes(content_pdf)

    # md = convert_pdf_to_markdown(content_pdf)
    # save_markdown(md, name)
    # assert title in md


def convert_pdf_to_markdown(srcdir=".", dstdir="out/"):
    """Convert the pdf file to markdown."""
    srcdir = Path("src").as_posix()
    cmd = f"npx @opendocsg/pdf2md --inputFolderPath={srcdir} --outputFolderPath={dstdir} --recursive"
    subprocess.run(cmd, shell=True, check=True)
