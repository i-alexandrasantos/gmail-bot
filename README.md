# 📧 Bot Automático para Gmail

Um bot simples em **Python** que automatiza o processo de criar e enviar novos e-mails no **Gmail**, clicando em posições pré-definidas na tela.
Ele seleciona um modelo, preenche os campos e repete o processo quantas vezes você quiser — economizando tempo e evitando a repetição manual 🔁

---

## ⚙️ O que ele faz

✅ Com o Gmail aberto em seu navegador, ele clica no botão de **“Escrever”**
✅ Seleciona um **modelo** (salvo no Gmail)
✅ Repete esse processo **N vezes**, conforme configurado
✅ Tudo isso **sem precisar de extensão no navegador**

---

## 🧠 Objetivo

Automatizar o envio de e-mails em massa **de forma simples**, apenas simulando os cliques e ações do usuário.
Ideal para quem quer otimizar tarefas repetitivas dentro do Gmail, como disparos internos, testes ou comunicações padronizadas.

---

## 🧩 Requisitos

* Python **3.8+**
* Gmail aberto e visível na tela (mesma resolução e zoom usados na configuração)
* Bibliotecas:

  ```
  pyautogui
  pyperclip
  keyboard
  ```

---

## 🚀 Instalação

```bash
git clone https://github.com/i-alexandrasantos/gmail-bot
cd gmail-bot
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

---

## 🛠️ Configuração

O bot usa **coordenadas da tela** para clicar nos botões do Gmail.
Você pode alterar as posições conforme sua resolução.

Use o código abaixo para capturar as coordenadas na tela:

```python
import pyautogui
import time

time.sleep(3)
print(pyautogui.position())
```

Abra o Gmail, posicione o mouse no botão desejado e veja no terminal as coordenadas X e Y.

Altere no código.

---

## ▶️ Como usar

Depois de configurar, basta rodar:

```bash
python gmail_bot.py
```

ou, se quiser basta clicar com o lado direito em **Abrir Com > Python**


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
Perfeito 💫
Aqui vai apenas o final pra você adicionar no seu README:

---

## ✨ Feito por

Desenvolvido com ☕ por [**Alexandra Santos**](https://github.com/i-alexandrasantos) 🚀
