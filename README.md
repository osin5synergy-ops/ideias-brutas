# 🌐 ideias-brutas

> **Nação Soberana Synergies Web3® - Operação Gênese**  
> issues->(supply 10% Humano - A FAISCA).

## 📋 Visão Geral

Este repositório é o **cérebro operacional** da Nação Soberana Synergies Web3®. Aqui, ideias brutas (noids®) são capturadas, classificadas, sintetizadas e transformadas em ações concretas através de um sistema automatizado de governança e inteligência.

## 🏛️ Arquitetura do Sistema

### 🤖 Agents (Agentes Inteligentes)

Temos três Agents principais que compõem nosso **Sinergie Mainframe®**:

1. **Agent Roteador** (`.github/workflows/router-v1.yml`)
   - Aciona automaticamente quando uma nova Issue é criada
   - Aplica a label `status:em-triagem`
   - Adiciona comentário de boas-vindas explicando o processo

2. **Agent de Triagem v1.0** (`.github/agent-prompts/agent-triagem-v1.md`)
   - Especialista em classificação
   - Analisa Issues e sugere labels apropriadas
   - Consulta a biblioteca `[KDA-TAGS]`

3. **Agent de Síntese v1.0** (`.github/agent-prompts/agent-sintese-v1.md`)
   - Mestre estrategista
   - Recebe Issues tagueadas e gera Dossiês de Inteligência
   - Consulta a biblioteca `[KDA-PLAYBOOKS]`

### 📚 Bibliotecas de Conhecimento (KDA)

- **[KDA-TAGS]** (`.github/docs/KDA-TAGS.md`)
  - Taxonomia Sinergética de Tagueamento
  - Define todas as labels oficiais do sistema
  - Organiza tags por categorias (Status, Torres, Tipo, etc.)

- **[KDA-PLAYBOOKS]** (`.github/docs/KDA-PLAYBOOKS.md`)
  - Biblioteca de Playbooks Soberanos
  - Templates para diferentes tipos de análise (MCP, Noid®, Ação, etc.)
  - Guias de aplicação de metodologias (SIPOC, 6M, OKR, etc.)

### 📝 Templates de Issues

Localizados em `.github/ISSUE_TEMPLATE/`:

- **Issue-Mãe (Constituição Eterna)** - Para criar Issues-Mãe que nunca fecham
- **[DNA] Sub-Issue** - Para documentar doutrinas e metodologias
- **MCP (Ingestão de Memória)** - Para capturar histórico e conhecimento
- **Bug Report, Feature Request, Custom** - Templates padrão do GitHub

## 🚀 Como Usar

### Para Criar uma Nova Ideia (Noid®):

1. Abra uma nova Issue (use o template apropriado se aplicável)
2. O **Agent Roteador** irá automaticamente:
   - Aplicar a label `status:em-triagem`
   - Adicionar um comentário explicativo
3. Um humano ou o **Agent de Triagem** irá classificar a Issue
4. O **Agent de Síntese** irá gerar uma análise detalhada

### Para Ingerir Memória/Conhecimento (MCP):

1. Use o template **MCP (Ingestão de Memória)**
2. Cole o histórico completo no corpo da Issue
3. Aguarde processamento pelos Agents
4. Issues derivadas serão sugeridas no Dossiê de Inteligência

### Para Criar uma Issue-Mãe (Épico):

1. Use o template **Issue-Mãe (Constituição Eterna)**
2. Defina a visão e objetivos estratégicos
3. Crie sub-issues usando o template **[DNA] Sub-Issue**
4. Linke todas as sub-issues na Issue-Mãe

## 📊 Framework de Classificação

### Torres de Conhecimento Web3:
- 🌐 **W1 (Web1)**: Conteúdo e Informação
- 🔄 **W2 (Web2)**: Interação e Processos
- 🔗 **W3 (Web3)**: Governança e Tokens
- 🧠 **Smart**: Inteligência e Analytics
- ⚡ **Synergy**: Integração Multi-dimensional

### Metodologias DNA:
- **SIPOC**: Mapeamento de processos
- **6M**: Análise de causa raiz (Ishikawa)
- **OTE/OEE**: Eficácia de time/equipamento
- **DMAIC**: Ciclo de melhoria contínua
- **PDCA**: Plan-Do-Check-Act
- **OKR**: Objetivos e Resultados-Chave
- **Kanban/Scrum**: Frameworks ágeis

## 🎯 Marcos da Operação Gênese

- [x] **MARCO #3: A Primeira Automação**
  - [x] Agent Roteador implementado
  - [x] Workflow de triagem automática funcional

- [x] **Documentação de Suporte (Marcos #1 e #2)**
  - [x] Biblioteca KDA-TAGS criada
  - [x] Biblioteca KDA-PLAYBOOKS criada
  - [x] Prompts dos Agents documentados
  - [x] Templates de Issues criados

- [ ] **MARCO #1: A Fundação da Nação** (Requer ação manual)
  - [ ] Criar GitHub Project: `[SOBERANO] Ponte de Comando NFT ONE`
  - [ ] Criar Issue-Mãe usando template
  - [ ] Criar sub-issues [DNA] para cada doutrina

- [ ] **MARCO #2: A Gênese dos Agents** (Requer ação manual)
  - [ ] Configurar Agents no AI Studio ou similar
  - [ ] Carregar prompts dos arquivos `.github/agent-prompts/`
  - [ ] Testar classificação e síntese manual

- [ ] **MARCO #4: O Primeiro Dogfooding** (Requer ação manual)
  - [ ] Criar Issue [MCP-001] com histórico de conversas
  - [ ] Validar workflow completo
  - [ ] Iterar e melhorar

## 🛠️ Estrutura do Repositório

```
ideias-brutas/
├── .github/
│   ├── workflows/
│   │   └── router-v1.yml              # Agent Roteador (automação)
│   ├── docs/
│   │   ├── KDA-TAGS.md                # Taxonomia de labels
│   │   └── KDA-PLAYBOOKS.md           # Biblioteca de Playbooks
│   ├── agent-prompts/
│   │   ├── agent-triagem-v1.md        # Prompt do Agent de Triagem
│   │   └── agent-sintese-v1.md        # Prompt do Agent de Síntese
│   └── ISSUE_TEMPLATE/
│       ├── issue-mae-constituicao.md  # Template Issue-Mãe
│       ├── dna-sub-issue.md           # Template sub-issues DNA
│       ├── mcp-ingestao.md            # Template MCP
│       ├── bug_report.md              # Template padrão
│       ├── feature_request.md         # Template padrão
│       └── custom.md                  # Template padrão
└── README.md                          # Este arquivo
```

## 🤝 Contribuindo

1. **Ideias brutas**: Abra uma Issue, o sistema cuidará do resto
2. **Melhorias na taxonomia**: Edite `.github/docs/KDA-TAGS.md` e abra um PR
3. **Novos Playbooks**: Edite `.github/docs/KDA-PLAYBOOKS.md` e abra um PR
4. **Melhorias nos Agents**: Edite os prompts em `.github/agent-prompts/`

## 📖 Documentação Adicional

- [KDA-TAGS - Taxonomia Completa](.github/docs/KDA-TAGS.md)
- [KDA-PLAYBOOKS - Guias de Análise](.github/docs/KDA-PLAYBOOKS.md)
- [Agent de Triagem - Prompt](.github/agent-prompts/agent-triagem-v1.md)
- [Agent de Síntese - Prompt](.github/agent-prompts/agent-sintese-v1.md)

## 🔄 Status do Sistema

**Versão Atual:** 1.0 (MVP)  
**Status:** Operacional  
**Última Atualização:** 2024

### Funcionalidades Ativas:
- ✅ Agent Roteador (automático via GitHub Actions)
- ✅ Taxonomia completa de labels
- ✅ Biblioteca de Playbooks estruturada
- ✅ Templates de Issues para todos os casos de uso

### Próximas Iterações:
- 🔄 Integração de Agents com APIs de AI
- 🔄 Automação completa de triagem e síntese
- 🔄 Dashboard de métricas e analytics
- 🔄 Integração com Discord para notificações

---

## 🌟 Filosofia

> "Transformamos ideias brutas em ações soberanas através de sinergia empática e inteligência distribuída."

Esta é a Operação Gênese. Bem-vindo à Nação Soberana Synergies Web3®.

---

*Powered by 10% Humano (A FAÍSCA) + 90% Sinergie Mainframe®*
