# Setup Virtual Environment — Python

Panduan setup virtual environment untuk project Flask di Windows, Linux, dan Mac.

---

## Opsi A: `venv` (Built-in Python — Paling Simpel)

### Mac / Linux

```bash
# 1. Masuk ke folder project
cd day-1/api

# 2. Buat virtual environment
python3 -m venv .venv

# 3. Aktifkan
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Jalankan app
python app.py

# 6. Keluar dari venv
deactivate
```

### Windows (Command Prompt)

```cmd
:: 1. Masuk ke folder project
cd day-1\api

:: 2. Buat virtual environment
python -m venv .venv

:: 3. Aktifkan
.venv\Scripts\activate.bat

:: 4. Install dependencies
pip install -r requirements.txt

:: 5. Jalankan app
python app.py

:: 6. Keluar dari venv
deactivate
```

### Windows (PowerShell)

```powershell
# 1. Masuk ke folder project
cd day-1\api

# 2. Buat virtual environment
python -m venv .venv

# 3. Izinkan script execution (sekali saja)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 4. Aktifkan
.venv\Scripts\Activate.ps1

# 5. Install dependencies
pip install -r requirements.txt

# 6. Jalankan app
python app.py

# 7. Keluar dari venv
deactivate
```

---

## Opsi B: `pipenv` (Dependency Manager)

### Install pipenv (semua OS)

```bash
pip install pipenv
```

### Mac / Linux

```bash
# 1. Masuk ke folder project
cd day-1/api

# 2. Install dependencies dari Pipfile (atau buat baru)
pipenv install

# 3. Aktifkan shell
pipenv shell

# 4. Jalankan app
python app.py

# 5. Keluar dari venv
exit
```

### Windows

```cmd
:: 1. Masuk ke folder project
cd day-1\api

:: 2. Install dependencies
pipenv install

:: 3. Aktifkan shell
pipenv shell

:: 4. Jalankan app
python app.py

:: 5. Keluar dari venv
exit
```

### Install package baru dengan pipenv

```bash
# Install package (otomatis update Pipfile)
pipenv install flask
pipenv install requests

# Install hanya untuk development
pipenv install pytest --dev

# Lihat dependency tree
pipenv graph
```

---

## Opsi C: `mise` + `pipenv` (Mac / Linux — Rekomendasi untuk project ini)

### 1. Install mise

```bash
curl https://mise.run | sh
echo 'eval "$(mise activate zsh)"' >> ~/.zshrc
source ~/.zshrc
```

### 2. Setup project

File `.mise.toml` di root project sudah dikonfigurasi:

```toml
[tools]
python = "3.11.13"
```

### 3. Install Python via mise

```bash
# Di root project
mise trust
mise install
```

### 4. Install pipenv via pip

```bash
pip install pipenv
```

### 5. Setup dan jalankan

```bash
cd day-1/api
pipenv install
pipenv shell
python app.py
```

---

## Cek Status Virtual Environment

```bash
# Cek Python yang aktif
which python        # Mac/Linux
where python        # Windows

# Cek packages yang terinstall
pip list

# Cek versi Python
python --version
```

Prompt terminal akan berubah saat venv aktif:
- `venv`: `(.venv) user@machine:~$`
- `pipenv`: `(api) user@machine:~$`

---

## Ringkasan Perbedaan

| | `venv` | `pipenv` | `mise` |
|---|---|---|---|
| Built-in | ✅ | ❌ (perlu install) | ❌ (perlu install) |
| Manage Python version | ❌ | ❌ | ✅ |
| Dependency lock file | ❌ | ✅ (`Pipfile.lock`) | - |
| Kemudahan | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Rekomendasi | Cepat & simpel | Project tim | Multi-project |
