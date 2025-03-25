import random

class ContentPlanningAgent:
    def __init__(self):
        self.section_templates = [
            "Introduction to {topic}",
            "Why {topic} is Important",
            "Key Benefits of {topic}",
            "Challenges in {topic}",
            "How to Implement {topic} Successfully",
            "Expert Insights on {topic}",
            "Future of {topic}"
        ]

    def create_outline(self, topic):
        outline = {
            "title": f"A Complete Guide to {topic}",
            "sections": []
        }

        # Add structured sections
        selected_sections = random.sample(self.section_templates, 4)  # Pick 4 random sections
        for template in selected_sections:
            outline['sections'].append({
                "heading": template.format(topic=topic),
                "key_points": [f"Key insight about {topic}", f"Current industry trend", "Expert recommendation"]
            })

        return outline
