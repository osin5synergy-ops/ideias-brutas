# ideias-brutas
issues->(supply 10% Humano - A FAISCA).

## 🤖 Intent Tag AI Agent

Este repositório conta com um agente de IA que automaticamente analisa issues e aplica tags apropriadas baseadas no conteúdo e contexto.

### Como Funciona

1. **Análise Automática**: Quando uma issue é criada ou editada, o agente analisa o título e descrição
2. **Classificação Inteligente**: Aplica tags baseadas em critérios definidos no [Agent Intent Tag-IA Playbook](./agent_intent_tag-IA.md)
3. **Tags Automáticas**: Adiciona tags de tipo, prioridade, área e complexidade automaticamente

### Categorias de Tags

- **Tipo**: `bug`, `feature`, `documentation`, `maintenance`
- **Prioridade**: `high-priority`, `medium-priority`, `low-priority`  
- **Área**: `frontend`, `backend`, `integration`, `infrastructure`
- **Complexidade**: `easy`, `medium`, `hard`

### Configuração

O agente é executado automaticamente via GitHub Actions. Para detalhes sobre os critérios de classificação, consulte o [playbook completo](./agent_intent_tag-IA.md).
