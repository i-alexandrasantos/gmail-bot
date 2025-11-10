# 📧 Bot Automático para Gmail

Um bot simples em **Python** que automatiza o processo de abrir e criar novos e-mails no **Gmail**, clicando em posições pré-definidas na tela.
Ele também seleciona um modelo específico e repete o processo quantas vezes você quiser — economizando tempo e evitando repetição manual 🔁

---

## ⚙️ O que ele faz

✅ Abre o Gmail (já logado e visível no navegador)
✅ Clica no botão de **“Escrever”**
✅ Abre o menu de **Modelos**
✅ Seleciona um modelo específico
✅ Repete esse processo **N vezes**, conforme configurado
✅ Tudo isso **sem precisar de extensão no navegador**

---

## 🧠 Objetivo

Automatizar tarefas repetitivas dentro do Gmail — como inserir um modelo e preparar vários e-mails rapidamente — de forma simples, apenas simulando cliques e ações do usuário.

---

## 🧩 Requisitos

* Python **3.8+**
* Gmail aberto e visível na tela (mesma resolução e zoom usados na configuração)
* Bibliotecas necessárias:

  ```
  pyautogui
  time
  ```

*(As bibliotecas `pyperclip` e `keyboard` não são obrigatórias neste projeto.)*

---

## 🚀 Instalação

```bash
git clone https://github.com/i-alexandrasantos/gmail-bot
cd gmail-bot
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
pip install pyautogui
```

---

## 🛠️ Configuração

O bot utiliza **coordenadas da tela** para clicar nos elementos do Gmail.
Essas coordenadas podem variar conforme sua resolução ou zoom do navegador.

Use o código abaixo para capturar as posições exatas:

```python
import pyautogui
import time

time.sleep(3)
print(pyautogui.position())
```

Abra o Gmail, posicione o mouse sobre o botão desejado e veja no terminal as coordenadas **X** e **Y**.
Depois, substitua essas posições no código principal (`gmail_bot.py`).

---

## ▶️ Como usar

Com o Gmail aberto e o código configurado com as posições certas, execute:

```bash
python gmail_bot.py
```

ou, se preferir, clique com o botão direito no arquivo e escolha:
**“Abrir com > Python”**

---

## 🧪 Dica

🔸 Antes de rodar com várias repetições, teste com `repeticoes = 1` para garantir que as posições estão corretas.
🔸 Aguarde alguns segundos após iniciar — o script tem um pequeno `time.sleep(5)` antes de começar.

---

## 🧰 Próximos passos (ideias)

* [ ] Interface para capturar posições automaticamente
* [ ] Detecção por imagem (em vez de coordenadas fixas)
* [ ] Modo visual com logs e status em tempo real

---

## 📜 Licença

Distribuído sob a licença **MIT**.
Veja o arquivo `LICENSE` para mais detalhes.

---

## ✨ Feito por

Desenvolvido com ☕ por [**Alexandra Santos**](https://github.com/i-alexandrasantos) 🚀
