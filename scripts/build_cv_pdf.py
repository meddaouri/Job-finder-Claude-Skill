#!/usr/bin/env python3
"""
Job Finder — convert a CV .docx to PDF with LibreOffice (keeps RTL scripts and CJK fonts intact).

Usage:
    python3 build_cv_pdf.py CV_Firstname_Lastname.docx [output_dir]

Requires LibreOffice (`soffice` or `libreoffice` on PATH). If it is not available, use the pdf skill
or tell the user to export the .docx to PDF from Word / Google Docs.
"""
import os
import shutil
import subprocess
import sys
import tempfile


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    src = os.path.abspath(sys.argv[1])
    out_dir = os.path.abspath(sys.argv[2]) if len(sys.argv) == 3 else os.path.dirname(src)
    if not os.path.isfile(src):
        sys.exit(f"error: {src} not found")
    exe = shutil.which("soffice") or shutil.which("libreoffice")
    if not exe:
        sys.exit("error: LibreOffice not found — use the pdf skill or export from Word/Google Docs")
    os.makedirs(out_dir, exist_ok=True)
    with tempfile.TemporaryDirectory() as profile:  # isolated profile avoids lock issues
        cmd = [exe, f"-env:UserInstallation=file://{profile}", "--headless", "--convert-to", "pdf",
               "--outdir", out_dir, src]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    pdf = os.path.join(out_dir, os.path.splitext(os.path.basename(src))[0] + ".pdf")
    if res.returncode != 0 or not os.path.isfile(pdf):
        sys.exit(f"error: conversion failed\n{res.stdout}\n{res.stderr}")
    print(pdf)


if __name__ == "__main__":
    main()
