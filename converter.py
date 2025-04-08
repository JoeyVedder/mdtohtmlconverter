import re
import markdown

def convert_markdown_to_html(md_text):
    md_text = re.sub(r'^(#{1,6})\s*(.*?)\s*#*$', r'<h\1>\2</h\1>', md_text) # Converts headers

    md_text = re.sub(r'(\*\*|__)(.*?)\1', r'<strong>\2</strong>', md_text) # Converts bold text 

    md_text = re.sub(r'(\*|_)(.*?)\1', r'<em>\2</em>', md_text) # Converts italic text 

    md_text = re.sub(r'`(.*?)`', r'<code>\1</code>', md_text) # Converts inline code 

    md_text = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', md_text, flags=re.DOTALL) # Converts code blocks 

    md_text = re.sub(r'^[\*\-\+]\s+(.*)', r'<li>\1</li>', md_text, flags=re.MULTILINE) # Converts unordered lists 
    md_text = re.sub(r'^\d+\.\s+(.*)', r'<li>\1</li>', md_text, flags=re.MULTILINE) # Converts ordered lists
    md_text = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', md_text) # Converts unordered list to <ul> tags
    md_text = re.sub(r'(<li>.*</li>)', r'<ol>\1</ol>', md_text) # Converts ordered list to <ol> tags 


    return md_text


