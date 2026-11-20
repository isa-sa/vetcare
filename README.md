# VetCare - Sistema de Gestão para Clínicas Veterinárias

Implementação da **Etapa 2 (Sprint 1 - 30% dos Requisitos Funcionais)** do projeto arquitetural VetCare, desenvolvido em **Python com Django** seguindo o estilo **Monólito Modular**.

## Funcionalidades Implementadas (Sprint 1)
- **Autenticação e Controle de Acesso (`contas`):** Login, logout, cadastro de usuários e restrição de rotas.
- **Gestão de Clientes (`clientes`):** Cadastro e listagem de Tutores e seus respectivos Pets com integridade referencial.
- **Agendamento Clínico (`agendamentos`):** Marcação de consultas com validação transacional (`@transaction.atomic`) contra conflitos de horário e controle de status.

## Estrutura Arquitetural
O sistema divide-se em módulos independentes (Django Apps) com isolamento de regras de negócio na camada `services.py`:
- `contas/`: Identidade e permissões.
- `clientes/`: Domínio de Tutores e Pacientes.
- `agendamentos/`: Domínio crítico de agenda e regras de concorrência.

## Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/isa-sa/vet-care]
   cd vetcare