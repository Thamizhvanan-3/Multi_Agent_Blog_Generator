class ContentGenerationAgent:
    def __init__(self):
        pass

    def generate_content(self, outline, research_data):
        """Generate well-structured content dynamically from research with expanded details"""
        content = f"# {outline['title']}\n\n"

        for section in outline['sections']:
            content += f"## {section['heading']}\n\n"

            # Use research data first before using placeholders
            if research_data:
                content += self._generate_paragraph(section['heading'], research_data) + "\n\n"
            else:
                content += f"🔍 {section['heading']} is a trending topic. Explore industry insights for more.\n\n"

            for point in section['key_points']:
                if research_data:
                    paragraph = self._generate_paragraph(point, research_data)
                    content += paragraph + "\n\n"
                else:
                    content += f"🔍 {point} is a key industry trend. Consider recent case studies.\n\n"

        return content

    def _generate_paragraph(self, topic, research_data):
        """Use real research data or meaningful fallback only if necessary"""
        if research_data and len(research_data) > 0:
            return f"- {research_data.pop(0)}"
        else:
            return f"🔍 {topic} is widely discussed. Experts suggest exploring recent case studies and industry insights."


    def _generate_expanded_text(self, topic):
        """Generate a detailed explanation for a topic when research data is missing"""
        return (
            f"🔍 {topic} is a growing field with significant impact. "
            f"Companies that effectively implement {topic} benefit from improved efficiency, "
            f"employee satisfaction, and long-term sustainability. Various studies suggest that "
            f"organizations focusing on {topic} experience increased engagement and productivity. "
            f"Future trends indicate that {topic} will continue evolving with technological "
            f"advancements and data-driven decision-making. "
            f"\n\n### Key Benefits of {topic}\n"
            f"- Increased flexibility and better work-life balance.\n"
            f"- Access to a global talent pool, allowing businesses to hire the best employees worldwide.\n"
            f"- Cost savings on office space and utilities.\n"
            f"- Higher employee retention rates due to improved job satisfaction.\n\n"
            f"### Challenges of {topic}\n"
            f"- Communication barriers between remote and in-office employees.\n"
            f"- Time zone differences that can cause delays in decision-making.\n"
            f"- Difficulty in maintaining company culture and team collaboration.\n"
            f"- Cybersecurity concerns when employees work from home.\n\n"
            f"### Expert Opinions\n"
            f"Industry leaders such as Google and Microsoft have embraced remote work, highlighting its impact "
            f"on productivity and employee engagement. According to a 2023 study, remote employees report a "
            f"20% increase in productivity compared to office-based employees.\n\n"
        )
