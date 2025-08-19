# 🚖 Projeto Urban Routes – Automação de Testes (QA-Brazil_Python_Automation)

Este repositório faz parte do **Bootcamp de Analista de QA da TripleTen** e contém os projetos das **Sprints 7 e 8**, com foco em **automação de testes usando Python, Pytest e Selenium WebDriver**.  
O objetivo principal foi implementar testes automatizados para validar o fluxo do aplicativo fictício **Urban Routes**, simulando cenários reais de solicitação de corridas.

---

## ✅ Funcionalidades Validadas
O fluxo de teste cobre todo o processo de solicitação de corrida no Urban Routes:
1. Definir endereço de origem e destino.  
2. Selecionar plano *Comfort*.  
3. Preencher número de telefone (com validação via código SMS).  
4. Adicionar cartão de crédito.  
5. Escrever comentário para o motorista.  
6. Solicitar cobertor e lenços.  
7. Solicitar 2 sorvetes 🍦.  
8. Pedir táxi e validar a exibição da janela de busca de carro.  

---

## 👨‍💻 Minhas Contribuições
- Estruturei a **arquitetura do projeto** em Python.  
- Criei arquivos auxiliares `helpers.py` e `data.py` para organizar dados de teste e funções.  
- Implementei **Page Object Model (POM)** para garantir manutenibilidade e reuso.  
- Desenvolvi testes **End-to-End (E2E)** cobrindo fluxos completos do usuário.  
- Configurei **setup e teardown** para inicialização e finalização dos testes.  

---

## 🛠 Tecnologias e Ferramentas Utilizadas
- **Linguagem:** Python 3  
- **Framework de Testes:** Pytest  
- **Automação Web:** Selenium WebDriver  
- **Design de Testes:** Page Object Model (POM)  
- **Controle de Versão:** Git e GitHub  
- **Ferramentas de Apoio:** DevTools, Figma  

---

## 📊 Resultados e Impacto
- Reduzi o esforço manual de validação com a implementação de testes automatizados.  
- Melhorei a organização do código com **Page Object Model**, facilitando futuras manutenções.  
- Permiti maior foco em **testes exploratórios** e identificação de cenários críticos.  

---

## 📚 Aprendizados e Desafios Superados
- Criação de **localizadores robustos** e reutilizáveis no Selenium.  
- Estruturação do projeto em conformidade com boas práticas de QA.  
- Uso do **Pytest** para relatórios mais claros e execução flexível dos testes.  
- Simulação de fluxos reais, aproximando a prática do ambiente corporativo.  

---

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Pattussi/QA-Brazil_Python_Automation.git
   cd QA-Brazil_Python_Automation
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute os testes:
   ```bash
   pytest -v
   ```

---

## ✨ Sobre Mim
Sou **Leonardo Pattussi**, profissional em transição para a área de **Qualidade de Software (QA)**.  
Após mais de 12 anos atuando como gerente comercial, concluí o **Bootcamp QA da TripleTen**, aplicando agora minha experiência analítica e de processos para garantir a entrega de produtos digitais de qualidade.  

📫 Contato: [pattussi@hotmail.com](mailto:pattussi@hotmail.com) | [LinkedIn](https://linkedin.com/in/leonardo-pattussi)  
