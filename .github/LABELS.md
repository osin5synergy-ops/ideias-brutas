# Configuração de Labels - Oráculo do GitHub

Este arquivo documenta as labels oficiais do repositório. Use esta referência para criar labels consistentes via interface do GitHub.

## 🏷️ Labels por Categoria

### 📋 Tipo de noid® (Issue)

| Label | Cor | Descrição |
|-------|-----|-----------|
| `KDA-DOC` | `#0366d6` | Documentação soberana - Issue Eterna |
| `DOC` | `#0075ca` | Sub-documentação - Cromossomos |
| `bug` | `#d73a4a` | Não-conformidade ou erro |
| `feature` | `#a2eeef` | Nova funcionalidade |
| `proposta:fine-tuning` | `#d4c5f9` | Melhoria na doutrina |
| `questão` | `#d876e3` | Pergunta ou dúvida |
| `NF-Ato` | `#1d76db` | Nota Fiscal de Atos |

### 🎯 Prioridade

| Label | Cor | Descrição |
|-------|-----|-----------|
| `crítico` | `#b60205` | Requer ação imediata |
| `alto` | `#d93f0b` | Importante, próximo sprint |
| `médio` | `#fbca04` | Importante, backlog |
| `baixo` | `#0e8a16` | Pode esperar |

### 📊 Status

| Label | Cor | Descrição |
|-------|-----|-----------|
| `triagem` | `#ffffff` | Aguardando classificação |
| `aprovado` | `#0e8a16` | Aprovado pela comunidade |
| `em-andamento` | `#fbca04` | Sendo trabalhado |
| `bloqueado` | `#b60205` | Impedimento identificado |
| `review` | `#d4c5f9` | Em revisão |
| `feito` | `#0e8a16` | Concluído |

### 🧬 Cromossomo (Área)

| Label | Cor | Descrição |
|-------|-----|-----------|
| `cromossomo:agents` | `#c5def5` | Relacionado a Agents |
| `cromossomo:noids` | `#c5def5` | Relacionado a noids® |
| `cromossomo:sala-guerra` | `#c5def5` | Relacionado à Sala de Guerra |
| `cromossomo:arquivo` | `#c5def5` | Relacionado ao Arquivo Nacional |
| `cromossomo:playbooks` | `#c5def5` | Relacionado a Playbooks |
| `cromossomo:nf-atos` | `#c5def5` | Relacionado a NF-Atos® |
| `cromossomo:arquitetura` | `#c5def5` | Relacionado a SI-p-POO-OC-ote® |

### 🤖 Especiais

| Label | Cor | Descrição |
|-------|-----|-----------|
| `log-soberano` | `#006b75` | Issue que recebe NF-Atos® do Agent Cronos |
| `oráculo` | `#5319e7` | Relacionado ao Oráculo do GitHub |
| `agents` | `#1d76db` | Relacionado a agents/automação |
| `workflow` | `#0366d6` | Relacionado a GitHub Actions |
| `documentação` | `#0075ca` | Mudanças em documentação |
| `conformidade` | `#7057ff` | Relacionado a conformidade |

### 👥 Comunidade

| Label | Cor | Descrição |
|-------|-----|-----------|
| `boa-primeira-issue` | `#7057ff` | Boa para iniciantes |
| `ajuda-necessária` | `#008672` | Precisa de ajuda externa |
| `discussão` | `#cc317c` | Requer discussão da comunidade |
| `duplicado` | `#cfd3d7` | Issue duplicada |
| `inválido` | `#e4e669` | Issue inválida |
| `wontfix` | `#ffffff` | Não será implementado |

## 📝 Como Usar

### Criar Labels Manualmente

1. Vá em `Settings` → `Labels` no GitHub
2. Clique em `New label`
3. Use o nome, cor e descrição desta tabela
4. Repita para todas as labels

### Aplicar Labels em Issues/PRs

```
# Via interface GitHub
Clique em "Labels" no lado direito da issue/PR

# Via comentário (com permissões adequadas)
/label add crítico
/label add cromossomo:agents
```

### Labels Automáticas

Alguns workflows aplicam labels automaticamente:

- **Agent de Conformidade:** Adiciona `conformidade` em PRs analisados
- **Agent Cronos:** Adiciona `NF-Ato` em registros do log

## 🎨 Código de Cores

- 🔴 **Vermelho** (`#b60205`, `#d73a4a`): Urgente/Crítico
- 🟠 **Laranja** (`#d93f0b`): Alta prioridade
- 🟡 **Amarelo** (`#fbca04`): Média prioridade
- 🟢 **Verde** (`#0e8a16`): Baixa prioridade/Concluído
- 🔵 **Azul** (`#0366d6`, `#0075ca`): Documentação/Info
- 🟣 **Roxo** (`#5319e7`, `#7057ff`): Especial/Oráculo
- 🔷 **Azul claro** (`#c5def5`): Categorização
- ⚪ **Branco/Cinza** (`#ffffff`, `#cfd3d7`): Triagem/Neutro

## 🔄 Evolução das Labels

Para propor novas labels ou mudanças:

1. Crie um noid® com label `proposta:fine-tuning`
2. Descreva a necessidade da nova label
3. Sugira nome, cor e descrição
4. Aguarde discussão e aprovação da comunidade
5. Após aprovação, a label será criada e este arquivo atualizado

## 📚 Referências

- [KDA-DOC] A Documentação Soberana do GitHub
- [DOC] noids® (A Unidade de Vontade)
- [DOC] Sala de Guerra (O Painel de Comando)
- GitHub Labels Documentation

---

**Mantido por:** Oráculo do GitHub  
**Última Atualização:** [Agent Cronos]  
**Versão:** 1.0

_Use labels consistentemente para melhor governança e organização._
