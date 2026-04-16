# study-mysql

MySQL / RDB 学習用リポジトリ  
教材: 一週間で学べるMySQL

## 環境
- MySQL 8.x
- Homebrew
- ユーザー: studyuser
- DB: SCHOOL

## セットアップ

1. `.env.example` をコピーして `.env` を作成
2. 必要に応じて値を編集
3. Docker を起動

```bash
cp .env.example .env
docker compose up -d
``