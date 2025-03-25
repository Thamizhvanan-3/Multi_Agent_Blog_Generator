from bs4 import BeautifulSoup
import markdown


class SEOOptimizationAgent:
    def __init__(self):
        self.common_keywords = ["remote work", "employee engagement", "HR technology"]

    def optimize(self, content, topic):
        """Enhance blog content for SEO while keeping readability"""
        html_content = markdown.markdown(content)
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove <strong> tags
        for tag in soup.find_all('strong'):
            tag.unwrap()

        # Ensure bullet points are formatted properly
        cleaned_text = []
        for line in soup.get_text().split("\n"):
            if "·" in line:  # If bullet points are detected
                cleaned_text.append(line.replace("·", "-"))  # Convert to proper markdown bullet
            else:
                cleaned_text.append(line)

        return "\n".join(cleaned_text)
