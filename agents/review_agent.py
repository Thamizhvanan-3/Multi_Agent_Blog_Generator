# review_agent.py
from textblob import TextBlob
import language_tool_python
import re

class ReviewAgent:
    def __init__(self):
        # Use public server instead of local download
        self.tool = language_tool_python.LanguageToolPublicAPI('en-US')
        
    def proofread(self, content):
        # Grammar and spelling check
        corrected_content = self._correct_grammar(content)
        
        # Improve readability
        improved_content = self._improve_readability(corrected_content)
        
        # Check for consistency
        final_content = self._check_consistency(improved_content)
        
        return final_content
    
    def _correct_grammar(self, content):
        matches = self.tool.check(content)
        return language_tool_python.utils.correct(content, matches)
    
    def _improve_readability(self, content):
        blob = TextBlob(content)
        
        # Split long sentences
        sentences = blob.sentences
        improved_sentences = []
        
        for sentence in sentences:
            if len(sentence.words) > 25:
                # Split very long sentences
                parts = str(sentence).split(',')
                if len(parts) > 1:
                    improved_sentences.extend(parts)
                else:
                    improved_sentences.append(str(sentence))
            else:
                improved_sentences.append(str(sentence))
                
        return ' '.join(improved_sentences)
    
    def _check_consistency(self, content):
        # Check for consistent terminology
        variations = {
            'HR': ['Human Resources', 'H.R.', 'hr'],
            'employee': ['staff', 'workers', 'team members']
        }
        
        for preferred, alternatives in variations.items():
            for alt in alternatives:
                content = re.sub(rf'\b{alt}\b', preferred, content, flags=re.IGNORECASE)
                
        return content