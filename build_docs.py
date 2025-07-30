#!/usr/bin/env python3
"""
PME Documentation Builder
英語版と日本語版を別々のディレクトリでビルドします
"""

import os
import subprocess
import shutil
from pathlib import Path


def run_command(cmd, cwd=None, env=None):
    """コマンドを実行"""
    print(f"実行中: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        print(f"エラー: {result.stderr}")
        return False
    print(f"成功: {result.stdout}")
    return True


def build_docs(source_dir, build_dir):
    """ドキュメントをビルド"""
    # ビルドディレクトリを作成
    build_path = Path(build_dir)
    build_path.mkdir(parents=True, exist_ok=True)

    # Sphinxビルドコマンド
    cmd = [
        "sphinx-build",
        "-b",
        "html",
        "-d",
        str(build_path / "doctrees"),
        str(source_dir),
        str(build_path),
    ]

    return run_command(cmd)


def main():
    """メイン関数"""
    print("PME ドキュメントビルダー")
    print("=" * 40)

    # 英語版をビルド
    print("\n1. 英語版をビルド中...")
    if build_docs("docs/source", "docs/build/en"):
        print("✅ 英語版ビルド完了")
    else:
        print("❌ 英語版ビルド失敗")
        return

    # 日本語版をビルド
    print("\n2. 日本語版をビルド中...")
    if build_docs("docs_ja/source", "docs_ja/build"):
        print("✅ 日本語版ビルド完了")
    else:
        print("❌ 日本語版ビルド失敗")
        return

    print("\n🎉 すべてのビルドが完了しました！")
    print(f"英語版: docs/build/en/index.html")
    print(f"日本語版: docs_ja/build/index.html")


if __name__ == "__main__":
    main()
