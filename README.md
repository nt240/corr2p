# corr2p

**Correlation coefficient → p-value CLI tool**
**相関係数から p 値を計算する CLI ツール**

---

## 🇬🇧 English

### Overview

`corr2p` is a simple command-line tool that calculates the *p-value* from a correlation coefficient `r` and a sample size `n`.
It uses **SciPy** for statistical computation and can be executed directly via **uvx**, including from GitHub.

### Features

* Compute p-value from correlation coefficient
* Uses SciPy's `pearsonr` equivalent formula
* Minimal CLI using Click
* Install-free usage with `uvx`

### Usage

#### Run directly from GitHub via uvx

```bash
uvx --from git+https://github.com/nt240/corr2p corr2p --r 0.5 --n 30
```

#### Output example

```
r=0.5, n=30, t=3.0091, p=0.0053658
```

### Local installation

```bash
uv sync
uv run corr2p --r 0.5 --n 30
```

### Requirements

* Python 3.13
* SciPy

---

## 🇯🇵 日本語

### 概要

`corr2p` は、相関係数 `r` とサンプルサイズ `n` から **p 値** を計算するシンプルな CLI ツールです。
統計計算には **SciPy** を使用し、**uvx** を使えば GitHub リポジトリから直接実行できます。

### 特徴

* 相関係数から p 値を計算
* SciPy の Pearson 相関の式を利用
* Click による最小限の CLI
* uvx によりインストール不要で実行可能

### 使い方

#### uvx で GitHub から直接実行

```bash
uvx --from git+https://github.com/nt240/corr2p corr2p --r 0.5 --n 30
```

#### 実行例

```
r=0.5, n=30, t=3.0091, p=0.0053658
```

### ローカル実行

```bash
uv sync
uv run corr2p --r 0.5 --n 30
```

### 必要環境

* Python 3.13
* SciPy

---

## License

MIT License
