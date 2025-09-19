# 🤖 Intent Tag AI Agent

## Overview

The Intent Tag AI Agent is an automated system that analyzes new GitHub issues and suggests appropriate labels based on content analysis. It uses rule-based keyword matching and pattern recognition specifically tuned for Portuguese language content.

## How It Works

### Trigger
- Automatically runs when a new issue is created via GitHub Actions
- Analyzes the issue title and body content
- Posts a comment with suggested labels for maintainer review

### Analysis Process
1. **Text Normalization**: Converts text to lowercase, removes markdown syntax, normalizes whitespace
2. **Keyword Extraction**: Identifies meaningful keywords while filtering out Portuguese stop words
3. **Pattern Matching**: Applies regex patterns to detect specific linguistic structures
4. **Confidence Scoring**: Calculates confidence scores based on keyword density and pattern matches
5. **Threshold Filtering**: Only suggests labels that meet minimum confidence thresholds
6. **Comment Generation**: Creates human-readable suggestions for maintainers

### Supported Labels

| Label | Description | Example Keywords |
|-------|-------------|------------------|
| `💡 Token de Insight` | Strategic ideas and innovations | ideia, insight, estratégia, inovação, solução |
| `🔥 Token de Dor` | Problems and pain points | problema, erro, bug, falha, dificuldade |
| `🏛️ Proposta de Governança` | Process and governance issues | governança, processo, política, estrutura |
| `ops` | Operations and infrastructure | operação, deploy, infraestrutura, automação |
| `strats` | Strategy and planning | estratégia, planejamento, mercado, crescimento |
| `tats` | Testing and validation | teste, validação, experimento, análise |

### Domain-Specific Intelligence

The agent is specifically tuned for this repository's context and includes:
- **Portuguese language processing** with proper stop word filtering
- **Domain-specific terminology** (e.g., "centauro", "synergies", "playbook")
- **Business context awareness** (e.g., names like "Adriano", "Maria Morena")
- **Technical patterns** for development and strategy discussions

## Example Output

When a new issue is created, the agent posts a comment like:

```markdown
🤖 **Intent Tag AI Agent**

Analisei o conteúdo desta issue e sugiro as seguintes tags:

• **💡 Token de Insight** (Confiança: Alta)
• **strats** (Confiança: Média)

**Análise:**
- Título analisado: "Nova estratégia para expansão"
- Palavras-chave identificadas no conteúdo
- Padrões linguísticos reconhecidos

**Próximos passos:**
Os mantenedores podem revisar essas sugestões e aplicar as labels apropriadas.

---
*Este comentário foi gerado automaticamente pelo Intent Tag AI Agent*
```

## Technical Implementation

### Architecture
- **GitHub Actions Workflow**: `.github/workflows/intent-tag-agent.yml`
- **Python Script**: `.github/workflows/intent_tag_agent.py`
- **Dependencies**: `requests` for GitHub API interaction

### Configuration
- **Keyword Mappings**: Extensive Portuguese keyword dictionaries for each label
- **Regex Patterns**: Language-specific patterns for detecting intent
- **Confidence Thresholds**: Configurable minimum confidence levels
- **Stop Words**: Portuguese stop word filtering for better accuracy

### Permissions Required
- `issues: write` - To post comments on issues
- `contents: read` - To access repository content

## Future Extensibility

The agent is designed to be easily extensible for AI integration:

1. **Modular Architecture**: The analysis logic is separated from the GitHub integration
2. **Pluggable Analyzers**: Easy to replace rule-based logic with AI models
3. **Configuration-Driven**: Labels and keywords can be updated without code changes
4. **API Ready**: Built with future external AI service integration in mind

## Testing

The agent includes comprehensive testing:
- Unit tests for keyword matching logic
- Integration tests with real issue examples
- Demo script showcasing capabilities
- Confidence scoring validation

## Benefits

- **Automatic Classification**: Reduces manual labeling effort
- **Consistent Categorization**: Applies labels based on defined criteria
- **Multilingual Support**: Properly handles Portuguese content
- **Domain Awareness**: Understands repository-specific terminology
- **Maintainer Control**: Suggestions only, maintainers make final decisions
- **Extensible Design**: Ready for future AI service integration