<div align="center">

<img src="https://github.com/Prateek-glitch/Primetrade.ai/blob/main/primetade_logo-removebg-preview.png" alt="Primetrade.ai Logo" width="200" />

# Primetrade.ai — Binance Futures Testnet Trading Bot

<img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=600&size=18&duration=2800&pause=1200&color=111111&center=true&vCenter=true&width=760&lines=Production-style+CLI+for+Binance+Futures+Testnet;MARKET+%E2%80%A2+LIMIT+%E2%80%A2+STOP+(Stop-Limit);Clean+Validation+%E2%80%A2+Structured+Logging+%E2%80%A2+Rich+UX" alt="Typing Animation" />

[![Status](https://img.shields.io/badge/status-production--style-111111?style=flat-square)](https://github.com/Prateek-glitch/Primetrade.ai)
[![Version](https://img.shields.io/badge/version-v1.0.0-111111?style=flat-square)](https://github.com/Prateek-glitch/Primetrade.ai)
[![Environment](https://img.shields.io/badge/environment-binance%20futures%20testnet-111111?style=flat-square)](https://testnet.binancefuture.com)

<img src="https://github.com/Prateek-glitch/Primetrade.ai/blob/main/primetrade_ai.jpeg?raw=true" alt="Primetrade.ai Hero Banner" width="100%" />

[Tech Stack](#-tech-stack) • [Quick Start](#-quick-start) • [Execution Syntax](#-execution-syntax) • [Architecture](#-architecture) • [Acceptance Mapping](#-acceptance-criteria-mapping) • [Roadmap](#-roadmap)

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" alt="animated divider" width="100%" />
</p>

---

## ⎈ STATS STRIP

| Python | Order Types | Architecture | Logging |
|---|---|---|---|
| 3.8+ | MARKET • LIMIT • STOP (Stop-Limit) | Decoupled Modular Layers | File + Console |

---

## ⬢ TECH STACK

<div align="left">

![Python](https://img.shields.io/badge/Python-111111?style=for-the-badge&logo=python&logoColor=white)
![Binance Futures Testnet](https://img.shields.io/badge/Binance_Futures_Testnet-111111?style=for-the-badge&logo=binance&logoColor=white)
![python-binance](https://img.shields.io/badge/python--binance-111111?style=for-the-badge&logo=python&logoColor=white)
![python-dotenv](https://img.shields.io/badge/python--dotenv-111111?style=for-the-badge&logo=python&logoColor=white)
![Rich CLI](https://img.shields.io/badge/Rich_CLI-111111?style=for-the-badge&logo=gnometerminal&logoColor=white)

</div>

---

## ⎔ TECHNICAL OVERVIEW

A production-style Python CLI for **Binance USDT-M Futures Testnet** with:
- deterministic input validation
- clean CLI command execution
- reusable order management layer
- structured logging and defensive exception handling

Supports:
- BUY / SELL
- MARKET / LIMIT
- STOP (Stop-Limit) as bonus enhancement

---

## ⌁ BUSINESS USE CASE

### Problem
Manual test order placement is repetitive, error-prone, and hard to audit.

### Solution
This project provides a clean execution utility that:
- validates before submission
- structures exchange calls through a reusable manager
- logs request/response lifecycle for traceability

---

## ⌬ FEATURE GRID (THREE PILLARS)

| Pillar | Capability | Impact |
|---|---|---|
| ⚙︎ Execution | MARKET / LIMIT / STOP routing | Exchange-ready order flow |
| 🛡 Validation | Strict checks for side/type/qty/price/stop-price | Lower invalid API calls |
| ◈ Observability | Rich CLI + file/console logs | Faster debugging and better UX |

---

## ⎘ QUICK START

### 1) Clone
```bash
git clone https://github.com/Prateek-glitch/Primetrade.ai.git
```

### 2) Enter
```bash
cd Primetrade.ai
```

### 3) Create venv
```bash
python -m venv .venv
```

### 4) Activate (macOS/Linux)
```bash
source .venv/bin/activate
```

### 5) Activate (Windows)
```powershell
.venv\Scripts\activate
```

### 6) Install deps
```bash
pip install -r requirements.txt
```

---

## ⎋ SECURE CONFIGURATION

Create `.env` in project root:

```dotenv
BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret
```

Security notes:
- never commit `.env`
- keep testnet and mainnet keys separate
- rotate keys on schedule

---

## ⎕ EXECUTION SYNTAX

**Run MARKET test**
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Run LIMIT test**
```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 80000
```

**Run STOP (Stop-Limit) test**
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type STOP --quantity 0.01 --price 76500 --stop-price 76000
```

---

## ⛉ ARCHITECTURE

### Diagram

<div align="center">
  <img src="https://github.com/Prateek-glitch/Primetrade.ai/blob/main/architecture1.svg" alt="Architecture Diagram: CLI to Binance API" width="95%" />
</div>

### Flow
```text
CLI (bot/cli.py)
   │
   ▼
Validator (bot/validators.py)
   │
   ▼
OrderManager (bot/orders.py)
   │
   ▼
Binance Client Wrapper (bot/client.py)
   │
   ▼
Binance Futures Testnet API
```

### Directory Structure
```text
Primetrade.ai/
├── bot/
│   ├── __init__.py
│   ├── cli.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── requirements.txt
├── trading_bot.log
��── primetrade_ai.jpeg
├── primetade_logo.png
└── README.md
```

### Decoupled Architecture Note
Core trading logic is isolated from CLI rendering.  
This enables reuse in:
- schedulers
- web APIs
- strategy workers
- queue-based execution systems

---

## ⚠ IMPORTANT — NTP / CLOCK SYNC

> [!WARNING]
> Binance signed requests are time-sensitive.  
> If system time is out of sync, requests may fail with:  
> `Timestamp for this request is outside of the recvWindow.`

Enable automatic date/time sync (NTP) before testing.

---

## ⊞ ACCEPTANCE CRITERIA MAPPING

| Requirement | Implementation | Status |
|---|---|---|
| Python 3.x app | Project runtime + `requirements.txt` | ✅ |
| MARKET orders | `OrderManager.place_order(... type='MARKET')` in `bot/orders.py` | ✅ |
| LIMIT orders | `OrderManager.place_order(... type='LIMIT')` in `bot/orders.py` | ✅ |
| BUY/SELL support | CLI `--side` + validator checks in `bot/cli.py`, `bot/validators.py` | ✅ |
| CLI input arguments | `argparse` in `bot/cli.py` | ✅ |
| Price required for LIMIT | `validate_order_input` in `bot/validators.py` | ✅ |
| Request summary output | Rich table in `bot/cli.py` | ✅ |
| Response details output | Rich panel in `bot/cli.py` | ✅ |
| Success/failure message | CLI response handling in `bot/cli.py` | ✅ |
| Structured layers | `client.py`, `orders.py`, `validators.py`, `cli.py` | ✅ |
| Logging requests/errors | `bot/logging_config.py`, `bot/orders.py` + `trading_bot.log` | ✅ |
| Exception handling | Validation + API/runtime handling in `cli.py` / `orders.py` | ✅ |
| Bonus order type | STOP (Stop-Limit) in `bot/orders.py` + CLI args | ✅ |
| Bonus UX | Rich-enhanced terminal output | ✅ |

---

## ⌁ SAMPLE OUTPUT (JSON)

### Success response (example)
```json
{
  "symbol": "BTCUSDT",
  "orderId": 13035431414,
  "status": "NEW",
  "side": "BUY",
  "type": "MARKET",
  "origQty": "0.010",
  "executedQty": "0.000",
  "avgPrice": "0.00000"
}
```

### Failure response (example)
```json
{
  "code": -1021,
  "msg": "Timestamp for this request is outside of the recvWindow."
}
```

---

## ⎚ KNOWN LIMITATIONS

- no automatic retry strategy on transient API/network errors
- no async/concurrent order execution
- no account balance/position pre-check before submission
- no built-in time synchronization helper (manual NTP sync required)
- no automated test suite yet

---

## ⌬ TROUBLESHOOTING

<details>
<summary><strong>Timestamp / recvWindow error</strong></summary>

- synchronize OS clock with NTP
- retry command after sync
- optionally expand recvWindow in future versions

</details>

<details>
<summary><strong>STOP order rejected (immediate trigger)</strong></summary>

- adjust `--stop-price` relative to current market
- verify BUY/SELL trigger logic before retry

</details>

<details>
<summary><strong>Missing API keys</strong></summary>

- ensure `.env` is present in project root
- verify exact key names:
  - `BINANCE_API_KEY`
  - `BINANCE_API_SECRET`

</details>

---

## ⌗ ROADMAP

- **v1.1** — request retry policy + timestamp sync helper
- **v1.2** — account/position checks + risk pre-validation
- **v1.3** — strategy plugin hooks (pluggable signal/execution modules)

---

<div align="center">

<sub>
Engineered by <strong>Prateek</strong> · Application Task Submission · Primetrade.ai Hiring Evaluation Context
</sub>

</div>
