#!/usr/bin/env python3
"""
Intent Tag AI Agent
Automatically analyzes GitHub issues and applies appropriate tags based on content analysis.
"""

import json
import re
import sys
from typing import List, Dict, Set
from dataclasses import dataclass


@dataclass
class TagCriteria:
    """Represents criteria for a specific tag."""
    name: str
    keywords: List[str]
    patterns: List[str]
    context_words: List[str]
    weight: float = 1.0


class IntentTagAgent:
    """AI Agent for automatically tagging GitHub issues based on content analysis."""
    
    def __init__(self):
        self.tag_criteria = self._initialize_criteria()
    
    def _initialize_criteria(self) -> Dict[str, List[TagCriteria]]:
        """Initialize tag criteria based on the playbook."""
        return {
            'type': [
                TagCriteria(
                    name='bug',
                    keywords=['bug', 'erro', 'falha', 'problema', 'não funciona', 'quebrado', 'exception', 'error'],
                    patterns=[r'não\s+(?:está\s+)?funcionando', r'erro\s+ao', r'falha\s+em', r'bug\s+em'],
                    context_words=['comportamento', 'inesperado', 'código', 'sistema']
                ),
                TagCriteria(
                    name='feature',
                    keywords=['feature', 'funcionalidade', 'nova', 'implementar', 'adicionar', 'criar', 'enhancement', 'melhorar'],
                    patterns=[r'gostaria\s+que', r'seria\s+útil', r'adicionar', r'implementar', r'melhorar'],
                    context_words=['solicitação', 'melhoria', 'novo', 'funcionalidade']
                ),
                TagCriteria(
                    name='documentation',
                    keywords=['documentação', 'docs', 'readme', 'tutorial', 'guia', 'manual', 'explicação'],
                    patterns=[r'documentar', r'falta\s+documentação', r'como\s+fazer'],
                    context_words=['explicação', 'tutorial', 'guia', 'manual']
                ),
                TagCriteria(
                    name='maintenance',
                    keywords=['manutenção', 'refactor', 'cleanup', 'organizar', 'otimizar', 'performance'],
                    patterns=[r'refatorar', r'otimizar', r'limpar\s+código'],
                    context_words=['manutenção', 'refatoração', 'otimização', 'limpeza']
                )
            ],
            'priority': [
                TagCriteria(
                    name='high-priority',
                    keywords=['urgente', 'crítico', 'bloqueador', 'segurança', 'production'],
                    patterns=[r'urgente', r'crítico', r'bloqueador'],
                    context_words=['bloqueio', 'impedem', 'crítica'],
                    weight=2.0
                ),
                TagCriteria(
                    name='medium-priority',
                    keywords=['importante', 'necessário', 'afeta usuários'],
                    patterns=[r'importante', r'necessário', r'afeta\s+usuários'],
                    context_words=['relevante', 'importante', 'usuários'],
                    weight=1.5
                ),
                TagCriteria(
                    name='low-priority',
                    keywords=['seria bom', 'melhoria', 'sugestão'],
                    patterns=[r'seria\s+bom', r'melhoria', r'sugestão'],
                    context_words=['sugestão', 'opcional', 'nice-to-have'],
                    weight=1.0
                )
            ],
            'area': [
                TagCriteria(
                    name='frontend',
                    keywords=['UI', 'interface', 'frontend', 'visual', 'design', 'CSS', 'HTML', 'JavaScript'],
                    patterns=[r'interface\s+do\s+usuário', r'frontend', r'visual'],
                    context_words=['usuário', 'tela', 'página', 'botão']
                ),
                TagCriteria(
                    name='backend',
                    keywords=['API', 'backend', 'servidor', 'banco de dados', 'performance', 'lógica'],
                    patterns=[r'API', r'backend', r'servidor'],
                    context_words=['servidor', 'banco', 'dados', 'lógica']
                ),
                TagCriteria(
                    name='integration',
                    keywords=['integração', 'API externa', 'webhook', 'conexão', 'terceiros'],
                    patterns=[r'integração', r'API\s+externa', r'webhook'],
                    context_words=['externa', 'terceiros', 'integração', 'conexão']
                ),
                TagCriteria(
                    name='infrastructure',
                    keywords=['deploy', 'infraestrutura', 'servidor', 'hosting', 'CI/CD', 'docker'],
                    patterns=[r'deploy', r'infraestrutura', r'CI/CD'],
                    context_words=['deploy', 'hosting', 'infraestrutura', 'servidor']
                )
            ],
            'complexity': [
                TagCriteria(
                    name='easy',
                    keywords=['simples', 'pequeno', 'rápido', 'direto'],
                    patterns=[r'simples', r'pequeno', r'rápido'],
                    context_words=['simples', 'fácil', 'pequeno', 'direto']
                ),
                TagCriteria(
                    name='medium',
                    keywords=['moderado', 'análise', 'múltiplos arquivos'],
                    patterns=[r'moderado', r'análise', r'múltiplos'],
                    context_words=['moderado', 'análise', 'múltiplos', 'arquivos']
                ),
                TagCriteria(
                    name='hard',
                    keywords=['complexo', 'arquitetural', 'refatoração', 'componentes'],
                    patterns=[r'complexo', r'arquitetural', r'refatoração'],
                    context_words=['complexo', 'arquitetural', 'refatoração', 'múltiplos']
                )
            ]
        }
    
    def analyze_issue(self, title: str, body: str, template_type: str = None) -> List[str]:
        """
        Analyze an issue and return appropriate tags.
        
        Args:
            title: Issue title
            body: Issue body/description
            template_type: Type of template used (bug_report, feature_request, etc.)
            
        Returns:
            List of tags to apply
        """
        text_content = f"{title} {body}".lower()
        suggested_tags = []
        
        # Analyze each category
        for category, criteria_list in self.tag_criteria.items():
            category_scores = {}
            
            for criteria in criteria_list:
                score = self._calculate_tag_score(text_content, criteria)
                if score > 0:
                    category_scores[criteria.name] = score
            
            # Select best tag from category
            if category_scores:
                best_tag = max(category_scores.items(), key=lambda x: x[1])
                suggested_tags.append(best_tag[0])
        
        # Apply template-based logic
        if template_type:
            template_tags = self._get_template_tags(template_type)
            for tag in template_tags:
                if tag not in suggested_tags:
                    suggested_tags.append(tag)
        
        # Ensure minimum tags
        if not any(tag in ['bug', 'feature', 'documentation', 'maintenance'] for tag in suggested_tags):
            # Default based on common patterns
            if any(word in text_content for word in ['bug', 'erro', 'falha', 'problema']):
                suggested_tags.append('bug')
            elif any(word in text_content for word in ['adicionar', 'implementar', 'nova']):
                suggested_tags.append('feature')
            else:
                suggested_tags.append('enhancement')
        
        return suggested_tags
    
    def _calculate_tag_score(self, text: str, criteria: TagCriteria) -> float:
        """Calculate relevance score for a tag based on criteria."""
        score = 0.0
        
        # Keyword matching
        for keyword in criteria.keywords:
            if keyword.lower() in text:
                score += 1.0 * criteria.weight
        
        # Pattern matching
        for pattern in criteria.patterns:
            if re.search(pattern, text, re.IGNORECASE):
                score += 1.5 * criteria.weight
        
        # Context word matching
        for context_word in criteria.context_words:
            if context_word.lower() in text:
                score += 0.5 * criteria.weight
        
        return score
    
    def _get_template_tags(self, template_type: str) -> List[str]:
        """Get default tags based on issue template type."""
        template_mapping = {
            'bug_report': ['bug'],
            'feature_request': ['feature'],
            'custom': []
        }
        return template_mapping.get(template_type, [])
    
    def format_tags_for_github(self, tags: List[str]) -> str:
        """Format tags for GitHub API or CLI usage."""
        return ','.join(tags)


def main():
    """Main function for CLI usage."""
    if len(sys.argv) < 3:
        print("Usage: python intent_tag_agent.py <title> <body> [template_type]")
        sys.exit(1)
    
    title = sys.argv[1]
    body = sys.argv[2]
    template_type = sys.argv[3] if len(sys.argv) > 3 else None
    
    agent = IntentTagAgent()
    tags = agent.analyze_issue(title, body, template_type)
    
    print("Suggested tags:", agent.format_tags_for_github(tags))


if __name__ == "__main__":
    main()