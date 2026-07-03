<div align="center">

# 🎓 SIRA
## Sistema Inteligente de Reconhecimento de Acesso

<img src="docs/logo.png" width="180">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv)
![DeepFace](https://img.shields.io/badge/DeepFace-Facial%20Recognition-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Status](https://img.shields.io/badge/Status-MVP-success)

Sistema inteligente de controle de acesso utilizando **Reconhecimento Facial**, desenvolvido em **Python + Django**, com geração de embeddings utilizando **DeepFace** e detecção facial através do **OpenCV**.

</div>

---

# 📖 Sobre o Projeto

O **SIRA** (Sistema Inteligente de Reconhecimento de Acesso) foi desenvolvido como um MVP para automatizar o registro de entrada de alunos, professores, servidores e visitantes em instituições de ensino.

Ao contrário dos sistemas tradicionais que utilizam cartões ou listas de presença, o SIRA utiliza **Visão Computacional** para identificar automaticamente as pessoas e registrar sua presença.

---

# 🎯 Objetivos

- Automatizar o controle de acesso
- Registrar presença automaticamente
- Reduzir fraudes
- Eliminar listas de presença
- Centralizar informações em um Dashboard Web

---

# 🚀 Tecnologias

| Tecnologia | Utilização |
|------------|------------|
| Python | Backend |
| Django | Framework Web |
| SQLite | Banco de Dados |
| OpenCV | Captura e detecção facial |
| DeepFace | Geração de Embeddings |
| NumPy | Manipulação matemática |
| HTML5 | Interface |
| CSS3 | Estilização |
| JavaScript | Atualizações futuras |

---

# 🏛 Arquitetura

```
                Webcam
                   │
                   ▼
          OpenCV Detecta Face
                   │
                   ▼
            DeepFace (FaceNet)
                   │
                   ▼
            Geração do Embedding
                   │
                   ▼
          Comparação com Banco
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
   Pessoa Encontrada     Desconhecido
          │
          ▼
 Registro de Presença
          │
          ▼
 Dashboard Django
```

---

# 📂 Estrutura do Projeto

```
idFace/

│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── reconhecimento/
│   ├── camera.py
│   ├── detector.py
│   ├── comparador.py
│   ├── registro.py
│   ├── reconhecer.py
│   └── config.py
│
├── media/
│   └── rostos/
│
├── templates/
│
├── static/
│
├── manage.py
│
└── db.sqlite3
```

---

# ⚙ Funcionalidades

## ✅ Login

- Login de administrador
- Controle de acesso

---

## ✅ Cadastro de Pessoas

Cadastro de:

- Alunos
- Visitantes
- Professores
- Servidores

Cada cadastro gera automaticamente:

- Embedding Facial
- Foto do usuário

---

## ✅ Reconhecimento Facial

O sistema:

1. Detecta o rosto
2. Gera o embedding
3. Compara com o banco
4. Identifica a pessoa
5. Registra presença

---

## ✅ Dashboard

O Dashboard apresenta:

- Total de pessoas cadastradas
- Presenças do dia
- Últimos registros
- Histórico

---

# 📸 Fluxo do Sistema

```
Administrador

↓

Cadastro

↓

Captura Facial

↓

DeepFace

↓

Embedding

↓

Banco de Dados

↓

Reconhecimento

↓

Registro de Presença

↓

Dashboard
```

---

# 🗄 Banco de Dados

## Pessoa

| Campo | Tipo |
|--------|------|
| id | Integer |
| nome | CharField |
| tipo | CharField |
| matrícula | CharField |
| email | CharField |
| foto | ImageField |
| embedding | JSONField |

---

## Presença

| Campo | Tipo |
|--------|------|
| id | Integer |
| pessoa | ForeignKey |
| data_hora | DateTime |

---

# ▶ Instalação

## Clonar projeto

```bash
git clone https://github.com/seuusuario/SIRA.git
```

---

## Criar ambiente virtual

Linux

```bash
python -m venv venv

source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Aplicar migrações

```bash
python manage.py migrate
```

---

## Criar administrador

```bash
python manage.py createsuperuser
```

---

## Executar servidor

```bash
python manage.py runserver
```

---

# 📷 Executar Reconhecimento

Abra o Shell do Django

```bash
python manage.py shell
```

Depois:

```python
from reconhecimento.reconhecer import reconhecer

reconhecer()
```

---

# 🔮 Roadmap

- [x] Login
- [x] Dashboard
- [x] Cadastro de Alunos
- [x] Cadastro de Visitantes
- [x] Reconhecimento Facial
- [x] Registro de Presença
- [ ] Captura guiada por Webcam
- [ ] Anti-Spoofing
- [ ] Dashboard em Tempo Real
- [ ] API REST
- [ ] Relatórios PDF
- [ ] Reconhecimento Multi-Câmera

---

# 📷 Telas

## Login

> Adicione uma imagem em:

```
docs/login.png
```

---

## Dashboard

```
docs/dashboard.png
```

---

## Cadastro

```
docs/cadastro.png
```

---

# 👨‍💻 Desenvolvedor

**Everton Espedito Silva Santos**

Licenciatura em Computação

Instituto Federal do Sertão Pernambucano

---

# 📄 Licença

Projeto desenvolvido para fins acadêmicos.

---

<div align="center">

### ⭐ Se este projeto foi útil, deixe uma estrela no repositório!

</div>