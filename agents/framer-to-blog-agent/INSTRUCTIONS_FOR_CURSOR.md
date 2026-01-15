# Instructions for Cursor Agent

When the user asks to deploy a blog post to Aibility, follow these steps:

1.  **Switch to the tool directory**:
    Navigate to the `framer-to-blog-agent` directory where this tool is located.

2.  **Identify the article file**:
    Locate the article HTML or Markdown file. Ensure it has the required metadata.

3.  **Run the deployment preparer**:
    ```bash
    python3 deploy.py /path/to/your/article.md
    ```
    (This generates the JSON metadata and the AI image).

4.  **Execute the Framer deployment**:
    - **CRITICAL**: Ask the user to provide the current Framer MCP SSE URL from the Unframer plugin.
    - Run the script with the provided URL:
    ```bash
    python3 scripts/framer_upsert.py clanky/your-generated-json.json "PASTE_URL_HERE"
    ```

5.  **Confirm success**: Show the image URL and confirm the article is in Framer CMS.

## Article Metadata Template
The article should start with:
```html
<!-- Title: Title here -->
<!-- Slug: slug-here -->
<!-- Category: Business/Nástroje/Tutoriál/Case Study/Etika/HR -->
<!-- Description: Brief description for the blog card -->
<!-- ImagePrompt: Aibility-style image description -->
<!-- Date: 2026-01-15T00:00:00.000Z -->
```
