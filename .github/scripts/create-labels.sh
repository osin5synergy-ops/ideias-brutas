#!/bin/bash
# Script para criar todas as labels da Taxonomia Sinergética
# Nação Soberana Synergies Web3® - Operação Gênese

echo "🏷️  Criando labels da Taxonomia Sinergética..."
echo ""

# Status do Ciclo de Vida
echo "📊 Criando labels de Status..."
gh label create "status:em-triagem" --color FFA500 --description "Issue aguardando classificação inicial" 2>/dev/null || echo "  ⚠️  Label 'status:em-triagem' já existe"
gh label create "status:classificada" --color 0E8A16 --description "Issue com tags apropriadas aplicadas" 2>/dev/null || echo "  ⚠️  Label 'status:classificada' já existe"
gh label create "status:em-sintese" --color 1D76DB --description "Agent de Síntese está processando" 2>/dev/null || echo "  ⚠️  Label 'status:em-sintese' já existe"
gh label create "status:aguardando-acao" --color FBCA04 --description "Aguardando execução/implementação" 2>/dev/null || echo "  ⚠️  Label 'status:aguardando-acao' já existe"
gh label create "status:em-progresso" --color 0052CC --description "Ação em andamento" 2>/dev/null || echo "  ⚠️  Label 'status:em-progresso' já existe"
gh label create "status:concluida" --color 6F42C1 --description "Issue finalizada" 2>/dev/null || echo "  ⚠️  Label 'status:concluida' já existe"
gh label create "status:arquivada" --color 6A737D --description "Arquivada para referência futura" 2>/dev/null || echo "  ⚠️  Label 'status:arquivada' já existe"

# Torres de Conhecimento
echo ""
echo "🗼 Criando labels de Torres..."
gh label create "torre:w1" --color E99695 --description "Web1 - Conteúdo e Informação" 2>/dev/null || echo "  ⚠️  Label 'torre:w1' já existe"
gh label create "torre:w2" --color 5319E7 --description "Web2 - Interação e Processos" 2>/dev/null || echo "  ⚠️  Label 'torre:w2' já existe"
gh label create "torre:w3" --color 0075CA --description "Web3 - Governança e Tokens" 2>/dev/null || echo "  ⚠️  Label 'torre:w3' já existe"
gh label create "torre:smart" --color BFD4F2 --description "Smart - Inteligência e Analytics" 2>/dev/null || echo "  ⚠️  Label 'torre:smart' já existe"
gh label create "torre:synergy" --color F9D0C4 --description "Synergy - Integração Multi-dimensional" 2>/dev/null || echo "  ⚠️  Label 'torre:synergy' já existe"

# Sinergia Empática
echo ""
echo "💡 Criando labels de Sinergia..."
gh label create "sinergia:logica" --color D4C5F9 --description "Lógico-Matemática" 2>/dev/null || echo "  ⚠️  Label 'sinergia:logica' já existe"
gh label create "sinergia:linguistica" --color C2E0C6 --description "Linguística" 2>/dev/null || echo "  ⚠️  Label 'sinergia:linguistica' já existe"
gh label create "sinergia:espacial" --color FFDDC1 --description "Espacial-Visual" 2>/dev/null || echo "  ⚠️  Label 'sinergia:espacial' já existe"
gh label create "sinergia:interpessoal" --color FCE4EC --description "Interpessoal" 2>/dev/null || echo "  ⚠️  Label 'sinergia:interpessoal' já existe"
gh label create "sinergia:intrapessoal" --color D1C4E9 --description "Intrapessoal" 2>/dev/null || echo "  ⚠️  Label 'sinergia:intrapessoal' já existe"
gh label create "sinergia:naturalista" --color C8E6C9 --description "Naturalista" 2>/dev/null || echo "  ⚠️  Label 'sinergia:naturalista' já existe"
gh label create "sinergia:musical" --color FFF9C4 --description "Musical-Rítmica" 2>/dev/null || echo "  ⚠️  Label 'sinergia:musical' já existe"
gh label create "sinergia:corporal" --color FFCCBC --description "Corporal-Cinestésica" 2>/dev/null || echo "  ⚠️  Label 'sinergia:corporal' já existe"

# DNA - Metodologias
echo ""
echo "🧬 Criando labels de DNA (Metodologias)..."
gh label create "dna:sipoc" --color B39DDB --description "SIPOC - Mapeamento de Processo" 2>/dev/null || echo "  ⚠️  Label 'dna:sipoc' já existe"
gh label create "dna:6m" --color 9FA8DA --description "6M (Ishikawa) - Análise de Causa Raiz" 2>/dev/null || echo "  ⚠️  Label 'dna:6m' já existe"
gh label create "dna:ote" --color 90CAF9 --description "OTE - Overall Team Effectiveness" 2>/dev/null || echo "  ⚠️  Label 'dna:ote' já existe"
gh label create "dna:oee" --color 81C784 --description "OEE - Overall Equipment Effectiveness" 2>/dev/null || echo "  ⚠️  Label 'dna:oee' já existe"
gh label create "dna:dmaic" --color AED581 --description "DMAIC - Define, Measure, Analyze, Improve, Control" 2>/dev/null || echo "  ⚠️  Label 'dna:dmaic' já existe"
gh label create "dna:pdca" --color FFD54F --description "PDCA - Plan, Do, Check, Act" 2>/dev/null || echo "  ⚠️  Label 'dna:pdca' já existe"
gh label create "dna:okr" --color FFB74D --description "OKR - Objectives and Key Results" 2>/dev/null || echo "  ⚠️  Label 'dna:okr' já existe"
gh label create "dna:kanban" --color FF8A65 --description "Kanban - Gestão Visual de Fluxo" 2>/dev/null || echo "  ⚠️  Label 'dna:kanban' já existe"
gh label create "dna:scrum" --color A1887F --description "Scrum - Framework Ágil" 2>/dev/null || echo "  ⚠️  Label 'dna:scrum' já existe"

# Prioridade
echo ""
echo "⚡ Criando labels de Prioridade..."
gh label create "prioridade:critica" --color D73A49 --description "P0 - Bloqueador ou emergência" 2>/dev/null || echo "  ⚠️  Label 'prioridade:critica' já existe"
gh label create "prioridade:alta" --color E99695 --description "P1 - Importante e urgente" 2>/dev/null || echo "  ⚠️  Label 'prioridade:alta' já existe"
gh label create "prioridade:media" --color FEF2C0 --description "P2 - Importante mas não urgente" 2>/dev/null || echo "  ⚠️  Label 'prioridade:media' já existe"
gh label create "prioridade:baixa" --color D4EDDA --description "P3 - Pode ser feito depois" 2>/dev/null || echo "  ⚠️  Label 'prioridade:baixa' já existe"
gh label create "prioridade:backlog" --color F8F9FA --description "P4 - Para consideração futura" 2>/dev/null || echo "  ⚠️  Label 'prioridade:backlog' já existe"

# Tipo de Issue
echo ""
echo "📝 Criando labels de Tipo..."
gh label create "tipo:mcp" --color 7057FF --description "MCP - Master Control Program (Ingestão de Memória)" 2>/dev/null || echo "  ⚠️  Label 'tipo:mcp' já existe"
gh label create "tipo:noid" --color BFD4F2 --description "Noid® - Ideia bruta original" 2>/dev/null || echo "  ⚠️  Label 'tipo:noid' já existe"
gh label create "tipo:dossie" --color 54A3D8 --description "Dossiê - Análise/síntese de inteligência" 2>/dev/null || echo "  ⚠️  Label 'tipo:dossie' já existe"
gh label create "tipo:acao" --color 0E8A16 --description "Ação - Task executável" 2>/dev/null || echo "  ⚠️  Label 'tipo:acao' já existe"
gh label create "tipo:epico" --color 5319E7 --description "Épico - Issue-mãe com sub-issues" 2>/dev/null || echo "  ⚠️  Label 'tipo:epico' já existe"
gh label create "tipo:bug" --color D73A49 --description "Bug - Problema a corrigir" 2>/dev/null || echo "  ⚠️  Label 'tipo:bug' já existe"
gh label create "tipo:enhancement" --color 84B6EB --description "Enhancement - Melhoria incremental" 2>/dev/null || echo "  ⚠️  Label 'tipo:enhancement' já existe"
gh label create "tipo:documentation" --color 0075CA --description "Documentação - Atualização de docs" 2>/dev/null || echo "  ⚠️  Label 'tipo:documentation' já existe"

# Contexto Especial
echo ""
echo "⭐ Criando labels de Contexto Especial..."
gh label create "especial:genese" --color FFD700 --description "Gênese - Parte da Operação Gênese" 2>/dev/null || echo "  ⚠️  Label 'especial:genese' já existe"
gh label create "especial:eterna" --color 8B00FF --description "Eterna - Issue-mãe permanente (nunca fechada)" 2>/dev/null || echo "  ⚠️  Label 'especial:eterna' já existe"
gh label create "especial:dogfooding" --color FF69B4 --description "Dogfooding - Uso interno do próprio sistema" 2>/dev/null || echo "  ⚠️  Label 'especial:dogfooding' já existe"
gh label create "especial:mvp" --color 00CED1 --description "MVP - Minimum Viable Product" 2>/dev/null || echo "  ⚠️  Label 'especial:mvp' já existe"
gh label create "especial:experimento" --color 98D8C8 --description "Experimento - Teste/prova de conceito" 2>/dev/null || echo "  ⚠️  Label 'especial:experimento' já existe"

echo ""
echo "✅ Processo concluído!"
echo ""
echo "📊 Total de labels na taxonomia: 50+"
echo "📚 Consulte .github/docs/KDA-TAGS.md para documentação completa"
echo ""
echo "🎯 Próximos passos:"
echo "  1. Verifique as labels em Settings → Labels"
echo "  2. Crie uma Issue de teste para validar o workflow"
echo "  3. Configure os Agents de Triagem e Síntese"
echo ""
echo "🌟 Operação Gênese - Nação Soberana Synergies Web3®"
