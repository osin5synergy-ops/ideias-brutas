#!/usr/bin/env python3
"""
Test script for Intent Tag AI Agent
Tests the keyword matching and pattern recognition logic
"""

import sys
import os

# Add the workflows directory to the path so we can import the agent
sys.path.append('.github/workflows')

try:
    from intent_tag_agent import IntentTagAgent
except ImportError:
    print("Could not import IntentTagAgent - make sure the script is in the right location")
    sys.exit(1)


class MockAgent(IntentTagAgent):
    """Mock version of IntentTagAgent for testing without GitHub API calls"""
    
    def __init__(self):
        # Set mock environment variables
        os.environ['GITHUB_TOKEN'] = 'mock_token'
        os.environ['REPOSITORY'] = 'test/repo'
        os.environ['ISSUE_NUMBER'] = '1'
        os.environ['ISSUE_TITLE'] = 'Test Issue'
        os.environ['ISSUE_BODY'] = 'Test body'
        
        # Initialize parent without calling API
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


def test_insight_detection():
    """Test detection of insight/idea tokens"""
    agent = MockAgent()
    
    test_cases = [
        ("Nova ideia para marketing", "Tenho uma sugestão interessante", ['💡 Token de Insight']),
        ("Estratégia inovadora", "E se usássemos uma nova abordagem?", ['💡 Token de Insight']),
        ("Epifania sobre arquitetura", "Descobri um modelo genial", ['💡 Token de Insight']),
    ]
    
    print("Testing Insight Detection:")
    for title, body, expected in test_cases:
        suggestions = agent.get_suggested_labels(title, body, threshold=1.0)
        suggested_labels = [label for label, score in suggestions]
        
        print(f"  Title: {title}")
        print(f"  Body: {body}")
        print(f"  Expected: {expected}")
        print(f"  Got: {suggested_labels}")
        
        # Check if at least one expected label is suggested
        found = any(label in suggested_labels for label in expected)
        print(f"  Result: {'✅ PASS' if found else '❌ FAIL'}")
        print()


def test_problem_detection():
    """Test detection of problem/pain tokens"""
    agent = MockAgent()
    
    test_cases = [
        ("Erro no sistema", "O sistema não funciona corretamente", ['🔥 Token de Dor']),
        ("Bug crítico", "Encontrei um problema com a aplicação", ['🔥 Token de Dor']),
        ("Péssima experiência", "Tive uma péssima experiência com o atendimento", ['🔥 Token de Dor']),
    ]
    
    print("Testing Problem Detection:")
    for title, body, expected in test_cases:
        suggestions = agent.get_suggested_labels(title, body, threshold=1.0)
        suggested_labels = [label for label, score in suggestions]
        
        print(f"  Title: {title}")
        print(f"  Body: {body}")
        print(f"  Expected: {expected}")
        print(f"  Got: {suggested_labels}")
        
        found = any(label in suggested_labels for label in expected)
        print(f"  Result: {'✅ PASS' if found else '❌ FAIL'}")
        print()


def test_governance_detection():
    """Test detection of governance tokens"""
    agent = MockAgent()
    
    test_cases = [
        ("Proposta de governança", "Precisamos estabelecer um novo processo", ['🏛️ Proposta de Governança']),
        ("Código de Urbanismo", "Devemos definir as diretrizes", ['🏛️ Proposta de Governança']),
        ("Estruturar workflow", "Formalizar o procedimento de trabalho", ['🏛️ Proposta de Governança']),
    ]
    
    print("Testing Governance Detection:")
    for title, body, expected in test_cases:
        suggestions = agent.get_suggested_labels(title, body, threshold=1.0)
        suggested_labels = [label for label, score in suggestions]
        
        print(f"  Title: {title}")
        print(f"  Body: {body}")
        print(f"  Expected: {expected}")
        print(f"  Got: {suggested_labels}")
        
        found = any(label in suggested_labels for label in expected)
        print(f"  Result: {'✅ PASS' if found else '❌ FAIL'}")
        print()


def test_real_issues():
    """Test with some real issue examples from the repository"""
    agent = MockAgent()
    
    real_cases = [
        (
            "gifity fifity",
            "Preciso expotar os arquivos .md do obsian para uma curadoria.",
            "Should detect insight/strategy"
        ),
        (
            "Ux effect raspadinha", 
            "Usar efeito raspadinha para ganhar algum brinde na tela do smart raspa e ao final da sensação de raspar alguma coisa como se tivesse tirando o efeito raspadinha mesmo da lotérica simular um efeito raspadinho uma lotérica para micro incentivos.",
            "Should detect insight"
        ),
        (
            "Validar NotebookLM",
            "Usar para validar os métodos GigiLPV e apelidisecure #46 #47",
            "Should detect testing/validation"
        )
    ]
    
    print("Testing Real Issues:")
    for title, body, description in real_cases:
        suggestions = agent.get_suggested_labels(title, body, threshold=0.5)
        
        print(f"  Title: {title}")
        print(f"  Body: {body[:100]}...")
        print(f"  Description: {description}")
        print(f"  Suggestions: {[(label, f'{score:.2f}') for label, score in suggestions]}")
        print()


if __name__ == "__main__":
    print("🧪 Running Intent Tag AI Agent Tests\n")
    
    test_insight_detection()
    test_problem_detection() 
    test_governance_detection()
    test_real_issues()
    
    print("✅ All tests completed!")