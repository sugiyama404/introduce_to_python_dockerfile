# Flask API with Clean Architecture

## 概要
このプロジェクトは、Flaskフレームワークとクリーンアーキテクチャを使用して構築されたAPIです。クリーンアーキテクチャに基づいて設計されており、コードの保守性、拡張性、テスト容易性が向上しています。このドキュメントでは、プロジェクトの構成、使用方法について説明します。

![ubuntu](https://img.shields.io/badge/Ubuntu-E95420?&logo=ubuntu&logoColor=white)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?logo=docker&logoColor=white)](https://www.docker.com/)
![Git](https://img.shields.io/badge/GIT-E44C30?logo=git&logoColor=white)
![gitignore](https://img.shields.io/badge/gitignore%20io-204ECF?logo=gitignoredotio&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?logo=githubactions&logoColor=white)
[![Python](https://img.shields.io/badge/Python-3.8.8-blue.svg?logo=python&logoColor=blue)](https://www.python.org/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v3-blue.svg)](https://docs.docker.com/compose/)
[![Flask](https://img.shields.io/badge/Flask-3.0.2-blue.svg?logo=flask&logoColor=white)](https://palletsprojects.com/p/flask/)
[![Pytest](https://img.shields.io/badge/pytest-8.1.1-blue.svg)](https://pytest.org/)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.28-blue.svg)
[![MySQL](https://img.shields.io/badge/MySQL-8.0.32-blue.svg?logo=mysql&logoColor=white)](https://www.mysql.com/)
![Commit Msg](https://img.shields.io/badge/Commit%20message-Eg-brightgreen.svg)
![Code Cmnt](https://img.shields.io/badge/code%20comment-Ja-brightgreen.svg)

# 特徴
+ クリーンアーキテクチャ: ビジネスロジックをUIやデータソースから分離することで、コードの保守性、テスト容易性、再利用性を向上させています。
+ Flaskフレームワーク: Python製の軽量で柔軟なWebフレームワークを利用することで、API開発を効率化しています。
+ Dockerfile: 保守性の高いDockerfileにより、開発環境、テスト環境、本番環境の構築を容易にし、異なる環境間での依存関係の差異を解消しています。

# クリーンアーキテクチャに基づいたディレクトリ構成

```
```

# 使用方法
1. 以下のコマンドでコンテナを立ち上げる。
```
docker compose up
```
2. apiにアクセス
http://localhost:8000/


# テスト結果

<p align="center">
  <img src="resources/test.png" alt="animated">
</p>
