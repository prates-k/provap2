# P2 - API Rest para Controle de Estoque (Back-End)

API desenvolvida como requisito avaliativo para a disciplina de Laboratório de Programação Back-End.
**Professor:** Alvaro Leiroz  
**Curso:** Engenharia de Software - 5º Período  
**Instituição:** Univassouras  

## 🚀 Sobre o Projeto
O projeto consiste em uma API Rest para gerenciamento e controle de estoque de produtos, permitindo o armazenamento de códigos de barras, nomes, preços e quantidades. A aplicação foi construída seguindo boas práticas de arquitetura, isolamento de ambiente, testes automatizados e containerização total.

## 🛠️ Tecnologias Utilizadas
* Python 3.12 & Django Rest Framework (DRF)
* SQLite (Banco de dados integrado ao container)
* Docker (Containerização completa da aplicação)
* Git & GitHub (Controle de versão e hospedagem do código)
* Thunder Client / Postman (Validação dos endpoints)

## 🧪 Testes Automatizados
A API conta com testes integrados para validar a integridade das operações do CRUD. Para rodar os testes localmente no ambiente de desenvolvimento, execute:
```bash
python manage.py test