# 🚀 Libras-Python

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://www.python.org/)

[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10.1-FF6F00?style=for-the-badge&logo=tensorflow)](https://www.tensorflow.org/)

[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv)](https://opencv.org/)

[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-2196F3?style=for-the-badge)](https://mediapipe.dev/)

[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#)

**Reconhecimento de letras em LIBRAS em tempo real utilizando visão computacional e inteligência artificial.**

</div>

---

# 📖 Sobre o Projeto

Este projeto utiliza **Python**, **TensorFlow**, **MediaPipe** e **OpenCV** para reconhecer letras da LIBRAS em tempo real através da webcam.

O sistema detecta automaticamente a mão do usuário, recorta a região da mão, envia para um modelo treinado em Keras e exibe na tela a letra identificada.

Além disso, o sistema consegue montar palavras automaticamente conforme o usuário soletra.

---

# ✨ Funcionalidades

- ✅ Reconhecimento de letras em tempo real
- ✅ Detecção automática da mão
- ✅ Webcam ao vivo
- ✅ Exibição da letra reconhecida
- ✅ Formação automática de palavras
- ✅ Caixa de detecção da mão
- ✅ Suporte a múltiplas letras da LIBRAS
- ✅ Inteligência Artificial com TensorFlow/Keras

---

# 🧠 Tecnologias Utilizadas

- Python 3.10
- TensorFlow 2.10.1
- Keras
- OpenCV
- MediaPipe
- NumPy

---

# 📁 Estrutura do Projeto

```bash
Libras-Python/
│
├── main.py
├── keras_model.h5
├── README.md
└── .gitignore
```

---

# 🖥️ Classes Reconhecidas

O modelo reconhece as seguintes letras:

```txt
A B C D E F G I L M N O P Q R S T U V W Y
```

---

# 📷 Como Funciona

1. A webcam captura o vídeo em tempo real
2. O MediaPipe detecta a mão
3. A mão é recortada automaticamente
4. O modelo de IA processa a imagem
5. A letra reconhecida aparece na tela
6. As letras são agrupadas formando palavras

---

# 🚀 Instalação Completa (Windows)

## 1. Instalar Python 3.10

Baixe:

https://www.python.org/downloads/release/python-31011/

Durante a instalação:

✅ Marque:

```txt
Add Python to PATH
```

---

# 2. Clonar o repositório

```bash
git clone https://github.com/minacabu/Libras-Python.git
cd Libras-Python
```

---

# 3. Criar ambiente virtual

```bash
python -m venv venv
```

---

# 4. Ativar ambiente virtual

## Windows

```bash
venv\Scripts\activate
```

## Linux/macOS

```bash
source venv/bin/activate
```

---

# 5. Atualizar pip

```bash
python -m pip install --upgrade pip
```

---

# 6. Instalar dependências corretas

## IMPORTANTE

As versões abaixo evitam erros de compatibilidade entre:

- TensorFlow
- NumPy
- MediaPipe
- OpenCV
- Protobuf

---

## Instalar NumPy

```bash
pip install numpy==1.24.3
```

---

## Instalar OpenCV

```bash
pip install opencv-python==4.7.0.72
```

---

## Instalar TensorFlow

```bash
pip install tensorflow==2.10.1
```

---

## Instalar MediaPipe

```bash
pip install mediapipe==0.10.9
```

---

## Corrigir protobuf

```bash
pip uninstall protobuf -y
pip install protobuf==3.20.0
```

---

# ▶️ Como Executar

Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

Execute:

```bash
python main.py
```

---

# ⌨️ Controles

| Tecla | Função |
|---|---|
| ESC | Fecha o programa |

---

# 🧠 Exemplo de Uso

Usuário faz os sinais:

```txt
C
A
S
A
```

Na tela aparece:

```txt
CASA
```


# 📌 Melhorias Futuras

- Reconhecimento de frases completas
- Maior fidelidade dos sinais
- Interface gráfica
- Suporte para mais sinais
- Treinamento personalizado
- Deploy Web
- Suporte para múltiplas mãos

---

# 🤝 Contribuição

Contribuições são bem-vindas.

1. Faça um fork
2. Crie uma branch
3. Commit suas alterações
4. Abra um Pull Request

---

# ⭐ Autores

Desenvolvido por:
Luan Rodrigues.
Anderson Gabriel da Silva Cavalcanti,
Geraldo Bezerra Martins Neto,
Guilherme Vieira
Telmo Lopes.


Se este projeto te ajudou, deixe uma estrela no repositório ⭐
