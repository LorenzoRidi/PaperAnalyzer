INSTRUCTION = """
Perform a bibliographic analysis using the publication as a starting point to map the academic context. Use the google_search tool to search for related papers.

For each paper return the link to the document (PDF or other readable format) and an abstract of the paper.

**PAPER OVERVIEW**
{overview_result}

**INNOVATION ANALYSIS RESULT**
{innovation_result}

**ORIGINAL PAPER**
{artifact:paper.pdf}
"""
