# [KDA-TAGS] A Taxonomia Sinergética de Tagueamento

> **Biblioteca de Conhecimento**: Sistema oficial de classificação para Issues (noids®) da Nação Soberana Synergies Web3®

## 📋 Visão Geral

Este documento define a taxonomia oficial de `labels` utilizadas no processo de triagem e classificação de Issues. Cada Issue (noid®) deve ser tagueada de acordo com múltiplas dimensões para facilitar a navegação, priorização e síntese.

---

## 🏷️ Categorias de Labels

### 1. **Status do Ciclo de Vida**
Indica em que fase do processo a Issue se encontra.

| Label | Descrição | Cor Sugerida |
|-------|-----------|--------------|
| `status:em-triagem` | Issue recém-criada, aguardando classificação inicial | `#FFA500` (laranja) |
| `status:classificada` | Issue já possui tags apropriadas | `#0E8A16` (verde) |
| `status:em-sintese` | Agent de Síntese está processando | `#1D76DB` (azul) |
| `status:aguardando-acao` | Aguardando execução/implementação | `#FBCA04` (amarelo) |
| `status:em-progresso` | Ação em andamento | `#0052CC` (azul escuro) |
| `status:concluida` | Issue finalizada | `#6F42C1` (roxo) |
| `status:arquivada` | Arquivada para referência futura | `#6A737D` (cinza) |

### 2. **Torres de Conhecimento** (Framework Web3)
Classificação segundo as 5 Torres do modelo Synergies Web3®.

| Label | Torre | Descrição |
|-------|-------|-----------|
| `torre:w1` | Web1 (Conteúdo) | Relacionado a informação, dados, documentação |
| `torre:w2` | Web2 (Interação) | Relacionado a processos, workflows, automações |
| `torre:w3` | Web3 (Governança) | Relacionado a tokens, contratos, descentralização |
| `torre:smart` | Smart (Inteligência) | Relacionado a AI, ML, analytics |
| `torre:synergy` | Synergy (Integração) | Issues multi-dimensionais que cruzam torres |

### 3. **Sinergia Empática** (Tipos de Inteligência)
Classifica a natureza da contribuição segundo as múltiplas inteligências.

| Label | Tipo de Inteligência | Descrição |
|-------|---------------------|-----------|
| `sinergia:logica` | Lógico-Matemática | Análise estrutural, algoritmos, métricas |
| `sinergia:linguistica` | Linguística | Documentação, comunicação, narrativas |
| `sinergia:espacial` | Espacial-Visual | Design, UX/UI, arquitetura de sistema |
| `sinergia:interpessoal` | Interpessoal | Colaboração, comunidade, governança |
| `sinergia:intrapessoal` | Intrapessoal | Reflexão, valores, propósito |
| `sinergia:naturalista` | Naturalista | Sustentabilidade, ecossistema, organicidade |
| `sinergia:musical` | Musical-Rítmica | Padrões, ciclos, harmonia de sistemas |
| `sinergia:corporal` | Corporal-Cinestésica | Prototipagem, execução, ação concreta |

### 4. **Metodologias e Doutrinas** (DNA da Nação)
Tags relacionadas aos frameworks e metodologias aplicáveis.

| Label | Metodologia | Descrição |
|-------|-------------|-----------|
| `dna:sipoc` | SIPOC | Mapeamento de processo (Supplier, Input, Process, Output, Customer) |
| `dna:6m` | 6M (Ishikawa) | Análise de causa raiz (Método, Material, Mão-de-obra, Máquina, Meio, Medida) |
| `dna:ote` | OTE | Overall Team Effectiveness - eficácia de equipe |
| `dna:oee` | OEE | Overall Equipment Effectiveness - eficácia de equipamento |
| `dna:dmaic` | DMAIC | Define, Measure, Analyze, Improve, Control |
| `dna:pdca` | PDCA | Plan, Do, Check, Act |
| `dna:okr` | OKR | Objectives and Key Results |
| `dna:kanban` | Kanban | Gestão visual de fluxo |
| `dna:scrum` | Scrum | Framework ágil |

### 5. **Prioridade e Urgência**
Classifica a importância e timing da Issue.

| Label | Nível | Descrição |
|-------|-------|-----------|
| `prioridade:critica` | P0 | Bloqueador ou emergência |
| `prioridade:alta` | P1 | Importante e urgente |
| `prioridade:media` | P2 | Importante mas não urgente |
| `prioridade:baixa` | P3 | Pode ser feito depois |
| `prioridade:backlog` | P4 | Para consideração futura |

### 6. **Tipo de Issue**
Natureza fundamental da Issue.

| Label | Tipo | Descrição |
|-------|------|-----------|
| `tipo:mcp` | MCP (Master Control Program) | Issue de ingestão de memória/conhecimento |
| `tipo:noid` | Noid® | Ideia bruta original |
| `tipo:dossie` | Dossiê | Análise/síntese de inteligência |
| `tipo:acao` | Ação | Task executável |
| `tipo:epico` | Épico | Issue-mãe que contém sub-issues |
| `tipo:bug` | Bug | Problema a corrigir |
| `tipo:enhancement` | Enhancement | Melhoria incremental |
| `tipo:documentation` | Documentação | Atualização de docs |

### 7. **Contexto Especial**
Marcadores para Issues com características especiais.

| Label | Contexto | Descrição |
|-------|----------|-----------|
| `especial:genese` | Gênese | Parte da Operação Gênese |
| `especial:eterna` | Eterna | Issue-mãe permanente (nunca fechada) |
| `especial:dogfooding` | Dogfooding | Uso interno do próprio sistema |
| `especial:mvp` | MVP | Minimum Viable Product |
| `especial:experimento` | Experimento | Teste/prova de conceito |

---

## 🎯 Diretrizes de Uso

### Para o Agent de Triagem:
1. Toda nova Issue deve receber ao menos uma tag de cada categoria principal (Status, Torre, Tipo)
2. Múltiplas tags podem ser aplicadas quando apropriado
3. Use o contexto completo da Issue para fazer sugestões precisas
4. Em caso de dúvida, marque como `status:em-triagem` e solicite revisão humana

### Para Humanos:
1. Revise as sugestões do Agent de Triagem
2. Adicione tags adicionais que o Agent possa ter perdido
3. Use as tags para filtrar e organizar o trabalho
4. Mantenha a taxonomia atualizada conforme o sistema evolui

---

## 📊 Exemplos de Tagueamento

### Exemplo 1: Ideia de Nova Funcionalidade
```
Labels: 
- status:em-triagem
- torre:w2
- sinergia:logica
- tipo:noid
- prioridade:media
```

### Exemplo 2: Ingestão de Memória (MCP)
```
Labels:
- status:em-triagem
- torre:smart
- tipo:mcp
- sinergia:linguistica
- prioridade:alta
- especial:genese
```

### Exemplo 3: Issue-Mãe (Constituição)
```
Labels:
- torre:synergy
- tipo:epico
- especial:eterna
- especial:genese
- prioridade:critica
```

---

## 🔄 Versionamento

- **Versão:** 1.0
- **Data:** 2024
- **Status:** Ativo
- **Próxima Revisão:** Após 100 Issues processadas

---

*Este documento é parte da Operação Gênese - Nação Soberana Synergies Web3®*
