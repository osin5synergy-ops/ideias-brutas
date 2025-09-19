# Agent Intent Tag-IA Playbook

## Objetivo
Este agente automaticamente analisa issues e aplica tags apropriadas baseadas no conteúdo e contexto da issue.

## Critérios de Classificação

### 1. Tipo de Issue

#### 🐛 Bug
- **Palavras-chave**: bug, erro, falha, problema, não funciona, quebrado, exception, error
- **Contexto**: Descrições de comportamento inesperado, erros de código, falhas de sistema
- **Padrões**: "Não está funcionando", "Erro ao...", "Falha em...", "Bug em..."

#### ✨ Feature
- **Palavras-chave**: feature, funcionalidade, nova, implementar, adicionar, criar, enhancement
- **Contexto**: Solicitações de novas funcionalidades ou melhorias
- **Padrões**: "Gostaria que...", "Seria útil...", "Adicionar...", "Implementar..."

#### 📚 Documentation
- **Palavras-chave**: documentação, docs, readme, tutorial, guia, manual, explicação
- **Contexto**: Issues relacionadas a documentação, tutoriais ou explicações
- **Padrões**: "Documentar...", "Falta documentação...", "Como fazer..."

#### 🔧 Maintenance
- **Palavras-chave**: manutenção, refactor, cleanup, organizar, otimizar, performance
- **Contexto**: Tarefas de manutenção, refatoração ou otimização
- **Padrões**: "Refatorar...", "Otimizar...", "Limpar código..."

### 2. Prioridade

#### 🔥 High Priority
- **Indicadores**: Bloqueadores, issues críticas, problemas de segurança
- **Palavras-chave**: urgente, crítico, bloqueador, segurança, production
- **Contexto**: Issues que impedem o funcionamento normal

#### ⚡ Medium Priority
- **Indicadores**: Funcionalidades importantes, bugs não críticos
- **Palavras-chave**: importante, necessário, afeta usuários
- **Contexto**: Issues relevantes mas não bloqueadoras

#### 📋 Low Priority
- **Indicadores**: Melhorias menores, sugestões
- **Palavras-chave**: seria bom, melhoria, sugestão
- **Contexto**: Nice-to-have, melhorias opcionais

### 3. Área/Componente

#### 🎨 Frontend
- **Palavras-chave**: UI, interface, frontend, visual, design, CSS, HTML, JavaScript
- **Contexto**: Issues relacionadas à interface do usuário

#### ⚙️ Backend
- **Palavras-chave**: API, backend, servidor, banco de dados, performance, lógica
- **Contexto**: Issues relacionadas ao servidor ou lógica de negócio

#### 🔌 Integration
- **Palavras-chave**: integração, API externa, webhook, conexão, terceiros
- **Contexto**: Issues sobre integrações com sistemas externos

#### 🏗️ Infrastructure
- **Palavras-chave**: deploy, infraestrutura, servidor, hosting, CI/CD, docker
- **Contexto**: Issues relacionadas à infraestrutura e deploy

### 4. Complexidade

#### 🟢 Easy
- **Indicadores**: Issues simples, mudanças pequenas
- **Estimativa**: Poucas linhas de código, alterações diretas

#### 🟡 Medium
- **Indicadores**: Issues que requerem análise moderada
- **Estimativa**: Múltiplos arquivos, lógica moderada

#### 🔴 Hard
- **Indicadores**: Issues complexas, mudanças arquiteturais
- **Estimativa**: Refatoração significativa, múltiplos componentes

## Regras de Aplicação

1. **Análise do Título**: Primeiro analise o título da issue
2. **Análise do Corpo**: Analise o conteúdo completo da descrição
3. **Contexto**: Considere templates usados (bug_report, feature_request, etc.)
4. **Múltiplas Tags**: Uma issue pode ter múltiplas tags de diferentes categorias
5. **Tag Mínima**: Toda issue deve ter pelo menos uma tag de tipo (bug, feature, etc.)

## Exemplos de Classificação

### Exemplo 1
**Título**: "Botão de login não funciona no Firefox"
**Tags**: `bug`, `frontend`, `medium-priority`, `easy`

### Exemplo 2  
**Título**: "Implementar sistema de notificações por email"
**Tags**: `feature`, `backend`, `integration`, `medium-priority`, `hard`

### Exemplo 3
**Título**: "Adicionar documentação da API"
**Tags**: `documentation`, `backend`, `low-priority`, `medium`

## Palavras de Exclusão

Não aplicar tags baseadas apenas nestas palavras sem contexto adicional:
- "teste", "test" (pode ser bug ou feature)
- "problema" (muito genérico)
- "questão", "dúvida" (pode ser documentation ou support)