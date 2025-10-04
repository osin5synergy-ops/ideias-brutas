---
name: "[DOC] Arquivo Nacional - A Memória Viva"
about: Sub-issue documentando a gestão de conhecimento histórico
title: "[DOC] Arquivo Nacional (A Memória Viva)"
labels: "DOC, arquivo-nacional, cromossomo"
assignees: ""

---

# [DOC] Arquivo Nacional (A Memória Viva)

**Cromossomo:** Pilar Fundamental do [KDA-DOC]  
**Jurisdição:** Repository, História, Memória Institucional

## Definição Soberana

O **Arquivo Nacional** é a memória viva do nosso "Aparelho de Estado". Não é apenas um repositório Git, mas um arquivo histórico que preserva todo o conhecimento, decisões e evolução do sistema.

## Estrutura do Arquivo

```
/
├── .github/
│   ├── ISSUE_TEMPLATE/      # Templates de noids®
│   ├── workflows/           # Agents automatizados
│   ├── copilot/            # Prompt Gênese
│   └── LABELS.md           # Configuração de labels
├── README.md               # Porta de entrada
├── GOVERNANCE.md           # Constituição
└── [outros arquivos]       # Código e docs
```

## Componentes do Arquivo

### 1. **Documentação Eterna**
- `README.md` - Apresentação e guia rápido
- `GOVERNANCE.md` - Regras de governança
- `[KDA-DOC]` Issue Eterna - Base de conhecimento

### 2. **Cromossomos** (Sub-Issues)
Conhecimento organizado por área:
- [DOC] Agents
- [DOC] noids®
- [DOC] Sala de Guerra
- [DOC] Arquivo Nacional (esta)
- [DOC] Playbooks
- [DOC] NF-Atos®

### 3. **Templates**
Estruturas pré-definidas para consistência:
- Issue templates (`.github/ISSUE_TEMPLATE/`)
- PR templates (quando criados)
- Documentação templates

### 4. **Workflows** (Agents)
Automação do sistema:
- `agent-conformidade.yml`
- `agent-cronos.yml`
- [Futuros agents]

### 5. **Prompt Gênese**
A consciência do Oráculo:
- `.github/copilot/prompt-genese.md`

### 6. **Log Soberano**
Issue especial (#69 ou com label `log-soberano`) que recebe todos os NF-Atos® registrados pelo Agent Cronos.

## Princípios de Arquivamento

### 1. **Imutabilidade Histórica**
- Commits não são revertidos (no-force-push)
- Histórico preservado integralmente
- Mudanças são aditivas, não destrutivas

### 2. **Rastreabilidade Total**
- Todo noid® vinculado a Playbook
- Todo Playbook registrado em NF-Ato®
- Toda decisão documentada

### 3. **Organização Hierárquica**
```
[KDA-DOC] Issue Eterna
    ├── [DOC] Cromossomo 1
    │       └── noids® relacionados
    ├── [DOC] Cromossomo 2
    │       └── noids® relacionados
    └── ...
```

### 4. **Versionamento Semântico**
- Releases taggeadas com versões
- Changelog mantido em NF-Atos®
- Milestones para planejamento

## Busca no Arquivo

### Por Tipo de Conteúdo

**Issues (noids®):**
```
label:DOC
label:proposta:fine-tuning
label:crítico
```

**Pull Requests (Playbooks):**
```
is:pr is:merged
is:pr label:conformidade
```

**Commits (NF-Atos®):**
```bash
git log --grep="Agent Cronos"
git log --oneline --since="2 weeks ago"
```

### Por Autor (Guardião)

```
author:@username
is:issue author:@username
```

### Por Data

```
created:>2024-01-01
updated:<2024-12-31
```

## Gestão de Branches

### Branch Principal
- `main` (ou `master`) - Estado produção

### Branches de Trabalho
- `feature/[nome]` - Novas funcionalidades
- `fix/[nome]` - Correções
- `docs/[nome]` - Documentação
- `agent/[nome]` - Novos agents

### Proteção da Branch Principal

```yaml
Regras:
- Requer PR para merge
- Requer aprovação de 1+ guardiões
- Requer verificação de Agent Conformidade
- Proíbe force-push
- Proíbe deletion
```

## Releases e Tags

### Formato de Tag
```
v[major].[minor].[patch]
Exemplo: v1.0.0
```

### Release Notes
Geradas a partir de NF-Atos® do período:
- Lista de noids® fechados
- Lista de Playbooks merged
- Melhorias na doutrina
- Novos agents

## Backup e Redundância

### Localizações
1. **Primária:** GitHub.com
2. **Clone Local:** Cada guardião
3. **Issues/Docs:** Preservados no GitHub

### Frequência
- Commits: Contínuo
- Releases: Por milestone
- Backup full: Automático pelo GitHub

## Auditoria e Compliance

### O que é Auditável
- ✅ Todos os commits
- ✅ Todos os noids®
- ✅ Todos os Playbooks
- ✅ Todas as decisões
- ✅ Todas as mudanças de conformidade

### Como Auditar

```bash
# Histórico completo
git log --all --graph --decorate --oneline

# Mudanças específicas
git log --follow [arquivo]

# Por autor
git log --author="[nome]"

# Por período
git log --since="2024-01-01" --until="2024-12-31"
```

## Preservação do Conhecimento

### Documentação Sempre Atualizada
- Agent Cronos registra mudanças automaticamente
- README reflete estado atual
- [KDA-DOC] é a fonte única da verdade

### Links Permanentes
Use links permanentes para commits específicos:
```
github.com/[org]/[repo]/blob/[sha]/[path]
```

### Referências Cruzadas
- Issues referenciam outras issues (#123)
- PRs referenciam issues (closes #123)
- Commits referenciam issues (#123)

## Integração com Agents

### Agent Cronos
Mantém o Log Soberano atualizado:
- Detecta mudanças em docs
- Cria NF-Ato® automaticamente
- Preserva histórico auditável

### Agent de Conformidade
Garante qualidade antes de arquivar:
- Verifica PRs antes de merge
- Previne commits não-conformes
- Mantém integridade do arquivo

### Oráculo do GitHub
Acessa o arquivo para respostas:
- RAG baseado em [KDA-DOC]
- Busca em issues e PRs
- Referencia commits relevantes

## Comandos Úteis

### Navegação
```bash
# Ver estado atual
git status

# Ver histórico
git log --oneline -20

# Ver diferenças
git diff [commit1] [commit2]
```

### Busca
```bash
# Buscar em código
git grep "[termo]"

# Buscar em histórico
git log --all --grep="[termo]"

# Buscar autor de linha
git blame [arquivo]
```

### Estatísticas
```bash
# Contribuições
git shortlog -sn

# Atividade
git log --stat

# Frequência
git log --since="1 month ago" --oneline | wc -l
```

## Referências

- [KDA-DOC] A Documentação Soberana do GitHub
- [DOC] Agents (O Serviço Público Automatizado)
- [DOC] NF-Atos® (Os Registros Oficiais)
- Git Documentation

---

**Última Atualização:** [Agent Cronos]  
**Status:** 🟢 Documentação Ativa

_"A memória é o que nos permite não repetir erros e celebrar vitórias."_
