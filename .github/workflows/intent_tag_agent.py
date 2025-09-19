#!/usr/bin/env python3
"""
Intent Tag AI Agent
Automatically analyzes new GitHub issues and suggests appropriate labels based on content analysis.
"""

import os
import re
import json
import requests
from typing import List, Dict, Set


class IntentTagAgent:
    def __init__(self):
        self.github_token = os.environ['GITHUB_TOKEN']
        self.repository = os.environ['REPOSITORY']
        self.issue_number = int(os.environ['ISSUE_NUMBER'])
        self.issue_title = os.environ.get('ISSUE_TITLE', '')
        self.issue_body = os.environ.get('ISSUE_BODY', '')
        
        self.headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        # Define available labels and their keywords/patterns
        self.label_mapping = {
            '💡 Token de Insight': {
                'keywords': [
                    'ideia', 'insight', 'sugestão', 'proposta', 'conceito', 'estratégia',
                    'oportunidade', 'inovação', 'solução', 'melhoria', 'visão', 'criativo',
                    'brainstorm', 'inspiração', 'descoberta', 'revelação', 'epifania',
                    'inteligência', 'genial', 'brilhante', 'arquitetura', 'modelo', 'framework',
                    # Domain-specific terms from repository
                    'efeito', 'usar', 'aplicar', 'implementar', 'sistema', 'ferramenta',
                    'recurso', 'funcionalidade', 'feature', 'método', 'abordagem', 'técnica',
                    'solução', 'alternativa', 'opção', 'possibilidade', 'cenário', 'canvas',
                    'playbook', 'protocolo', 'doutrina', 'centauro', 'synergies', 'token',
                    'curadoria', 'análise', 'validar', 'testar', 'explorar', 'expansão'
                ],
                'patterns': [
                    r'e se .*\?',
                    r'que tal .*\?',
                    r'seria interessante',
                    r'poderia.*funcionar',
                    r'nova.*abordagem',
                    r'estratégia.*para',
                    r'usar.*para',
                    r'aplicar.*em',
                    r'implementar.*um',
                    r'criar.*um.*sistema'
                ]
            },
            '🔥 Token de Dor': {
                'keywords': [
                    'problema', 'erro', 'bug', 'falha', 'issue', 'defeito', 'dificuldade',
                    'limitação', 'bloqueio', 'impedimento', 'frustração', 'não funciona',
                    'quebrado', 'lento', 'travando', 'crashando', 'indisponível',
                    'péssima experiência', 'atendimento ruim', 'falhou', 'não consegue'
                ],
                'patterns': [
                    r'não .*funciona',
                    r'não .*consegue',
                    r'erro.*ao',
                    r'falha.*em',
                    r'problema.*com',
                    r'está.*quebrado',
                    r'péssima.*experiência'
                ]
            },
            '🏛️ Proposta de Governança': {
                'keywords': [
                    'governança', 'processo', 'política', 'regra', 'procedimento', 'protocolo',
                    'workflow', 'metodologia', 'framework', 'estrutura', 'organização',
                    'padronização', 'definição', 'diretrizes', 'normas', 'regulamento',
                    'constituição', 'lei', 'código', 'urbanismo', 'kda', 'wiki'
                ],
                'patterns': [
                    r'devemos.*definir',
                    r'precisamos.*estabelecer',
                    r'proposta.*de.*mudança',
                    r'novo.*processo',
                    r'formalizar.*o',
                    r'estruturar.*com',
                    r'código.*de.*urbanismo'
                ]
            },
            'ops': {
                'keywords': [
                    'operação', 'deploy', 'produção', 'infraestrutura', 'servidor', 'devops',
                    'monitoramento', 'logs', 'backup', 'security', 'performance', 'automação',
                    'pipeline', 'ci/cd', 'workflow', 'integração', 'deployment', 'release'
                ],
                'patterns': [
                    r'automation',
                    r'deploy.*para',
                    r'configurar.*ambiente',
                    r'pipeline.*de'
                ]
            },
            'strats': {
                'keywords': [
                    'estratégia', 'planejamento', 'roadmap', 'visão', 'missão', 'objetivo',
                    'meta', 'plano', 'direcionamento', 'posicionamento', 'mercado', 'negócio',
                    'comercial', 'vendas', 'marketing', 'crescimento', 'expansão', 'cliente',
                    'ponte', 'centauro', 'sinergias', 'ecossistema', 'lead', 'oportunidade',
                    # Domain-specific strategic terms
                    'cavalaria', 'crew', 'mkt', 'case', 'carta', 'convite', 'proposta',
                    'parceria', 'colaboração', 'aliança', 'diplomacia', 'conciliação',
                    'bridge', 'interface', 'governo', 'liderança', 'moderadora', 'paraguai',
                    'floripa', 'adriano', 'triunfo', 'joao', 'crespo', 'maria', 'morena'
                ],
                'patterns': [
                    r'estratégia.*para',
                    r'plano.*de.*ação',
                    r'mercado.*do',
                    r'expandir.*para',
                    r'lead.*quente',
                    r'oportunidade.*de',
                    r'parceria.*com',
                    r'colaboração.*entre'
                ]
            },
            'tats': {
                'keywords': [
                    'teste', 'validação', 'experimento', 'prova de conceito', 'poc', 'mvp',
                    'protótipo', 'demo', 'sample', 'exemplo', 'trial', 'piloto',
                    # Testing and validation specific terms
                    'validar', 'testar', 'verificar', 'analisar', 'checar', 'conferir',
                    'debug', 'troubleshoot', 'diagnosticar', 'monitorar', 'observar',
                    'experiência', 'usuário', 'feedback', 'revisão', 'auditoria',
                    'notebooklm', 'método', 'técnica', 'ferramenta', 'recurso', 'app'
                ],
                'patterns': [
                    r'test.*',
                    r'validar.*',
                    r'experim.*',
                    r'prova.*de.*conceito',
                    r'será.*que.*consigo',
                    r'vou.*tentar',
                    r'fazendo.*teste'
                ]
            }
        }

    def normalize_text(self, text: str) -> str:
        """Normalize text for analysis (lowercase, remove special chars, etc)"""
        if not text:
            return ""
        
        # Convert to lowercase and remove extra whitespace
        text = text.lower().strip()
        
        # Remove markdown syntax
        text = re.sub(r'[#*`_\[\]()]', ' ', text)
        
        # Remove URLs
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', text)
        
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)
        
        return text

    def extract_keywords(self, text: str) -> Set[str]:
        """Extract meaningful keywords from text"""
        normalized = self.normalize_text(text)
        
        # Split into words and filter out common stop words
        stop_words = {
            'a', 'o', 'e', 'de', 'do', 'da', 'em', 'um', 'uma', 'para', 'com', 'por', 
            'que', 'se', 'não', 'mas', 'ou', 'como', 'quando', 'onde', 'porque', 'seu',
            'sua', 'ele', 'ela', 'este', 'esta', 'isso', 'aqui', 'ali', 'muito', 'mais',
            'também', 'só', 'já', 'ainda', 'bem', 'então', 'assim', 'depois', 'antes'
        }
        
        words = set(re.findall(r'\b\w{3,}\b', normalized))
        return words - stop_words

    def analyze_content(self, title: str, body: str) -> Dict[str, float]:
        """Analyze issue content and return label confidence scores"""
        full_text = f"{title} {body}"
        normalized_text = self.normalize_text(full_text)
        content_keywords = self.extract_keywords(full_text)
        
        scores = {}
        
        for label_name, criteria in self.label_mapping.items():
            score = 0.0
            
            # Check keyword matches
            keyword_matches = 0
            for keyword in criteria['keywords']:
                if keyword in normalized_text:
                    keyword_matches += 1
                    # Give higher weight to title matches
                    if keyword in self.normalize_text(title):
                        score += 2.0
                    else:
                        score += 1.0
            
            # Check pattern matches
            pattern_matches = 0
            for pattern in criteria.get('patterns', []):
                if re.search(pattern, normalized_text):
                    pattern_matches += 1
                    score += 1.5
            
            # Normalize score based on content length and matches
            if len(content_keywords) > 0:
                keyword_density = keyword_matches / len(content_keywords)
                score += keyword_density * 5
            
            scores[label_name] = score
        
        return scores

    def get_suggested_labels(self, title: str, body: str, threshold: float = 1.0) -> List[str]:
        """Get suggested labels based on content analysis"""
        scores = self.analyze_content(title, body)
        
        # Sort by score and filter by threshold
        suggested = []
        for label, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            if score >= threshold:
                suggested.append((label, score))
        
        return suggested

    def post_comment(self, comment_body: str) -> bool:
        """Post a comment on the issue with suggested labels"""
        url = f"https://api.github.com/repos/{self.repository}/issues/{self.issue_number}/comments"
        
        data = {
            'body': comment_body
        }
        
        response = requests.post(url, headers=self.headers, json=data)
        return response.status_code == 201

    def format_suggestion_comment(self, suggestions: List[tuple]) -> str:
        """Format the suggestion comment with analysis results"""
        if not suggestions:
            return """🤖 **Intent Tag AI Agent**

Analisei esta issue mas não consegui identificar tags específicas com alta confiança. 

Os mantenedores podem revisar e aplicar as labels apropriadas manualmente.

---
*Este comentário foi gerado automaticamente pelo Intent Tag AI Agent*"""

        comment = """🤖 **Intent Tag AI Agent**

Analisei o conteúdo desta issue e sugiro as seguintes tags:

"""
        
        for label, score in suggestions:
            confidence = "Alta" if score >= 3.0 else "Média" if score >= 2.0 else "Baixa"
            comment += f"• **{label}** (Confiança: {confidence})\n"
        
        comment += f"""

**Análise:**
- Título analisado: "{self.issue_title}"
- Palavras-chave identificadas no conteúdo
- Padrões linguísticos reconhecidos

**Próximos passos:**
Os mantenedores podem revisar essas sugestões e aplicar as labels apropriadas.

---
*Este comentário foi gerado automaticamente pelo Intent Tag AI Agent*"""
        
        return comment

    def run(self):
        """Main execution method"""
        print(f"Analyzing issue #{self.issue_number}: {self.issue_title}")
        
        # Analyze issue content
        suggestions = self.get_suggested_labels(self.issue_title, self.issue_body)
        
        print(f"Found {len(suggestions)} suggested labels")
        for label, score in suggestions:
            print(f"  - {label}: {score:.2f}")
        
        # Format and post comment
        comment = self.format_suggestion_comment(suggestions)
        
        if self.post_comment(comment):
            print("Successfully posted suggestion comment")
        else:
            print("Failed to post comment")
            return 1
        
        return 0


if __name__ == "__main__":
    agent = IntentTagAgent()
    exit_code = agent.run()
    exit(exit_code)