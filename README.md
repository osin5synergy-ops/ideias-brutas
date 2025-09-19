# ideias-brutas
issues->(supply 10% Humano - A FAISCA).

## Intent Tag AI Agent 🤖

Este repositório conta com um **Intent Tag AI Agent** que analisa automaticamente o conteúdo de novas issues e sugere as tags (labels) mais apropriadas.

### Como funciona

Quando uma nova issue é criada, o agente:

1. **Analisa o conteúdo** do título e corpo da issue
2. **Identifica palavras-chave** e padrões linguísticos em português
3. **Sugere labels** baseado em regras pré-definidas
4. **Comenta na issue** com as sugestões para revisão dos mantenedores

### Labels disponíveis

- `💡 Token de Insight` - Ideias estratégicas e inovações
- `🔥 Token de Dor` - Problemas e dificuldades relatadas
- `🏛️ Proposta de Governança` - Questões de processo e estrutura
- `ops` - Operações e infraestrutura
- `strats` - Estratégia e planejamento
- `tats` - Testes e validações

### Tecnologia

O agente utiliza:
- **GitHub Actions** para automação
- **Análise de texto baseada em regras** para classificação
- **Correspondência de palavras-chave** em português
- **Reconhecimento de padrões linguísticos** específicos

O sistema é projetado para ser facilmente extensível para futuras integrações com serviços de IA externos.
