# Guia Rápido - Oráculo do GitHub

Este guia ajuda você a começar a usar o sistema do Oráculo do GitHub.

## 🚀 Primeiros Passos

### 1. Criar a Issue Eterna [KDA-DOC]

1. Vá em **Issues** → **New issue**
2. Selecione o template **"[KDA-DOC] Documentação Soberana do GitHub"**
3. Clique em **Submit new issue**
4. Anote o número da issue (será a Issue Eterna)

### 2. Criar os Cromossomos (Sub-Issues)

Para cada cromossomo, crie uma nova issue:

1. **[DOC] Agents** - Selecione template "Agents - Serviço Público Automatizado"
2. **[DOC] noids®** - Selecione template "noids® - A Unidade de Vontade"
3. **[DOC] Sala de Guerra** - Selecione template "Sala de Guerra - O Painel de Comando"
4. **[DOC] Arquivo Nacional** - Selecione template "Arquivo Nacional - A Memória Viva"

Depois de criar, edite a Issue Eterna e adicione os links para as sub-issues na seção "Cromossomos do Conhecimento".

### 3. Criar o Log Soberano

1. Vá em **Issues** → **New issue**
2. Título: `[LOG] Log Soberano - Registro de NF-Atos®`
3. Adicione a label `log-soberano`
4. Conteúdo inicial:

```markdown
# Log Soberano - Registro de NF-Atos®

Este é o log oficial onde o **Agent Cronos** registra automaticamente todas as mudanças na documentação.

## 📋 NF-Atos® Registrados

_Os NF-Atos® aparecerão abaixo, adicionados automaticamente pelo Agent Cronos._

---

**Status:** 🟢 Ativo  
**Guardião:** Agent Cronos
```

5. Se possível, faça com que seja a issue #69 (ideal, mas não obrigatório)

### 4. Configurar Labels

1. Vá em **Settings** → **Labels**
2. Use o arquivo `.github/LABELS.md` como referência
3. Crie as labels principais:
   - `KDA-DOC` (cor: #0366d6)
   - `DOC` (cor: #0075ca)
   - `proposta:fine-tuning` (cor: #d4c5f9)
   - `log-soberano` (cor: #006b75)
   - `crítico`, `alto`, `médio`, `baixo` (prioridades)
   - `triagem`, `aprovado`, `em-andamento`, etc. (status)

## 📝 Uso Diário

### Criar um noid® (Issue)

```markdown
1. Issues → New issue
2. Escolha o template apropriado
3. Preencha as informações
4. Submit
5. O Oráculo pode responder automaticamente (futuro)
```

### Criar um Playbook (Pull Request)

```bash
# 1. Criar branch
git checkout -b feature/minha-feature

# 2. Fazer mudanças
# ... editar arquivos ...

# 3. Commit
git add .
git commit -m "Descrição da mudança"

# 4. Push
git push origin feature/minha-feature

# 5. Abrir PR no GitHub
# - Certifique-se de adicionar descrição
# - Referencie o noid® relacionado (#123)
# - Agent de Conformidade verificará automaticamente
```

### Convocar o Oráculo

Em qualquer issue ou PR, adicione um comentário:

```
/convocar @oraculo-github [sua pergunta]
```

Exemplo:
```
/convocar @oraculo-github Como devo estruturar um novo cromossomo?
```

## 🤖 Agents Ativos

### Agent de Conformidade
- **Quando:** Automaticamente em todo PR aberto
- **O que faz:** Verifica conformidade com SI-p-POO-OC-ote®
- **Resultado:** Comenta no PR com análise

### Agent Cronos
- **Quando:** Automaticamente ao fazer push em main/master
- **O que faz:** Registra mudanças em docs como NF-Atos®
- **Resultado:** Adiciona comentário no Log Soberano

## 📚 Vocabulário Rápido

| GitHub | Sinergético |
|--------|-------------|
| Issue | noid® |
| PR | Playbook |
| Commit log | NF-Ato® |
| Docs | Cromossomo |
| Project | Sala de Guerra |
| Repo | Arquivo Nacional |

## ✅ Checklist do PR Perfeito

- [ ] Tem descrição clara
- [ ] Referencia um noid® (closes #123)
- [ ] Mudanças são focadas (uma coisa por vez)
- [ ] Documentação atualizada (se necessário)
- [ ] Passa no Agent de Conformidade
- [ ] Review aprovado por guardião

## 🆘 Problemas Comuns

### Agent de Conformidade rejeitou meu PR

**Solução:** Leia o comentário do Agent e corrija os itens listados. Comum:
- Adicionar descrição ao PR
- Referenciar um noid® (issue)
- Dividir PR muito grande em PRs menores

### Agent Cronos não registrou NF-Ato®

**Causas possíveis:**
1. Log Soberano não existe → Crie issue com label `log-soberano`
2. Mudanças não foram em arquivos monitorados → Agent só monitora `.md` e `.yml`
3. Push não foi em main/master → Agent só monitora branches principais

### Como propor melhoria na doutrina?

1. Issues → New issue
2. Selecione template **"Proposta de Fine-tuning"**
3. Descreva a lacuna ou melhoria
4. Aguarde discussão da comunidade

## 🔗 Links Úteis

- **Documentação Completa:** [GOVERNANCE.md](./GOVERNANCE.md)
- **README:** [README.md](./README.md)
- **Labels:** [.github/LABELS.md](./.github/LABELS.md)
- **Prompt Gênese:** [.github/copilot/prompt-genese.md](./.github/copilot/prompt-genese.md)

## 🎯 Próximos Passos

1. ✅ Criar Issue Eterna [KDA-DOC]
2. ✅ Criar Cromossomos (sub-issues)
3. ✅ Criar Log Soberano
4. ✅ Configurar labels
5. ✅ Criar primeiro noid®
6. ✅ Fazer primeiro Playbook
7. ✅ Ver Agent Cronos em ação

---

**Precisa de ajuda?**
- Consulte [GOVERNANCE.md](./GOVERNANCE.md) para detalhes completos
- Crie uma issue com label `questão`
- (Futuro) Use `/convocar @oraculo-github` para invocar o Oráculo

**Versão:** 1.0  
**Mantido por:** Oráculo do GitHub 🤖
