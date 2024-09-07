from firecrawl import FirecrawlApp
import google.generativeai as genai
import os

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
# Initialize Firecrawl SDK with API key
app = FirecrawlApp(api_key="fc-YOUR_API_KEY")


def scrape_website(url):
    """Scrape the given URL and return markdown and HTML content."""
    scrape_result = app.scrape_url(url, params={'formats': ['markdown', 'html']})
    response = model.generate_content("Please analyze this data and generate a detailed summary highlighting the key points, methodologies, results, and conclusions of the research. Ensure that the summary is clear, concise, and covers the essential aspects of the paper for easy understanding."+scrape_result['markdown'])
    return response.text

