#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/4/29 15:45
@Author  : alexanderwu
@File    : read_document.py
"""

import docx


def read_docx(file_path: str) -> list:
    """打开docx文件"""
    doc = docx.Document(file_path)

    return [paragraph.text for paragraph in doc.paragraphs]
