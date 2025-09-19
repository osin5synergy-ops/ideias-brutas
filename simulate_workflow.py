#!/usr/bin/env python3
"""
Simulate GitHub Actions workflow behavior locally
Shows what the workflow would do when processing issues.
"""

from intent_tag_agent import IntentTagAgent
import json


def simulate_github_workflow():
    """Simulate the GitHub Actions workflow processing."""
    agent = IntentTagAgent()
    
    # Mock issue data (similar to what GitHub webhook would provide)
    mock_issues = [
        {
            'title': 'Erro 500 ao fazer login com Google OAuth',
            'body': '''**Describe the bug**
            Quando tento fazer login usando Google OAuth, recebo erro 500.
            
            **To Reproduce**
            1. Vá para a página de login
            2. Clique em "Login com Google"
            3. Complete a autenticação
            4. Veja o erro
            
            **Expected behavior**
            Deveria fazer login normalmente.''',
            'template_type': 'bug_report'
        },
        {
            'title': 'Adicionar filtros avançados na listagem de produtos',
            'body': '''**Is your feature request related to a problem?**
            Sim, é difícil encontrar produtos específicos na lista.
            
            **Describe the solution you'd like**
            Gostaria que houvesse filtros por categoria, preço e avaliação.
            
            **Additional context**
            Isso melhoraria muito a experiência do usuário.''',
            'template_type': 'feature_request'
        },
        {
            'title': 'Como configurar variáveis de ambiente?',
            'body': 'Preciso de documentação sobre como configurar as variáveis de ambiente para desenvolvimento local.',
            'template_type': 'custom'
        }
    ]
    
    print("🤖 Simulando GitHub Actions Workflow")
    print("=" * 50)
    
    for i, issue in enumerate(mock_issues, 1):
        print(f"\n📋 Issue #{i}: {issue['title']}")
        print(f"📄 Template: {issue['template_type']}")
        
        # Step 1: Extract template type (simulated)
        template_type = issue['template_type']
        print(f"🔍 Template detectado: {template_type}")
        
        # Step 2: Run the AI agent
        tags = agent.analyze_issue(issue['title'], issue['body'], template_type)
        formatted_tags = agent.format_tags_for_github(tags)
        
        print(f"🏷️  Tags sugeridas: {formatted_tags}")
        
        # Step 3: Simulate GitHub API call
        print("📝 Simulando aplicação das tags...")
        
        # Step 4: Simulate comment
        comment = f"""🤖 **Intent Tag AI Agent**

Automaticamente analisei esta issue e apliquei as seguintes tags:
{chr(10).join(f'- `{tag}`' for tag in tags)}

_Esta classificação foi baseada no [Agent Intent Tag-IA Playbook](./agent_intent_tag-IA.md)._"""
        
        print("💬 Comentário que seria adicionado:")
        print(comment)
        print("-" * 50)
    
    print("\n✅ Simulação concluída!")
    print("🚀 Em produção, isso aconteceria automaticamente a cada nova issue.")


if __name__ == "__main__":
    simulate_github_workflow()