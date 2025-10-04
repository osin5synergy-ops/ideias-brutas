# Configuração de Labels - Nação Soberana Synergies Web3®

# Este arquivo pode ser usado para criar labels via script ou manualmente
# Formato: Nome | Cor (hex) | Descrição

## Status do Ciclo de Vida
status:em-triagem | FFA500 | Issue aguardando classificação inicial
status:classificada | 0E8A16 | Issue com tags apropriadas aplicadas
status:em-sintese | 1D76DB | Agent de Síntese está processando
status:aguardando-acao | FBCA04 | Aguardando execução/implementação
status:em-progresso | 0052CC | Ação em andamento
status:concluida | 6F42C1 | Issue finalizada
status:arquivada | 6A737D | Arquivada para referência futura

## Torres de Conhecimento
torre:w1 | E99695 | Web1 - Conteúdo e Informação
torre:w2 | 5319E7 | Web2 - Interação e Processos
torre:w3 | 0075CA | Web3 - Governança e Tokens
torre:smart | BFD4F2 | Smart - Inteligência e Analytics
torre:synergy | F9D0C4 | Synergy - Integração Multi-dimensional

## Sinergia Empática (Tipos de Inteligência)
sinergia:logica | D4C5F9 | Lógico-Matemática
sinergia:linguistica | C2E0C6 | Linguística
sinergia:espacial | FFDDC1 | Espacial-Visual
sinergia:interpessoal | FCE4EC | Interpessoal
sinergia:intrapessoal | D1C4E9 | Intrapessoal
sinergia:naturalista | C8E6C9 | Naturalista
sinergia:musical | FFF9C4 | Musical-Rítmica
sinergia:corporal | FFCCBC | Corporal-Cinestésica

## Metodologias e Doutrinas (DNA)
dna:sipoc | B39DDB | SIPOC - Mapeamento de Processo
dna:6m | 9FA8DA | 6M (Ishikawa) - Análise de Causa Raiz
dna:ote | 90CAF9 | OTE - Overall Team Effectiveness
dna:oee | 81C784 | OEE - Overall Equipment Effectiveness
dna:dmaic | AED581 | DMAIC - Define, Measure, Analyze, Improve, Control
dna:pdca | FFD54F | PDCA - Plan, Do, Check, Act
dna:okr | FFB74D | OKR - Objectives and Key Results
dna:kanban | FF8A65 | Kanban - Gestão Visual de Fluxo
dna:scrum | A1887F | Scrum - Framework Ágil

## Prioridade e Urgência
prioridade:critica | D73A49 | P0 - Bloqueador ou emergência
prioridade:alta | E99695 | P1 - Importante e urgente
prioridade:media | FEF2C0 | P2 - Importante mas não urgente
prioridade:baixa | D4EDDA | P3 - Pode ser feito depois
prioridade:backlog | F8F9FA | P4 - Para consideração futura

## Tipo de Issue
tipo:mcp | 7057FF | MCP - Master Control Program (Ingestão de Memória)
tipo:noid | BFD4F2 | Noid® - Ideia bruta original
tipo:dossie | 54A3D8 | Dossiê - Análise/síntese de inteligência
tipo:acao | 0E8A16 | Ação - Task executável
tipo:epico | 5319E7 | Épico - Issue-mãe com sub-issues
tipo:bug | D73A49 | Bug - Problema a corrigir
tipo:enhancement | 84B6EB | Enhancement - Melhoria incremental
tipo:documentation | 0075CA | Documentação - Atualização de docs

## Contexto Especial
especial:genese | FFD700 | Gênese - Parte da Operação Gênese
especial:eterna | 8B00FF | Eterna - Issue-mãe permanente (nunca fechada)
especial:dogfooding | FF69B4 | Dogfooding - Uso interno do próprio sistema
especial:mvp | 00CED1 | MVP - Minimum Viable Product
especial:experimento | 98D8C8 | Experimento - Teste/prova de conceito

---

## Script de Criação Rápida (GitHub CLI)

Para criar todas as labels de uma vez usando GitHub CLI (gh):

```bash
# Status
gh label create "status:em-triagem" --color FFA500 --description "Issue aguardando classificação inicial"
gh label create "status:classificada" --color 0E8A16 --description "Issue com tags apropriadas aplicadas"
gh label create "status:em-sintese" --color 1D76DB --description "Agent de Síntese está processando"
gh label create "status:aguardando-acao" --color FBCA04 --description "Aguardando execução/implementação"
gh label create "status:em-progresso" --color 0052CC --description "Ação em andamento"
gh label create "status:concluida" --color 6F42C1 --description "Issue finalizada"
gh label create "status:arquivada" --color 6A737D --description "Arquivada para referência futura"

# Torres
gh label create "torre:w1" --color E99695 --description "Web1 - Conteúdo e Informação"
gh label create "torre:w2" --color 5319E7 --description "Web2 - Interação e Processos"
gh label create "torre:w3" --color 0075CA --description "Web3 - Governança e Tokens"
gh label create "torre:smart" --color BFD4F2 --description "Smart - Inteligência e Analytics"
gh label create "torre:synergy" --color F9D0C4 --description "Synergy - Integração Multi-dimensional"

# Sinergia
gh label create "sinergia:logica" --color D4C5F9 --description "Lógico-Matemática"
gh label create "sinergia:linguistica" --color C2E0C6 --description "Linguística"
gh label create "sinergia:espacial" --color FFDDC1 --description "Espacial-Visual"
gh label create "sinergia:interpessoal" --color FCE4EC --description "Interpessoal"
gh label create "sinergia:intrapessoal" --color D1C4E9 --description "Intrapessoal"
gh label create "sinergia:naturalista" --color C8E6C9 --description "Naturalista"
gh label create "sinergia:musical" --color FFF9C4 --description "Musical-Rítmica"
gh label create "sinergia:corporal" --color FFCCBC --description "Corporal-Cinestésica"

# DNA
gh label create "dna:sipoc" --color B39DDB --description "SIPOC - Mapeamento de Processo"
gh label create "dna:6m" --color 9FA8DA --description "6M (Ishikawa) - Análise de Causa Raiz"
gh label create "dna:ote" --color 90CAF9 --description "OTE - Overall Team Effectiveness"
gh label create "dna:oee" --color 81C784 --description "OEE - Overall Equipment Effectiveness"
gh label create "dna:dmaic" --color AED581 --description "DMAIC - Define, Measure, Analyze, Improve, Control"
gh label create "dna:pdca" --color FFD54F --description "PDCA - Plan, Do, Check, Act"
gh label create "dna:okr" --color FFB74D --description "OKR - Objectives and Key Results"
gh label create "dna:kanban" --color FF8A65 --description "Kanban - Gestão Visual de Fluxo"
gh label create "dna:scrum" --color A1887F --description "Scrum - Framework Ágil"

# Prioridade
gh label create "prioridade:critica" --color D73A49 --description "P0 - Bloqueador ou emergência"
gh label create "prioridade:alta" --color E99695 --description "P1 - Importante e urgente"
gh label create "prioridade:media" --color FEF2C0 --description "P2 - Importante mas não urgente"
gh label create "prioridade:baixa" --color D4EDDA --description "P3 - Pode ser feito depois"
gh label create "prioridade:backlog" --color F8F9FA --description "P4 - Para consideração futura"

# Tipo
gh label create "tipo:mcp" --color 7057FF --description "MCP - Master Control Program (Ingestão de Memória)"
gh label create "tipo:noid" --color BFD4F2 --description "Noid® - Ideia bruta original"
gh label create "tipo:dossie" --color 54A3D8 --description "Dossiê - Análise/síntese de inteligência"
gh label create "tipo:acao" --color 0E8A16 --description "Ação - Task executável"
gh label create "tipo:epico" --color 5319E7 --description "Épico - Issue-mãe com sub-issues"
gh label create "tipo:bug" --color D73A49 --description "Bug - Problema a corrigir"
gh label create "tipo:enhancement" --color 84B6EB --description "Enhancement - Melhoria incremental"
gh label create "tipo:documentation" --color 0075CA --description "Documentação - Atualização de docs"

# Especial
gh label create "especial:genese" --color FFD700 --description "Gênese - Parte da Operação Gênese"
gh label create "especial:eterna" --color 8B00FF --description "Eterna - Issue-mãe permanente (nunca fechada)"
gh label create "especial:dogfooding" --color FF69B4 --description "Dogfooding - Uso interno do próprio sistema"
gh label create "especial:mvp" --color 00CED1 --description "MVP - Minimum Viable Product"
gh label create "especial:experimento" --color 98D8C8 --description "Experimento - Teste/prova de conceito"
```

## Uso do Script

Execute no diretório do repositório:

```bash
cd /path/to/ideias-brutas
gh label create ... (cada comando acima)
```

Ou crie um arquivo `create-labels.sh` com o conteúdo acima e execute:

```bash
chmod +x create-labels.sh
./create-labels.sh
```

---

*Configuração de labels da Operação Gênese - Nação Soberana Synergies Web3®*
