#!/usr/bin/env python3
"""
Test script for Intent Tag AI Agent
Tests various scenarios to ensure correct tag classification.
"""

from intent_tag_agent import IntentTagAgent


def test_scenarios():
    """Test various issue scenarios."""
    agent = IntentTagAgent()
    
    test_cases = [
        {
            'title': 'Botão de login não funciona no Firefox',
            'body': 'O botão de login não responde quando clico nele. Isso acontece apenas no Firefox.',
            'expected_type': 'bug',
            'expected_area': 'frontend'
        },
        {
            'title': 'Implementar sistema de notificações por email',
            'body': 'Gostaria que o sistema enviasse notificações por email para manter usuários informados.',
            'expected_type': 'feature',
            'expected_priority': 'medium-priority'
        },
        {
            'title': 'Adicionar documentação da API',
            'body': 'Falta documentação sobre como usar a API. Seria importante ter um guia.',
            'expected_type': 'documentation',
            'expected_area': 'backend'
        },
        {
            'title': 'Refatorar código do módulo de autenticação',
            'body': 'O código precisa ser otimizado e limpo para melhor manutenção.',
            'expected_type': 'maintenance'
        },
        {
            'title': 'URGENTE: Sistema não conecta com banco de dados',
            'body': 'Erro crítico que está bloqueando a aplicação em produção.',
            'expected_type': 'bug',
            'expected_priority': 'high-priority',
            'expected_area': 'backend'
        },
        {
            'title': 'Melhorar design da página inicial',
            'body': 'Seria bom atualizar o visual da interface para ficar mais moderno.',
            'expected_type': 'feature',
            'expected_priority': 'low-priority',
            'expected_area': 'frontend'
        }
    ]
    
    print("🧪 Testando Intent Tag AI Agent\n")
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Teste {i}: {test_case['title']}")
        
        tags = agent.analyze_issue(
            test_case['title'], 
            test_case['body']
        )
        
        print(f"Tags sugeridas: {', '.join(tags)}")
        
        # Validate expected tags
        passed_checks = []
        if 'expected_type' in test_case:
            if test_case['expected_type'] in tags:
                passed_checks.append(f"✅ Tipo: {test_case['expected_type']}")
            else:
                passed_checks.append(f"❌ Tipo esperado: {test_case['expected_type']}")
        
        if 'expected_priority' in test_case:
            if test_case['expected_priority'] in tags:
                passed_checks.append(f"✅ Prioridade: {test_case['expected_priority']}")
            else:
                passed_checks.append(f"❌ Prioridade esperada: {test_case['expected_priority']}")
        
        if 'expected_area' in test_case:
            if test_case['expected_area'] in tags:
                passed_checks.append(f"✅ Área: {test_case['expected_area']}")
            else:
                passed_checks.append(f"❌ Área esperada: {test_case['expected_area']}")
        
        for check in passed_checks:
            print(f"  {check}")
        
        print("-" * 50)
    
    print("\n✨ Testes concluídos!")


if __name__ == "__main__":
    test_scenarios()