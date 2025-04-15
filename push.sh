#!/bin/bash

# 获取提交信息
if [ -z "$1" ]; then
    echo "Usage: ./push.sh \"your commit message\""
    exit 1
fi

# 显示当前状态
echo "Current git status:"
git status

# 添加所有更改
echo -e "\nAdding all changes..."
git add .

# 提交更改
echo -e "\nCommitting changes with message: $1"
git commit -m "$1"

# 推送到远程仓库
echo -e "\nPushing to remote repository..."
git push origin main

echo -e "\nPush completed successfully!" 