# Configuração do Campo SIPOC no GitHub Projects Beta

Este guia fornece instruções passo a passo para configurar um campo personalizado "Etapa SIPOC" no seu projeto do GitHub Projects Beta.

## O que é SIPOC?

SIPOC é uma metodologia de mapeamento de processos que identifica:
- **S**upply (Fornecimento)
- **I**nput (Entrada)
- **P**rocess (Processo)
- **O**utput (Saída)
- **C**ustomer (Cliente)

## Pré-requisitos

- Acesso ao GitHub Projects Beta
- Permissões de administrador no projeto

## Passos para Configuração

### 1. Acesse seu projeto no GitHub Projects Beta

1. Navegue até o seu repositório no GitHub
2. Clique na aba **"Projects"**
3. Entre em seu projeto existente ou crie um novo projeto

### 2. Adicione o Campo Personalizado (Custom Field)

1. No topo direito do seu board, clique em **"Fields"** ou **"Campos"**
2. Clique em **"+ New field"** (ou **"Adicionar campo"**)

### 3. Configure o Campo

Preencha as seguintes informações:

- **Nome:** `Etapa SIPOC`
- **Tipo:** `Dropdown` (menu suspenso)
- **Opções:**
  - `Supply` (Fornecimento)
  - `Input` (Entrada)
  - `Process` (Processo)
  - `Output` (Saída)
  - `Customer` (Cliente)

### 4. Configuração Detalhada das Opções

Para cada opção do dropdown, adicione:

1. **Supply**
   - Descrição: Recursos e fornecedores necessários
   - Cor sugerida: Azul

2. **Input**
   - Descrição: Entradas e insumos do processo
   - Cor sugerida: Verde

3. **Process**
   - Descrição: Etapas e atividades do processo
   - Cor sugerida: Laranja

4. **Output**
   - Descrição: Resultados e produtos gerados
   - Cor sugerida: Roxo

5. **Customer**
   - Descrição: Clientes e beneficiários finais
   - Cor sugerida: Vermelho

### 5. Salvar e Aplicar

1. Clique em **"Save field"** ou **"Salvar campo"**
2. O campo estará disponível para todos os itens do projeto

## Como Usar o Campo SIPOC

Após a configuração, você pode:

1. **Categorizar Issues:** Atribuir uma etapa SIPOC a cada issue
2. **Filtrar por Etapa:** Usar filtros para visualizar apenas itens de uma etapa específica
3. **Criar Views:** Organizar o board por etapas SIPOC
4. **Gerar Relatórios:** Acompanhar o progresso por categoria

## Exemplo de Uso

```
Issue: "Definir requisitos do sistema"
Etapa SIPOC: Input

Issue: "Desenvolver funcionalidade X"
Etapa SIPOC: Process

Issue: "Entregar documentação"
Etapa SIPOC: Output
```

## Benefícios

- **Visualização Clara:** Entenda onde cada tarefa se encaixa no processo geral
- **Melhor Organização:** Organize o trabalho por etapas lógicas
- **Identificação de Gaps:** Identifique lacunas no processo
- **Comunicação Eficaz:** Facilita a comunicação sobre o status do projeto

## Troubleshooting

### Campo não aparece
- Verifique se você tem permissões de administrador
- Recarregue a página do projeto

### Opções não salvam
- Certifique-se de clicar em "Save" após cada opção
- Verifique a conexão com a internet

### Campo não é aplicado aos itens existentes
- O campo será aplicado apenas a novos itens por padrão
- Para aplicar a itens existentes, edite cada item individualmente

## Próximos Passos

Após configurar o campo SIPOC, considere:

1. Treinar a equipe sobre a metodologia SIPOC
2. Criar templates de issues para cada etapa
3. Configurar automações baseadas nas etapas
4. Estabelecer critérios de transição entre etapas

---

*Documentação criada para facilitar a implementação da metodologia SIPOC no GitHub Projects Beta.*