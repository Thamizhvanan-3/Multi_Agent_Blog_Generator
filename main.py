import os
from agents.research_agent import ResearchAgent
from agents.content_planning_agent import ContentPlanningAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.seo_optimization_agent import SEOOptimizationAgent
from agents.review_agent import ReviewAgent


# Initialize agents
research_agent = ResearchAgent()
content_planning_agent = ContentPlanningAgent()
content_generation_agent = ContentGenerationAgent()
seo_optimization_agent = SEOOptimizationAgent()
review_agent = ReviewAgent()

# Define topic
test_topic = "Remote Work Strategies"

# Fetch real research data
research_data = research_agent.research_topic(test_topic)

# Generate structured outline
outline = content_planning_agent.create_outline(test_topic)

# Generate content dynamically from real research
content = content_generation_agent.generate_content(outline, research_data)

# Optimize content for SEO
optimized_content = seo_optimization_agent.optimize(content, test_topic)

# Proofread content
final_content = review_agent.proofread(optimized_content)

# Save the final blog post
output_dir = "blog_posts"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "final_blog.md")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_content)

print(f"\n✅ Blog post successfully generated: {output_file}")
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_as_pdf(content, filename):
    """Save blog content as a PDF file with proper encoding"""
    pdf_filename = f"{filename}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont("Helvetica", 12)

    y = 750  # Start position
    for line in content.split("\n"):
        c.drawString(50, y, line)
        y -= 20  # Move down each line
        if y < 50:  # Create a new page if space runs out
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750

    c.save()
    print(f"✅ PDF saved as: {pdf_filename}")

# Example usage
save_as_pdf(final_content, f"blog_posts/{test_topic.replace(' ', '_')}")
