#!/usr/bin/env python3
"""
Demo script for Intent Tag AI Agent
Shows interactive usage of the agent for manual testing.
"""

from intent_tag_agent import IntentTagAgent


def interactive_demo():
    """Interactive demo of the tag agent."""
    agent = IntentTagAgent()
    
    print("🤖 Intent Tag AI Agent - Demo Interativo")
    print("=" * 50)
    print("Digite issues para ver como serão classificadas.")
    print("Digite 'sair' para terminar.\n")
    
    while True:
        try:
            print("\n📝 Nova Issue:")
            title = input("Título: ").strip()
            
            if title.lower() in ['sair', 'exit', 'quit']:
                break
                
            if not title:
                print("❌ Título não pode estar vazio!")
                continue
                
            body = input("Descrição: ").strip()
            
            # Analyze the issue
            tags = agent.analyze_issue(title, body)
            
            print(f"\n🏷️  Tags sugeridas: {', '.join(tags)}")
            print(f"📋 Formatado para GitHub: {agent.format_tags_for_github(tags)}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    print("\n👋 Obrigado por usar o Intent Tag AI Agent!")


def example_issues():
    """Show some example issues and their classifications."""
    agent = IntentTagAgent()
    
    examples = [
        ("Login quebrado", "O sistema não aceita minha senha"),
        ("Adicionar dark mode", "Seria útil ter um tema escuro na aplicação"),
        ("Como configurar API?", "Preciso de documentação sobre a configuração"),
        ("Otimizar performance", "O sistema está lento, precisa refatorar o código")
    ]
    
    print("🌟 Exemplos de Classificação")
    print("=" * 40)
    
    for title, body in examples:
        tags = agent.analyze_issue(title, body)
        print(f"\n📝 '{title}'")
        print(f"🏷️  {', '.join(tags)}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--examples":
        example_issues()
    else:
        interactive_demo()