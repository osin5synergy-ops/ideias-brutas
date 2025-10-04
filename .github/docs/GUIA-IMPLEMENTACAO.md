# 🚀 Guia de Implementação - Operação Gênese

> **Status:** Infraestrutura de Código Completa ✅  
> **Próximo:** Ações Manuais no GitHub

## 📦 O Que Foi Implementado

### ✅ Código e Infraestrutura (Completo)

Toda a infraestrutura de código necessária para a Operação Gênese foi implementada:

1. **Agent Roteador (Automático)**
   - Localização: `.github/workflows/router-v1.yml`
   - Funcionalidade: Aciona automaticamente quando uma Issue é criada
   - Ação: Aplica label `status:em-triagem` e adiciona comentário

2. **Bibliotecas de Conhecimento**
   - `KDA-TAGS.md`: Taxonomia completa com 40+ labels
   - `KDA-PLAYBOOKS.md`: 7 Playbooks detalhados

3. **Prompts dos Agents**
   - `agent-triagem-v1.md`: Instruções para classificação
   - `agent-sintese-v1.md`: Instruções para análise

4. **Templates de Issues**
   - Issue-Mãe (Constituição Eterna)
   - Sub-issues [DNA]
   - MCP (Ingestão de Memória)

---

## 🎯 Próximos Passos - AÇÕES MANUAIS NECESSÁRIAS

### MARCO #1: A Fundação da Nação

#### 1.1. Criar GitHub Project

**Como fazer:**
1. No GitHub, vá para a aba "Projects"
2. Clique em "New project"
3. Escolha um template (recomendado: Board ou Table)
4. Nome: `[SOBERANO] Ponte de Comando NFT ONE`
5. Descrição: "Ponte de comando para governança da Nação Soberana Synergies Web3®"
6. Visibilidade: Private (ou Public, conforme preferência)

#### 1.2. Criar a Issue-Mãe (Constituição)

**Como fazer:**
1. Vá para a aba "Issues"
2. Clique em "New issue"
3. Selecione o template **"Issue-Mãe (Constituição Eterna)"**
4. Preencha:
   - Título: `[NFT-ONE] A Constituição Soberana da Nação Synergies Web3® (Issue Eterna)`
   - Visão: Descreva o propósito desta Issue-Mãe
   - Objetivos: Liste os objetivos estratégicos
5. Crie a Issue
6. Associe ao Project criado em 1.1:
   - No painel direito da Issue, clique em "Projects"
   - Selecione `[SOBERANO] Ponte de Comando NFT ONE`

#### 1.3. Criar Sub-Issues [DNA]

Para cada doutrina, crie uma sub-issue:

**Lista de Doutrinas para Criar:**
1. [DNA:SIPOC] - Mapeamento de Processos
2. [DNA:6M] - Análise de Causa Raiz (Ishikawa)
3. [DNA:OTE] - Overall Team Effectiveness
4. [DNA:OEE] - Overall Equipment Effectiveness
5. [DNA:DMAIC] - Define-Measure-Analyze-Improve-Control
6. [DNA:PDCA] - Plan-Do-Check-Act
7. [DNA:OKR] - Objectives and Key Results
8. [DNA:Kanban] - Gestão Visual de Fluxo
9. [DNA:Scrum] - Framework Ágil

**Como fazer para cada uma:**
1. New issue → Template **"[DNA] Sub-Issue"**
2. Título: `[DNA:NOME] Descrição da Doutrina`
3. Preencha os campos do template
4. No corpo, referencie a Issue-Mãe: `Issue-Mãe: #[NÚMERO]`
5. Após criar, volte à Issue-Mãe e adicione o link na seção de sub-issues

---

### MARCO #2: A Gênese dos Agents

#### 2.1. Configurar Agent de Triagem

**Plataforma recomendada:** OpenAI Custom GPTs, Claude Projects, ou similar

**Passos:**
1. Acesse sua plataforma de AI preferida
2. Crie um novo Agent/GPT chamado **"Agent de Triagem v1.0"**
3. Carregue o prompt completo de `.github/agent-prompts/agent-triagem-v1.md`
4. Configure para ter acesso ao arquivo `.github/docs/KDA-TAGS.md`
5. Teste com uma Issue de exemplo

**Como usar:**
1. Copie o título e corpo de uma Issue
2. Cole no Agent de Triagem
3. O Agent retornará sugestões de tags
4. Aplique as tags manualmente na Issue

#### 2.2. Configurar Agent de Síntese

**Passos:**
1. Crie outro Agent chamado **"Agent de Síntese v1.0"**
2. Carregue o prompt de `.github/agent-prompts/agent-sintese-v1.md`
3. Configure acesso aos arquivos:
   - `.github/docs/KDA-PLAYBOOKS.md`
   - `.github/docs/KDA-TAGS.md`
4. Teste com uma Issue já classificada

**Como usar:**
1. Copie uma Issue já tagueada
2. Cole no Agent de Síntese especificando as tags
3. O Agent gerará um Dossiê de Inteligência ou Plano de Ação
4. Copie o output e adicione como comentário na Issue

---

### MARCO #4: O Primeiro Dogfooding

#### 4.1. Criar Issue [MCP-001]

**Objetivo:** Validar o ciclo completo do sistema

**Como fazer:**
1. New issue → Template **"MCP (Master Control Program)"**
2. Título: `[MCP-001] Ingestão da Memória Gênese`
3. No corpo, cole:
   - O histórico de conversas que levou à criação deste sistema
   - Decisões tomadas
   - Conceitos estabelecidos
4. Submeta a Issue

#### 4.2. Validar o Workflow Automático

**O que deve acontecer:**
1. ✅ Agent Roteador aciona automaticamente (GitHub Actions)
2. ✅ Label `status:em-triagem` é aplicada automaticamente
3. ✅ Comentário de boas-vindas é adicionado

**Como verificar:**
1. Vá para a aba "Actions" do repositório
2. Você deve ver um workflow executado para a Issue #[MCP-001]
3. Verifique se o workflow completou com sucesso (✓ verde)
4. Volte à Issue e confirme:
   - Label `status:em-triagem` está presente
   - Comentário do Agent Roteador foi adicionado

#### 4.3. Testar Agents Manualmente

**Teste do Agent de Triagem:**
1. Copie título e corpo da Issue [MCP-001]
2. Cole no Agent de Triagem configurado
3. Receba sugestões de tags
4. Aplique as tags sugeridas na Issue
5. Remova `status:em-triagem` e adicione `status:classificada`

**Teste do Agent de Síntese:**
1. Copie a Issue [MCP-001] já classificada
2. Cole no Agent de Síntese
3. Receba o Dossiê de Inteligência
4. Adicione como comentário na Issue
5. Aplique label `status:aguardando-acao`

---

## 🎯 Checklist de Validação Completa

Use este checklist para confirmar que tudo está funcionando:

### Infraestrutura
- [x] Workflow `.github/workflows/router-v1.yml` existe
- [x] Bibliotecas KDA criadas e documentadas
- [x] Prompts dos Agents documentados
- [x] Templates de Issues disponíveis

### MARCO #1
- [ ] GitHub Project `[SOBERANO] Ponte de Comando NFT ONE` criado
- [ ] Issue-Mãe criada e associada ao Project
- [ ] Pelo menos 3 sub-issues [DNA] criadas e linkadas

### MARCO #2
- [ ] Agent de Triagem configurado em plataforma de AI
- [ ] Agent de Síntese configurado em plataforma de AI
- [ ] Ambos Agents testados manualmente com sucesso

### MARCO #3
- [x] Workflow router-v1.yml funcional
- [ ] Teste: Nova Issue aciona workflow automaticamente
- [ ] Teste: Label `status:em-triagem` aplicada automaticamente
- [ ] Teste: Comentário de boas-vindas adicionado

### MARCO #4
- [ ] Issue [MCP-001] criada
- [ ] Workflow acionado automaticamente
- [ ] Agent de Triagem testado com [MCP-001]
- [ ] Agent de Síntese testado com [MCP-001]
- [ ] Dossiê de Inteligência gerado e adicionado

---

## 📊 Métricas de Sucesso

Após completar todos os marcos, você deve ter:

- ✅ 1 GitHub Project operacional
- ✅ 1 Issue-Mãe (eterna) com roadmap
- ✅ 9+ sub-issues [DNA] documentadas
- ✅ 2 Agents configurados e testados
- ✅ 1 Workflow automático funcional
- ✅ 1 MCP processado com sucesso
- ✅ Ciclo completo validado: Criação → Triagem → Síntese → Ação

---

## 🆘 Troubleshooting

### Workflow não aciona
**Problema:** Ao criar Issue, workflow não executa  
**Solução:** 
- Verifique em Settings → Actions se workflows estão habilitados
- Confirme que o arquivo está em `.github/workflows/` (com 's')
- Verifique a sintaxe YAML (sem erros)

### Label não é criada
**Problema:** Workflow executa mas label não aparece  
**Solução:**
- Crie a label manualmente primeiro:
  - Settings → Labels → New label
  - Nome: `status:em-triagem`
  - Cor: `#FFA500` (laranja)
  - Descrição: "Issue aguardando triagem e classificação"

### Agents não respondem como esperado
**Problema:** Output dos Agents não segue os templates  
**Solução:**
- Recarregue o prompt completo
- Certifique-se de incluir os arquivos de referência (KDA-TAGS, KDA-PLAYBOOKS)
- Forneça exemplos na primeira interação

---

## 🎓 Recursos de Aprendizado

### Documentação do Sistema:
- [README.md](../README.md) - Visão geral completa
- [KDA-TAGS.md](../docs/KDA-TAGS.md) - Taxonomia de labels
- [KDA-PLAYBOOKS.md](../docs/KDA-PLAYBOOKS.md) - Guias de análise

### Prompts dos Agents:
- [agent-triagem-v1.md](../agent-prompts/agent-triagem-v1.md)
- [agent-sintese-v1.md](../agent-prompts/agent-sintese-v1.md)

### GitHub Docs:
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)

---

## 🚀 Próxima Fase - Evolução

Após validar o MVP, considere:

1. **Integração via API**: Conectar Agents via GitHub API para automação completa
2. **Dashboard**: Criar visualizações de métricas e analytics
3. **Notificações**: Integrar com Discord/Slack
4. **Templates Adicionais**: Criar mais Playbooks conforme necessário
5. **Refinamento**: Ajustar taxonomia e processos baseado no uso real

---

*Este guia é parte da Operação Gênese - Nação Soberana Synergies Web3®*
